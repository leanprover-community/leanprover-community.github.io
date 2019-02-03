---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/11537Accessingconstructortypeintacticdefinition.html
---

## Stream: [new members](https://leanprover-community.github.io/archive/113489newmembers/index.html)
### Topic: [Accessing constructor type in tactic definition](https://leanprover-community.github.io/archive/113489newmembers/11537Accessingconstructortypeintacticdefinition.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Jesse Michael Han (Oct 18 2018 at 06:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Accessing%20constructor%20type%20in%20tactic%20definition/near/136019547):
<p>Hello everyone,</p>
<p>I'm trying to write the following function:</p>
<div class="codehilite"><pre><span></span><span class="kn">inductive</span> <span class="n">hewwo</span> <span class="o">:</span> <span class="kt">Type</span>
<span class="bp">|</span> <span class="n">foo</span> <span class="o">:</span> <span class="n">nat</span> <span class="bp">→</span> <span class="n">hewwo</span>
<span class="bp">|</span> <span class="n">bar</span> <span class="o">:</span> <span class="n">nat</span> <span class="bp">→</span> <span class="n">hewwo</span>

<span class="n">def</span> <span class="n">g</span> <span class="o">:</span> <span class="n">hewwo</span> <span class="bp">→</span> <span class="bp">ℕ</span> <span class="o">:=</span>
<span class="k">begin</span>
<span class="n">intro</span> <span class="n">hello</span><span class="o">,</span>
<span class="n">cases</span> <span class="n">hello</span><span class="o">,</span>
<span class="n">sorry</span> <span class="c1">--help! intended behavior is g foo k = 0, g bar k = 1</span>
<span class="kn">end</span>
</pre></div>


<p>where the goal state at the <code>sorry</code> is</p>
<div class="codehilite"><pre><span></span><span class="mi">2</span> <span class="n">goals</span>
<span class="n">case</span> <span class="n">hewwo</span><span class="bp">.</span><span class="n">foo</span>
<span class="n">hello</span> <span class="o">:</span> <span class="n">nat</span>
<span class="err">⊢</span> <span class="n">nat</span>

<span class="n">case</span> <span class="n">hewwo</span><span class="bp">.</span><span class="n">bar</span>
<span class="n">hello</span> <span class="o">:</span> <span class="n">nat</span>
<span class="err">⊢</span> <span class="n">nat</span>
</pre></div>


<p>I know the sane way to do this is to just use the equation compiler, but I want to know: in this situation, how can I introduce new hypotheses which have the type of the constructors <code>foo</code> and <code>bar</code> into context?</p>
<p>If I furthermore write something like</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">g</span> <span class="o">:</span> <span class="n">hewwo</span> <span class="bp">→</span> <span class="bp">ℕ</span> <span class="o">:=</span>
<span class="k">begin</span>
<span class="n">intro</span> <span class="n">hello</span><span class="o">,</span>
<span class="n">cases</span> <span class="n">hello</span><span class="o">,</span>
<span class="o">{</span><span class="n">cases</span> <span class="n">hewwo</span><span class="bp">.</span><span class="n">foo</span><span class="o">,}</span>
<span class="kn">end</span>
</pre></div>


<p>the error message gives something tantalizing close:</p>
<div class="codehilite"><pre><span></span><span class="mi">219</span><span class="o">:</span><span class="mi">2</span><span class="o">:</span> <span class="n">cases</span> <span class="n">tactic</span> <span class="n">failed</span><span class="o">,</span> <span class="n">it</span> <span class="n">is</span> <span class="n">not</span> <span class="n">applicable</span> <span class="n">to</span> <span class="n">the</span> <span class="n">given</span> <span class="kn">hypothesis</span>
<span class="n">state</span><span class="o">:</span>
<span class="n">hello</span> <span class="o">:</span> <span class="n">nat</span><span class="o">,</span>
<span class="bp">_</span><span class="n">x</span> <span class="o">:</span> <span class="n">nat</span> <span class="bp">→</span> <span class="n">hewwo</span>
<span class="err">⊢</span> <span class="n">nat</span>
</pre></div>


<p>but I don't know how to access this <code>_x</code> normally.</p>

#### [ Johan Commelin (Oct 18 2018 at 06:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Accessing%20constructor%20type%20in%20tactic%20definition/near/136019612):
<p><span class="user-mention" data-user-id="116045">@Jesse Michael Han</span> Your to goals are tagged with a descriptive name. It contains "foo" and "bar".</p>

#### [ Johan Commelin (Oct 18 2018 at 06:26)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Accessing%20constructor%20type%20in%20tactic%20definition/near/136019652):
<p>Your actual "foo" and "bar" is still called <code>hello</code>.</p>

#### [ Johan Commelin (Oct 18 2018 at 06:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Accessing%20constructor%20type%20in%20tactic%20definition/near/136019660):
<p>Hmmm, that is not exactly correct. Sorry. So you have a <code>hello : nat</code> in those contexts. And that is the one you want to provide. (Your goal is also a <code>nat</code>.)</p>

#### [ Johan Commelin (Oct 18 2018 at 06:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Accessing%20constructor%20type%20in%20tactic%20definition/near/136019661):
<p>My point is, you can close the goal with <del><code>exact hello</code></del> (see below).</p>

#### [ Mario Carneiro (Oct 18 2018 at 06:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Accessing%20constructor%20type%20in%20tactic%20definition/near/136019707):
<p>well, I think he wants <code>exact 0, exact 1</code></p>

