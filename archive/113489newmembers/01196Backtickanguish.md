---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/01196Backtickanguish.html
---

## Stream: [new members](index.html)
### Topic: [Backtick anguish](01196Backtickanguish.html)

---


{% raw %}
#### [ Edward Ayers (Aug 17 2018 at 00:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Backtick%20anguish/near/132269318):
<p>What am I doing wrong here?</p>
<div class="codehilite"><pre><span></span><span class="n">meta</span> <span class="n">def</span> <span class="n">my_tactic</span> <span class="o">(</span><span class="n">q</span> <span class="o">:</span> <span class="kt">Prop</span><span class="o">)</span> <span class="o">:</span> <span class="n">tactic</span> <span class="n">unit</span> <span class="o">:=</span>
  <span class="n">do</span>
  <span class="n">define</span> <span class="bp">`</span><span class="n">qq</span> <span class="bp">`</span><span class="o">(</span><span class="n">q</span><span class="o">)</span>
</pre></div>


<div class="codehilite"><pre><span></span><span class="n">failed</span> <span class="n">to</span> <span class="n">synthesize</span> <span class="n">type</span> <span class="n">class</span> <span class="kn">instance</span> <span class="n">for</span>
<span class="n">q</span> <span class="o">:</span> <span class="kt">Prop</span><span class="o">,</span>
<span class="n">my_tactic</span> <span class="o">:</span> <span class="n">tactic</span> <span class="n">unit</span>
<span class="err">⊢</span> <span class="n">reflected</span> <span class="n">q</span>
</pre></div>

#### [ Edward Ayers (Aug 17 2018 at 00:38)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Backtick%20anguish/near/132269450):
<p>Alternatively:</p>
<div class="codehilite"><pre><span></span><span class="kn">open</span> <span class="n">tactic</span>
<span class="n">def</span> <span class="n">my_lemma</span> <span class="o">(</span><span class="n">q</span> <span class="o">:</span> <span class="kt">Prop</span><span class="o">)</span> <span class="o">:</span> <span class="n">q</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">define_core</span> <span class="bp">`</span><span class="n">qq</span> <span class="bp">`</span><span class="o">(</span><span class="n">q</span><span class="o">),</span>
  <span class="n">sorry</span>
<span class="kn">end</span>
</pre></div>


<div class="codehilite"><pre><span></span><span class="n">unknown</span> <span class="n">identifier</span> <span class="err">&#39;</span><span class="n">q&#39;</span>
</pre></div>

#### [ Simon Hudon (Aug 17 2018 at 00:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Backtick%20anguish/near/132269475):
<p><code> `(q) </code> is used to build <code>expr</code> values but its type is actually <code>reflected q</code>. This is a long way of saying that Lean is trying to convert a known value into an expression. Because <code>q</code> is a local variable, its value is not know and cannot be reflected. You need to go through <code> to_expr ``(q) </code></p>

#### [ Edward Ayers (Aug 17 2018 at 00:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Backtick%20anguish/near/132269478):
<p>I want to pass the <code>local_const</code> with the pretty name <code>"q"</code> as the type arg to <code>define_core</code></p>

#### [ Simon Hudon (Aug 17 2018 at 00:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Backtick%20anguish/near/132269547):
<p>Your code could be adapted into the following:</p>
<div class="codehilite"><pre><span></span><span class="kn">open</span> <span class="n">tactic</span>
<span class="n">def</span> <span class="n">my_lemma</span> <span class="o">(</span><span class="n">q</span> <span class="o">:</span> <span class="kt">Prop</span><span class="o">)</span> <span class="o">:</span> <span class="n">q</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="o">(</span><span class="n">do</span> <span class="n">my_q</span> <span class="bp">&lt;-</span> <span class="n">to_expr</span> <span class="bp">``</span><span class="o">(</span><span class="n">q</span><span class="o">),</span> <span class="n">define_core</span> <span class="bp">`</span><span class="n">qq</span> <span class="n">my_q</span><span class="o">),</span>
  <span class="n">sorry</span>
<span class="kn">end</span>
</pre></div>


<p>or, more concisely:</p>
<div class="codehilite"><pre><span></span><span class="kn">open</span> <span class="n">tactic</span>
<span class="n">def</span> <span class="n">my_lemma</span> <span class="o">(</span><span class="n">q</span> <span class="o">:</span> <span class="kt">Prop</span><span class="o">)</span> <span class="o">:</span> <span class="n">q</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="o">(</span><span class="n">to_expr</span> <span class="bp">``</span><span class="o">(</span><span class="n">q</span><span class="o">)</span> <span class="bp">&gt;&gt;=</span> <span class="n">define_core</span> <span class="bp">`</span><span class="n">qq</span><span class="o">),</span>
  <span class="n">sorry</span>
<span class="kn">end</span>
</pre></div>

#### [ Edward Ayers (Aug 17 2018 at 00:44)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Backtick%20anguish/near/132269677):
<p>This code still errors for me</p>

#### [ Edward Ayers (Aug 17 2018 at 00:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Backtick%20anguish/near/132269696):
<p><code>unknown identifier 'q'</code></p>

#### [ Edward Ayers (Aug 17 2018 at 00:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Backtick%20anguish/near/132269755):
<div class="codehilite"><pre><span></span><span class="n">invalid</span> <span class="n">define</span> <span class="n">tactic</span><span class="o">,</span> <span class="n">expression</span> <span class="n">is</span> <span class="n">not</span> <span class="n">a</span> <span class="n">type</span>
  <span class="err">⁇</span>
<span class="n">state</span><span class="o">:</span>
<span class="mi">2</span> <span class="n">goals</span>
<span class="n">q</span> <span class="o">:</span> <span class="kt">Prop</span>
<span class="err">⊢</span> <span class="n">q</span>

<span class="n">q</span> <span class="o">:</span> <span class="kt">Prop</span>
<span class="err">⊢</span> <span class="n">Sort</span> <span class="err">?</span>
</pre></div>

#### [ Simon Hudon (Aug 17 2018 at 00:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Backtick%20anguish/near/132269770):
<p>Oh! I see why. Use <code>(to_expr ```(q) &gt;&gt;= define_core `qq)</code>: <code>q</code> is not available in the scope of your tactic code. With three ticks, you're disabling scope checking when compiling that tactic. Equivalently, you can do <code>(get_local `q &gt;&gt;= define_core `qq)</code>.</p>


{% endraw %}
