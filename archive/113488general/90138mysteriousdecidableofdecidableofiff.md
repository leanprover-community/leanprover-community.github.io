---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/90138mysteriousdecidableofdecidableofiff.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [mysterious decidable_of_decidable_of_iff](https://leanprover-community.github.io/archive/113488general/90138mysteriousdecidableofdecidableofiff.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Sean Leather (Mar 01 2018 at 14:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mysterious%20decidable_of_decidable_of_iff/near/123137155):
<p>This is also peculiar. I came upon the following which didn't resolve with <code>refl</code> or <code>simp</code>:</p>
<div class="codehilite"><pre><span></span><span class="err">⊢</span> <span class="n">ite</span> <span class="o">(</span><span class="n">y</span> <span class="bp">=</span> <span class="n">x</span><span class="o">)</span> <span class="n">t₂</span> <span class="o">(</span><span class="n">varf</span> <span class="n">y</span><span class="o">)</span> <span class="bp">=</span> <span class="n">ite</span> <span class="o">(</span><span class="n">y</span> <span class="bp">=</span> <span class="n">x</span><span class="o">)</span> <span class="n">t₂</span> <span class="o">(</span><span class="n">varf</span> <span class="n">y</span><span class="o">)</span>
</pre></div>


<p>Upon further inspection with <code>set_option pp.all true</code>, I found:</p>
<div class="codehilite"><pre><span></span><span class="err">⊢</span> <span class="bp">@</span><span class="n">eq</span><span class="bp">.</span><span class="o">{</span><span class="mi">1</span><span class="o">}</span> <span class="o">(</span><span class="n">tts</span><span class="bp">.</span><span class="n">typ</span> <span class="n">V</span><span class="o">)</span>
    <span class="o">(</span><span class="bp">@</span><span class="n">ite</span><span class="bp">.</span><span class="o">{</span><span class="mi">1</span><span class="o">}</span> <span class="o">(</span><span class="bp">@</span><span class="n">eq</span><span class="bp">.</span><span class="o">{</span><span class="mi">1</span><span class="o">}</span> <span class="n">V</span> <span class="n">y</span> <span class="n">x</span><span class="o">)</span>
      <span class="o">(</span><span class="bp">_</span><span class="n">inst_1</span> <span class="n">y</span> <span class="n">x</span><span class="o">)</span>
      <span class="o">(</span><span class="n">tts</span><span class="bp">.</span><span class="n">typ</span> <span class="n">V</span><span class="o">)</span>
      <span class="n">t₂</span>
      <span class="o">(</span><span class="bp">@</span><span class="n">tts</span><span class="bp">.</span><span class="n">typ</span><span class="bp">.</span><span class="n">varf</span> <span class="n">V</span> <span class="n">y</span><span class="o">))</span>
    <span class="o">(</span><span class="bp">@</span><span class="n">ite</span><span class="bp">.</span><span class="o">{</span><span class="mi">1</span><span class="o">}</span> <span class="o">(</span><span class="bp">@</span><span class="n">eq</span><span class="bp">.</span><span class="o">{</span><span class="mi">1</span><span class="o">}</span> <span class="n">V</span> <span class="n">y</span> <span class="n">x</span><span class="o">)</span>
      <span class="o">(</span><span class="bp">@</span><span class="n">decidable_of_decidable_of_iff</span> <span class="o">(</span><span class="bp">@</span><span class="n">eq</span><span class="bp">.</span><span class="o">{</span><span class="mi">1</span><span class="o">}</span> <span class="n">V</span> <span class="n">y</span> <span class="n">x</span><span class="o">)</span> <span class="o">(</span><span class="bp">@</span><span class="n">eq</span><span class="bp">.</span><span class="o">{</span><span class="mi">1</span><span class="o">}</span> <span class="n">V</span> <span class="n">y</span> <span class="n">x</span><span class="o">)</span> <span class="o">(</span><span class="bp">_</span><span class="n">inst_1</span> <span class="n">y</span> <span class="n">x</span><span class="o">)</span> <span class="o">(</span><span class="n">iff</span><span class="bp">.</span><span class="n">refl</span> <span class="o">(</span><span class="bp">@</span><span class="n">eq</span><span class="bp">.</span><span class="o">{</span><span class="mi">1</span><span class="o">}</span> <span class="n">V</span> <span class="n">y</span> <span class="n">x</span><span class="o">)))</span>
      <span class="o">(</span><span class="n">tts</span><span class="bp">.</span><span class="n">typ</span> <span class="n">V</span><span class="o">)</span>
      <span class="n">t₂</span>
      <span class="o">(</span><span class="bp">@</span><span class="n">tts</span><span class="bp">.</span><span class="n">typ</span><span class="bp">.</span><span class="n">varf</span> <span class="n">V</span> <span class="n">y</span><span class="o">))</span>
</pre></div>


<p>Of course, the goal can be reached with:</p>
<div class="codehilite"><pre><span></span><span class="n">by_cases</span> <span class="n">h</span> <span class="o">:</span> <span class="n">y</span> <span class="bp">=</span> <span class="n">x</span><span class="bp">;</span> <span class="n">simp</span> <span class="o">[</span><span class="n">h</span><span class="o">]</span>
</pre></div>


<p>But what I'm curious about is (1) why it's there in the first place and (2) why it isn't resolved with <code>refl</code> (why is it not defeq?).</p>
<p>My guess for (1) is that it came from one of the <a href="https://github.com/leanprover/lean/blob/39270fd46f49fecb30649f5ec527da7bbd4cdb13/library/init/logic.lean#L882-L891" target="_blank" title="https://github.com/leanprover/lean/blob/39270fd46f49fecb30649f5ec527da7bbd4cdb13/library/init/logic.lean#L882-L891"><code>congr</code> theorems in <code>library/init/logic.lean</code></a>.</p>
<p>As for (2), I tried adding:</p>
<div class="codehilite"><pre><span></span><span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="kn">theorem</span> <span class="n">decidable_of_decidable_of_iff_refl</span> <span class="o">:</span>
  <span class="bp">∀</span> <span class="o">(</span><span class="n">d</span> <span class="o">:</span> <span class="n">decidable</span> <span class="n">p</span><span class="o">),</span> <span class="n">decidable_of_decidable_of_iff</span> <span class="n">d</span> <span class="o">(</span><span class="n">iff</span><span class="bp">.</span><span class="n">refl</span> <span class="n">p</span><span class="o">)</span> <span class="bp">=</span> <span class="n">d</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">is_true</span> <span class="bp">_</span><span class="o">)</span>  <span class="o">:=</span> <span class="n">rfl</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">is_false</span> <span class="bp">_</span><span class="o">)</span> <span class="o">:=</span> <span class="n">rfl</span>
