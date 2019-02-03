---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/08348parallelcombinator.html
---

## Stream: [new members](https://leanprover-community.github.io/archive/113489newmembers/index.html)
### Topic: [parallel combinator](https://leanprover-community.github.io/archive/113489newmembers/08348parallelcombinator.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Olli (Sep 13 2018 at 13:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/parallel%20combinator/near/133876440):
<p>is there a way to use the <code>exact</code> tactic with the parallel tactic combinator:</p>
<p>works:</p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">:</span> <span class="n">p</span> <span class="bp">∧</span> <span class="n">q</span> <span class="bp">↔</span> <span class="n">q</span> <span class="bp">∧</span> <span class="n">p</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">split</span><span class="o">,</span>
  <span class="n">exact</span> <span class="bp">λ</span> <span class="bp">⟨</span><span class="n">h1</span><span class="o">,</span> <span class="n">h2</span><span class="bp">⟩</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">h2</span><span class="o">,</span> <span class="n">h1</span><span class="bp">⟩</span><span class="o">,</span>
  <span class="n">exact</span> <span class="bp">λ</span> <span class="bp">⟨</span><span class="n">h1</span><span class="o">,</span> <span class="n">h2</span><span class="bp">⟩</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">h2</span><span class="o">,</span> <span class="n">h1</span><span class="bp">⟩</span><span class="o">,</span>
<span class="kn">end</span>
</pre></div>


<p>fails:</p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">:</span> <span class="n">p</span> <span class="bp">∧</span> <span class="n">q</span> <span class="bp">↔</span> <span class="n">q</span> <span class="bp">∧</span> <span class="n">p</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">split</span><span class="bp">;</span>
  <span class="n">exact</span> <span class="bp">λ</span> <span class="bp">⟨</span><span class="n">h1</span><span class="o">,</span> <span class="n">h2</span><span class="bp">⟩</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">h2</span><span class="o">,</span> <span class="n">h1</span><span class="bp">⟩</span><span class="o">,</span>
<span class="kn">end</span>
</pre></div>


<p>with:</p>
<div class="codehilite"><pre><span></span>equation compiler failed to create auxiliary declaration &#39;_example._match_1&#39;
nested exception message:
invalid object declaration, environment already has an object named &#39;_example._match_1&#39;
</pre></div>

#### [ Kenny Lau (Sep 13 2018 at 16:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/parallel%20combinator/near/133886990):
<p>does <code>rintro</code> work?</p>

#### [ Ali Sever (Sep 13 2018 at 19:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/parallel%20combinator/near/133901349):
<p>This also works,</p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">:</span> <span class="n">p</span> <span class="bp">∧</span> <span class="n">q</span> <span class="bp">↔</span> <span class="n">q</span> <span class="bp">∧</span> <span class="n">p</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">split</span><span class="bp">;</span>
  <span class="n">exact</span> <span class="n">and</span><span class="bp">.</span><span class="n">symm</span>
<span class="kn">end</span>
</pre></div>

#### [ Mario Carneiro (Sep 13 2018 at 19:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/parallel%20combinator/near/133901899):
<p><span class="user-mention" data-user-id="110024">@Sebastian Ullrich</span> This seems to be indicative of a very strange dependency between parsing and creating definitions. Does this still behave the same way in lean 4?</p>

#### [ Mario Carneiro (Sep 13 2018 at 20:18)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/parallel%20combinator/near/133903258):
<p>Oh wow, this is stranger than I thought.</p>
<div class="codehilite"><pre><span></span><span class="kn">open</span> <span class="n">tactic</span>

