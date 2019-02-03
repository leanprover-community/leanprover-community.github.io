---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/81093recursivesplit.html
---

## Stream: [general](index.html)
### Topic: [recursive split](81093recursivesplit.html)

---


{% raw %}
#### [ Patrick Massot (Jul 02 2018 at 15:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/recursive%20split/near/128962808):
<p>Do we have a recursive split tactic? My goal looks likes <code>a ∧ b ∧ c ∧ d</code> and I would like to write one word and get four non-nested goals.</p>

#### [ Sean Leather (Jul 02 2018 at 15:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/recursive%20split/near/128962925):
<p>There's only one “word” in <code>refine ⟨_, _, _, _⟩</code>. <span class="emoji emoji-1f609" title="wink">:wink:</span></p>

#### [ Patrick Massot (Jul 02 2018 at 15:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/recursive%20split/near/128963057):
<p>Obviously, this is not exactly as readable as I hoped for, but at least this indeed does the trick.</p>

#### [ Sebastian Ullrich (Jul 02 2018 at 15:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/recursive%20split/near/128964010):
<p><code>repeat { any_goals { split } }</code> :)</p>

#### [ Sebastian Ullrich (Jul 02 2018 at 15:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/recursive%20split/near/128964047):
<p>...which at least is a bit more general and could be extracted into a new tactic</p>

#### [ Jakob von Raumer (Jul 02 2018 at 15:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/recursive%20split/near/128964146):
<p>Isn't ther also a <code>rcases</code> in mathlib that does this?</p>

#### [ Kenny Lau (Jul 02 2018 at 15:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/recursive%20split/near/128964164):
<p>that destructs hypotheses</p>

#### [ Sean Leather (Jul 02 2018 at 15:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/recursive%20split/near/128964437):
<blockquote>
<p><code>repeat { any_goals { split } }</code> <span class="emoji emoji-1f603" title="smiley">:smiley:</span></p>
</blockquote>
<p>How efficient is that? For <code>g1 ∧ g2 ∧ g3 ∧ g4</code>, I'm guessing that's 4 applications of <code>any_goals</code>, but <code>any_goals</code> would also test all previously <code>split</code> goals each time, right? I suppose it could be improved by “remembering” that <code>split</code> failed for a visited goal.</p>

#### [ Sebastian Ullrich (Jul 02 2018 at 15:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/recursive%20split/near/128964553):
<p>How big are your conjunctions that you expect this to be a problem <span class="emoji emoji-1f626" title="frowning">:frowning:</span> ? <code>split</code> isn't exactly an expensive tactic.</p>

#### [ Patrick Massot (Jul 02 2018 at 17:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/recursive%20split/near/128969257):
<p>I like that this version seems easy to turn into a new tactic. But, in the case I'm looking at, this creates too many goals, with stupid meta-variables</p>

#### [ Simon Hudon (Jul 02 2018 at 17:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/recursive%20split/near/128970861):
<p>Do you have existential quantifications?</p>

#### [ Simon Hudon (Jul 02 2018 at 17:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/recursive%20split/near/128971009):
<p>You can also use <code>constructor_matching* _ ∧ _</code> to make sure it only splits conjunctions</p>

#### [ Patrick Massot (Jul 02 2018 at 17:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/recursive%20split/near/128971022):
<p>Yes, hidden in subset image. After much effort, I managed to minimize to:</p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">(</span><span class="n">α</span> <span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span><span class="o">)</span> <span class="o">(</span><span class="n">s</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">s&#39;</span> <span class="o">:</span> <span class="n">set</span> <span class="n">β</span><span class="o">)</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">β</span><span class="o">)</span> <span class="o">:</span>
  <span class="n">f</span> <span class="err">&#39;&#39;</span> <span class="n">s</span> <span class="err">⊆</span> <span class="n">s&#39;</span> <span class="bp">∧</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">f</span> <span class="err">&#39;&#39;</span> <span class="n">s</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="c1">-- refine ⟨_, _⟩,</span>
  <span class="n">repeat</span> <span class="o">{</span> <span class="n">all_goals</span> <span class="o">{</span> <span class="n">split</span> <span class="o">}</span> <span class="o">},</span>
<span class="kn">end</span>
</pre></div>


{% endraw %}
