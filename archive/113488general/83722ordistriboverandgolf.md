---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/83722ordistriboverandgolf.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [or distrib over and golf](https://leanprover-community.github.io/archive/113488general/83722ordistriboverandgolf.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kevin Buzzard (Oct 18 2018 at 21:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/or%20distrib%20over%20and%20golf/near/136067247):
<p>A student just asked me this:</p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">(</span><span class="n">P</span> <span class="n">Q</span> <span class="n">R</span> <span class="o">:</span> <span class="kt">Prop</span><span class="o">)</span> <span class="o">:</span> <span class="n">P</span> <span class="bp">∨</span> <span class="o">(</span><span class="n">Q</span> <span class="bp">∧</span> <span class="n">R</span><span class="o">)</span> <span class="bp">↔</span> <span class="o">(</span><span class="n">P</span> <span class="bp">∨</span> <span class="n">Q</span><span class="o">)</span> <span class="bp">∧</span> <span class="o">(</span><span class="n">P</span> <span class="bp">∨</span> <span class="n">R</span><span class="o">)</span> <span class="o">:=</span> <span class="n">sorry</span>
</pre></div>


<p>They proved it in 60 lines :-) I said that there were probably quicker proofs. How quick can we get it?</p>

#### [ Chris Hughes (Oct 18 2018 at 21:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/or%20distrib%20over%20and%20golf/near/136067269):
<p><code>by finish</code></p>

#### [ Sebastien Gouezel (Oct 18 2018 at 21:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/or%20distrib%20over%20and%20golf/near/136067327):
<p><code>by tauto</code> (one letter less)</p>

#### [ Kevin Buzzard (Oct 18 2018 at 21:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/or%20distrib%20over%20and%20golf/near/136067345):
<p>I couldn't get finish to work :-/</p>

#### [ Kevin Buzzard (Oct 18 2018 at 21:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/or%20distrib%20over%20and%20golf/near/136067349):
<p>But I got <code>or_and_distrib_left</code> to work :-)</p>

#### [ Rob Lewis (Oct 18 2018 at 21:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/or%20distrib%20over%20and%20golf/near/136067355):
<p><code>finish</code> doesn't work for me, but <code>split; finish</code> does.</p>

#### [ Chris Hughes (Oct 18 2018 at 21:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/or%20distrib%20over%20and%20golf/near/136067468):
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">(</span><span class="n">P</span> <span class="n">Q</span> <span class="n">R</span> <span class="o">:</span> <span class="kt">Prop</span><span class="o">)</span> <span class="o">:</span> <span class="n">P</span> <span class="bp">∨</span> <span class="o">(</span><span class="n">Q</span> <span class="bp">∧</span> <span class="n">R</span><span class="o">)</span> <span class="bp">↔</span> <span class="o">(</span><span class="n">P</span> <span class="bp">∨</span> <span class="n">Q</span><span class="o">)</span> <span class="bp">∧</span> <span class="o">(</span><span class="n">P</span> <span class="bp">∨</span> <span class="n">R</span><span class="o">)</span> <span class="o">:=</span>
<span class="bp">⟨λ</span> <span class="n">h</span><span class="o">,</span> <span class="n">h</span><span class="bp">.</span><span class="n">elim</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">h</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">or</span><span class="bp">.</span><span class="n">inl</span> <span class="n">h</span><span class="o">,</span> <span class="n">or</span><span class="bp">.</span><span class="n">inl</span> <span class="n">h</span><span class="bp">⟩</span><span class="o">)</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">h</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">or</span><span class="bp">.</span><span class="n">inr</span> <span class="n">h</span><span class="bp">.</span><span class="mi">1</span><span class="o">,</span> <span class="n">or</span><span class="bp">.</span><span class="n">inr</span> <span class="n">h</span><span class="bp">.</span><span class="mi">2</span><span class="bp">⟩</span><span class="o">),</span>
  <span class="bp">λ</span> <span class="n">h</span><span class="o">,</span> <span class="n">h</span><span class="bp">.</span><span class="mi">1</span><span class="bp">.</span><span class="n">elim</span> <span class="n">or</span><span class="bp">.</span><span class="n">inl</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">hQ</span><span class="o">,</span> <span class="n">h</span><span class="bp">.</span><span class="mi">2</span><span class="bp">.</span><span class="n">elim</span> <span class="n">or</span><span class="bp">.</span><span class="n">inl</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">hR</span><span class="o">,</span> <span class="n">or</span><span class="bp">.</span><span class="n">inr</span> <span class="bp">⟨</span><span class="n">hQ</span><span class="o">,</span> <span class="n">hR</span><span class="bp">⟩</span><span class="o">))</span>
</pre></div>

