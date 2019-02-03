---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/81153Leanpuzzle3.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [Lean puzzle #3](https://leanprover-community.github.io/archive/113488general/81153Leanpuzzle3.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Keeley Hoek (Nov 27 2018 at 09:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20puzzle%20%233/near/148625272):
<p>Next up in my series of lean puzzles, consider the following code snippet:</p>
<div class="codehilite"><pre><span></span><span class="kn">universe</span> <span class="n">u</span>

<span class="n">meta</span> <span class="n">def</span> <span class="n">do_some_nonsense</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">(</span><span class="n">t</span> <span class="o">:</span> <span class="n">tactic</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="n">tactic</span> <span class="n">α</span> <span class="o">:=</span>
  <span class="n">tactic</span><span class="bp">.</span><span class="n">down</span> <span class="o">(</span><span class="n">tactic</span><span class="bp">.</span><span class="n">up</span> <span class="o">(</span><span class="n">tactic</span><span class="bp">.</span><span class="n">trace</span> <span class="s2">&quot;ELLO1&quot;</span><span class="o">)</span> <span class="bp">&gt;&gt;</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">up</span> <span class="n">t</span><span class="o">)</span>

<span class="n">meta</span> <span class="n">def</span> <span class="n">do_some_nonsense&#39;</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">(</span><span class="n">t</span> <span class="o">:</span> <span class="n">tactic</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="n">tactic</span> <span class="n">α</span> <span class="o">:=</span>
  <span class="o">(</span><span class="n">tactic</span><span class="bp">.</span><span class="n">up</span> <span class="o">(</span><span class="n">tactic</span><span class="bp">.</span><span class="n">trace</span> <span class="s2">&quot;ELLO2&quot;</span><span class="o">)</span> <span class="bp">&gt;&gt;</span> <span class="n">t</span><span class="o">)</span>

<span class="n">meta</span> <span class="n">def</span> <span class="n">tactic_bind_override</span> <span class="o">{</span><span class="n">α</span> <span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">(</span><span class="n">t₁</span> <span class="o">:</span> <span class="n">tactic</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">t₂</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">tactic</span> <span class="n">β</span><span class="o">)</span> <span class="o">:</span> <span class="n">tactic</span> <span class="n">β</span> <span class="o">:=</span>
<span class="c1">-- do_some_nonsense (t₁ &gt;&gt;= (λ a, t₂ a))</span>
<span class="n">do_some_nonsense&#39;</span> <span class="o">(</span><span class="n">t₁</span> <span class="bp">&gt;&gt;=</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">a</span><span class="o">,</span> <span class="n">t₂</span> <span class="n">a</span><span class="o">))</span>

<span class="bp">@</span><span class="o">[</span><span class="kn">inline</span><span class="o">,</span> <span class="kn">instance</span><span class="o">,</span> <span class="n">priority</span> <span class="mi">2000</span><span class="o">]</span> <span class="n">meta</span> <span class="n">def</span> <span class="n">bind_override</span> <span class="o">:</span> <span class="n">has_bind</span> <span class="n">tactic</span> <span class="o">:=</span>
<span class="bp">⟨@</span><span class="n">tactic_bind_override</span><span class="bp">⟩</span>

<span class="n">meta</span> <span class="n">def</span> <span class="n">go</span> <span class="o">:</span> <span class="n">tactic</span> <span class="n">unit</span> <span class="o">:=</span>
<span class="n">tactic</span><span class="bp">.</span><span class="n">trace</span> <span class="s2">&quot;A&quot;</span>

<span class="n">run_cmd</span> <span class="n">go</span>
</pre></div>

#### [ Keeley Hoek (Nov 27 2018 at 09:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20puzzle%20%233/near/148625276):
<p>We are just stealing control of the <code>bind</code> function associated to the tactic monad, to prepend every single bind with a trace statement by calling <code>do_some_nonesense</code> (possibly the primed version). If you run the code as I have given it, the expected</p>
<div class="codehilite"><pre><span></span>ELLO2
A
</pre></div>


<p>will be printed. On the other hand, try uncommenting the commented line and commenting the line below it. This calls a slightly different version of <code>do_some_nonsense</code>, but no longer prints <code>ELLO1</code> before the <code>A</code>. Indeed, if you use <code>set_option trace.compiler.optimize_bytecode true</code> to inspect the code emitted for the <code>go</code> function, you will see that no call to <code>tactic_bind_override</code> is even being made anymore and lean is resorting to the builtin <code>interaction_monad_bind</code>.</p>

#### [ Keeley Hoek (Nov 27 2018 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20puzzle%20%233/near/148625320):
<p>The puzzle: determine why this is. (Spoiler, I have no idea)</p>

#### [ Keeley Hoek (Nov 27 2018 at 10:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20puzzle%20%233/near/148625471):
<p>Serious hint but still what the: replacing <code>tactic.down</code> with <code>tactic.down.{0}</code> makes it work</p>

#### [ Sebastian Ullrich (Nov 27 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20puzzle%20%233/near/148625601):
<p>what the</p>

#### [ Gabriel Ebner (Nov 27 2018 at 10:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20puzzle%20%233/near/148626504):
<p>This is interesting!  You might want to look at the universe parameters of the declarations:</p>
<div class="codehilite"><pre><span></span><span class="bp">#</span><span class="kn">eval</span> <span class="n">do</span>
<span class="n">env</span> <span class="err">←</span> <span class="n">get_env</span><span class="o">,</span>
<span class="o">[</span><span class="bp">``</span><span class="n">tactic_bind_override</span><span class="o">,</span> <span class="bp">``</span><span class="n">do_some_nonsense</span><span class="o">,</span> <span class="bp">``</span><span class="n">do_some_nonsense&#39;</span><span class="o">]</span>
  <span class="bp">.</span><span class="n">for_each</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">n</span><span class="o">,</span> <span class="n">do</span>
    <span class="n">decl</span> <span class="err">←</span> <span class="n">returnex</span> <span class="err">$</span> <span class="n">env</span><span class="bp">.</span><span class="n">get</span> <span class="n">n</span><span class="o">,</span>
    <span class="n">trace</span> <span class="o">(</span><span class="n">n</span><span class="o">,</span> <span class="n">decl</span><span class="bp">.</span><span class="n">univ_params</span><span class="o">)</span>
<span class="c">/-</span><span class="cm"></span>
<span class="cm">scratch20181127.lean:18:0: information trace output</span>
<span class="cm">(tactic_bind_override, [u])</span>
<span class="cm">(do_some_nonsense, [u, u_1])</span>
<span class="cm">(do_some_nonsense&#39;, [u])</span>
<span class="cm">-/</span>
</pre></div>

#### [ Sebastian Ullrich (Nov 27 2018 at 10:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20puzzle%20%233/near/148626617):
<p>There really should be a linter for non-inferable instances :)</p>


{% endraw %}
