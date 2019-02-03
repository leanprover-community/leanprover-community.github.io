---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/53646DeMorgansProof.html
---

## Stream: [general](index.html)
### Topic: [De Morgan's Proof](53646DeMorgansProof.html)

---


{% raw %}
#### [ Stephanie Wang (Dec 13 2018 at 22:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s%20Proof/near/151734970):
<p>I'm new to Lean, can someone help me out with this proof of this version of De Morgan's Law? I'm having trouble coming up with the forward proof</p>
<div class="codehilite"><pre><span></span>theorem demorgans_law : ¬(p ∨ q) ↔ ¬p ∧ ¬q :=
  iff.intro(
  --
  )
  (
  assume h : ¬p ∧ ¬q,
  not_or h.left h.right
  )
</pre></div>

#### [ Kevin Buzzard (Dec 13 2018 at 22:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s%20Proof/near/151735268):
<p>I'd start like this:</p>
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">demorgans_law</span> <span class="o">(</span><span class="n">p</span> <span class="n">q</span> <span class="o">:</span> <span class="kt">Prop</span><span class="o">)</span> <span class="o">:</span> <span class="bp">¬</span><span class="o">(</span><span class="n">p</span> <span class="bp">∨</span> <span class="n">q</span><span class="o">)</span> <span class="bp">↔</span> <span class="bp">¬</span><span class="n">p</span> <span class="bp">∧</span> <span class="bp">¬</span><span class="n">q</span> <span class="o">:=</span>
  <span class="n">iff</span><span class="bp">.</span><span class="n">intro</span><span class="o">(</span>
    <span class="bp">λ</span> <span class="n">h</span><span class="o">,</span><span class="bp">⟨_</span><span class="o">,</span><span class="bp">_⟩</span>
  <span class="o">)</span>
  <span class="o">(</span>
  <span class="k">assume</span> <span class="n">h</span> <span class="o">:</span> <span class="bp">¬</span><span class="n">p</span> <span class="bp">∧</span> <span class="bp">¬</span><span class="n">q</span><span class="o">,</span>
  <span class="n">not_or</span> <span class="n">h</span><span class="bp">.</span><span class="n">left</span> <span class="n">h</span><span class="bp">.</span><span class="n">right</span>
  <span class="o">)</span>
</pre></div>

#### [ Kevin Buzzard (Dec 13 2018 at 22:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s%20Proof/near/151735351):
<p>and there is a red error on each of the _'s. I'd then try and figure out how to solve them. Actually, I'm a mathematician, so really I'd go straight into tactic mode...</p>

#### [ Kevin Buzzard (Dec 13 2018 at 22:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s%20Proof/near/151735412):
<p>Ok so I can do it but it might look incomprehensible. Do you just want a solution or a hint?</p>

#### [ Stephanie Wang (Dec 13 2018 at 22:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s%20Proof/near/151735550):
<p>a comprehensible solution would be nice!</p>

#### [ Kevin Buzzard (Dec 13 2018 at 22:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s%20Proof/near/151735667):
<p>Then you want to use tactic mode!</p>

#### [ Chris Hughes (Dec 13 2018 at 22:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s%20Proof/near/151735761):
<p><code>assume h, and intro (assume hp, h (or.inl hp)) (assume hq, h (or.inr hq))</code></p>

#### [ Kevin Buzzard (Dec 13 2018 at 22:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s%20Proof/near/151735780):
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">demorgans_law&#39;</span> <span class="o">(</span><span class="n">p</span> <span class="n">q</span> <span class="o">:</span> <span class="kt">Prop</span><span class="o">)</span> <span class="o">:</span> <span class="bp">¬</span><span class="o">(</span><span class="n">p</span> <span class="bp">∨</span> <span class="n">q</span><span class="o">)</span> <span class="bp">↔</span> <span class="bp">¬</span><span class="n">p</span> <span class="bp">∧</span> <span class="bp">¬</span><span class="n">q</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">split</span><span class="o">,</span>
  <span class="o">{</span> <span class="n">intro</span> <span class="n">hnpq</span><span class="o">,</span>
    <span class="n">split</span><span class="o">,</span>
    <span class="o">{</span> <span class="n">intro</span> <span class="n">hp</span><span class="o">,</span>
      <span class="n">apply</span> <span class="n">hnpq</span><span class="o">,</span>
      <span class="n">left</span><span class="o">,</span>
      <span class="n">assumption</span>
    <span class="o">},</span>
    <span class="o">{</span> <span class="n">intro</span> <span class="n">hq</span><span class="o">,</span>
      <span class="n">apply</span> <span class="n">hnpq</span><span class="o">,</span>
      <span class="n">right</span><span class="o">,</span>
      <span class="n">assumption</span>
    <span class="o">}</span>
  <span class="o">},</span>
  <span class="n">sorry</span>
<span class="kn">end</span>
</pre></div>


<p>half way there</p>