#### [ Bryan Gin-ge Chen (Oct 18 2018 at 06:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Accessing%20constructor%20type%20in%20tactic%20definition/near/136019709):
<p>Is this what you want?</p>
<div class="codehilite"><pre><span></span><span class="kn">inductive</span> <span class="n">hewwo</span> <span class="o">:</span> <span class="kt">Type</span>
<span class="bp">|</span> <span class="n">foo</span> <span class="o">:</span> <span class="n">nat</span> <span class="bp">→</span> <span class="n">hewwo</span>
<span class="bp">|</span> <span class="n">bar</span> <span class="o">:</span> <span class="n">nat</span> <span class="bp">→</span> <span class="n">hewwo</span>

<span class="n">def</span> <span class="n">g</span> <span class="o">:</span> <span class="n">hewwo</span> <span class="bp">→</span> <span class="bp">ℕ</span> <span class="o">:=</span>
<span class="k">begin</span>
<span class="n">intro</span> <span class="n">hello</span><span class="o">,</span>
<span class="n">cases</span> <span class="n">hello</span><span class="o">,</span>
<span class="o">{</span> <span class="n">exact</span> <span class="mi">0</span> <span class="o">},</span>
<span class="o">{</span> <span class="n">exact</span> <span class="mi">1</span> <span class="o">}</span>
<span class="kn">end</span>

<span class="bp">#</span><span class="kn">eval</span> <span class="n">g</span> <span class="o">(</span><span class="n">hewwo</span><span class="bp">.</span><span class="n">foo</span> <span class="mi">40</span><span class="o">)</span>
<span class="bp">#</span><span class="kn">eval</span> <span class="n">g</span> <span class="o">(</span><span class="n">hewwo</span><span class="bp">.</span><span class="n">bar</span> <span class="mi">4</span><span class="o">)</span>
</pre></div>

#### [ Jesse Michael Han (Oct 18 2018 at 06:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Accessing%20constructor%20type%20in%20tactic%20definition/near/136020216):
<p>Thanks for the prompt responses, guys! You're right, I should have chosen a less trivial toy intended behavior.</p>
<p><span class="user-mention" data-user-id="112680">@Johan Commelin</span> Okay, I see. So, to introduce that <code>_x</code>, I can just use <code>have := hewwo.foo</code> (resp. <code>bar</code>).</p>

#### [ Bryan Gin-ge Chen (Oct 18 2018 at 06:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Accessing%20constructor%20type%20in%20tactic%20definition/near/136020333):
<p>What's the actual thing you're trying to do? <code>have := hewwo.foo</code> only gives you a hypothesis <code>this : ℕ → hewwo</code>.</p>

#### [ Bryan Gin-ge Chen (Oct 18 2018 at 06:57)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Accessing%20constructor%20type%20in%20tactic%20definition/near/136020477):
<p>Oh, I misread your first message. I guess that's what you wanted after all.</p>

#### [ Jesse Michael Han (Oct 18 2018 at 07:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Accessing%20constructor%20type%20in%20tactic%20definition/near/136020878):
<p>Right, I was just wondering where the data on the left hand side (if you write this using the equation compiler):</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">HEWWO</span> <span class="o">:</span> <span class="n">hewwo</span> <span class="bp">→</span> <span class="bp">ℕ</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">foo</span> <span class="n">i</span><span class="o">)</span> <span class="o">:=</span> <span class="mi">0</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">bar</span> <span class="n">i</span><span class="o">)</span> <span class="o">:=</span> <span class="mi">1</span>
</pre></div>


<p>goes if you try to write it with tactics instead. As Johan pointed out (and as I failed to notice :^)), once inside the case environment, Lean introduces <code>hello : nat</code> corresponding to <code>i</code>, and we can retrieve <code>foo</code> with <code>have :=</code>.</p>

#### [ Bryan Gin-ge Chen (Oct 18 2018 at 07:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Accessing%20constructor%20type%20in%20tactic%20definition/near/136021621):
<p>When you're using <code>cases</code> to define a function, you don't need to worry about retrieving <code>foo</code> or <code>bar</code> anymore. <code>cases</code> takes care of all of that automatically. All you have to do is provide terms of the output type <code>nat</code> when it asks you to. </p>
<p>Note that <code>have := hewwo.foo</code> doesn't depend on anything the <code>cases</code> statement introduces. You can write it before or after the <code>cases</code> statement with exactly the same effect. All the <code>have</code> tactic does is introduce a new term into the tactic state.  Furthermore, all that lean remembers from <code>have</code> is the type of the term after <code>:=</code>, so it's mostly useful for introducing proof terms and not data. In particular, you can check that the tactic state is the same whether you write <code>have := hewwo.foo</code> or <code>have := hewwo.bar</code>. </p>
<p>Sometimes it can be useful to introduce local definitions, e.g. notation for a function or some other piece of "data", but to do that, one uses <code>let</code> instead.</p>

#### [ Jesse Michael Han (Oct 18 2018 at 07:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Accessing%20constructor%20type%20in%20tactic%20definition/near/136022027):
<blockquote>
<p>Note that have := hewwo.foo doesn't depend on anything the cases statement introduces. You can write it before or after the cases statement with exactly the same effect. All the have tactic does is introduce a new term into the tactic state. Furthermore, all that lean remembers from have is the type of the term after :=, so it's mostly useful for introducing proof terms and not data. In particular, you can check that the tactic state is the same whether you write have := hewwo.foo or have := hewwo.bar. </p>
</blockquote>
<p>I see---thanks!</p>


{% endraw %}
