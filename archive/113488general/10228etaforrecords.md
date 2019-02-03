---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/10228etaforrecords.html
---

## Stream: [general](index.html)
### Topic: [eta for records](10228etaforrecords.html)

---


{% raw %}
#### [ Johan Commelin (Jan 09 2019 at 08:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/eta%20for%20records/near/154705125):
<p>(<span class="emoji emoji-26a0" title="warning">:warning:</span> I'm a mathematician who is about to use some terminology he doesn't understand.)<br>
What are the pros and cons of eta for records? Why does Lean not have eta for records?</p>

#### [ Gabriel Ebner (Jan 09 2019 at 09:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/eta%20for%20records/near/154707201):
<blockquote>
<p>Why does Lean not have eta for records?</p>
</blockquote>
<p>Because records (<code>structure</code>) in Lean are just inductives with a single (non-recursive) constructor.  And we don't have η for inductives either (I'm pretty sure that causes type-checking to be undecidable).</p>

#### [ Gabriel Ebner (Jan 09 2019 at 09:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/eta%20for%20records/near/154707304):
<p>Pros:</p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">(</span><span class="n">p</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">×</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="n">p</span> <span class="bp">=</span> <span class="o">(</span><span class="n">p</span><span class="bp">.</span><span class="mi">1</span><span class="o">,</span> <span class="n">p</span><span class="bp">.</span><span class="mi">2</span><span class="o">)</span> <span class="o">:=</span> <span class="n">rfl</span>
<span class="kn">example</span> <span class="o">(</span><span class="n">C</span><span class="o">)</span> <span class="o">[</span><span class="err">𝓒</span> <span class="o">:</span> <span class="n">category</span> <span class="n">C</span><span class="o">]</span> <span class="o">:=</span> <span class="n">opposite</span> <span class="o">(</span><span class="n">opposite</span> <span class="err">𝓒</span><span class="o">)</span> <span class="bp">=</span> <span class="err">𝓒</span> <span class="o">:=</span> <span class="n">rfl</span>
</pre></div>

#### [ Sebastian Ullrich (Jan 09 2019 at 09:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/eta%20for%20records/near/154707306):
<p>Agda has (opt-out) eta for inductive, non-recursive records. Which at least terminates, but may still slow down unification.</p>


{% endraw %}