<span class="n">meta</span> <span class="n">def</span> <span class="n">mytac</span> <span class="o">:</span> <span class="n">tactic</span> <span class="n">unit</span> <span class="o">:=</span>
<span class="n">do</span> <span class="n">tgt</span> <span class="err">←</span> <span class="n">target</span><span class="o">,</span>
   <span class="n">i_to_expr_strict</span> <span class="bp">``</span><span class="o">(</span><span class="bp">λ</span> <span class="bp">⟨</span><span class="n">h1</span><span class="o">,</span> <span class="n">h2</span><span class="bp">⟩</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">h2</span><span class="o">,</span> <span class="n">h1</span><span class="bp">⟩</span> <span class="o">:</span> <span class="err">%%</span><span class="n">tgt</span><span class="o">)</span> <span class="bp">&gt;&gt;=</span> <span class="n">exact</span>

<span class="n">meta</span> <span class="n">def</span> <span class="n">twice</span> <span class="o">(</span><span class="n">tac</span> <span class="o">:</span> <span class="n">tactic</span> <span class="n">unit</span><span class="o">)</span> <span class="o">:</span> <span class="n">tactic</span> <span class="n">unit</span> <span class="o">:=</span> <span class="n">tac</span> <span class="bp">&gt;&gt;</span> <span class="n">tac</span>

<span class="kn">example</span> <span class="o">{</span><span class="n">p</span> <span class="n">q</span> <span class="o">:</span> <span class="kt">Prop</span><span class="o">}</span> <span class="o">:</span> <span class="n">p</span> <span class="bp">∧</span> <span class="n">q</span> <span class="bp">↔</span> <span class="n">q</span> <span class="bp">∧</span> <span class="n">p</span> <span class="o">:=</span> <span class="c1">-- doesn&#39;t work</span>
<span class="k">begin</span>
  <span class="n">split</span><span class="o">,</span>
  <span class="n">twice</span> <span class="o">(</span><span class="n">do</span> <span class="o">{</span>
    <span class="n">tgt</span> <span class="err">←</span> <span class="n">target</span><span class="o">,</span>
    <span class="n">i_to_expr_strict</span> <span class="bp">``</span><span class="o">(</span><span class="bp">λ</span> <span class="bp">⟨</span><span class="n">h1</span><span class="o">,</span> <span class="n">h2</span><span class="bp">⟩</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">h2</span><span class="o">,</span> <span class="n">h1</span><span class="bp">⟩</span> <span class="o">:</span> <span class="err">%%</span><span class="n">tgt</span><span class="o">)</span> <span class="bp">&gt;&gt;=</span> <span class="n">exact</span>
  <span class="o">})</span>
<span class="kn">end</span>

<span class="kn">example</span> <span class="o">{</span><span class="n">p</span> <span class="n">q</span> <span class="o">:</span> <span class="kt">Prop</span><span class="o">}</span> <span class="o">:</span> <span class="n">p</span> <span class="bp">∧</span> <span class="n">q</span> <span class="bp">↔</span> <span class="n">q</span> <span class="bp">∧</span> <span class="n">p</span> <span class="o">:=</span> <span class="c1">-- works</span>
<span class="k">begin</span>
  <span class="n">split</span><span class="o">,</span>
  <span class="n">do</span> <span class="o">{</span>
    <span class="n">tgt</span> <span class="err">←</span> <span class="n">target</span><span class="o">,</span>
    <span class="n">i_to_expr_strict</span> <span class="bp">``</span><span class="o">(</span><span class="bp">λ</span> <span class="bp">⟨</span><span class="n">h1</span><span class="o">,</span> <span class="n">h2</span><span class="bp">⟩</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">h2</span><span class="o">,</span> <span class="n">h1</span><span class="bp">⟩</span> <span class="o">:</span> <span class="err">%%</span><span class="n">tgt</span><span class="o">)</span> <span class="bp">&gt;&gt;=</span> <span class="n">exact</span><span class="o">,</span>
    <span class="n">tgt</span> <span class="err">←</span> <span class="n">target</span><span class="o">,</span>
    <span class="n">i_to_expr_strict</span> <span class="bp">``</span><span class="o">(</span><span class="bp">λ</span> <span class="bp">⟨</span><span class="n">h1</span><span class="o">,</span> <span class="n">h2</span><span class="bp">⟩</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">h2</span><span class="o">,</span> <span class="n">h1</span><span class="bp">⟩</span> <span class="o">:</span> <span class="err">%%</span><span class="n">tgt</span><span class="o">)</span> <span class="bp">&gt;&gt;=</span> <span class="n">exact</span>
  <span class="o">}</span>
<span class="kn">end</span>

<span class="kn">example</span> <span class="o">{</span><span class="n">p</span> <span class="n">q</span> <span class="o">:</span> <span class="kt">Prop</span><span class="o">}</span> <span class="o">:</span> <span class="n">p</span> <span class="bp">∧</span> <span class="n">q</span> <span class="bp">↔</span> <span class="n">q</span> <span class="bp">∧</span> <span class="n">p</span> <span class="o">:=</span> <span class="c1">-- works</span>
<span class="k">begin</span>
  <span class="n">split</span><span class="o">,</span>
  <span class="n">twice</span> <span class="n">mytac</span>
<span class="kn">end</span>
</pre></div>


<p>My new theory is that it has something to do with the way a tactic is elaborated when it contains a subexpression with side effects like this</p>

#### [ Sebastian Ullrich (Sep 13 2018 at 22:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/parallel%20combinator/near/133912590):
<p>Yeah, <code>to_expr</code> is creating a new elaborator. This is horrible, haha</p>

#### [ Sebastian Ullrich (Sep 13 2018 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/parallel%20combinator/near/133912887):
<p>Well, I guess it could just skip auxiliary names that have already been taken</p>


{% endraw %}