#### [ Scott Olson (Oct 18 2018 at 23:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/or%20distrib%20over%20and%20golf/near/136072685):
<p>If one didn't want to use a high level tactic, I'm fond of pattern matching for this style of "take it apart and put it back together in another shape" proof:</p>
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">ltr</span> <span class="o">{</span><span class="n">P</span> <span class="n">Q</span> <span class="n">R</span> <span class="o">:</span> <span class="kt">Prop</span><span class="o">}</span> <span class="o">:</span> <span class="n">P</span> <span class="bp">∨</span> <span class="o">(</span><span class="n">Q</span> <span class="bp">∧</span> <span class="n">R</span><span class="o">)</span> <span class="bp">→</span> <span class="o">(</span><span class="n">P</span> <span class="bp">∨</span> <span class="n">Q</span><span class="o">)</span> <span class="bp">∧</span> <span class="o">(</span><span class="n">P</span> <span class="bp">∨</span> <span class="n">R</span><span class="o">)</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">or</span><span class="bp">.</span><span class="n">inl</span> <span class="n">hp</span><span class="o">)</span> <span class="o">:=</span> <span class="bp">⟨</span><span class="n">or</span><span class="bp">.</span><span class="n">inl</span> <span class="n">hp</span><span class="o">,</span> <span class="n">or</span><span class="bp">.</span><span class="n">inl</span> <span class="n">hp</span><span class="bp">⟩</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">or</span><span class="bp">.</span><span class="n">inr</span> <span class="bp">⟨</span><span class="n">hq</span><span class="o">,</span> <span class="n">hr</span><span class="bp">⟩</span><span class="o">)</span> <span class="o">:=</span> <span class="bp">⟨</span><span class="n">or</span><span class="bp">.</span><span class="n">inr</span> <span class="n">hq</span><span class="o">,</span> <span class="n">or</span><span class="bp">.</span><span class="n">inr</span> <span class="n">hr</span><span class="bp">⟩</span>

<span class="kn">lemma</span> <span class="n">rtl</span> <span class="o">{</span><span class="n">P</span> <span class="n">Q</span> <span class="n">R</span> <span class="o">:</span> <span class="kt">Prop</span><span class="o">}</span> <span class="o">:</span> <span class="o">(</span><span class="n">P</span> <span class="bp">∨</span> <span class="n">Q</span><span class="o">)</span> <span class="bp">∧</span> <span class="o">(</span><span class="n">P</span> <span class="bp">∨</span> <span class="n">R</span><span class="o">)</span> <span class="bp">→</span> <span class="n">P</span> <span class="bp">∨</span> <span class="o">(</span><span class="n">Q</span> <span class="bp">∧</span> <span class="n">R</span><span class="o">)</span>
<span class="bp">|</span> <span class="bp">⟨</span><span class="n">or</span><span class="bp">.</span><span class="n">inl</span> <span class="n">hp</span><span class="o">,</span> <span class="bp">_⟩</span> <span class="o">:=</span> <span class="n">or</span><span class="bp">.</span><span class="n">inl</span> <span class="n">hp</span>
<span class="bp">|</span> <span class="bp">⟨_</span><span class="o">,</span> <span class="n">or</span><span class="bp">.</span><span class="n">inl</span> <span class="n">hp</span><span class="bp">⟩</span> <span class="o">:=</span> <span class="n">or</span><span class="bp">.</span><span class="n">inl</span> <span class="n">hp</span>
<span class="bp">|</span> <span class="bp">⟨</span><span class="n">or</span><span class="bp">.</span><span class="n">inr</span> <span class="n">hq</span><span class="o">,</span> <span class="n">or</span><span class="bp">.</span><span class="n">inr</span> <span class="n">hr</span><span class="bp">⟩</span> <span class="o">:=</span> <span class="n">or</span><span class="bp">.</span><span class="n">inr</span> <span class="bp">⟨</span><span class="n">hq</span><span class="o">,</span> <span class="n">hr</span><span class="bp">⟩</span>

<span class="kn">example</span> <span class="o">{</span><span class="n">P</span> <span class="n">Q</span> <span class="n">R</span> <span class="o">:</span> <span class="kt">Prop</span><span class="o">}</span> <span class="o">:</span> <span class="n">P</span> <span class="bp">∨</span> <span class="o">(</span><span class="n">Q</span> <span class="bp">∧</span> <span class="n">R</span><span class="o">)</span> <span class="bp">↔</span> <span class="o">(</span><span class="n">P</span> <span class="bp">∨</span> <span class="n">Q</span><span class="o">)</span> <span class="bp">∧</span> <span class="o">(</span><span class="n">P</span> <span class="bp">∨</span> <span class="n">R</span><span class="o">)</span> <span class="o">:=</span>
<span class="n">iff</span><span class="bp">.</span><span class="n">intro</span> <span class="n">ltr</span> <span class="n">rtl</span>
</pre></div>

#### [ Scott Olson (Oct 18 2018 at 23:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/or%20distrib%20over%20and%20golf/near/136072824):
<p>This isn't exactly golfing it, but I find it really clear for proofs that are merely reorganizing "data"</p>

#### [ Kevin Buzzard (Oct 19 2018 at 00:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/or%20distrib%20over%20and%20golf/near/136075871):
<p>Thanks for all of these -- I believe the student is a learner and is reading the answers so it's great to see the options which are available</p>


{% endraw %}
