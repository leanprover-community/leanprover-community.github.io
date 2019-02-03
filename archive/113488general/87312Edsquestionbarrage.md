---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/87312Edsquestionbarrage.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [Ed's question barrage](https://leanprover-community.github.io/archive/113488general/87312Edsquestionbarrage.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Edward Ayers (Aug 11 2018 at 11:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/131947644):
<p>Massive thanks to <span class="user-mention" data-user-id="110049">@Mario Carneiro</span> for helping me. I'll buy you beers next time we are in the same physical location to within 100m.</p>

#### [ Edward Ayers (Aug 11 2018 at 12:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/131948511):
<p>In the constructor for <code>mvar</code> for <code>expr</code>, are the arguments pretty name, unique name, type? You said that <code>local_const</code>s type argument shouldn't be trusted because its sometimes a placeholder. Is that true for <code>mvar</code>s type arg too?</p>

#### [ Edward Ayers (Aug 11 2018 at 12:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/131948744):
<p>Also in <code>expr</code> what is <code>macro</code> used for?</p>

#### [ Edward Ayers (Aug 11 2018 at 12:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/131948754):
<p>Are they macros in the same sense as C macros?</p>

#### [ Mario Carneiro (Aug 11 2018 at 12:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/131948868):
<p>I am not sure about the reliability of <code>mvar</code> types; they aren't found in the local context so probably that's the only place the data is stored, meaning it has to be reliable</p>

#### [ Mario Carneiro (Aug 11 2018 at 12:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/131948870):
<p>still, <code>infer_type</code> should always work</p>

#### [ Mario Carneiro (Aug 11 2018 at 12:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/131948884):
<p><code>expr.macro</code> is a C++ thing. Those are basically "promises" to build an expr by some C++ code, you can't build them in lean</p>

#### [ Mario Carneiro (Aug 11 2018 at 12:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/131948888):
<p>You can unfold a macro and force it to evaluate</p>

#### [ Mario Carneiro (Aug 11 2018 at 12:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/131948951):
<p>They are used for <code>sorry</code>, meta recursive calls (which are not compiled to recursors like the non-meta versions), builtin projections, and they also are ephemeral structures in some specialized tactics</p>

#### [ Edward Ayers (Aug 11 2018 at 12:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/131949182):
<p>What are some examples of meta recursive calls?</p>

#### [ Mario Carneiro (Aug 11 2018 at 12:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/131949189):
<p><code>meta def rec := rec</code></p>

#### [ Mario Carneiro (Aug 11 2018 at 12:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/131949232):
<div class="codehilite"><pre><span></span>meta def rec : nat -&gt; nat | x := rec (x + 1)
</pre></div>

#### [ Edward Ayers (Aug 11 2018 at 12:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/131949263):
<p>What is a builtin projection?</p>

#### [ Mario Carneiro (Aug 11 2018 at 12:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/131949560):
<div class="codehilite"><pre><span></span>structure foo := (mynat : ℕ)
#print foo.mynat

-- @[reducible]
-- def foo.mynat : foo → ℕ :=
-- λ (c : foo), [foo.mynat c]
</pre></div>


<p>the thing in brackets is a macro</p>

#### [ Edward Ayers (Aug 11 2018 at 12:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/131949625):
<p>cool</p>

#### [ Edward Ayers (Aug 11 2018 at 12:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/131949675):
<p>I am reading <code>decalaration.lean</code>. And I came across</p>
<blockquote>
<p>Reducibility hints are used in the convertibility checker.<br>
When trying to solve a constraint such a</p>
<div class="codehilite"><pre><span></span>       (f ...) =?= (g ...)
</pre></div>


<p>where f and g are definitions, the checker has to decide which one will be unfolded.<br>
  If      f (g) is opaque,     then g (f) is unfolded if it is also not marked as opaque,<br>
  Else if f (g) is abbrev,     then f (g) is unfolded if g (f) is also not marked as abbrev,<br>
  Else if f and g are regular, then we unfold the one with the biggest definitional height.<br>
  Otherwise both are unfolded.</p>
</blockquote>
<p>Is there a way I can get programmatic access to the "definitional height" of a declaration (other than expanding it and calculating it myself)?</p>

#### [ Edward Ayers (Aug 11 2018 at 13:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/131949878):
<p>Ah it's an argument to <code>regular</code></p>

#### [ Edward Ayers (Aug 11 2018 at 13:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/131949886):
<p>sorry was on the next line.</p>

#### [ Edward Ayers (Aug 11 2018 at 13:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/131950012):
<p>So to get the definitional height you would do</p>
<div class="codehilite"><pre><span></span><span class="n">env</span> <span class="bp">&lt;-</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">get_env</span>
<span class="n">defn</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="o">(</span><span class="n">regular</span> <span class="n">h</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">)</span> <span class="bp">_</span>  <span class="bp">&lt;-</span> <span class="n">environment</span><span class="bp">.</span><span class="n">get</span> <span class="n">env</span> <span class="n">my_name</span>
<span class="n">return</span> <span class="n">h</span>
</pre></div>

#### [ Edward Ayers (Aug 11 2018 at 13:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/131950392):
<p>Is the convertability checker the same thing as the unifier?</p>

#### [ Edward Ayers (Aug 11 2018 at 13:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/131950628):
<p>What's the best way of adding some arbitrary data to the environment?. Eg, I've calculated a table for a tactic and I don't want to regenerate this table for every invocation of the tactic, I just want to retrieve it from the environment somehow.</p>

#### [ Mario Carneiro (Aug 11 2018 at 13:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/131951039):
<p>You can make a <code>def</code> containing the data</p>

#### [ Edward Ayers (Aug 11 2018 at 13:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/131951102):
<p>makes sense.</p>

#### [ Edward Ayers (Aug 11 2018 at 13:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/131951113):
<p>That is so much more straightforward than the Isabelle way!</p>

#### [ Mario Carneiro (Aug 11 2018 at 13:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/131951119):
<p>your ability to store arbitrary data in the environment is limited; for the most part it's just <code>expr</code>s</p>

#### [ Mario Carneiro (Aug 11 2018 at 13:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/131951166):
<p>Ideally you would want to store any vm_obj in the environment, but I don't know any way to do that besides reflecting it to an expr</p>

#### [ Edward Ayers (Aug 11 2018 at 13:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/131951168):
<p>I'd make a def with <code>mk_local_def</code> right?</p>

#### [ Mario Carneiro (Aug 11 2018 at 13:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/131951181):
<p>no, that's for local constants</p>

#### [ Edward Ayers (Aug 11 2018 at 13:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/131951225):
<p><code>add_meta_definition</code>?</p>

#### [ Mario Carneiro (Aug 11 2018 at 13:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/131951229):
<p>oh, I didn't know that one was there, that's useful</p>

#### [ Mario Carneiro (Aug 11 2018 at 13:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/131951230):
<p>yes</p>

#### [ Edward Ayers (Aug 11 2018 at 13:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/131951295):
<p>When I reflect to an <code>expr</code>, that means it actually has to build an <code>expr</code> tree which represents the data in some way right? It sounds like one would get performance issues if you wanted to save a gigantic rewrite table or similar.</p>

#### [ Mario Carneiro (Aug 11 2018 at 13:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/131951461):
<p>The <code>simp_lemmas</code> data structure is designed for handling big rewrite tables</p>

#### [ Mario Carneiro (Aug 11 2018 at 13:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/131951519):
<p>You can cache data in special types inside user attributes as well</p>

#### [ Edward Ayers (Aug 11 2018 at 14:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/131952210):
<p><code>simp_lemmas</code> looks good but I can only access the data through calls to <code>simp_lemmas.rewrite</code> so I am stuck with <code>simp</code>s implementation. Not necessarily a showstopper but I can't retrieve arbitrary exprs from it.</p>

#### [ Edward Ayers (Aug 11 2018 at 14:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/131952213):
<p>Please could you give some examples of this?</p>
<blockquote>
<p>You can cache data in special types inside user attributes as well</p>
</blockquote>

#### [ Mario Carneiro (Aug 11 2018 at 14:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/131952632):
<p>I'm referring to the <code>cache_ty</code> and <code>param_ty</code> in <code>user_attribute</code>, but it's not really a solution - <code>param_ty</code> has to be reflectable (so it is probably just stored as an <code>expr</code>) and <code>cache_ty</code> needs to be pure-functionally created from the list of all defs with the attribute in the environment (so it can only depend on things that are ultimately <code>expr</code>s). Still that cache has some promise</p>

#### [ Mario Carneiro (Aug 11 2018 at 14:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/131953023):
<p>I'm not positive this is actually working the way you would want, but here's the general idea:</p>
<div class="codehilite"><pre><span></span>structure mydata := (n : nat)

@[user_attribute]
meta def mydata_attr : user_attribute (name_map mydata) unit :=
{ name := `mydata, descr := &quot;stuff&quot;,
  cache_cfg := ⟨λ l, l.mfoldl (λ m n, do
    d ← get_decl n,
    v ← eval_expr mydata d.value,
    return (m.insert n v)) (name_map.mk _), []⟩ }

@[mydata] def X : mydata := ⟨500^2⟩

run_cmd do
  m ← mydata_attr.get_cache,
  v ← m.find ``X,
  trace v.n
</pre></div>

#### [ Edward Ayers (Aug 11 2018 at 15:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/131954639):
<ul>
<li>In <code>pexpr</code>, has it already disambiguated overloaded operators such as <code>+</code></li>
</ul>

#### [ Edward Ayers (Aug 11 2018 at 15:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/131954645):
<ul>
<li>is the process <code>pexpr -&gt; expr</code> called "elaboration"?</li>
</ul>

#### [ Edward Ayers (Aug 11 2018 at 15:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/131954830):
<ul>
<li>Filling in the implicit arguments of a <code>pexpr</code> is the same problem as finding a proof. So does it make sense to think of the process <code>pexpr -&gt; expr</code> as a kind of tactic driven by the structure of the <code>pexpr</code>?</li>
</ul>

#### [ Edward Ayers (Aug 11 2018 at 15:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/131954891):
<ul>
<li>It seems that you can't do <code>pexpr -&gt; expr</code> without recursively infering the types of the subpexprs of the <code>pexpr</code>. Is this right? In which case why not cache all of the types and then you never have to call <code>infer_type</code>? My guess would be that it would take up too much space.</li>
</ul>

#### [ Edward Ayers (Aug 11 2018 at 15:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/131955082):
<ul>
<li>Why does the <code>eval_expr α e</code> tactic need to be given the type of <code>e</code> as well?</li>
</ul>

#### [ Edward Ayers (Aug 11 2018 at 15:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/131955226):
<ul>
<li>Is the <code>target</code> tactic the same as <code>get_goals &gt;&gt;= (list.head &gt;&gt; return)</code>?</li>
</ul>

#### [ Edward Ayers (Aug 11 2018 at 15:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/131955636):
<ul>
<li>The definition of <code>intro</code> is</li>
</ul>
<div class="codehilite"><pre><span></span><span class="n">meta</span> <span class="n">def</span> <span class="n">intro</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="n">name</span><span class="o">)</span> <span class="o">:</span> <span class="n">tactic</span> <span class="n">expr</span> <span class="o">:=</span>
<span class="n">do</span> <span class="n">t</span> <span class="err">←</span> <span class="n">target</span><span class="o">,</span>
   <span class="k">if</span> <span class="n">expr</span><span class="bp">.</span><span class="n">is_pi</span> <span class="n">t</span> <span class="bp">∨</span> <span class="n">expr</span><span class="bp">.</span><span class="n">is_let</span> <span class="n">t</span> <span class="k">then</span> <span class="n">intro_core</span> <span class="n">n</span>
   <span class="k">else</span> <span class="n">whnf_target</span> <span class="bp">&gt;&gt;</span> <span class="n">intro_core</span> <span class="n">n</span>
</pre></div>


<p>But I can't figure out what I am doing wrong in the last two examples below:</p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">-&gt;</span> <span class="n">b</span> <span class="bp">-&gt;</span> <span class="n">a</span> <span class="o">:=</span>
<span class="k">begin</span>
    <span class="n">intro</span> <span class="n">hello</span><span class="o">,</span>
    <span class="n">sorry</span>
<span class="kn">end</span>

<span class="kn">example</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">-&gt;</span> <span class="n">b</span> <span class="bp">-&gt;</span> <span class="n">a</span> <span class="o">:=</span>
<span class="k">begin</span>
    <span class="n">intro_core</span> <span class="n">hello</span><span class="o">,</span> <span class="c1">-- errors here &quot;unknown identifier &#39;hello&#39;&quot;</span>
    <span class="n">sorry</span>
<span class="kn">end</span>

<span class="kn">example</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">-&gt;</span> <span class="n">b</span> <span class="bp">-&gt;</span> <span class="n">a</span> <span class="o">:=</span>
<span class="k">begin</span>
    <span class="n">whnf_target</span><span class="o">,</span>
    <span class="n">intro_core</span> <span class="n">hello</span><span class="o">,</span> <span class="c1">-- errors here &quot;unknown identifier &#39;hello&#39;&quot;</span>
    <span class="n">sorry</span>
<span class="kn">end</span>
</pre></div>

#### [ Edward Ayers (Aug 11 2018 at 15:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/131956067):
<ul>
<li>Does <code>get_unused_name n</code> just check if <code>n</code> is currently being used, and if not, sticks an <code>_1</code>/ <code>_2</code>/... on the end?</li>
</ul>

#### [ Edward Ayers (Aug 11 2018 at 15:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/131956115):
<ul>
<li>If I invoke <code>local_context</code>, will that always be a list of <code>local_const</code>s or are there ways of getting other forms of <code>expr</code> in the context?</li>
</ul>

#### [ Rob Lewis (Aug 11 2018 at 15:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/131956118):
<p>I can try to save Mario some time and answer a few of these....</p>
<blockquote>
<ul>
<li>In <code>pexpr</code>, has it already disambiguated overloaded operators such as <code>+</code></li>
</ul>
</blockquote>
<p>No. But note that <code>+</code> isn't "overloaded," exactly. <code>+</code> is notation for <code>has_add.add</code> which applies to any type with a <code>has_add</code> type class instance. A <code>pexpr</code> using <code>+</code> hasn't filled in the implicit type or the instance yet. And for notation that really is overloaded, a <code>pexpr</code> will represent the ambiguity with a macro, I think.</p>

#### [ Rob Lewis (Aug 11 2018 at 15:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/131956125):
<blockquote>
<ul>
<li>is the process <code>pexpr -&gt; expr</code> called "elaboration"?</li>
</ul>
</blockquote>
<p>Yes.</p>

#### [ Rob Lewis (Aug 11 2018 at 15:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/131956131):
<blockquote>
<ul>
<li>Filling in the implicit arguments of a <code>pexpr</code> is the same problem as finding a proof. So does it make sense to think of the process <code>pexpr -&gt; expr</code> as a kind of tactic driven by the structure of the <code>pexpr</code>?</li>
</ul>
</blockquote>
<p>Yeah, I guess. Notice the tactic <code>to_expr</code> does exactly this.</p>

#### [ Rob Lewis (Aug 11 2018 at 15:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/131956175):
<blockquote>
<ul>
<li>It seems that you can't do <code>pexpr -&gt; expr</code> without recursively infering the types of the subpexprs of the <code>pexpr</code>. Is this right? In which case why not cache all of the types and then you never have to call <code>infer_type</code>? My guess would be that it would take up too much space.</li>
</ul>
</blockquote>
<p>Are you asking why each <code>expr</code> object doesn't store its type? Yeah, this would take up a huge amount of space.</p>

#### [ Rob Lewis (Aug 11 2018 at 15:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/131956234):
<blockquote>
<ul>
<li>Why does the <code>eval_expr α e</code> tactic need to be given the type of <code>e</code> as well?</li>
</ul>
</blockquote>
<p>I'm not 100% clear on how <code>eval_expr</code> works, but here's my intuition, anyway. If you didn't give the expected type, you'd have to "guess" it by inferring the type of <code>e</code>, which would give you an <code>expr</code>, not a type. You need a way to go from this <code>expr</code> to a type, which is why you have the <code>[reflected α]</code> instance.</p>

#### [ Kevin Buzzard (Aug 11 2018 at 16:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/131956301):
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">-&gt;</span> <span class="n">b</span> <span class="bp">-&gt;</span> <span class="n">a</span> <span class="o">:=</span>
<span class="k">begin</span>
    <span class="n">intro_core</span> <span class="n">hello</span><span class="o">,</span> <span class="c1">-- errors here &quot;unknown identifier &#39;hello&#39;&quot;</span>
    <span class="n">sorry</span>
<span class="kn">end</span>
</pre></div>

#### [ Rob Lewis (Aug 11 2018 at 16:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/131956302):
<blockquote>
<ul>
<li>Is the <code>target</code> tactic the same as <code>get_goals &gt;&gt;= (list.head &gt;&gt; return)</code>?</li>
</ul>
</blockquote>
<p>I think, roughly. It's the type of the first goal metavariable.</p>

#### [ Rob Lewis (Aug 11 2018 at 16:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/131956314):
<blockquote>
<ul>
<li>The definition of <code>intro</code> is</li>
</ul>
<div class="codehilite"><pre><span></span><span class="n">meta</span> <span class="n">def</span> <span class="n">intro</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="n">name</span><span class="o">)</span> <span class="o">:</span> <span class="n">tactic</span> <span class="n">expr</span> <span class="o">:=</span>
<span class="n">do</span> <span class="n">t</span> <span class="err">←</span> <span class="n">target</span><span class="o">,</span>
   <span class="k">if</span> <span class="n">expr</span><span class="bp">.</span><span class="n">is_pi</span> <span class="n">t</span> <span class="bp">∨</span> <span class="n">expr</span><span class="bp">.</span><span class="n">is_let</span> <span class="n">t</span> <span class="k">then</span> <span class="n">intro_core</span> <span class="n">n</span>
   <span class="k">else</span> <span class="n">whnf_target</span> <span class="bp">&gt;&gt;</span> <span class="n">intro_core</span> <span class="n">n</span>
</pre></div>


<p>But I can't figure out what I am doing wrong in the last two examples below:</p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">-&gt;</span> <span class="n">b</span> <span class="bp">-&gt;</span> <span class="n">a</span> <span class="o">:=</span>
<span class="k">begin</span>
    <span class="n">intro</span> <span class="n">hello</span><span class="o">,</span>
    <span class="n">sorry</span>
<span class="kn">end</span>

<span class="kn">example</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">-&gt;</span> <span class="n">b</span> <span class="bp">-&gt;</span> <span class="n">a</span> <span class="o">:=</span>
<span class="k">begin</span>
    <span class="n">intro_core</span> <span class="n">hello</span><span class="o">,</span> <span class="c1">-- errors here &quot;unknown identifier &#39;hello&#39;&quot;</span>
    <span class="n">sorry</span>
<span class="kn">end</span>

<span class="kn">example</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">-&gt;</span> <span class="n">b</span> <span class="bp">-&gt;</span> <span class="n">a</span> <span class="o">:=</span>
<span class="k">begin</span>
    <span class="n">whnf_target</span><span class="o">,</span>
    <span class="n">intro_core</span> <span class="n">hello</span><span class="o">,</span> <span class="c1">-- errors here &quot;unknown identifier &#39;hello&#39;&quot;</span>
    <span class="n">sorry</span>
<span class="kn">end</span>
</pre></div>


</blockquote>
<p>You've noticed the difference between the tactic monad and "interactive mode." When you're using tactics for proofs, in begin/end blocks, they get parsed differently than when you're writing tactics. The <code>intro</code> in begin/end is actually tactic.interactive.intro.</p>

#### [ Edward Ayers (Aug 11 2018 at 16:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/131956358):
<blockquote>
<p>I think, roughly. It's the type of the first goal metavariable.</p>
</blockquote>
<p>The docs for <code>target</code> confused me because they say it returns the "main goal" but this seems to always be the first goal.</p>

#### [ Rob Lewis (Aug 11 2018 at 16:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/131956359):
<p><code>intro_core</code> isn't an interactive tactic. It expects a name, which you'd have to give in the form <code> `hello </code>.</p>

#### [ Rob Lewis (Aug 11 2018 at 16:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/131956373):
<p><code>tactic.intro</code> expects the same. <code>tactic.interactive.intro</code> expects some text to follow that it will parse into a name.</p>

#### [ Kevin Buzzard (Aug 11 2018 at 16:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/131956386):
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">-&gt;</span> <span class="n">b</span> <span class="bp">-&gt;</span> <span class="n">a</span> <span class="o">:=</span>
<span class="k">begin</span>
    <span class="n">intro_core</span> <span class="n">hello</span><span class="o">,</span> <span class="c1">-- errors here &quot;unknown identifier &#39;hello&#39;&quot;</span>
    <span class="n">sorry</span>
<span class="kn">end</span>
</pre></div>


<p>The <code>intro</code> in a <code>begin end</code> block is <code>tactic.interactive.intro</code>not <code>tactic.intro</code>. I don't know if this helps or whether you're already way ahead of this, but it was something that confused me for a while.</p>
<p>PS just beaten to it by Rob :-)</p>

#### [ Mario Carneiro (Aug 11 2018 at 16:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/131956462):
<p>the "main goal" is the first goal</p>

#### [ Rob Lewis (Aug 11 2018 at 16:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/131956469):
<blockquote>
<ul>
<li>If I invoke <code>local_context</code>, will that always be a list of <code>local_const</code>s or are there ways of getting other forms of <code>expr</code> in the context?</li>
</ul>
</blockquote>
<p>I think it's only <code>local_const</code> exprs, yes.</p>

#### [ Rob Lewis (Aug 11 2018 at 16:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/131956568):
<blockquote>
<ul>
<li>Does <code>get_unused_name n</code> just check if <code>n</code> is currently being used, and if not, sticks an <code>_1</code>/ <code>_2</code>/... on the end?</li>
</ul>
</blockquote>
<p>This one I'm not sure, I've never really paid attention. It will give you a name that starts with <code>n</code> that won't conflict with anything.</p>

#### [ Mario Carneiro (Aug 11 2018 at 16:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/131956570):
<blockquote>
<p>Why does the eval_expr α e tactic need to be given the type of e as well?</p>
</blockquote>
<p>This is done for typechecking purposes. You are given <code>e</code> which is an <code>expr</code>, but you want to return something of type <code>α</code>. What is <code>α</code>? You would need to have a function <code>e.type : expr -&gt; Type</code> to define "the type of <code>e</code>", but that doesn't work because of universe issues. So instead you just assert the type you want and lean checks it (I think, maybe it just crashes if you got it wrong)</p>

#### [ Kevin Buzzard (Aug 11 2018 at 16:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/131956630):
<p>could <code>has_one.one</code> be an example of an <code>expr</code>? Or some such thing? I'm wondering when Lean decides that <code>1</code> should be a natural if it can't think of any better ideas.</p>

#### [ Mario Carneiro (Aug 11 2018 at 16:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/131956680):
<p><code>has_one.one</code> has a big pi type, but <code> `(has_one.one)</code> is an expr</p>

#### [ Rob Lewis (Aug 11 2018 at 16:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/131956690):
<p>I think it's specifically numerals that default to <code>nat</code> if there's no other information, right? This happens at elaboration time.</p>

#### [ Edward Ayers (Aug 11 2018 at 19:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/131962977):
<p>What's the best way to discover if <code>expr</code> e has form <code>Exists (a : A), B a</code>? Or alternatively <code>Exists p</code>?</p>

#### [ Simon Hudon (Aug 11 2018 at 19:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/131963019):
<p>One simple way is to do:</p>
<div class="codehilite"><pre><span></span><span class="n">do</span> <span class="bp">`</span><span class="o">(</span><span class="n">Exists</span> <span class="err">%%</span><span class="n">p</span><span class="o">)</span> <span class="bp">&lt;-</span> <span class="n">pure</span> <span class="n">e</span> <span class="bp">|</span> <span class="n">fail</span> <span class="s2">&quot;e is in bad shape&quot;</span><span class="o">,</span>
       <span class="c1">-- do stuff with `p`</span>
</pre></div>

#### [ Edward Ayers (Aug 12 2018 at 16:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/131999207):
<ul>
<li>Am I right in thinking that <code>rbtree</code> doesn't come with function to remove items from it?</li>
</ul>

#### [ Mario Carneiro (Aug 12 2018 at 16:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/131999315):
<p>I... guess you're right</p>

#### [ Mario Carneiro (Aug 12 2018 at 16:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/131999368):
<p>that's a bit annoying, I was hoping not to have to touch <code>rbtree</code></p>

#### [ Edward Ayers (Aug 12 2018 at 17:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132001112):
<p>Could I use <code>rb_map</code>, which does have this?</p>

#### [ Edward Ayers (Aug 12 2018 at 18:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132002458):
<p>If I do <code>a &lt;|&gt; b</code> for the <code>option</code> type, will the VM not evaluate <code>b</code> if <code>a</code> is <code>some _</code>?</p>

#### [ Edward Ayers (Aug 12 2018 at 19:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132004998):
<p>Is anyone doing 23 trees in mathlib?</p>

#### [ Edward Ayers (Aug 12 2018 at 19:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132005004):
<p>I've started coding it up</p>

#### [ Kevin Buzzard (Aug 12 2018 at 19:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132005866):
<p>Is it maths?</p>

#### [ Edward Ayers (Aug 12 2018 at 20:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132006154):
<p>It's a datastructure</p>

#### [ Edward Ayers (Aug 12 2018 at 20:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132006159):
<p>like rbtree</p>

#### [ Edward Ayers (Aug 13 2018 at 00:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132012981):
<p>Is there a way to have conditionals in <code>match</code> statements? Eg something like:</p>
<div class="codehilite"><pre><span></span><span class="k">match</span> <span class="n">x</span> <span class="k">with</span>
<span class="bp">|</span><span class="o">(</span><span class="n">some</span> <span class="n">y</span><span class="o">)</span>  <span class="n">where</span>  <span class="n">y</span> <span class="bp">&gt;</span> <span class="mi">5</span> <span class="o">:=</span> <span class="s2">&quot;hello&quot;</span>
<span class="bp">|_</span> <span class="o">:=</span> <span class="s2">&quot;nope&quot;</span>
<span class="kn">end</span>
</pre></div>

#### [ Simon Hudon (Aug 13 2018 at 00:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132013028):
<p><code>"nope"</code></p>

#### [ Simon Hudon (Aug 13 2018 at 00:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132013031):
<p>No conditions built into <code>match</code></p>

#### [ Mario Carneiro (Aug 13 2018 at 02:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132015917):
<blockquote>
<p>If I do a &lt;|&gt; b for the option type, will the VM not evaluate b if a is some _?</p>
</blockquote>
<p>It will evaluate both sides, unless <code>option.orelse</code> is inlined. If you want to avoid this, you can make an <code>option.orelse'</code> that takes a <code>thunk (option A)</code> for its second argument</p>

#### [ Mario Carneiro (Aug 13 2018 at 02:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132015937):
<blockquote>
<p>Is anyone doing 23 trees in mathlib? I've started coding it up</p>
</blockquote>
<p>I have no current plans for this, go ahead. We would be happy to take it</p>

#### [ Mario Carneiro (Aug 13 2018 at 02:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132015940):
<blockquote>
<p>Is there a way to have conditionals in match statements?</p>
</blockquote>
<p>No, as Simon said; although in this case you can write the following:</p>
<div class="codehilite"><pre><span></span>match x with
| (some (y+6)) := &quot;hello&quot;
| _ := &quot;nope&quot;
end
</pre></div>


<p>I would recommend just using <code>if</code> though.</p>

#### [ Patrick Massot (Aug 13 2018 at 02:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132015956):
<p>What if he gets tired towards the middle of the task, and ends up with 11 trees instead of 23?</p>

#### [ Simon Hudon (Aug 13 2018 at 02:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132016137):
<p>That's a linked list. We won't be so welcoming because we have those.</p>

#### [ Patrick Massot (Aug 13 2018 at 02:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132016190):
<p>Damn it. What was the probability that roughly cutting in half the number 23 would lead to another meaningful sentence?</p>

#### [ Simon Hudon (Aug 13 2018 at 02:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132016191):
<p>Btw, why do we want 2-3 trees while we have red-back trees? What do you get from 2-3 trees that you don't get from red-black trees?</p>

#### [ Mario Carneiro (Aug 13 2018 at 02:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132016192):
<p>I guess with 12 trees he will have a trie</p>

#### [ Mario Carneiro (Aug 13 2018 at 02:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132016239):
<p>different performance characteristics... I'm okay with implementing datastructures for their own sake because of this</p>

#### [ Mario Carneiro (Aug 13 2018 at 02:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132016289):
<p>but it's true that rb trees already implement the same API as it were, so if you are a programmer who needs a map type and doesn't want to bother with writing data structures you can use them instead</p>

#### [ Simon Hudon (Aug 13 2018 at 02:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132016293):
<p>As I understand it, a red-black tree is basically a 2-3 tree where the balancing invariant is formulated in terms of tree height instead of node degree, that's why I'm surprised it would get a different performance profile</p>

#### [ Mario Carneiro (Aug 13 2018 at 02:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132016412):
<p>From <a href="https://www.cs.purdue.edu/homes/ayg/CS251/slides/chap13b.pdf" target="_blank" title="https://www.cs.purdue.edu/homes/ayg/CS251/slides/chap13b.pdf">https://www.cs.purdue.edu/homes/ayg/CS251/slides/chap13b.pdf</a> , it seems like 2-3 trees or 2-3-4 trees are actually just simpler versions of rb trees</p>

#### [ Mario Carneiro (Aug 13 2018 at 02:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132016455):
<p>the advantage of rb trees is normalizing the node layout, but this doesn't matter when you are writing inductives in lean</p>

#### [ Sebastian Ullrich (Aug 13 2018 at 02:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132016680):
<p>Huh, that's an interesting slide format</p>

#### [ Kevin Buzzard (Aug 13 2018 at 12:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132037220):
<blockquote>
<p>Huh, that's an interesting slide format</p>
</blockquote>
<p>Judging by the name of the pdf, this might be a chapter from a book, and books are still traditionally in portrait format I guess.</p>

#### [ Gabriel Ebner (Aug 13 2018 at 13:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132038925):
<p>Those are definitely slides, but more like old-school ones for overhead projectors.</p>

#### [ Patrick Massot (Aug 13 2018 at 13:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132038975):
<p>Maybe Sebastian was referring to the Batman delirium at the end</p>

#### [ Edward Ayers (Aug 13 2018 at 19:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132062075):
<p>Yes I'm just treating making 23 trees as another exercise. I copied the implementation details from Isabelle and then added dependent types to it. I managed to prove that my trees are balanced using just dependent types (each node has a height param in its type). It was fun to see that it worked and I learned a lot. I made no considerations for performance so <code>rbtree</code> is still better and more concise. The deletion algo for 23 trees is horrifying so there is likely a mistake in there, but at least I proved that it's balanced!</p>
<p>Here is a link to the source but I've made no attempt to make it readable yet. I haven't even tested it. <br>
<a href="https://github.com/EdAyers/mathlib/blob/tree23/data/tree23.lean" target="_blank" title="https://github.com/EdAyers/mathlib/blob/tree23/data/tree23.lean">https://github.com/EdAyers/mathlib/blob/tree23/data/tree23.lean</a></p>
<p>Some thoughts from doing this,<br>
- It can be difficult to decide which typeclasses to use. Should I use <code>linear_order</code>? <code>decidable_rel</code>? And so on.<br>
- The coercions from <code>decidable</code> to if statements are kind of magical.<br>
-  There is a lemma <code>lt_min_key_imp_outside</code> which I basically did by taking a random walk through the space of valid tactics until <code>no goals</code> appeared. Any tips on how this can be tightened up would be appreciated.<br>
- Proving anything about the <code>del</code> method will be a nightmare. So if the deletion method for rb trees is simpler then I am happy to abandon these.<br>
- The main thing I learnt is that you are much better off using non-dependent-type driven datatypes and then restricting with propositions at the end. Using dependent types just makes coding too tedious.</p>

#### [ Edward Ayers (Aug 13 2018 at 20:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132062193):
<p>I also had an attempt at proving some things about <code>rbtree</code>s but it is very tedious. I think that I am not using the automation very effectively.</p>

#### [ Edward Ayers (Aug 13 2018 at 20:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132062277):
<p>I'm going to use <code>native.rb_tree</code> in the future instead, but I don't regret implementing this because it taught me a lot about Lean.</p>

#### [ Edward Ayers (Aug 13 2018 at 20:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132062574):
<p>My dream was that I wouldn't have to write tests for my code, because I could just prove that it is correct!</p>

#### [ Simon Hudon (Aug 13 2018 at 20:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132062764):
<p>Have you put your code somewhere on github. We can look at it to see if we can make your proving more effective</p>

#### [ Edward Ayers (Aug 13 2018 at 20:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132062860):
<p>yes see link above in this thread</p>

#### [ Edward Ayers (Aug 13 2018 at 20:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132062870):
<p><a href="https://github.com/EdAyers/mathlib/blob/tree23/data/tree23.lean" target="_blank" title="https://github.com/EdAyers/mathlib/blob/tree23/data/tree23.lean">https://github.com/EdAyers/mathlib/blob/tree23/data/tree23.lean</a></p>

#### [ Edward Ayers (Aug 13 2018 at 20:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132062916):
<p>I'll push the rbtree experiments in a few hours.</p>

#### [ Edward Ayers (Aug 15 2018 at 20:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132190818):
<p>Why is it that <code>#check λ x, x + 1</code> is <code> ℕ → ℕ</code> and not <code>[has_add ?m] [has_one ?m] ?m -&gt; ?m</code></p>

#### [ Edward Ayers (Aug 15 2018 at 20:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132190837):
<p>What is causing the elaborator to default to <code>nat</code>?</p>

#### [ Bryan Gin-ge Chen (Aug 15 2018 at 20:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132190906):
<p>(deleted)</p>

#### [ Kenny Lau (Aug 15 2018 at 20:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132190908):
<p>I think <code>1</code> is default to <code>nat</code></p>

#### [ Edward Ayers (Aug 15 2018 at 20:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132191067):
<p>Right but where is the defaultness set?</p>

#### [ Kevin Buzzard (Aug 15 2018 at 20:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132191292):
<p>At some point in the elaboration process, Lean <em>sometimes</em> says "if I can't figure out what that 1 is, I'm going to assume it's a nat". I think the point this occurs is near the end, if at all. Maybe you can even concoct something where <code>example</code> behaves differently to <code>definition</code> using this sort of thing.</p>

#### [ Kevin Buzzard (Aug 15 2018 at 20:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132191371):
<p>(deleted nonsense)</p>

#### [ Edward Ayers (Aug 15 2018 at 20:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132191517):
<p>Perhaps <code>1</code> is always <code>nat</code>, and there is a type coercion from <code>nat</code> to all of the other kinds of numbers?</p>

#### [ Kevin Buzzard (Aug 15 2018 at 20:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132191535):
<p>That's not how it works, I'm pretty sure.</p>

#### [ Kevin Buzzard (Aug 15 2018 at 20:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132191555):
<p>Unfortunately, as I found out earlier this week, it's very difficult to switch the number literal parser off.</p>

#### [ Kevin Buzzard (Aug 15 2018 at 20:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132191572):
<p><code>1</code> is <code>has_one.one</code></p>

#### [ Edward Ayers (Aug 15 2018 at 20:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132191626):
<p>The thing I can't figure out is if the <code>nat</code> default is set somewhere in <code>init</code> or whether it is baked in to the elaborator.</p>

#### [ Kevin Buzzard (Aug 15 2018 at 20:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132191902):
<p>I think it is baked into the elaborator. I think that <code>#check</code> cannot possibly return <code>[has_add ?m] [has_one ?m] ...</code> because I don't think Lean thinks these are part of the expression.</p>

#### [ Kevin Buzzard (Aug 15 2018 at 20:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132191960):
<p>So eventually it gets to a point where it can't figure out where this type class inference thing is coming from and at that point it decides it's going to go for nat. You should check all this with an expert.</p>

#### [ Mario Carneiro (Aug 15 2018 at 20:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132192958):
<p>The nat default is baked into the elaborator, but it is not necessary for it to operate</p>

#### [ Mario Carneiro (Aug 15 2018 at 20:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132192998):
<p>it could just as easily return <code>?m -&gt; ?m</code>, and there would be (hidden) subgoals for those typeclasses</p>

#### [ Mario Carneiro (Aug 15 2018 at 20:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132193030):
<blockquote>
<p>Perhaps 1 is always nat, and there is a type coercion from nat to all of the other kinds of numbers?</p>
</blockquote>
<p>Lean used to work like this, but the current version uses a polymorphic 1 function</p>

#### [ Mario Carneiro (Aug 15 2018 at 21:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132193177):
<p>I find the nat default distateful precisely because it's the only thing about lean definitions which is not configured within lean</p>

#### [ Mario Carneiro (Aug 15 2018 at 21:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132193240):
<p>if kevin decided to write his own core.lean with <code>xnat</code>, lean would probably complain</p>

#### [ Mario Carneiro (Aug 15 2018 at 21:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132193396):
<p><a href="https://github.com/leanprover/lean/blob/master/src/frontends/lean/elaborator.cpp#L3609-L3610" target="_blank" title="https://github.com/leanprover/lean/blob/master/src/frontends/lean/elaborator.cpp#L3609-L3610">https://github.com/leanprover/lean/blob/master/src/frontends/lean/elaborator.cpp#L3609-L3610</a></p>

#### [ Edward Ayers (Aug 16 2018 at 16:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132241830):
<p>I can see why Leo did this though, since <code>nat</code> is initial with respect to <code>has_one</code> and <code>has_add</code> so you don't really lose any generality by doing this and 90% of the time you mean <code>nat</code> anyway.</p>

#### [ Mario Carneiro (Aug 16 2018 at 16:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132242032):
<p>note again that lean does <em>not</em> use anything like <code>nat.cast</code> to get an arbitrary value of type <code>A</code> from a nat</p>

#### [ Mario Carneiro (Aug 16 2018 at 16:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132242070):
<p>If you type <code>4 : A</code>, it is translated by the parser to <code>bit0 (bit0 1)</code>, where <code>bit0</code> and <code>has_one.one</code> are polymorphic functions</p>

#### [ Mario Carneiro (Aug 16 2018 at 16:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132242083):
<p>this term will make absolutely no reference to <code>nat</code></p>

#### [ Mario Carneiro (Aug 16 2018 at 16:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132242194):
<p>The reason this was done, I believe, is that without a default type being assigned as a last resort, you can never write a numeral without a type ascription somewhere, so a beginner will type <code>#eval 2 + 2</code> and get a weird error message instead of the obvious answer</p>

#### [ Edward Ayers (Aug 16 2018 at 16:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132242196):
<p>What is the difference between synthesizing and elaborating?</p>

#### [ Edward Ayers (Aug 16 2018 at 16:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132242261):
<p>My guess is synthesizing is when the elaborator tries to guess an expr for a given type sig</p>

#### [ Mario Carneiro (Aug 16 2018 at 16:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132242270):
<p>I'm not sure there is a difference, they are both fairly general terms</p>

#### [ Mario Carneiro (Aug 16 2018 at 16:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132242360):
<p>elaboration is broadly the process of taking a parsed pre-expression, an AST, and including and inferring all missing type information to make it a valid term of the formal logic</p>

#### [ Mario Carneiro (Aug 16 2018 at 16:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132242385):
<p>synthesis is just what you call putting data into one of these holes</p>

#### [ Edward Ayers (Aug 16 2018 at 16:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132242406):
<p>Ok. So when you make the proof to a lemma by writing out a proof term. Making that a valid <code>expr</code> is elaboration. Does the process of making a valid proof term using <code>begin ... end</code> also count as elaboration?</p>

#### [ Mario Carneiro (Aug 16 2018 at 16:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132242407):
<p>There are multiple methods used by the elaborator to synthesize expressions, but the major workhorses are unification and typeclass inference</p>

#### [ Mario Carneiro (Aug 16 2018 at 16:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132242482):
<p>I'm not sure I would call tactic evaluation a part of elaboration, but it occurs in the middle of the elaboration cycle, yes</p>

#### [ Mario Carneiro (Aug 16 2018 at 16:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132242512):
<p>you could view the tactic framework as a giant plugin to the elaborator</p>

#### [ Edward Ayers (Aug 16 2018 at 16:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132242526):
<p>Yes that's how I'm viewing it. It's a beautiful way of doing it.</p>

#### [ Edward Ayers (Aug 16 2018 at 16:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132242701):
<p>When I write <code>def asdf (myarg : mytype . mytactic) : ... := ...</code>. I can't quite figure out what the tactic is doing. Is Lean making a tactic state with the goal as <code>mytype</code> and <code>myarg</code> as a local constant?</p>

#### [ Edward Ayers (Aug 16 2018 at 16:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132242779):
<p>So I use this by writing <code>asdf (myvalue)</code>. Or is the idea that the <code>mytactic</code> should be used to synthesize <code>myarg</code> if it is not provided explicitly?</p>

#### [ Edward Ayers (Aug 16 2018 at 16:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132243188):
<p>Also, <code>expr</code> has the argument <code>elaborated := tt</code>. I am guessing that <code>expr tt</code> is a term that has been elaborated, and hence is valid. Whereas a <code>expr ff</code> has not been checked to be valid, eg I just made a nonsense term myself from the <code>expr</code> constructors. So <code>expr ff</code>/<code>expr tt</code> is like <code>term</code>/<code>cterm</code> in Isabelle.</p>

#### [ Edward Ayers (Aug 16 2018 at 16:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132243213):
<p>But then I can make <code>expr tt</code> from the <code>expr</code> constructors too, so that can't be it.</p>

#### [ Edward Ayers (Aug 16 2018 at 16:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132243275):
<p>But in that case I can't see what the difference could be between <code>expr tt</code> and <code>expr ff</code>.</p>

#### [ Mario Carneiro (Aug 16 2018 at 16:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132243775):
<blockquote>
<p>Or is the idea that the mytactic should be used to synthesize myarg if it is not provided explicitly?</p>
</blockquote>
<p>this</p>

#### [ Mario Carneiro (Aug 16 2018 at 16:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132243807):
<p>it is a variant on optional parameters where the default value is synthesized by a tactic</p>

#### [ Mario Carneiro (Aug 16 2018 at 16:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132243887):
<blockquote>
<p>Whereas a expr ff has not been checked to be valid, eg I just made a nonsense term myself from the expr constructors. </p>
</blockquote>
<p>Not quite. <code>expr ff</code> is the same as <code>pexpr</code>, and it represents those pre-expressions I mentioned</p>

#### [ Edward Ayers (Aug 16 2018 at 16:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132243924):
<p>So an <code>expr ff</code> can have wildcard holes in it?</p>

#### [ Mario Carneiro (Aug 16 2018 at 16:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132243941):
<p>They actually differ from <code>expr</code> structurally, i.e. if I write <code>x + y</code> then the <code>pexpr</code> for this is <code>has_add.add x y</code> with 2 arguments, and the <code>expr</code> is <code>has_add.add ?m1 ?m2 x y</code> or <code>has_add.add nat nat.has_add x y</code> with 4 arguments</p>

#### [ Edward Ayers (Aug 16 2018 at 16:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132244028):
<p>nice</p>

#### [ Mario Carneiro (Aug 16 2018 at 16:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132244041):
<p>they could have been defined as separate inductive types, but they share enough of the major structure that it seemed redundant</p>

#### [ Mario Carneiro (Aug 16 2018 at 16:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132244073):
<p>lean 4 will have these separate, with <code>pexpr</code> becoming <code>syntax</code> which is completely different</p>

#### [ Mario Carneiro (Aug 16 2018 at 16:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132244129):
<p>it will be much more like an AST for lean</p>

#### [ Edward Ayers (Aug 16 2018 at 16:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132244157):
<p>Ah I just found <code>@[reducible] meta def pexpr := expr ff</code> in source</p>

#### [ Edward Ayers (Aug 16 2018 at 16:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132244276):
<p><code>meta constant pexpr.mk_placeholder : pexpr</code> seems to be the magic <code>constant</code> that lets you do placeholders. You can't use metavariables because you might not be in a tactic monad so you can't make fresh ones.</p>

#### [ Mario Carneiro (Aug 16 2018 at 16:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132244306):
<p>mk_placeholder is basically the AST corresponding to <code>_</code> as a token</p>

#### [ Edward Ayers (Aug 16 2018 at 16:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132244319):
<p>Am I right in thinking that <em>the</em> placeholder is distinct from metavars, but elaborating a <code>pexpr</code> turns these into metavars?</p>

#### [ Mario Carneiro (Aug 16 2018 at 16:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132244328):
<p>there is only one, and it is elaborated to a new metavariable every time</p>

#### [ Edward Ayers (Aug 16 2018 at 16:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132244555):
<p>Will the elaborator for Lean 4 be written in Lean rather than C++?</p>

#### [ Mario Carneiro (Aug 16 2018 at 16:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132244569):
<p>parser yes, elaborator maybe</p>

#### [ Edward Ayers (Aug 16 2018 at 16:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132244612):
<p>That would blow my mind</p>

#### [ Mario Carneiro (Aug 16 2018 at 16:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132244634):
<p>I think the idea is to completely self host</p>

#### [ Edward Ayers (Aug 16 2018 at 16:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132244638):
<p>I can't wait for Lean 4</p>

#### [ Mario Carneiro (Aug 16 2018 at 16:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132244653):
<p>but it's hard, not the least because the lean VM is currently not efficient enough to support this</p>

#### [ Mario Carneiro (Aug 16 2018 at 16:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132244670):
<p>so they will need to implement a real lean compiler to machine code</p>

#### [ Edward Ayers (Aug 16 2018 at 16:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132244677):
<p>To do the elaborator in Lean you would need some kind of super simple bootstrap elaborator in C++ with everything explicit and build up from there.</p>

#### [ Mario Carneiro (Aug 16 2018 at 16:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132244767):
<p>even in core lean for much of the files you don't have the tactic framework set up yet so it's all explicit terms</p>

#### [ Mario Carneiro (Aug 16 2018 at 16:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132244804):
<p>I don't know exactly how the full bootstrap process would work, it might just run itself on the previous version of lean to avoid messy business</p>

#### [ Edward Ayers (Aug 16 2018 at 16:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132244873):
<p>Right but then you can't build Lean from scratch which would be sad, you would then need to maintain both C++ and Lean elaborators.</p>

#### [ Mario Carneiro (Aug 16 2018 at 17:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132245452):
<p><span class="user-mention" data-user-id="110024">@Sebastian Ullrich</span> can tell you more about the extent of current bootstrapping plans</p>

#### [ Edward Ayers (Aug 16 2018 at 17:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132248684):
<p>I'm reading through the kernel code. Let me just write down what I think is happening and then I can be corrected.<br>
- <code>expr.cpp</code> is doing roughly the same thing as <code>expr.lean</code>, just a big inductive type with helper methods.<br>
- <code>type_checker</code> infers the type for a given <code>expr</code> or throws if it isn't a valid expr. Saying that a given <code>expr</code> typechecks is equivalent to saying that the <code>expr</code> can be built just using the inference rules of CIC (up to being able to synthesize metavars later). <br>
- You inject a <code>normalizer_extension</code> into the kernel to dictate how the typechecker should put terms in WHNF. If there is a bug in the injected <code>normalizer_extension</code> then the kernel will be compromised too. So quotients and inductives are normalizer_extensions.<br>
- So the kernel is happy when it is given an environment, which is an ordered dictionary of declarations indexed by <code>name</code>, and all of the declarations' <code>expr</code>s typecheck.</p>

#### [ Edward Ayers (Aug 16 2018 at 18:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132249735):
<p>In the <a href="https://leanprover.github.io/papers/system.pdf" target="_blank" title="https://leanprover.github.io/papers/system.pdf">system description</a> for Lean it says that the typechecker can also produce unification constraints, but this feature doesn't seem to be in the<code>type_checker.h</code>, although I could not be reading thoroughly enough, where is the code that does type_checking and also spits out some unification constraints?</p>

#### [ Leonardo de Moura (Aug 16 2018 at 18:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132250626):
<p><span class="user-mention" data-user-id="121918">@Edward Ayers</span> You have to go back in time to see the unification constraints :) <a href="https://github.com/leanprover/lean/blob/CADE25/src/kernel/type_checker.h" target="_blank" title="https://github.com/leanprover/lean/blob/CADE25/src/kernel/type_checker.h">https://github.com/leanprover/lean/blob/CADE25/src/kernel/type_checker.h</a><br>
We abandoned this approach in Lean 3. Now, the kernel type checker is simpler and has no support for meta-variables (unification variables). The elaborator uses a different module for inferring types and solving unification constraints.</p>

#### [ Sebastian Ullrich (Aug 16 2018 at 18:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132250884):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> </p>
<blockquote>
<p>I don't know exactly how the full bootstrap process would work, it might just run itself on the previous version of lean to avoid messy business</p>
</blockquote>
<p>Yes, this is how all bootstrapping compilers work. But instead of a binary file, we want to store the previous version as extracted C++ code, which should be at least slightly more inspectable and git-friendly</p>

#### [ Edward Ayers (Aug 16 2018 at 18:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132250969):
<p>Thanks Leo. Also <code>elab_context.h</code> is confusing me. The comment talks about <code>tactic_context</code>. But I can't find any other mentions of <code>tactic_context</code>. I also can't spot the definition of <code>type_context</code>, only <code>type_context_old</code></p>

#### [ Edward Ayers (Aug 16 2018 at 19:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132252758):
<p>I'm really keen to see the C++ code that is used to keep track of metavariables, local context and so on while a tactic or elaborator is being run. It seems to be <code>type_context_old</code> but I'm not sure because of the <code>old</code> suffix.</p>

#### [ Gabriel Ebner (Aug 16 2018 at 19:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132252927):
<p><code>type_context</code> was renamed to <code>type_context_old</code> in the preparation of the changes for Lean 4.  You should really be looking at <code>type_context_old</code>, it was the <code>type_context</code> for most of Lean 3.</p>

#### [ Edward Ayers (Aug 16 2018 at 19:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132253032):
<p>In the <code>type_context.h</code> there is a large comment starting with <code>NEW DESIGN notes. (This is work in progress)</code>, is this how Lean 3 works or is it how Lean 4 works?</p>

#### [ Gabriel Ebner (Aug 16 2018 at 19:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132253156):
<p>This is a change that was introduced late in Lean 3, and the todo is also implemented now with the <code>unfreeze_local_intstances</code> tactic.</p>

#### [ Simon Hudon (Aug 16 2018 at 19:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132253773):
<p><span class="user-mention" data-user-id="121918">@Edward Ayers</span> I recommend you start using different topics for your different questions so that other people may determine at a glance if the discussion is relevant to what they're working on.</p>

#### [ Edward Ayers (Aug 16 2018 at 19:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132253799):
<p>ok will do</p>

#### [ Simon Hudon (Aug 16 2018 at 19:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132253828):
<p>Thanks!</p>

#### [ Kevin Buzzard (Aug 16 2018 at 20:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Ed%27s%20question%20barrage/near/132257907):
<p>I like the question barrage :-) but I do see Simon's logic. I often start new threads with more descriptive titles now and it works better for search when I come back to them later.</p>


{% endraw %}
