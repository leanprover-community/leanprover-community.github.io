---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/59364Usingifthenelsedefinitions.html
---

## Stream: [new members](https://leanprover-community.github.io/archive/113489newmembers/index.html)
### Topic: [Using if-then-else definitions](https://leanprover-community.github.io/archive/113489newmembers/59364Usingifthenelsedefinitions.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Mark Dickinson (Nov 03 2018 at 21:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Using%20if-then-else%20definitions/near/137127809):
<p>I'm missing something fundamental. If I've defined a function <code>ℕ → ℕ</code> by making use of the if-then-else construct, how do I go about proving anything about that function? For example, given:</p>
<div class="codehilite"><pre><span></span><span class="kn">definition</span> <span class="n">nat_max</span> <span class="o">(</span><span class="n">m</span> <span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:=</span> <span class="k">if</span> <span class="n">m</span> <span class="bp">&lt;</span> <span class="n">n</span> <span class="k">then</span> <span class="n">n</span> <span class="k">else</span> <span class="n">m</span>
</pre></div>


<p>How do I prove something like</p>
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">max_right</span> <span class="o">(</span><span class="n">m</span> <span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="n">m</span> <span class="bp">&lt;</span> <span class="n">n</span> <span class="bp">→</span> <span class="n">nat_max</span> <span class="n">m</span> <span class="n">n</span> <span class="bp">=</span> <span class="n">n</span> <span class="o">:=</span> <span class="n">sorry</span>
</pre></div>


<p>? This seems as though it should be trivial, but I'm struggling. <code>unfold nat_max, by_cases (m &lt; n)</code>gives me two cases, one of which is an easy contradiction. The other then looks like:</p>
<div class="codehilite"><pre><span></span><span class="n">m</span> <span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">,</span>
<span class="n">h</span> <span class="o">:</span> <span class="n">m</span> <span class="bp">&lt;</span> <span class="n">n</span>
<span class="err">⊢</span> <span class="n">m</span> <span class="bp">&lt;</span> <span class="n">n</span> <span class="bp">→</span> <span class="bp">@</span><span class="n">ite</span> <span class="o">(</span><span class="n">m</span> <span class="bp">&lt;</span> <span class="n">n</span><span class="o">)</span> <span class="o">(</span><span class="n">nat</span><span class="bp">.</span><span class="n">decidable_lt</span> <span class="n">m</span> <span class="n">n</span><span class="o">)</span> <span class="bp">ℕ</span> <span class="n">n</span> <span class="n">m</span> <span class="bp">=</span> <span class="n">n</span>
</pre></div>


<p>and at that point I'm stuck.</p>

#### [ Chris Hughes (Nov 03 2018 at 21:38)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Using%20if-then-else%20definitions/near/137127855):
<p><code>rw if_pos h</code></p>

#### [ Mark Dickinson (Nov 03 2018 at 21:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Using%20if-then-else%20definitions/near/137127916):
<p>Ah, and <code>if_pos</code> was the fundamental thing I was missing. Thank you!</p>

#### [ Mark Dickinson (Nov 03 2018 at 21:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Using%20if-then-else%20definitions/near/137128090):
<p>Meta-question: what's the right way for a newcomer to find out about things like <code>if_pos</code>? Is it reasonable to say that any attempt to learn Lean has to include reading through the source of the standard library at some point?</p>

#### [ Mark Dickinson (Nov 03 2018 at 21:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Using%20if-then-else%20definitions/near/137128134):
<p>Though looking at the definition of <code>if_pos</code>, I really _should_ have been able to construct it from first principles ...</p>

#### [ Bryan Gin-ge Chen (Nov 03 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Using%20if-then-else%20definitions/near/137128145):
<p>Speaking as another relatively new member, <a href="https://github.com/leanprover/mathlib/blob/master/docs/naming.md" target="_blank" title="https://github.com/leanprover/mathlib/blob/master/docs/naming.md">the naming convention</a> + the VS code extension's "Intellisense" window and then <code>tactic.find</code> are usually what I go to first. Then I ask here.</p>

#### [ Chris Hughes (Nov 03 2018 at 21:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Using%20if-then-else%20definitions/near/137128147):
<p>Ask on Zulip probably. Usually Ctrl-clicking on <code>ite</code> will take you to the file where it was defined, and there'll usually be all the obvious lemmas about it there, but that seems to not be the case this time.</p>

#### [ Mark Dickinson (Nov 03 2018 at 21:57)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Using%20if-then-else%20definitions/near/137128386):
<p>Thanks, both.</p>

#### [ Kevin Buzzard (Nov 03 2018 at 22:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Using%20if-then-else%20definitions/near/137128585):
<p>This time last year I remember Kenny and I fretting over exactly this question -- a constructor for <code>ite</code> -- and I found <code>if_pos</code> by grepping through the source code :-)</p>


{% endraw %}
