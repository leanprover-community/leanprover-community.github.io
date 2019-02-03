---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/19171builtintactics.html
---

## Stream: [new members](https://leanprover-community.github.io/archive/113489newmembers/index.html)
### Topic: [builtin tactics](https://leanprover-community.github.io/archive/113489newmembers/19171builtintactics.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Olli (Sep 15 2018 at 15:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/builtin%20tactics/near/134011488):
<p>is there an even simpler way to write <code>{ left, assumption} &lt;|&gt; { right, assumption }</code> ?</p>

#### [ Kenny Lau (Sep 15 2018 at 15:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/builtin%20tactics/near/134011636):
<p><code>simp*</code></p>

#### [ Olli (Sep 15 2018 at 15:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/builtin%20tactics/near/134011708):
<p>thanks</p>

#### [ Olli (Sep 15 2018 at 15:30)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/builtin%20tactics/near/134012389):
<p>is there a way to do pattern matching in tactic mode?</p>

#### [ Olli (Sep 15 2018 at 15:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/builtin%20tactics/near/134012448):
<p>if there was I would think it'd be with the <code>let</code> tactic, but I can't seem to get it to work</p>

#### [ Chris Hughes (Sep 15 2018 at 15:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/builtin%20tactics/near/134012572):
<p>rcases</p>

#### [ Olli (Sep 15 2018 at 21:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/builtin%20tactics/near/134023310):
<p>how come I can't just repeat <code>constructor</code> here:</p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">{</span><span class="n">p</span> <span class="n">q</span><span class="o">}</span> <span class="o">:</span> <span class="bp">¬</span><span class="o">(</span><span class="n">p</span> <span class="bp">∨</span> <span class="n">q</span><span class="o">)</span> <span class="bp">→</span> <span class="bp">¬</span><span class="n">p</span> <span class="bp">∧</span> <span class="bp">¬</span><span class="n">q</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">intro</span> <span class="n">h</span><span class="o">,</span>
  <span class="n">constructor</span><span class="bp">;</span>
  <span class="n">intro</span> <span class="n">hpq</span><span class="bp">;</span>
  <span class="n">apply</span> <span class="n">h</span><span class="o">,</span>
  <span class="n">constructor</span><span class="o">,</span> <span class="n">assumption</span><span class="o">,</span>
  <span class="n">constructor</span><span class="o">,</span> <span class="n">assumption</span>
  <span class="c1">-- Doesn&#39;t work because before `assumption` state is:</span>
  <span class="c1">-- p q : Prop,</span>
  <span class="c1">-- h : ¬(p ∨ q),</span>
  <span class="c1">-- hpq : q</span>
  <span class="c1">-- ⊢ p</span>
<span class="kn">end</span>
</pre></div>


<p>but yet this works:</p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">{</span><span class="n">p</span> <span class="n">q</span><span class="o">}</span> <span class="o">:</span> <span class="bp">¬</span><span class="o">(</span><span class="n">p</span> <span class="bp">∨</span> <span class="n">q</span><span class="o">)</span> <span class="bp">→</span> <span class="bp">¬</span><span class="n">p</span> <span class="bp">∧</span> <span class="bp">¬</span><span class="n">q</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">intro</span> <span class="n">h</span><span class="o">,</span>
  <span class="n">constructor</span><span class="bp">;</span>
  <span class="n">intro</span> <span class="n">hpq</span><span class="bp">;</span>
  <span class="n">apply</span> <span class="n">h</span><span class="o">,</span>
  <span class="n">constructor</span><span class="o">,</span> <span class="n">assumption</span><span class="o">,</span>
  <span class="n">apply</span> <span class="n">or</span><span class="bp">.</span><span class="n">inr</span> <span class="n">hpq</span>
<span class="kn">end</span>
</pre></div>

#### [ Kenny Lau (Sep 15 2018 at 21:21)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/builtin%20tactics/near/134023364):
<p>Lean can't possibly know which constructor to use</p>

#### [ Olli (Sep 15 2018 at 21:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/builtin%20tactics/near/134023405):
<p>hmm I see, I was originally trying to write it as <code>repeat { constructor, assumption }</code>, but yeah I think I understand how this is ambigious</p>

#### [ Kevin Buzzard (Sep 15 2018 at 22:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/builtin%20tactics/near/134025252):
<p>Some symmetries in maths are lost in computer science. Or and And are different types of things. And only has one constructor (to prove <code>and p q</code> you have to supply both a proof of <code>p</code> and a proof of <code>q</code> all in one go) but Or has two (to prove <code>or p q</code> you have two choices). If you look at the definitions as inductive types by right clicking on <code>and</code> or <code>or</code> in a working Lean session and peeking at the definition you will see this. For inductive types with one constructor like <code>and</code> or <code>subtype</code> or <code>group</code> the <code>constructor</code> tactic does a predictable thing. For types like <code>or</code> with more than one constructor the tactic just, I think, chooses the first one, so for <code>or</code> I think <code>constructor</code> does the same as <code>left</code>.</p>

#### [ Olli (Sep 15 2018 at 22:43)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/builtin%20tactics/near/134025625):
<p>yeah it's probably a good idea to avoid using <code>constructor</code> with types having more than one constructor then?</p>
<p>so far my strategy for solving these exercises has been just staring at the tactic state while trying to make progress and not giving too much thought to what is happening in the bigger picture, and this is working surprisingly well, but there are some traps like this that lead to dead-ends</p>

#### [ Mario Carneiro (Sep 15 2018 at 22:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/builtin%20tactics/near/134025763):
<p>you can use constructor as long as only one of the constructors is applicable</p>


{% endraw %}
