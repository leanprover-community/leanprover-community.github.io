---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/64616metadefsyntaxerror.html
---

## Stream: [new members](index.html)
### Topic: [meta def syntax error](64616metadefsyntaxerror.html)

---


{% raw %}
#### [ Ken Roe (Jul 18 2018 at 04:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/meta%20def%20syntax%20error/near/129846795):
<p>I was trying out the example from the Lean meta programming paper.  However their example gives a syntax error:</p>
<div class="codehilite"><pre><span></span><span class="kn">open</span> <span class="n">tactic</span>
<span class="kn">open</span> <span class="n">monad</span>
<span class="kn">open</span> <span class="n">expr</span>
<span class="kn">open</span> <span class="n">smt_tactic</span>

<span class="n">meta</span> <span class="n">def</span> <span class="n">findd</span> <span class="o">:</span> <span class="n">expr</span> <span class="bp">→</span> <span class="n">list</span> <span class="n">expr</span> <span class="bp">→</span> <span class="n">tactic</span> <span class="n">expr</span>
<span class="bp">|</span> <span class="n">e</span> <span class="o">[]</span> <span class="o">:=</span> <span class="n">failed</span>
<span class="bp">|</span> <span class="n">e</span> <span class="o">(</span><span class="n">h</span><span class="bp">::</span><span class="n">hs</span><span class="o">)</span> <span class="o">:=</span>
    <span class="n">do</span> <span class="n">t</span> <span class="err">←</span> <span class="n">infer_type</span> <span class="n">h</span><span class="o">,</span>
    <span class="o">(</span><span class="n">unify</span> <span class="n">e</span> <span class="n">t</span> <span class="bp">&gt;&gt;</span> <span class="n">return</span> <span class="n">h</span><span class="o">)</span> <span class="bp">&lt;|&gt;</span> <span class="n">find</span> <span class="n">e</span> <span class="n">hs</span><span class="bp">.</span>
</pre></div>


<p>The "return" statement gives the following error:  (Ignore the line numbers, I've got other stuff in the file)</p>
<div class="codehilite"><pre><span></span><span class="n">traversal</span><span class="bp">.</span><span class="n">lean</span><span class="o">:</span><span class="mi">88</span><span class="o">:</span><span class="mi">18</span><span class="o">:</span> <span class="n">error</span>
<span class="n">invalid</span> <span class="n">expression</span>
<span class="n">traversal</span><span class="bp">.</span><span class="n">lean</span><span class="o">:</span><span class="mi">88</span><span class="o">:</span><span class="mi">18</span><span class="o">:</span> <span class="n">error</span>
<span class="n">command</span> <span class="n">expected</span>
</pre></div>


<p>This is with Lean 3.4.1.  How do I fix the error?</p>

#### [ Mario Carneiro (Jul 18 2018 at 04:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/meta%20def%20syntax%20error/near/129846865):
<p>the name of the def is <code>findd</code>?</p>

#### [ Mario Carneiro (Jul 18 2018 at 04:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/meta%20def%20syntax%20error/near/129846918):
<p>the <code>command expected</code> error is often fixed by scrolling down or setting the lean checking mode (on the status bar) to "check visible files" instead of "check visible lines"</p>

#### [ Reid Barton (Jul 18 2018 at 05:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/meta%20def%20syntax%20error/near/129848796):
<p>Or restarting lean.</p>


{% endraw %}