#### [ Kevin Buzzard (Dec 13 2018 at 22:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s%20Proof/near/151735899):
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">demorgans_law&#39;</span> <span class="o">(</span><span class="n">p</span> <span class="n">q</span> <span class="o">:</span> <span class="kt">Prop</span><span class="o">)</span> <span class="o">:</span> <span class="bp">¬</span><span class="o">(</span><span class="n">p</span> <span class="bp">∨</span> <span class="n">q</span><span class="o">)</span> <span class="bp">↔</span> <span class="bp">¬</span><span class="n">p</span> <span class="bp">∧</span> <span class="bp">¬</span><span class="n">q</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">split</span><span class="o">,</span>
  <span class="o">{</span> <span class="n">intro</span> <span class="n">hnpq</span><span class="o">,</span>
    <span class="n">split</span><span class="o">,</span>
    <span class="o">{</span> <span class="n">intro</span> <span class="n">hp</span><span class="o">,</span>
      <span class="n">apply</span> <span class="n">hnpq</span><span class="o">,</span>
      <span class="n">left</span><span class="o">,</span>
      <span class="n">assumption</span>
    <span class="o">},</span>
    <span class="o">{</span> <span class="n">intro</span> <span class="n">hq</span><span class="o">,</span>
      <span class="n">apply</span> <span class="n">hnpq</span><span class="o">,</span>
      <span class="n">right</span><span class="o">,</span>
      <span class="n">assumption</span>
    <span class="o">}</span>
  <span class="o">},</span>
  <span class="n">intro</span> <span class="n">hnpnq</span><span class="o">,</span>
  <span class="n">intro</span> <span class="n">hpq</span><span class="o">,</span>
  <span class="n">cases</span> <span class="n">hnpnq</span> <span class="k">with</span> <span class="n">hnp</span> <span class="n">hnq</span><span class="o">,</span>
  <span class="n">cases</span> <span class="n">hpq</span><span class="o">,</span>
    <span class="n">contradiction</span><span class="o">,</span>
    <span class="n">contradiction</span>
<span class="kn">end</span>
</pre></div>


<p>My impression is that computer scientists prefer these term mode things that you were writing, but I've been teaching mathematicians this stuff and tactic mode seems to be far easier for them.</p>

#### [ Kevin Buzzard (Dec 13 2018 at 22:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s%20Proof/near/151735933):
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">demorgans_law</span> <span class="o">(</span><span class="n">p</span> <span class="n">q</span> <span class="o">:</span> <span class="kt">Prop</span><span class="o">)</span> <span class="o">:</span> <span class="bp">¬</span><span class="o">(</span><span class="n">p</span> <span class="bp">∨</span> <span class="n">q</span><span class="o">)</span> <span class="bp">↔</span> <span class="bp">¬</span><span class="n">p</span> <span class="bp">∧</span> <span class="bp">¬</span><span class="n">q</span> <span class="o">:=</span>
<span class="bp">⟨λ</span> <span class="n">h</span><span class="o">,</span> <span class="bp">⟨λ</span> <span class="n">hp</span><span class="o">,</span> <span class="n">h</span> <span class="err">$</span> <span class="n">or</span><span class="bp">.</span><span class="n">inl</span> <span class="n">hp</span><span class="o">,</span> <span class="bp">λ</span> <span class="n">hq</span><span class="o">,</span> <span class="n">h</span> <span class="err">$</span> <span class="n">or</span><span class="bp">.</span><span class="n">inr</span> <span class="n">hq</span><span class="bp">⟩</span><span class="o">,</span>
  <span class="bp">λ</span> <span class="bp">⟨</span><span class="n">hnp</span><span class="o">,</span> <span class="n">hnq</span><span class="bp">⟩</span> <span class="n">hn</span><span class="o">,</span> <span class="n">or</span><span class="bp">.</span><span class="n">elim</span> <span class="n">hn</span> <span class="n">hnp</span> <span class="n">hnq</span><span class="bp">⟩</span>
</pre></div>


<p>Computer science proof, incomprehensibled to the max. Chris posted the perhaps happy medium you were looking for.</p>

#### [ Kevin Buzzard (Dec 13 2018 at 22:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s%20Proof/near/151736068):
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">demorgans_law&#39;&#39;</span> <span class="o">(</span><span class="n">p</span> <span class="n">q</span> <span class="o">:</span> <span class="kt">Prop</span><span class="o">):</span> <span class="bp">¬</span><span class="o">(</span><span class="n">p</span> <span class="bp">∨</span> <span class="n">q</span><span class="o">)</span> <span class="bp">↔</span> <span class="bp">¬</span><span class="n">p</span> <span class="bp">∧</span> <span class="bp">¬</span><span class="n">q</span> <span class="o">:=</span>
  <span class="n">iff</span><span class="bp">.</span><span class="n">intro</span><span class="o">(</span>
    <span class="k">assume</span> <span class="n">h</span><span class="o">,</span> <span class="n">and</span><span class="bp">.</span><span class="n">intro</span> <span class="o">(</span><span class="k">assume</span> <span class="n">hp</span><span class="o">,</span> <span class="n">h</span> <span class="o">(</span><span class="n">or</span><span class="bp">.</span><span class="n">inl</span> <span class="n">hp</span><span class="o">))</span> <span class="o">(</span><span class="k">assume</span> <span class="n">hq</span><span class="o">,</span> <span class="n">h</span> <span class="o">(</span><span class="n">or</span><span class="bp">.</span><span class="n">inr</span> <span class="n">hq</span><span class="o">))</span>
  <span class="o">)</span>
  <span class="o">(</span>
  <span class="k">assume</span> <span class="n">h</span> <span class="o">:</span> <span class="bp">¬</span><span class="n">p</span> <span class="bp">∧</span> <span class="bp">¬</span><span class="n">q</span><span class="o">,</span>
  <span class="n">not_or</span> <span class="n">h</span><span class="bp">.</span><span class="n">left</span> <span class="n">h</span><span class="bp">.</span><span class="n">right</span>
  <span class="o">)</span>
</pre></div>

#### [ Stephanie Wang (Dec 13 2018 at 22:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/De%20Morgan%27s%20Proof/near/151736196):
<p>Ok this makes a lot of sense to me, thanks so much.</p>


{% endraw %}
