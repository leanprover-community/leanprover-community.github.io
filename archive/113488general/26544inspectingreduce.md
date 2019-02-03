---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/26544inspectingreduce.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [inspecting #reduce](https://leanprover-community.github.io/archive/113488general/26544inspectingreduce.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Moses Schönfinkel (Jun 07 2018 at 12:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inspecting%20%23reduce/near/127709156):
<p>Is there a <code>set_option</code> of sorts to see what steps <code>#reduce</code> is going through to debug a <em>(deterministic) timeout</em>?</p>

#### [ Sean Leather (Jun 07 2018 at 13:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inspecting%20%23reduce/near/127712838):
<p>I have no idea, but I did this:</p>
<div class="codehilite"><pre><span></span>$ cd lean/tests; git grep set_option
</pre></div>


<p>Looking around, I found these possible options:</p>
<div class="codehilite"><pre><span></span>set_option profiler true
set_option trace.elaborator_detail true
set_option trace.compiler.code_gen true
</pre></div>


<p>Perhaps one of those will help, or perhaps looking at <code>lean/tests</code> will.</p>

#### [ Moses Schönfinkel (Jun 08 2018 at 09:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inspecting%20%23reduce/near/127760106):
<p>Thank you Sean. It seems that <code>profiler</code> and <code>compiler.*</code> pertain to <code>#eval</code> only. There's a little bit of information from <code>elaborator.*</code> in this regard, but it somewhat unsurprisingly doesn't provide much beyond how parsing transpired and how it typed the AST <em>before</em> sending it for reduction. Going through <code>lean/tests</code> doesn't yield much either. There's a secret <code>import tools.debugger</code> but even there are no options to look into reduce. I'll just go through the implementation, can't be that bad :P.</p>

#### [ Sean Leather (Jun 08 2018 at 09:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inspecting%20%23reduce/near/127760302):
<p>Good luck!</p>
<div class="codehilite"><pre><span></span><span class="n">library</span><span class="o">/</span><span class="n">init</span><span class="o">/</span><span class="n">meta</span><span class="o">/</span><span class="n">tactic</span><span class="p">.</span><span class="nl">lean</span><span class="p">:</span><span class="mi">1204</span><span class="o">:</span>    <span class="n">memory</span> <span class="n">allocations</span> <span class="p">(</span><span class="n">in</span> <span class="n">thousands</span><span class="p">)</span> <span class="n">performed</span> <span class="n">by</span> <span class="err">&#39;</span><span class="n">tac</span><span class="err">&#39;</span><span class="p">.</span> <span class="n">This</span> <span class="n">is</span> <span class="n">a</span> <span class="n">deterministic</span> <span class="n">way</span> <span class="n">of</span> <span class="n">interrupting</span>
<span class="n">library</span><span class="o">/</span><span class="n">init</span><span class="o">/</span><span class="n">util</span><span class="p">.</span><span class="nl">lean</span><span class="p">:</span><span class="mi">34</span><span class="o">:</span>  <span class="n">This</span> <span class="n">is</span> <span class="n">a</span> <span class="n">deterministic</span> <span class="n">way</span> <span class="n">of</span> <span class="n">interrupting</span> <span class="kt">long</span> <span class="n">running</span> <span class="n">tasks</span><span class="p">.</span> <span class="o">-/</span>
<span class="n">src</span><span class="o">/</span><span class="n">shell</span><span class="o">/</span><span class="n">lean</span><span class="p">.</span><span class="nl">cpp</span><span class="p">:</span><span class="mi">200</span><span class="o">:</span>    <span class="n">std</span><span class="o">::</span><span class="n">cout</span> <span class="o">&lt;&lt;</span> <span class="s">&quot;                     this is a deterministic way of interrupting long running tasks</span><span class="se">\n</span><span class="s">&quot;</span><span class="p">;</span>
<span class="n">src</span><span class="o">/</span><span class="n">util</span><span class="o">/</span><span class="n">exception</span><span class="p">.</span><span class="nl">cpp</span><span class="p">:</span><span class="mi">29</span><span class="o">:</span>    <span class="k">return</span> <span class="s">&quot;(deterministic) timeout&quot;</span><span class="p">;</span>
<span class="n">src</span><span class="o">/</span><span class="n">util</span><span class="o">/</span><span class="n">json</span><span class="p">.</span><span class="nl">hpp</span><span class="p">:</span><span class="mi">7760</span><span class="o">:</span>        <span class="n">deterministic</span> <span class="n">finite</span> <span class="n">automaton</span> <span class="p">(</span><span class="n">DFA</span><span class="p">)</span> <span class="n">by</span> <span class="n">the</span> <span class="n">tool</span>
<span class="n">src</span><span class="o">/</span><span class="n">util</span><span class="o">/</span><span class="n">sexpr</span><span class="o">/</span><span class="n">options</span><span class="p">.</span><span class="nl">cpp</span><span class="p">:</span><span class="mi">29</span><span class="o">:</span>    <span class="n">register_unsigned_option</span><span class="p">(</span><span class="o">*</span><span class="n">g_timeout</span><span class="p">,</span> <span class="mi">0</span><span class="p">,</span> <span class="s">&quot;the (deterministic) timeout is measured as the maximum of memory allocations (in thousands) per task, the default is unbounded&quot;</span><span class="p">);</span>
<span class="n">tests</span><span class="o">/</span><span class="n">lean</span><span class="o">/</span><span class="n">induction_generalize_premise_args</span><span class="p">.</span><span class="nl">lean</span><span class="p">:</span><span class="mi">8</span><span class="o">:</span>  <span class="n">lemma</span> <span class="n">deterministic_aux</span> <span class="p">(</span><span class="n">c</span> <span class="err">σ</span> <span class="n">c</span><span class="err">&#39;₁</span> <span class="n">c</span><span class="err">&#39;₂</span> <span class="err">σ&#39;₁</span> <span class="err">σ&#39;₂</span><span class="p">)</span> <span class="p">(</span><span class="nl">h₁</span> <span class="p">:</span> <span class="n">smallstep</span> <span class="err">⟨</span><span class="n">c</span><span class="p">,</span> <span class="err">σ⟩</span> <span class="err">⟨</span><span class="n">c</span><span class="err">&#39;₁</span><span class="p">,</span> <span class="err">σ&#39;₁⟩</span><span class="p">)</span>
</pre></div>

#### [ Moses Schönfinkel (Jun 08 2018 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inspecting%20%23reduce/near/127760487):
<p>It is somewhat mysterious to me why <code>#eval</code> works just fine and <code>#reduce</code> gets stuck, even though I've been told that <code>#reduce</code> can get stuck on axioms such as <code>propext</code> - however everything I have should be perfectly computable as witnessed by <code>#eval</code>. Getting <code>#reduce</code> to work should mean that I can also use defeq to compute <code>rfl</code> proofs for me, which is the ultimate goal.</p>

#### [ Gabriel Ebner (Jun 08 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inspecting%20%23reduce/near/127761349):
<p>Just to confirm: there are no tools to trace the computation of <code>#reduce</code> (at least that I know of).  Your best bet is to probably to run lean in a debugger and set a breakpoint on <code>normalize_fn::normalize</code> (or add a <code>tout() &lt;&lt; e &lt;&lt; "\n"</code> there).</p>

#### [ Gabriel Ebner (Jun 08 2018 at 10:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inspecting%20%23reduce/near/127761361):
<blockquote>
<p>however everything I have should be perfectly computable as witnessed by #eval</p>
</blockquote>
<p>That's the point.  <code>#eval</code> (VM computation) can evaluate more things than <code>#reduce</code> (definitional reduction).</p>

#### [ Moses Schönfinkel (Jun 08 2018 at 11:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inspecting%20%23reduce/near/127762471):
<p>How does that conceptually make sense in pure settings? Does it have something to do with non-transitive defeq? Isn't pure computation technically just definitional reduction?</p>

#### [ Gabriel Ebner (Jun 08 2018 at 11:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inspecting%20%23reduce/near/127762817):
<p>Can you clarify the term "pure setting"?  The main area where definitional reduction can get stuck where VM computation succeeds is on terms with axioms---VM computation erases all Props and proofs, and hence does not care whether you use axioms or not.  Practically speaking, there is also a big performance difference.</p>

#### [ Moses Schönfinkel (Jun 08 2018 at 12:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inspecting%20%23reduce/near/127764272):
<p>I just wanted to avoid having to think about side-effects that can possibly influence computation as it is being executed, that's why I said "pure setting". However, VM computation erasing Props/proofs is interesting in my scenario - I think I know where it's getting stuck. I have a structure that has both <code>x</code> and a proof of <code>P x</code> - what I end up asking for is the <code>x</code> only. The interesting part is that if proof of <code>P x</code> is sorry, it reduces just fine - but I think that also makes sense.</p>

#### [ Moses Schönfinkel (Jun 08 2018 at 12:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/inspecting%20%23reduce/near/127764406):
<p>I'll fix it by using less dependent typing, thank you so much, I think I've got this :).</p>


{% endraw %}