</pre></div>


<p>and:</p>
<div class="codehilite"><pre><span></span><span class="n">simp</span> <span class="o">[</span><span class="n">decidable_of_decidable_of_iff_refl</span> <span class="bp">_</span><span class="o">]</span>
</pre></div>


<p>but nothing changed, and <code>decidable_of_decidable_of_iff_refl</code> didn't show up with <code>set_option trace.simplify true</code>.</p>

#### [ Gabriel Ebner (Mar 01 2018 at 14:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mysterious%20decidable_of_decidable_of_iff/near/123137356):
<p>simp only allows you to rewrite at positions that you can "reach" via congruence lemmas.  Since congruence lemmas typically skip subsingletons (such as decidability instances), you can't simp there.</p>

#### [ Gabriel Ebner (Mar 01 2018 at 14:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mysterious%20decidable_of_decidable_of_iff/near/123137363):
<p><code>rw decidable_of_decidable_of_iff_refl</code> could work</p>

#### [ Sean Leather (Mar 01 2018 at 14:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mysterious%20decidable_of_decidable_of_iff/near/123137364):
<p><code>rw decidable_of_decidable_of_iff_refl _, apply_instance</code> works</p>

#### [ Gabriel Ebner (Mar 01 2018 at 14:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mysterious%20decidable_of_decidable_of_iff/near/123137370):
<p>Have you tried <code>congr</code> on the original goal?</p>

#### [ Sean Leather (Mar 01 2018 at 14:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mysterious%20decidable_of_decidable_of_iff/near/123137425):
<p>Ah, that works.</p>

#### [ Sebastian Ullrich (Mar 01 2018 at 14:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mysterious%20decidable_of_decidable_of_iff/near/123137435):
<p>I suppose this shows that simp should really use refl as a rule instead of just at the very end</p>

#### [ Sebastian Ullrich (Mar 01 2018 at 14:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mysterious%20decidable_of_decidable_of_iff/near/123137448):
<p>Then it should be able to close that goal together with if_congr</p>

#### [ Gabriel Ebner (Mar 01 2018 at 14:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mysterious%20decidable_of_decidable_of_iff/near/123137511):
<p><span class="user-mention" data-user-email="sebasti@nullri.ch" data-user-id="110024">@Sebastian Ullrich</span> Can you elaborate on how refl would work here?  Neither side of the equation can be simplified, not even with refl.  AFAICT the only thing that would help is if simp applied the congruence lemmas to the equation (like backchaining).</p>

#### [ Sebastian Ullrich (Mar 01 2018 at 14:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mysterious%20decidable_of_decidable_of_iff/near/123137706):
<p><span class="user-mention" data-user-email="gebner@gebner.org" data-user-id="110043">@Gabriel Ebner</span> You're right, I was confused about the role of congr lemmas in simp</p>


{% endraw %}
