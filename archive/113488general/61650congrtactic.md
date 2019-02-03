---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/61650congrtactic.html
---

## Stream: [general](index.html)
### Topic: [congr tactic](61650congrtactic.html)

---


{% raw %}
#### [ Sean Leather (Mar 01 2018 at 14:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/congr%20tactic/near/123137699):
<p>How do I know when to use the <code>congr</code> tactic? It's not in the Lean reference. Are there any good examples? I should've <a href="https://gitter.im/leanprover_public/Lobby?at=5a8d2134c3c5f8b90de5020b" target="_blank" title="https://gitter.im/leanprover_public/Lobby?at=5a8d2134c3c5f8b90de5020b">learned</a> already, but I'm slow. <span class="emoji emoji-1f642" title="simple smile">:simple_smile:</span></p>

#### [ Gabriel Ebner (Mar 01 2018 at 14:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/congr%20tactic/near/123137723):
<p>As a motivating example you could try it on <code>a + b + c = a + c + b</code> and see what subgoals you get.</p>

#### [ Sean Leather (Mar 01 2018 at 14:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/congr%20tactic/near/123137799):
<div class="codehilite"><pre><span></span><span class="n">state</span><span class="o">:</span>
<span class="mi">2</span> <span class="n">goals</span>
<span class="n">a</span> <span class="n">b</span> <span class="n">c</span> <span class="o">:</span> <span class="bp">ℕ</span>
<span class="err">⊢</span> <span class="n">b</span> <span class="bp">=</span> <span class="n">c</span>

<span class="n">a</span> <span class="n">b</span> <span class="n">c</span> <span class="o">:</span> <span class="bp">ℕ</span>
<span class="err">⊢</span> <span class="n">c</span> <span class="bp">=</span> <span class="n">b</span>
</pre></div>

#### [ Gabriel Ebner (Mar 01 2018 at 14:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/congr%20tactic/near/123137804):
<p>With regards to the other thread: congr (and all other uses of congruence lemmas in lean such as <code>cc</code> and <code>simp</code>) skips all arguments that are have a <code>subsingleton</code> instance.  For <code>congr</code> and <code>cc</code> this means you don't need to explicitly show that they're equal.  For <code>simp</code> this means you can't rewrite there.</p>

#### [ Gabriel Ebner (Mar 01 2018 at 14:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/congr%20tactic/near/123137911):
<p>Looking back, this may have been a bad example.  The point is: if you have an equality, then <code>congr</code> stubbornly reduces it to equalities of subterms (the topmost positions where the two sides differ, that is).</p>


{% endraw %}
