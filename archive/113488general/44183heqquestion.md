---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/44183heqquestion.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [heq question](https://leanprover-community.github.io/archive/113488general/44183heqquestion.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kevin Buzzard (May 20 2018 at 20:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126840954):
<p>I wanted to get affine scheme = scheme finished today, but I have run into a problem whereby restricting to an open subset is not quite the same as restricting to the same not-defeq version of trhe open subset</p>

#### [ Kevin Buzzard (May 20 2018 at 20:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126840994):
<p>Here's a fairly minimised question</p>

#### [ Kevin Buzzard (May 20 2018 at 20:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126840999):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">set</span>
<span class="kn">section</span> <span class="n">oh_heq</span>
<span class="kn">parameters</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">(</span><span class="n">U</span> <span class="n">V</span> <span class="n">W</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">)</span>

<span class="kn">lemma</span> <span class="n">HU1</span> <span class="o">:</span> <span class="n">U</span> <span class="err">∩</span> <span class="n">V</span> <span class="err">∩</span> <span class="n">W</span> <span class="err">⊆</span> <span class="n">U</span> <span class="o">:=</span> <span class="n">set</span><span class="bp">.</span><span class="n">subset</span><span class="bp">.</span><span class="n">trans</span> <span class="o">(</span><span class="n">set</span><span class="bp">.</span><span class="n">inter_subset_left</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">)</span> <span class="o">(</span><span class="n">set</span><span class="bp">.</span><span class="n">inter_subset_left</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">)</span>
<span class="kn">lemma</span> <span class="n">HV1</span> <span class="o">:</span> <span class="n">U</span> <span class="err">∩</span> <span class="n">V</span> <span class="err">∩</span> <span class="n">W</span> <span class="err">⊆</span> <span class="n">V</span> <span class="o">:=</span> <span class="n">set</span><span class="bp">.</span><span class="n">subset</span><span class="bp">.</span><span class="n">trans</span> <span class="o">(</span><span class="n">set</span><span class="bp">.</span><span class="n">inter_subset_left</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">)</span> <span class="o">(</span><span class="n">set</span><span class="bp">.</span><span class="n">inter_subset_right</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">)</span>
<span class="kn">lemma</span> <span class="n">HW1</span> <span class="o">:</span> <span class="n">U</span> <span class="err">∩</span> <span class="n">V</span> <span class="err">∩</span> <span class="n">W</span> <span class="err">⊆</span> <span class="n">W</span> <span class="o">:=</span> <span class="n">set</span><span class="bp">.</span><span class="n">inter_subset_right</span> <span class="bp">_</span> <span class="bp">_</span>
<span class="kn">lemma</span> <span class="n">HU2</span> <span class="o">:</span> <span class="n">U</span> <span class="err">∩</span> <span class="o">(</span><span class="n">V</span> <span class="err">∩</span> <span class="n">W</span><span class="o">)</span> <span class="err">⊆</span> <span class="n">U</span> <span class="o">:=</span> <span class="n">set</span><span class="bp">.</span><span class="n">inter_subset_left</span> <span class="bp">_</span> <span class="bp">_</span>
<span class="kn">lemma</span> <span class="n">HV2</span> <span class="o">:</span> <span class="n">U</span> <span class="err">∩</span> <span class="o">(</span><span class="n">V</span> <span class="err">∩</span> <span class="n">W</span><span class="o">)</span> <span class="err">⊆</span> <span class="n">V</span> <span class="o">:=</span> <span class="n">set</span><span class="bp">.</span><span class="n">subset</span><span class="bp">.</span><span class="n">trans</span> <span class="o">(</span><span class="n">set</span><span class="bp">.</span><span class="n">inter_subset_right</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">)</span> <span class="o">(</span><span class="n">set</span><span class="bp">.</span><span class="n">inter_subset_left</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">)</span>
<span class="kn">lemma</span> <span class="n">HW2</span> <span class="o">:</span> <span class="n">U</span> <span class="err">∩</span> <span class="o">(</span><span class="n">V</span> <span class="err">∩</span> <span class="n">W</span><span class="o">)</span> <span class="err">⊆</span> <span class="n">W</span> <span class="o">:=</span> <span class="n">set</span><span class="bp">.</span><span class="n">subset</span><span class="bp">.</span><span class="n">trans</span> <span class="o">(</span><span class="n">set</span><span class="bp">.</span><span class="n">inter_subset_right</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">)</span> <span class="o">(</span><span class="n">set</span><span class="bp">.</span><span class="n">inter_subset_right</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">)</span>

<span class="kn">example</span> <span class="o">(</span><span class="n">F</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">[</span><span class="bp">∀</span> <span class="n">Z</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">,</span> <span class="n">group</span> <span class="o">(</span><span class="n">F</span> <span class="n">Z</span><span class="o">)]</span>
<span class="o">(</span><span class="n">Fres</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">X</span> <span class="n">Y</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">,</span> <span class="n">X</span> <span class="err">⊆</span> <span class="n">Y</span> <span class="bp">→</span> <span class="n">F</span> <span class="n">Y</span> <span class="bp">→</span> <span class="n">F</span> <span class="n">X</span><span class="o">)</span>
<span class="o">(</span><span class="n">i</span> <span class="o">:</span> <span class="n">F</span> <span class="n">U</span><span class="o">)</span> <span class="o">(</span><span class="n">j</span> <span class="o">:</span> <span class="n">F</span> <span class="n">V</span><span class="o">)</span> <span class="o">(</span><span class="n">k</span> <span class="o">:</span> <span class="n">F</span> <span class="n">W</span><span class="o">)</span> <span class="o">:</span>
<span class="n">Fres</span> <span class="o">(</span><span class="n">U</span> <span class="err">∩</span> <span class="n">V</span> <span class="err">∩</span> <span class="n">W</span><span class="o">)</span> <span class="n">U</span> <span class="n">HU1</span> <span class="n">i</span> <span class="bp">*</span> <span class="n">Fres</span> <span class="o">(</span><span class="n">U</span> <span class="err">∩</span> <span class="n">V</span> <span class="err">∩</span> <span class="n">W</span><span class="o">)</span> <span class="n">V</span> <span class="n">HV1</span> <span class="n">j</span> <span class="bp">*</span> <span class="n">Fres</span> <span class="o">(</span><span class="n">U</span> <span class="err">∩</span> <span class="n">V</span> <span class="err">∩</span> <span class="n">W</span><span class="o">)</span> <span class="n">W</span> <span class="n">HW1</span> <span class="n">k</span>
<span class="bp">==</span> <span class="n">Fres</span> <span class="o">(</span><span class="n">U</span> <span class="err">∩</span> <span class="o">(</span><span class="n">V</span> <span class="err">∩</span> <span class="n">W</span><span class="o">))</span> <span class="n">U</span> <span class="n">HU2</span> <span class="n">i</span> <span class="bp">*</span> <span class="n">Fres</span> <span class="o">(</span><span class="n">U</span> <span class="err">∩</span> <span class="o">(</span><span class="n">V</span> <span class="err">∩</span> <span class="n">W</span><span class="o">))</span> <span class="n">V</span> <span class="n">HV2</span> <span class="n">j</span> <span class="bp">*</span> <span class="n">Fres</span> <span class="o">(</span><span class="n">U</span> <span class="err">∩</span> <span class="o">(</span><span class="n">V</span> <span class="err">∩</span> <span class="n">W</span><span class="o">))</span> <span class="n">W</span> <span class="n">HW2</span> <span class="n">k</span>
<span class="o">:=</span> <span class="n">sorry</span>

<span class="kn">end</span> <span class="n">oh_heq</span>
</pre></div>

#### [ Kevin Buzzard (May 20 2018 at 20:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126841002):
<p>Is that example true?</p>

#### [ Kevin Buzzard (May 20 2018 at 20:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126841010):
<p>What's going on is that I am constructing an element of F(U cap V cap W)</p>

#### [ Kevin Buzzard (May 20 2018 at 20:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126841012):
<p>and I'm constructing "the same" element of F(U cap (V cap W))</p>

#### [ Kevin Buzzard (May 20 2018 at 20:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126841014):
<p>and I want them to be equal</p>

#### [ Kevin Buzzard (May 20 2018 at 20:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126841015):
<p>or hequal</p>

#### [ Kevin Buzzard (May 20 2018 at 20:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126841061):
<p>I feel like I ran into this sort of problem once before</p>

#### [ Kevin Buzzard (May 20 2018 at 20:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126841062):
<p>and I tried some of the suggestions there</p>

#### [ Kevin Buzzard (May 20 2018 at 20:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126841064):
<p>(before minimising)</p>

#### [ Kevin Buzzard (May 20 2018 at 20:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126841070):
<p><code>congr</code> turns the goal into 29 goals, not all of which are true</p>

#### [ Kevin Buzzard (May 20 2018 at 20:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126841079):
<p><a href="#narrow/stream/113488-general/topic/dependent.20congr_arg.3F" title="#narrow/stream/113488-general/topic/dependent.20congr_arg.3F">https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/dependent.20congr_arg.3F</a></p>

#### [ Kevin Buzzard (May 20 2018 at 20:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126841081):
<p>was the old thread</p>

#### [ Kevin Buzzard (May 20 2018 at 20:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126841123):
<p>simp fails to simplify</p>

#### [ Kevin Buzzard (May 20 2018 at 20:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126841131):
<p>cc fails</p>

#### [ Kevin Buzzard (May 20 2018 at 20:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126841142):
<p>hmm maybe I should tell simp that the two intersections are equal</p>

#### [ Kevin Buzzard (May 20 2018 at 20:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126841143):
<div class="codehilite"><pre><span></span> <span class="k">begin</span>
<span class="k">have</span> <span class="n">Hinter</span> <span class="o">:</span> <span class="n">U</span> <span class="err">∩</span> <span class="n">V</span> <span class="err">∩</span> <span class="n">W</span> <span class="bp">=</span> <span class="n">U</span> <span class="err">∩</span> <span class="o">(</span><span class="n">V</span> <span class="err">∩</span> <span class="n">W</span><span class="o">)</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">cc</span><span class="o">,</span>
<span class="n">simp</span> <span class="o">[</span><span class="n">Hinter</span><span class="o">],</span>
<span class="kn">end</span>
</pre></div>

#### [ Kevin Buzzard (May 20 2018 at 20:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126841144):
<p>fails to simplify</p>

#### [ Kevin Buzzard (May 20 2018 at 21:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126841196):
<p>Is what I have written provable?</p>

#### [ Kevin Buzzard (May 20 2018 at 21:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126841200):
<p>I don't understand how to use <code>subst</code></p>

#### [ Kevin Buzzard (May 20 2018 at 21:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126841296):
<p>Is there some crazy diamond thing going on?</p>

#### [ Kevin Buzzard (May 20 2018 at 21:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126841297):
<p>Is the issue that I have put a ring structure on F (U cap V cap W)</p>

#### [ Kevin Buzzard (May 20 2018 at 21:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126841298):
<p>and a ring structure on F(U cap (V cap W))</p>

#### [ Kevin Buzzard (May 20 2018 at 21:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126841300):
<p>sorry -- a group structure</p>

#### [ Kevin Buzzard (May 20 2018 at 21:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126841301):
<p>[in real life I have rings]</p>

#### [ Kevin Buzzard (May 20 2018 at 21:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126841303):
<p>and a proof that U cap V cap W = U cap (V cap W)</p>

#### [ Kevin Buzzard (May 20 2018 at 21:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126841310):
<p>but now there's the question as to whether the group structures get identified?</p>

#### [ Kevin Buzzard (May 20 2018 at 21:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126841311):
<p>aargh</p>

#### [ Kevin Buzzard (May 20 2018 at 21:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126841312):
<p>Am I in real trouble here??</p>

#### [ Kevin Buzzard (May 20 2018 at 21:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126841406):
<div class="codehilite"><pre><span></span><span class="k">begin</span>
<span class="k">have</span> <span class="n">Hinter</span> <span class="o">:</span> <span class="n">U</span> <span class="err">∩</span> <span class="n">V</span> <span class="err">∩</span> <span class="n">W</span> <span class="bp">=</span> <span class="n">U</span> <span class="err">∩</span> <span class="o">(</span><span class="n">V</span> <span class="err">∩</span> <span class="n">W</span><span class="o">)</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">cc</span><span class="o">,</span>
<span class="n">refine</span> <span class="n">eq</span><span class="bp">.</span><span class="n">drec_on</span> <span class="n">Hinter</span> <span class="bp">_</span><span class="o">,</span>
<span class="n">congr</span><span class="o">,</span>
<span class="c1">-- now three goals:</span>
<span class="c1">-- ⊢ Fres (U ∩ V ∩ W) U HU1 i = Fres (U ∩ V ∩ W) U HU2 i</span>
<span class="c1">-- ⊢ Fres (U ∩ V ∩ W) V HV1 j = Fres (U ∩ V ∩ W) V HV2 j</span>
<span class="c1">-- ⊢ Fres (U ∩ V ∩ W) W HW1 k = Fres (U ∩ V ∩ W) W HW2 k</span>
<span class="n">sorry</span><span class="o">,</span><span class="n">sorry</span><span class="o">,</span><span class="n">sorry</span>
<span class="kn">end</span>
</pre></div>

#### [ Kevin Buzzard (May 20 2018 at 21:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126841408):
<p>Possible progress</p>

#### [ Chris Hughes (May 20 2018 at 21:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126841482):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">set</span>
<span class="kn">section</span> <span class="n">oh_heq</span>
<span class="kn">parameters</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">(</span><span class="n">U</span> <span class="n">V</span> <span class="n">W</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">)</span>

<span class="kn">lemma</span> <span class="n">HU1</span> <span class="o">:</span> <span class="n">U</span> <span class="err">∩</span> <span class="n">V</span> <span class="err">∩</span> <span class="n">W</span> <span class="err">⊆</span> <span class="n">U</span> <span class="o">:=</span> <span class="n">set</span><span class="bp">.</span><span class="n">subset</span><span class="bp">.</span><span class="n">trans</span> <span class="o">(</span><span class="n">set</span><span class="bp">.</span><span class="n">inter_subset_left</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">)</span> <span class="o">(</span><span class="n">set</span><span class="bp">.</span><span class="n">inter_subset_left</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">)</span>
<span class="kn">lemma</span> <span class="n">HV1</span> <span class="o">:</span> <span class="n">U</span> <span class="err">∩</span> <span class="n">V</span> <span class="err">∩</span> <span class="n">W</span> <span class="err">⊆</span> <span class="n">V</span> <span class="o">:=</span> <span class="n">set</span><span class="bp">.</span><span class="n">subset</span><span class="bp">.</span><span class="n">trans</span> <span class="o">(</span><span class="n">set</span><span class="bp">.</span><span class="n">inter_subset_left</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">)</span> <span class="o">(</span><span class="n">set</span><span class="bp">.</span><span class="n">inter_subset_right</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">)</span>
<span class="kn">lemma</span> <span class="n">HW1</span> <span class="o">:</span> <span class="n">U</span> <span class="err">∩</span> <span class="n">V</span> <span class="err">∩</span> <span class="n">W</span> <span class="err">⊆</span> <span class="n">W</span> <span class="o">:=</span> <span class="n">set</span><span class="bp">.</span><span class="n">inter_subset_right</span> <span class="bp">_</span> <span class="bp">_</span>
<span class="kn">lemma</span> <span class="n">HU2</span> <span class="o">:</span> <span class="n">U</span> <span class="err">∩</span> <span class="o">(</span><span class="n">V</span> <span class="err">∩</span> <span class="n">W</span><span class="o">)</span> <span class="err">⊆</span> <span class="n">U</span> <span class="o">:=</span> <span class="n">set</span><span class="bp">.</span><span class="n">inter_subset_left</span> <span class="bp">_</span> <span class="bp">_</span>
<span class="kn">lemma</span> <span class="n">HV2</span> <span class="o">:</span> <span class="n">U</span> <span class="err">∩</span> <span class="o">(</span><span class="n">V</span> <span class="err">∩</span> <span class="n">W</span><span class="o">)</span> <span class="err">⊆</span> <span class="n">V</span> <span class="o">:=</span> <span class="n">set</span><span class="bp">.</span><span class="n">subset</span><span class="bp">.</span><span class="n">trans</span> <span class="o">(</span><span class="n">set</span><span class="bp">.</span><span class="n">inter_subset_right</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">)</span> <span class="o">(</span><span class="n">set</span><span class="bp">.</span><span class="n">inter_subset_left</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">)</span>
<span class="kn">lemma</span> <span class="n">HW2</span> <span class="o">:</span> <span class="n">U</span> <span class="err">∩</span> <span class="o">(</span><span class="n">V</span> <span class="err">∩</span> <span class="n">W</span><span class="o">)</span> <span class="err">⊆</span> <span class="n">W</span> <span class="o">:=</span> <span class="n">set</span><span class="bp">.</span><span class="n">subset</span><span class="bp">.</span><span class="n">trans</span> <span class="o">(</span><span class="n">set</span><span class="bp">.</span><span class="n">inter_subset_right</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">)</span> <span class="o">(</span><span class="n">set</span><span class="bp">.</span><span class="n">inter_subset_right</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">)</span>

<span class="kn">set_option</span> <span class="n">trace</span><span class="bp">.</span><span class="n">app_builder</span> <span class="n">true</span>

<span class="kn">lemma</span> <span class="n">T</span> <span class="o">(</span><span class="n">F</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">[</span><span class="bp">∀</span> <span class="n">Z</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">,</span> <span class="n">group</span> <span class="o">(</span><span class="n">F</span> <span class="n">Z</span><span class="o">)]</span>
<span class="o">(</span><span class="n">Fres</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">X</span> <span class="n">Y</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">,</span> <span class="n">X</span> <span class="err">⊆</span> <span class="n">Y</span> <span class="bp">→</span> <span class="n">F</span> <span class="n">Y</span> <span class="bp">→</span> <span class="n">F</span> <span class="n">X</span><span class="o">)</span>
<span class="o">(</span><span class="n">i</span> <span class="o">:</span> <span class="n">F</span> <span class="n">U</span><span class="o">)</span> <span class="o">(</span><span class="n">j</span> <span class="o">:</span> <span class="n">F</span> <span class="n">V</span><span class="o">)</span> <span class="o">(</span><span class="n">k</span> <span class="o">:</span> <span class="n">F</span> <span class="n">W</span><span class="o">)</span> <span class="o">(</span><span class="n">s</span> <span class="n">t</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">)</span>
<span class="o">(</span><span class="n">hst</span> <span class="o">:</span> <span class="n">s</span> <span class="bp">=</span> <span class="n">t</span><span class="o">)</span>
<span class="o">(</span><span class="n">hsU</span> <span class="o">:</span> <span class="n">s</span> <span class="err">⊆</span> <span class="n">U</span><span class="o">)</span> <span class="o">(</span><span class="n">hsV</span> <span class="o">:</span> <span class="n">s</span> <span class="err">⊆</span> <span class="n">V</span><span class="o">)</span> <span class="o">(</span><span class="n">hsW</span> <span class="o">:</span> <span class="n">s</span> <span class="err">⊆</span> <span class="n">W</span><span class="o">)</span>
<span class="o">(</span><span class="n">htU</span> <span class="o">:</span> <span class="n">t</span> <span class="err">⊆</span> <span class="n">U</span><span class="o">)</span> <span class="o">(</span><span class="n">htV</span> <span class="o">:</span> <span class="n">t</span> <span class="err">⊆</span> <span class="n">V</span><span class="o">)</span> <span class="o">(</span><span class="n">htW</span> <span class="o">:</span> <span class="n">t</span> <span class="err">⊆</span> <span class="n">W</span><span class="o">)</span> <span class="o">:</span>
<span class="n">Fres</span> <span class="n">s</span> <span class="n">U</span> <span class="n">hsU</span> <span class="n">i</span> <span class="bp">*</span> <span class="n">Fres</span> <span class="n">s</span> <span class="n">V</span> <span class="n">hsV</span> <span class="n">j</span> <span class="bp">*</span> <span class="n">Fres</span> <span class="n">s</span> <span class="n">W</span> <span class="n">hsW</span> <span class="n">k</span>
<span class="bp">==</span> <span class="n">Fres</span> <span class="n">t</span> <span class="n">U</span> <span class="n">htU</span> <span class="n">i</span> <span class="bp">*</span> <span class="n">Fres</span> <span class="n">t</span> <span class="n">V</span> <span class="n">htV</span> <span class="n">j</span> <span class="bp">*</span> <span class="n">Fres</span> <span class="n">t</span> <span class="n">W</span> <span class="n">htW</span> <span class="n">k</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">subst</span> <span class="n">hst</span>

<span class="kn">example</span> <span class="o">(</span><span class="n">F</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">[</span><span class="bp">∀</span> <span class="n">Z</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">,</span> <span class="n">group</span> <span class="o">(</span><span class="n">F</span> <span class="n">Z</span><span class="o">)]</span>
<span class="o">(</span><span class="n">Fres</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">X</span> <span class="n">Y</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">,</span> <span class="n">X</span> <span class="err">⊆</span> <span class="n">Y</span> <span class="bp">→</span> <span class="n">F</span> <span class="n">Y</span> <span class="bp">→</span> <span class="n">F</span> <span class="n">X</span><span class="o">)</span>
<span class="o">(</span><span class="n">i</span> <span class="o">:</span> <span class="n">F</span> <span class="n">U</span><span class="o">)</span> <span class="o">(</span><span class="n">j</span> <span class="o">:</span> <span class="n">F</span> <span class="n">V</span><span class="o">)</span> <span class="o">(</span><span class="n">k</span> <span class="o">:</span> <span class="n">F</span> <span class="n">W</span><span class="o">)</span> <span class="o">:</span>
<span class="n">Fres</span> <span class="o">(</span><span class="n">U</span> <span class="err">∩</span> <span class="n">V</span> <span class="err">∩</span> <span class="n">W</span><span class="o">)</span> <span class="n">U</span> <span class="n">HU1</span> <span class="n">i</span> <span class="bp">*</span> <span class="n">Fres</span> <span class="o">(</span><span class="n">U</span> <span class="err">∩</span> <span class="n">V</span> <span class="err">∩</span> <span class="n">W</span><span class="o">)</span> <span class="n">V</span> <span class="n">HV1</span> <span class="n">j</span> <span class="bp">*</span> <span class="n">Fres</span> <span class="o">(</span><span class="n">U</span> <span class="err">∩</span> <span class="n">V</span> <span class="err">∩</span> <span class="n">W</span><span class="o">)</span> <span class="n">W</span> <span class="n">HW1</span> <span class="n">k</span>
<span class="bp">==</span> <span class="n">Fres</span> <span class="o">(</span><span class="n">U</span> <span class="err">∩</span> <span class="o">(</span><span class="n">V</span> <span class="err">∩</span> <span class="n">W</span><span class="o">))</span> <span class="n">U</span> <span class="n">HU2</span> <span class="n">i</span> <span class="bp">*</span> <span class="n">Fres</span> <span class="o">(</span><span class="n">U</span> <span class="err">∩</span> <span class="o">(</span><span class="n">V</span> <span class="err">∩</span> <span class="n">W</span><span class="o">))</span> <span class="n">V</span> <span class="n">HV2</span> <span class="n">j</span> <span class="bp">*</span> <span class="n">Fres</span> <span class="o">(</span><span class="n">U</span> <span class="err">∩</span> <span class="o">(</span><span class="n">V</span> <span class="err">∩</span> <span class="n">W</span><span class="o">))</span> <span class="n">W</span> <span class="n">HW2</span> <span class="n">k</span> <span class="o">:=</span>
<span class="n">T</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="o">(</span><span class="n">set</span><span class="bp">.</span><span class="n">inter_assoc</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">)</span> <span class="n">HU1</span> <span class="n">HV1</span> <span class="n">HW1</span> <span class="n">HU2</span> <span class="n">HV2</span> <span class="n">HW2</span>
</pre></div>


<p>Trouble is <code>subst</code> doesn't work very well when the expression is more complicated than <code>s = t</code></p>

#### [ Kevin Buzzard (May 20 2018 at 21:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126841531):
<p>aah we're back with subst</p>

#### [ Kevin Buzzard (May 20 2018 at 21:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126841533):
<p>I wrote <code>subst [random_thing]</code> and I get an error I don't understand</p>

#### [ Kevin Buzzard (May 20 2018 at 21:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126841539):
<p>so I gave up on subst very early</p>

#### [ Kevin Buzzard (May 20 2018 at 21:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126841540):
<p>you're suggesting I persevere</p>

#### [ Kevin Buzzard (May 20 2018 at 21:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126841542):
<p>My actual use case has rings and it's addition not multiplication</p>

#### [ Kevin Buzzard (May 20 2018 at 21:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126841543):
<p>but it's very close to this</p>

#### [ Chris Hughes (May 20 2018 at 21:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126841544):
<p>I used to use <code>eq.drec_on</code> with an explicit motive for things like this. That's really messy.</p>

#### [ Kevin Buzzard (May 20 2018 at 21:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126841547):
<p>As you saw I tried eq.drec_on and made some progress</p>

#### [ Kevin Buzzard (May 20 2018 at 21:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126841561):
<p>I perhaps need to learn how to use subst</p>

#### [ Kevin Buzzard (May 20 2018 at 21:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126841592):
<p>You saw I proved <code>Hinter : U ∩ V ∩ W = U ∩ (V ∩ W)</code></p>

#### [ Kevin Buzzard (May 20 2018 at 21:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126841596):
<p>but <code>subst Hinter</code>, which somehow feels like what I want to do, gives me <code>subst tactic failed, hypothesis 'Hinter' is not of the form (x = t) or (t = x)</code></p>

#### [ Kevin Buzzard (May 20 2018 at 21:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126841597):
<p>That error message is really unhelpful</p>

#### [ Kevin Buzzard (May 20 2018 at 21:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126841598):
<p>Does anyone know what it actually means?</p>

#### [ Kevin Buzzard (May 20 2018 at 21:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126841599):
<p>Hinter looks like both of those forms to me :-)</p>

#### [ Kevin Buzzard (May 20 2018 at 21:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126841656):
<div class="codehilite"><pre><span></span><span class="k">begin</span>
<span class="k">have</span> <span class="n">Hinter</span> <span class="o">:</span> <span class="n">U</span> <span class="err">∩</span> <span class="n">V</span> <span class="err">∩</span> <span class="n">W</span> <span class="bp">=</span> <span class="n">U</span> <span class="err">∩</span> <span class="o">(</span><span class="n">V</span> <span class="err">∩</span> <span class="n">W</span><span class="o">)</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">cc</span><span class="o">,</span>
<span class="n">subst</span> <span class="n">Hinter</span><span class="o">,</span> <span class="c1">-- subst tactic failed, hypothesis &#39;Hinter&#39; is not of the form (x = t) or (t = x)</span>
<span class="n">sorry</span>
<span class="kn">end</span>
</pre></div>

#### [ Kevin Buzzard (May 20 2018 at 21:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126841659):
<p>How is that different to what you're doing?</p>

#### [ Chris Hughes (May 20 2018 at 21:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126841716):
<p>I think it's basically that it has to be a really simple expression. <code>x = t</code> is fine, but anything like <code> f x = t</code> is not. I might be wrong about that.</p>

#### [ Kevin Buzzard (May 20 2018 at 21:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126841717):
<p>You are telling me that subst won't work unless it literally is (one letter) = (one letter)?</p>

#### [ Kevin Buzzard (May 20 2018 at 21:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126841719):
<p>Well at the end of the day you apparently proved it and I definitely didn't</p>

#### [ Chris Hughes (May 20 2018 at 21:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126841721):
<p>I think so.</p>

#### [ Kevin Buzzard (May 20 2018 at 21:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126841722):
<p><code>set_option trace.app_builder true</code></p>

#### [ Kevin Buzzard (May 20 2018 at 21:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126841724):
<p>What was that all about?</p>

#### [ Chris Hughes (May 20 2018 at 21:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126841775):
<p>In this code your goal shouldn't typecheck</p>
<div class="codehilite"><pre><span></span><span class="k">begin</span>
<span class="k">have</span> <span class="n">Hinter</span> <span class="o">:</span> <span class="n">U</span> <span class="err">∩</span> <span class="n">V</span> <span class="err">∩</span> <span class="n">W</span> <span class="bp">=</span> <span class="n">U</span> <span class="err">∩</span> <span class="o">(</span><span class="n">V</span> <span class="err">∩</span> <span class="n">W</span><span class="o">)</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">cc</span><span class="o">,</span>
<span class="n">refine</span> <span class="n">eq</span><span class="bp">.</span><span class="n">drec_on</span> <span class="n">Hinter</span> <span class="bp">_</span><span class="o">,</span>
<span class="n">congr</span><span class="o">,</span>
<span class="c1">-- now three goals:</span>
<span class="c1">-- ⊢ Fres (U ∩ V ∩ W) U HU1 i = Fres (U ∩ V ∩ W) U HU2 i</span>
<span class="c1">-- ⊢ Fres (U ∩ V ∩ W) V HV1 j = Fres (U ∩ V ∩ W) V HV2 j</span>
<span class="c1">-- ⊢ Fres (U ∩ V ∩ W) W HW1 k = Fres (U ∩ V ∩ W) W HW2 k</span>
<span class="n">sorry</span><span class="o">,</span><span class="n">sorry</span><span class="o">,</span><span class="n">sorry</span>
<span class="kn">end</span>
</pre></div>

#### [ Chris Hughes (May 20 2018 at 21:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126841776):
<p>but it does.</p>

#### [ Chris Hughes (May 20 2018 at 21:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126841792):
<blockquote>
<p><code>set_option trace.app_builder true</code></p>
</blockquote>
<p>That was because something didn't work and the error message suggested I do that.</p>

#### [ Kevin Buzzard (May 20 2018 at 21:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126841794):
<p>yeah that was a bit scary with the =</p>

#### [ Kevin Buzzard (May 20 2018 at 21:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126841797):
<p>but if X = Y then F X = F Y</p>

#### [ Kevin Buzzard (May 20 2018 at 21:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126841855):
<p>Thanks Chris</p>

#### [ Kevin Buzzard (May 20 2018 at 21:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126841858):
<p>Indeed your proof works</p>

#### [ Kevin Buzzard (May 20 2018 at 21:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126841898):
<p>I am currently mulling over having to translate it into the real life situation</p>

#### [ Chris Hughes (May 20 2018 at 21:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126842102):
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">(</span><span class="n">F</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">[</span><span class="bp">∀</span> <span class="n">Z</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">,</span> <span class="n">group</span> <span class="o">(</span><span class="n">F</span> <span class="n">Z</span><span class="o">)]</span>
<span class="o">(</span><span class="n">Fres</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">X</span> <span class="n">Y</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">,</span> <span class="n">X</span> <span class="err">⊆</span> <span class="n">Y</span> <span class="bp">→</span> <span class="n">F</span> <span class="n">Y</span> <span class="bp">→</span> <span class="n">F</span> <span class="n">X</span><span class="o">)</span>
<span class="o">(</span><span class="n">i</span> <span class="o">:</span> <span class="n">F</span> <span class="n">U</span><span class="o">)</span> <span class="o">(</span><span class="n">j</span> <span class="o">:</span> <span class="n">F</span> <span class="n">V</span><span class="o">)</span> <span class="o">(</span><span class="n">k</span> <span class="o">:</span> <span class="n">F</span> <span class="n">W</span><span class="o">)</span> <span class="o">:</span>
<span class="n">Fres</span> <span class="o">(</span><span class="n">U</span> <span class="err">∩</span> <span class="n">V</span> <span class="err">∩</span> <span class="n">W</span><span class="o">)</span> <span class="n">U</span> <span class="n">HU1</span> <span class="n">i</span> <span class="bp">*</span> <span class="n">Fres</span> <span class="o">(</span><span class="n">U</span> <span class="err">∩</span> <span class="n">V</span> <span class="err">∩</span> <span class="n">W</span><span class="o">)</span> <span class="n">V</span> <span class="n">HV1</span> <span class="n">j</span> <span class="bp">*</span> <span class="n">Fres</span> <span class="o">(</span><span class="n">U</span> <span class="err">∩</span> <span class="n">V</span> <span class="err">∩</span> <span class="n">W</span><span class="o">)</span> <span class="n">W</span> <span class="n">HW1</span> <span class="n">k</span>
<span class="bp">==</span> <span class="n">Fres</span> <span class="o">(</span><span class="n">U</span> <span class="err">∩</span> <span class="o">(</span><span class="n">V</span> <span class="err">∩</span> <span class="n">W</span><span class="o">))</span> <span class="n">U</span> <span class="n">HU2</span> <span class="n">i</span> <span class="bp">*</span> <span class="n">Fres</span> <span class="o">(</span><span class="n">U</span> <span class="err">∩</span> <span class="o">(</span><span class="n">V</span> <span class="err">∩</span> <span class="n">W</span><span class="o">))</span> <span class="n">V</span> <span class="n">HV2</span> <span class="n">j</span> <span class="bp">*</span> <span class="n">Fres</span> <span class="o">(</span><span class="n">U</span> <span class="err">∩</span> <span class="o">(</span><span class="n">V</span> <span class="err">∩</span> <span class="n">W</span><span class="o">))</span> <span class="n">W</span> <span class="n">HW2</span> <span class="n">k</span> <span class="o">:=</span>
<span class="k">have</span> <span class="n">Hinter</span> <span class="o">:</span> <span class="n">U</span> <span class="err">∩</span> <span class="n">V</span> <span class="err">∩</span> <span class="n">W</span> <span class="bp">=</span> <span class="n">U</span> <span class="err">∩</span> <span class="o">(</span><span class="n">V</span> <span class="err">∩</span> <span class="n">W</span><span class="o">)</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">cc</span><span class="o">,</span>
<span class="bp">@</span><span class="n">eq</span><span class="bp">.</span><span class="n">drec_on</span> <span class="bp">_</span> <span class="o">(</span><span class="n">U</span> <span class="err">∩</span> <span class="n">V</span> <span class="err">∩</span> <span class="n">W</span><span class="o">)</span>
<span class="o">(</span><span class="bp">λ</span> <span class="n">s</span> <span class="n">h</span><span class="o">,</span> <span class="n">Fres</span> <span class="o">(</span><span class="n">U</span> <span class="err">∩</span> <span class="n">V</span> <span class="err">∩</span> <span class="n">W</span><span class="o">)</span> <span class="n">U</span> <span class="n">HU1</span> <span class="n">i</span> <span class="bp">*</span> <span class="n">Fres</span> <span class="o">(</span><span class="n">U</span> <span class="err">∩</span> <span class="n">V</span> <span class="err">∩</span> <span class="n">W</span><span class="o">)</span> <span class="n">V</span> <span class="n">HV1</span> <span class="n">j</span> <span class="bp">*</span> <span class="n">Fres</span> <span class="o">(</span><span class="n">U</span> <span class="err">∩</span> <span class="n">V</span> <span class="err">∩</span> <span class="n">W</span><span class="o">)</span> <span class="n">W</span> <span class="n">HW1</span> <span class="n">k</span>
<span class="bp">==</span> <span class="n">Fres</span> <span class="n">s</span> <span class="n">U</span> <span class="o">(</span><span class="n">h</span> <span class="bp">▸</span> <span class="n">HU1</span><span class="o">)</span> <span class="n">i</span> <span class="bp">*</span> <span class="n">Fres</span> <span class="n">s</span> <span class="n">V</span> <span class="o">(</span><span class="n">h</span> <span class="bp">▸</span> <span class="n">HV1</span><span class="o">)</span> <span class="n">j</span> <span class="bp">*</span> <span class="n">Fres</span> <span class="n">s</span> <span class="n">W</span> <span class="o">(</span><span class="n">h</span> <span class="bp">▸</span> <span class="n">HW1</span><span class="o">)</span> <span class="n">k</span><span class="o">)</span> <span class="bp">_</span> <span class="n">Hinter</span> <span class="o">(</span><span class="n">heq</span><span class="bp">.</span><span class="n">refl</span> <span class="bp">_</span><span class="o">)</span>
</pre></div>

#### [ Chris Hughes (May 20 2018 at 21:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126842149):
<p>Probably the best solution is to get <code>subst</code> to work properly. Might be a good after exams project.</p>

#### [ Kevin Buzzard (May 20 2018 at 22:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126843676):
<p>Thanks a lot for this Chris! I'll see if this method works in my actual file</p>

#### [ Mario Carneiro (May 21 2018 at 00:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126846183):
<p>This works, but I'm not very happy with the result</p>
<div class="codehilite"><pre><span></span>theorem proof_irrel_heq {p q : Prop} (e : p = q) (hp : p) (hq : q) : hp == hq :=
by subst q; congr

example (F : set α → Type) [∀ Z : set α, group (F Z)]
(Fres : ∀ X Y : set α, X ⊆ Y → F Y → F X)
(i : F U) (j : F V) (k : F W) :
Fres (U ∩ V ∩ W) U HU1 i * Fres (U ∩ V ∩ W) V HV1 j * Fres (U ∩ V ∩ W) W HW1 k
== Fres (U ∩ (V ∩ W)) U HU2 i * Fres (U ∩ (V ∩ W)) V HV2 j * Fres (U ∩ (V ∩ W)) W HW2 k
:=
by have := set.inter_assoc U V W;
   congr; try{assumption};
   { apply proof_irrel_heq, congr, assumption }
</pre></div>

#### [ Mario Carneiro (May 21 2018 at 00:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126846280):
<p>Didn't I tell you partial functions give you headaches?</p>

#### [ Mario Carneiro (May 21 2018 at 00:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126846474):
<p>Why do you have a <code>heq</code> goal in the first place?</p>

#### [ Kenny Lau (May 21 2018 at 00:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126846718):
<p>because of bad interface</p>

#### [ Mario Carneiro (May 21 2018 at 00:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126846779):
<p>oh, there's a bug in <code>congr</code></p>

#### [ Mario Carneiro (May 21 2018 at 00:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126846874):
<div class="codehilite"><pre><span></span>meta def congr&#39; : parse small_nat? → tactic unit
| none         := focus1 (assumption &lt;|&gt; (congr_core &gt;&gt;
  all_goals (reflexivity &lt;|&gt; try (congr&#39; none))))
| (some 0)     := failed
| (some (n+1)) := focus1 (assumption &lt;|&gt; (congr_core &gt;&gt;
  all_goals (reflexivity &lt;|&gt; try (congr&#39; (some n)))))
</pre></div>


<p>now the following proof works:</p>
<div class="codehilite"><pre><span></span>by have := set.inter_assoc U V W;
   congr&#39;; apply proof_irrel_heq; congr&#39;
</pre></div>

#### [ Kenny Lau (May 21 2018 at 00:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126846883):
<p>say what</p>

#### [ Mario Carneiro (May 21 2018 at 00:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126846933):
<p>The congr tactic itself should read:</p>
<div class="codehilite"><pre><span></span>meta def congr : tactic unit :=
do focus1 (assumption &lt;|&gt; (congr_core &gt;&gt; all_goals (reflexivity &lt;|&gt; try congr)))
</pre></div>


<p>instead of </p>
<div class="codehilite"><pre><span></span>meta def congr : tactic unit :=
do focus1 (try assumption &gt;&gt; congr_core &gt;&gt; all_goals (try reflexivity &gt;&gt; try congr))
</pre></div>

#### [ Mario Carneiro (May 21 2018 at 00:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126846934):
<p>but I don't know if we are still doing bugfixes in 3.4.1</p>

#### [ Mario Carneiro (May 21 2018 at 00:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126846936):
<p>so I made my own <code>congr</code> instead</p>

#### [ Mario Carneiro (May 21 2018 at 00:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126846990):
<p>Not sure why those proof irrel goals appear though, they should also be taken care of by <code>congr</code></p>

#### [ Kevin Buzzard (May 21 2018 at 09:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126860293):
<blockquote>
<p>Why do you have a <code>heq</code> goal in the first place?</p>
</blockquote>
<p>I thought of a way around it, in this case.</p>

#### [ Kevin Buzzard (May 21 2018 at 09:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126860302):
<p>The reason was that I wanted to prove two structures were equal, but one depended on (U cap V cap W) and one on (U cap (V cap W)), because of the way the structures were made (I was trying to prove addition on a quotient type was associative).</p>

#### [ Kevin Buzzard (May 21 2018 at 09:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126860350):
<p><code>congr</code> would go insane when presented with the problem (the first time I tried it, it turned my goal into 176 goals, no typo)</p>

#### [ Kevin Buzzard (May 21 2018 at 09:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126860351):
<p>Kenny suggested a mk_inj solution and that led to the heqs</p>

#### [ Kevin Buzzard (May 21 2018 at 09:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126860352):
<p>I remember Chris moaning about heqs before</p>

#### [ Kevin Buzzard (May 21 2018 at 09:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126860358):
<p>But last night, 10 minutes after I switched my laptop off and started doing the dishes</p>

#### [ Kevin Buzzard (May 21 2018 at 09:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126860360):
<p>I realised I could probably work around it on this occasion, by doing something a mathematican would never understand</p>

#### [ Kevin Buzzard (May 21 2018 at 09:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126860361):
<p>I should restrict my section on U cap (V cap W) to a section on U cap V cap W :-)</p>

#### [ Kevin Buzzard (May 21 2018 at 09:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126860401):
<p>This only changes it up to equivalence, which is OK for me</p>

#### [ Kevin Buzzard (May 21 2018 at 09:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126860409):
<p>[terminology: a sheaf is, amongst other things, a map F : (open sets in a top space) -&gt; (rings) together with restriction maps F(U) -&gt; F(V) whenever V is a subset of U]</p>

#### [ Kevin Buzzard (May 21 2018 at 09:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126860447):
<p>The concept of restricting to a subset which is non-definitionally-equal to the set you started with is alien to mathematics but it's exactly the crazy idea which will get me out of this hell</p>

#### [ Kevin Buzzard (May 21 2018 at 09:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126860467):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> Is Chris right when he suggests that subst could do with some work? His solution seemed to be "subst hst, where h : s = t, and then apply when s and t are more complicated"</p>

#### [ Kevin Buzzard (May 21 2018 at 09:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126860471):
<p>as opposed to "subst [the thing we actually want to subst]"</p>

#### [ Kevin Buzzard (May 21 2018 at 09:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126860477):
<p>I could imagine that Chris might want to learn something about tactics over the summer. He has two months of being paid to work for me and can do anything</p>

#### [ Kevin Buzzard (May 21 2018 at 09:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126860478):
<p>as long as his boss OK's it</p>

#### [ Mario Carneiro (May 21 2018 at 09:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126860530):
<p>I was thinking of suggesting that myself. I assume you have some composition axioms, so it might be easiest to work with the restriction from (U/\V)/\W to U/\V/\W</p>

#### [ Mario Carneiro (May 21 2018 at 09:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126860540):
<p>It's not as crazy as it sounds; it's basically using (part of) the fact that (U/\V)/\W and U/\V/\W are "isomorphic but not equal" in the DTT sense</p>

#### [ Mario Carneiro (May 21 2018 at 09:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126860581):
<p>it helps to think like in category theory here</p>

#### [ Mario Carneiro (May 21 2018 at 09:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126860586):
<p><code>subst</code> is a very basic tactic. It does one thing, and does it well</p>

#### [ Mario Carneiro (May 21 2018 at 09:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126860647):
<p>you give it a hypothesis of the form <code>term = x</code> or <code>x = term</code>, and it will eliminate <code>x</code> in favor of <code>term</code> everywhere. This is rather restrictive, but the upside is that it <em>never</em> gets tripped up in dependencies like <code>rw</code> and <code>simp</code> can, because it is implemented purely using <code>eq.drec</code> and the variable restriction ensures that the motive is always type correct</p>

#### [ Kevin Buzzard (May 21 2018 at 09:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126860650):
<p>Oh -- <code>x = t</code> means <code>x = term</code>? ;-)</p>

#### [ Mario Carneiro (May 21 2018 at 09:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126860680):
<p>(you can also say <code>subst x</code> instead of <code>subst h</code> when you have <code>h : x = term</code> in the context)</p>

#### [ Kevin Buzzard (May 21 2018 at 09:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126860694):
<p>isomorphic but not equal is something I know well in the context where the underlying sets are different, but I am only just coming to terms with generalising the idea to situations where the DTTist thinks they're isomorphic and the ZFCist is blinded by this because they think they're equal :-)</p>

#### [ Kevin Buzzard (May 21 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126860699):
<p>Unrelated -- I see you wrote (U cap V) cap W v U cap V cap W</p>

#### [ Kevin Buzzard (May 21 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126860701):
<p>I claim that you mean U cap (V cap W) vs U cap V cap W</p>

#### [ Kevin Buzzard (May 21 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126860702):
<p>and actually this is minorly annoying</p>

#### [ Kevin Buzzard (May 21 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126860703):
<p>because my proofs that x is in U cap V cap W</p>

#### [ Kevin Buzzard (May 21 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126860705):
<p>all look like &lt;&lt;HU,HV&gt;,HW&gt;</p>

#### [ Mario Carneiro (May 21 2018 at 09:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126860744):
<p>ah, cap is left assoc?</p>

#### [ Kevin Buzzard (May 21 2018 at 09:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126860745):
<p>Is this an oversight</p>

#### [ Kevin Buzzard (May 21 2018 at 09:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126860746):
<p>I assume it is</p>

#### [ Kevin Buzzard (May 21 2018 at 09:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126860747):
<p>and I already noticed that this was annoying</p>

#### [ Kevin Buzzard (May 21 2018 at 09:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126860749):
<p>but I wasn't confident enough to know whether there are other reasons for this</p>

#### [ Mario Carneiro (May 21 2018 at 09:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126860750):
<p>I don't have any strong opinions on whether union and intersection are left or right assoc</p>

#### [ Kevin Buzzard (May 21 2018 at 09:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126860751):
<p>all I knew is that my proofs were two characters longer than I wanted them to be</p>

#### [ Kevin Buzzard (May 21 2018 at 09:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126860758):
<p>you would do if you had to keep writing &lt;&lt;HU,HV&gt;,HW&gt;</p>

#### [ Kevin Buzzard (May 21 2018 at 09:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126860763):
<p>heh</p>

#### [ Kevin Buzzard (May 21 2018 at 09:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126860765):
<p>maybe I should restrict to U cap (V cap W)</p>

#### [ Mario Carneiro (May 21 2018 at 09:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126860766):
<p>also lost two chars there</p>

#### [ Kevin Buzzard (May 21 2018 at 09:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126860768):
<p>yeah but I only have to do that once</p>

#### [ Kevin Buzzard (May 21 2018 at 09:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126860810):
<p>Something else I noticed</p>

#### [ Kevin Buzzard (May 21 2018 at 09:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126860811):
<p>was that existsi is kind of dumb</p>

#### [ Mario Carneiro (May 21 2018 at 09:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126860812):
<p>I never use it tbh</p>

#### [ Kevin Buzzard (May 21 2018 at 09:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126860813):
<p>existsi (&lt;&lt;HU,HV&gt;,HW&gt;)</p>

#### [ Mario Carneiro (May 21 2018 at 09:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126860814):
<p>lol no</p>

#### [ Kevin Buzzard (May 21 2018 at 09:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126860816):
<p>"That doesn't make sense"</p>

#### [ Kevin Buzzard (May 21 2018 at 09:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126860820):
<p>"You have to tell me the type"</p>

#### [ Kevin Buzzard (May 21 2018 at 09:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126860822):
<p>"because I don't know the type"</p>

#### [ Kevin Buzzard (May 21 2018 at 09:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126860828):
<p>"even though the goal is "there exists a proof that x is in U cap V cap W"</p>

#### [ Kevin Buzzard (May 21 2018 at 09:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126860829):
<p>"</p>

#### [ Mario Carneiro (May 21 2018 at 09:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126860830):
<p>just use refine instead</p>

#### [ Kevin Buzzard (May 21 2018 at 09:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126860833):
<p>What are your views on "existsi _,tactic.swap"</p>

#### [ Kevin Buzzard (May 21 2018 at 09:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126860834):
<p>I think you once told me to avoid it</p>

#### [ Kevin Buzzard (May 21 2018 at 09:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126860835):
<p>but it does exactly what I want sometimes</p>

#### [ Kevin Buzzard (May 21 2018 at 09:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126860878):
<p>"let's just remove the bloody exists symbol and make it a goal"</p>

#### [ Mario Carneiro (May 21 2018 at 09:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126860880):
<p>For exploratory tactic writing it's fine I guess</p>

#### [ Kevin Buzzard (May 21 2018 at 09:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126860881):
<p>what about definitive scheme writing?</p>

#### [ Kevin Buzzard (May 21 2018 at 09:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126860884):
<p>:-)</p>

#### [ Kevin Buzzard (May 21 2018 at 09:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126860890):
<p>I guess it's all exploratory as far as I am concerned</p>

#### [ Kevin Buzzard (May 21 2018 at 09:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126860892):
<p>OK back to work</p>

#### [ Kevin Buzzard (May 21 2018 at 09:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126860893):
<p>Thanks for the comments as ever</p>

#### [ Kevin Buzzard (May 21 2018 at 09:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126861159):
<p>rofl</p>

#### [ Kevin Buzzard (May 21 2018 at 09:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126861161):
<p>I proved associativity</p>

#### [ Kevin Buzzard (May 21 2018 at 09:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126861163):
<p>end of proof looks like this</p>

#### [ Kevin Buzzard (May 21 2018 at 09:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126861164):
<div class="codehilite"><pre><span></span>  <span class="n">existsi</span> <span class="o">(</span><span class="n">Ua</span> <span class="err">∩</span> <span class="n">Ub</span> <span class="err">∩</span> <span class="n">Uc</span><span class="o">),</span> <span class="c1">-- brainwave</span>
  <span class="n">existsi</span> <span class="o">(</span><span class="bp">⟨⟨</span><span class="n">Hxa</span><span class="o">,</span><span class="n">Hxb</span><span class="bp">⟩</span><span class="o">,</span><span class="n">Hxc</span><span class="bp">⟩</span> <span class="o">:</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">Ua</span> <span class="err">∩</span> <span class="n">Ub</span> <span class="err">∩</span> <span class="n">Uc</span><span class="o">),</span>
  <span class="n">existsi</span> <span class="o">(</span><span class="n">Hstandard</span> <span class="bp">_</span> <span class="bp">_</span> <span class="o">(</span><span class="n">Hstandard</span> <span class="bp">_</span> <span class="bp">_</span> <span class="n">BUa</span> <span class="n">BUb</span><span class="o">)</span> <span class="n">BUc</span><span class="o">),</span>
  <span class="n">existsi</span> <span class="o">(</span><span class="n">set</span><span class="bp">.</span><span class="n">subset</span><span class="bp">.</span><span class="n">refl</span> <span class="o">(</span><span class="n">Ua</span> <span class="err">∩</span> <span class="n">Ub</span> <span class="err">∩</span> <span class="n">Uc</span><span class="o">)),</span>
  <span class="n">existsi</span> <span class="o">((</span><span class="n">set</span><span class="bp">.</span><span class="n">inter_assoc</span> <span class="n">Ua</span> <span class="n">Ub</span> <span class="n">Uc</span> <span class="bp">▸</span> <span class="n">set</span><span class="bp">.</span><span class="n">subset</span><span class="bp">.</span><span class="n">refl</span> <span class="bp">_</span><span class="o">)</span> <span class="o">:</span> <span class="n">Ua</span> <span class="err">∩</span> <span class="n">Ub</span> <span class="err">∩</span> <span class="n">Uc</span> <span class="err">⊆</span> <span class="n">Ua</span> <span class="err">∩</span> <span class="o">(</span><span class="n">Ub</span> <span class="err">∩</span> <span class="n">Uc</span><span class="o">)),</span>
  <span class="n">rw</span> <span class="o">(</span><span class="n">presheaf_of_rings_on_basis</span><span class="bp">.</span><span class="n">res_is_ring_morphism</span> <span class="n">FPRB</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">)</span><span class="bp">.</span><span class="n">map_add</span><span class="o">,</span>
  <span class="n">rw</span> <span class="o">(</span><span class="n">presheaf_of_rings_on_basis</span><span class="bp">.</span><span class="n">res_is_ring_morphism</span> <span class="n">FPRB</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">)</span><span class="bp">.</span><span class="n">map_add</span><span class="o">,</span>
  <span class="n">rw</span> <span class="o">(</span><span class="n">presheaf_of_rings_on_basis</span><span class="bp">.</span><span class="n">res_is_ring_morphism</span> <span class="n">FPRB</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">)</span><span class="bp">.</span><span class="n">map_add</span><span class="o">,</span>
  <span class="n">rw</span> <span class="o">(</span><span class="n">presheaf_of_rings_on_basis</span><span class="bp">.</span><span class="n">res_is_ring_morphism</span> <span class="n">FPRB</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">)</span><span class="bp">.</span><span class="n">map_add</span><span class="o">,</span>
  <span class="n">rw</span> <span class="o">(</span><span class="n">presheaf_of_rings_on_basis</span><span class="bp">.</span><span class="n">res_is_ring_morphism</span> <span class="n">FPRB</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">)</span><span class="bp">.</span><span class="n">map_add</span><span class="o">,</span>
  <span class="n">rw</span> <span class="o">(</span><span class="n">presheaf_of_rings_on_basis</span><span class="bp">.</span><span class="n">res_is_ring_morphism</span> <span class="n">FPRB</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">)</span><span class="bp">.</span><span class="n">map_add</span><span class="o">,</span>
  <span class="n">rw</span> <span class="err">←</span><span class="n">presheaf_of_types_on_basis</span><span class="bp">.</span><span class="n">Hcomp&#39;</span><span class="o">,</span>
  <span class="n">rw</span> <span class="err">←</span><span class="n">presheaf_of_types_on_basis</span><span class="bp">.</span><span class="n">Hcomp&#39;</span><span class="o">,</span>
  <span class="n">rw</span> <span class="err">←</span><span class="n">presheaf_of_types_on_basis</span><span class="bp">.</span><span class="n">Hcomp&#39;</span><span class="o">,</span>
  <span class="n">rw</span> <span class="err">←</span><span class="n">presheaf_of_types_on_basis</span><span class="bp">.</span><span class="n">Hcomp&#39;</span><span class="o">,</span>
  <span class="n">rw</span> <span class="err">←</span><span class="n">presheaf_of_types_on_basis</span><span class="bp">.</span><span class="n">Hcomp&#39;</span><span class="o">,</span>
  <span class="n">rw</span> <span class="err">←</span><span class="n">presheaf_of_types_on_basis</span><span class="bp">.</span><span class="n">Hcomp&#39;</span><span class="o">,</span>
  <span class="n">rw</span> <span class="err">←</span><span class="n">presheaf_of_types_on_basis</span><span class="bp">.</span><span class="n">Hcomp&#39;</span><span class="o">,</span>
  <span class="n">rw</span> <span class="err">←</span><span class="n">presheaf_of_types_on_basis</span><span class="bp">.</span><span class="n">Hcomp&#39;</span><span class="o">,</span>
  <span class="n">rw</span> <span class="err">←</span><span class="n">presheaf_of_types_on_basis</span><span class="bp">.</span><span class="n">Hcomp&#39;</span><span class="o">,</span>
  <span class="n">rw</span> <span class="err">←</span><span class="o">(</span><span class="n">presheaf_of_rings_on_basis</span><span class="bp">.</span><span class="n">res_is_ring_morphism</span> <span class="n">FPRB</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">)</span><span class="bp">.</span><span class="n">map_add</span><span class="o">,</span>
  <span class="n">rw</span> <span class="o">(</span><span class="n">presheaf_of_rings_on_basis</span><span class="bp">.</span><span class="n">res_is_ring_morphism</span> <span class="n">FPRB</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">)</span><span class="bp">.</span><span class="n">map_add</span><span class="o">,</span>
  <span class="n">rw</span> <span class="err">←</span><span class="n">presheaf_of_types_on_basis</span><span class="bp">.</span><span class="n">Hcomp&#39;</span><span class="o">,</span>
  <span class="n">rw</span> <span class="err">←</span><span class="n">presheaf_of_types_on_basis</span><span class="bp">.</span><span class="n">Hcomp&#39;</span><span class="o">,</span>
  <span class="n">rw</span> <span class="n">add_assoc</span><span class="o">,</span>
</pre></div>

#### [ Kevin Buzzard (May 21 2018 at 09:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126861165):
<p>restrict to isomorphic set</p>

#### [ Kevin Buzzard (May 21 2018 at 09:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126861171):
<p>prove some trivialities</p>

#### [ Kevin Buzzard (May 21 2018 at 09:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126861173):
<p>a bit of rewriting</p>

#### [ Kevin Buzzard (May 21 2018 at 09:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126861174):
<p>and apply associativity</p>

#### [ Kevin Buzzard (May 21 2018 at 09:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126861177):
<p>not sure that proof is mathlib-ready</p>

#### [ Mario Carneiro (May 21 2018 at 09:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126861289):
<p>have you tried using <code>simp</code> instead of <code>rw</code>?</p>

#### [ Kevin Buzzard (May 21 2018 at 09:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126861295):
<p>simp insists on rewriting a+b+c as c+a+b</p>

#### [ Kevin Buzzard (May 21 2018 at 09:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126861296):
<p>on exactly one side</p>

#### [ Kevin Buzzard (May 21 2018 at 09:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126861298):
<p>so I never got it to do anything useful</p>

#### [ Kevin Buzzard (May 21 2018 at 09:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126861347):
<p>anyway, this is a breakthrough because if I can prove add_assoc I can prove all the ring axioms</p>

#### [ Kevin Buzzard (May 21 2018 at 09:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126861403):
<p>simp [add_assoc,more stuff] doesn't even do it when we're on the last line</p>

#### [ Kevin Buzzard (May 21 2018 at 09:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126861404):
<p>My goal is too messy for simp</p>

#### [ Kevin Buzzard (May 21 2018 at 09:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126861405):
<p>I need comp</p>

#### [ Kevin Buzzard (May 21 2018 at 09:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126861413):
<p>lol</p>

#### [ Kevin Buzzard (May 21 2018 at 09:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126861419):
<p><code>    simp [add_assoc,add_comm,(presheaf_of_rings_on_basis.res_is_ring_morphism FPRB _ _ _).map_add,presheaf_of_types_on_basis.Hcomp']</code> turns a goal which is closed by <code>rw add_assoc</code> to a goal which is closed by <code>rw add_comm</code></p>

#### [ Kevin Buzzard (May 21 2018 at 09:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126861421):
<p>thanks simp</p>

#### [ Kevin Buzzard (May 21 2018 at 09:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126861481):
<p>goal is <code>(FPRB.to_presheaf_of_types_on_basis).res _ _ _ sa + (FPRB.to_presheaf_of_types_on_basis).res _ _ _ sb +
      (FPRB.to_presheaf_of_types_on_basis).res _ _ _ sc =
    (FPRB.to_presheaf_of_types_on_basis).res _ _ _ sa +
      ((FPRB.to_presheaf_of_types_on_basis).res _ _ _ sb + (FPRB.to_presheaf_of_types_on_basis).res _ _ _ sc)</code></p>

#### [ Kevin Buzzard (May 21 2018 at 09:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126861483):
<p><code>    simp [add_assoc,add_comm],</code></p>

#### [ Kevin Buzzard (May 21 2018 at 09:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126861525):
<p>goal becomes <code>(FPRB.to_presheaf_of_types_on_basis).res _ _ _ sc + (FPRB.to_presheaf_of_types_on_basis).res _ _ _ sb =
    (FPRB.to_presheaf_of_types_on_basis).res _ _ _ sb + (FPRB.to_presheaf_of_types_on_basis).res _ _ _ sc</code></p>

#### [ Kevin Buzzard (May 21 2018 at 09:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126861527):
<p>Unless my eyes are deceiving me simp just turned add_assoc into add_comm</p>

#### [ Kevin Buzzard (May 21 2018 at 09:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126861532):
<p>terms are in a comm_ring</p>

#### [ Kevin Buzzard (May 21 2018 at 09:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126861601):
<p>obviously-minimised version doesn't exhibit the problem</p>

#### [ Kevin Buzzard (May 21 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126861645):
<p>sa,sb,sc all in different rings, the FPRB...res is mapping them down all into the same ring</p>

#### [ Kevin Buzzard (May 21 2018 at 09:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126861663):
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">(</span><span class="n">R</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">[</span><span class="n">comm_ring</span> <span class="n">R</span><span class="o">]</span> <span class="o">(</span><span class="n">α</span> <span class="n">β</span> <span class="n">γ</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">b</span> <span class="o">:</span> <span class="n">β</span><span class="o">)</span> <span class="o">(</span><span class="n">c</span> <span class="o">:</span> <span class="n">γ</span><span class="o">)</span>
<span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">R</span><span class="o">)</span> <span class="o">(</span><span class="n">g</span> <span class="o">:</span> <span class="n">β</span> <span class="bp">→</span> <span class="n">R</span><span class="o">)</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">γ</span> <span class="bp">→</span> <span class="n">R</span><span class="o">)</span> <span class="o">:</span> <span class="n">f</span> <span class="n">a</span> <span class="bp">+</span> <span class="n">g</span> <span class="n">b</span> <span class="bp">+</span> <span class="n">h</span> <span class="n">c</span> <span class="bp">=</span> <span class="n">f</span> <span class="n">a</span> <span class="bp">+</span> <span class="o">(</span><span class="n">g</span> <span class="n">b</span> <span class="bp">+</span> <span class="n">h</span> <span class="n">c</span><span class="o">)</span> <span class="o">:=</span> <span class="k">begin</span>
<span class="n">simp</span> <span class="o">[</span><span class="n">add_assoc</span><span class="o">,</span><span class="n">add_comm</span><span class="o">],</span>
<span class="kn">end</span>
</pre></div>

#### [ Kevin Buzzard (May 21 2018 at 09:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126861664):
<p>works fine</p>

#### [ Kevin Buzzard (May 21 2018 at 09:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126861705):
<p>so it's something in my <code>_</code>s</p>

#### [ Kevin Buzzard (May 21 2018 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126861768):
<p>but at the end of the day I have a goal which can be cleared (without errors) either with <code>rw add_assoc</code> or <code>simp [add_assoc,add_comm],rw add_comm</code></p>

#### [ Kevin Buzzard (May 21 2018 at 10:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126861886):
<p>hey stupid comm_ring, why are you asking me to prove a+0=a and 0+a=a and a+b=b+a?</p>

#### [ Kevin Buzzard (May 21 2018 at 10:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126861889):
<p>well, I know why</p>

#### [ Kevin Buzzard (May 21 2018 at 10:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126861891):
<p>but wouldn't it be nice if you didn't</p>

#### [ Kevin Buzzard (May 21 2018 at 10:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126861896):
<p>I need a better comm_ring constructor I guess</p>

#### [ Chris Hughes (May 21 2018 at 10:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126863336):
<p><code>simp only</code> might help</p>

#### [ Mario Carneiro (May 21 2018 at 11:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126863815):
<p>you can always add <code>-add_comm</code> to your simp set to fix superfluous rewriting</p>

#### [ Kevin Buzzard (May 21 2018 at 11:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126863881):
<p><code>existsi (Ua ∩ Ua)</code></p>

#### [ Kevin Buzzard (May 21 2018 at 11:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126863882):
<p>I can't believe I just wrote that</p>

#### [ Kevin Buzzard (May 21 2018 at 11:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126863883):
<p>proving add_neg</p>

#### [ Kevin Buzzard (May 21 2018 at 11:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126863923):
<p>just restrict everything down to there and it will be fine</p>

#### [ Patrick Massot (May 21 2018 at 11:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126864002):
<p>Just to be sure: Kevin, do you know you can write <code>repeat { rw (presheaf_of_rings_on_basis.res_is_ring_morphism FPRB _ _ _).map_add, },</code>?</p>

#### [ Kevin Buzzard (May 21 2018 at 11:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126864156):
<p>yeah, but I like watching the goal slowly decay</p>

#### [ Kevin Buzzard (May 21 2018 at 11:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126864162):
<p>I just had to write <code> rw is_ring_hom.map_neg (FPRB.res _ _ _);try {apply_instance},</code></p>

#### [ Kevin Buzzard (May 21 2018 at 11:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126864164):
<p>that surprised me.</p>

#### [ Patrick Massot (May 21 2018 at 11:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126864168):
<p>I'm still puzzled each time I need to write <code>apply_instance</code>.</p>

#### [ Patrick Massot (May 21 2018 at 11:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126864171):
<p>I don't understand why Lean doesn't do that for me</p>

#### [ Patrick Massot (May 21 2018 at 11:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126864177):
<p>sometimes</p>

#### [ Kevin Buzzard (May 21 2018 at 11:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126864179):
<p>I applied map_neg (the statement that a morphism of rings satisfies f(-x)=-f(x))</p>

#### [ Kevin Buzzard (May 21 2018 at 11:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126864185):
<p>and all of a sudden it asked me if f was a ring hom and was the source a ring?</p>

#### [ Kevin Buzzard (May 21 2018 at 11:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126864191):
<p>and apply_instance said yes</p>

#### [ Patrick Massot (May 21 2018 at 11:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126864254):
<p>Exactly the kind of situation where I'm puzzled</p>

#### [ Patrick Massot (May 21 2018 at 11:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126864257):
<p>Why isn't this automatic?</p>

#### [ Kevin Buzzard (May 21 2018 at 11:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126864259):
<p>I dunno</p>

#### [ Kevin Buzzard (May 21 2018 at 11:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126864298):
<p>I have two choices today</p>

#### [ Patrick Massot (May 21 2018 at 11:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126864301):
<p>Is it a bug in the <code>apply</code> tactic?</p>

#### [ Kevin Buzzard (May 21 2018 at 11:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126864305):
<p>I could spend a pleasant day verifying the axioms of a ring</p>

#### [ Patrick Massot (May 21 2018 at 11:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126864306):
<p>(Or simp, refine,...)</p>

#### [ Kevin Buzzard (May 21 2018 at 11:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126864307):
<p>or I could mark 100 proofs of various trivial lemmas about sup of a set of reals</p>

#### [ Kevin Buzzard (May 21 2018 at 11:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126864309):
<p>and I am currently at home doing the former</p>

#### [ Kevin Buzzard (May 21 2018 at 11:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126864312):
<p>and I'm already on add_comm</p>

#### [ Kevin Buzzard (May 21 2018 at 11:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126864318):
<p>but I really should be doing the latter...</p>

#### [ Patrick Massot (May 21 2018 at 11:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126864323):
<p>Too bad you can't quite hire Kenny or Chris to mark these exams for you...</p>

#### [ Kevin Buzzard (May 21 2018 at 11:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126864324):
<p>I knew that once I managed add_assoc the rest would be trivial</p>

#### [ Kevin Buzzard (May 21 2018 at 11:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126864326):
<p>but it takes time</p>

#### [ Kevin Buzzard (May 21 2018 at 11:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126864327):
<p>rofl</p>

#### [ Kevin Buzzard (May 21 2018 at 11:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126864330):
<p>I'm not sure if the university would be keen on students marking their own scripts</p>

#### [ Patrick Massot (May 21 2018 at 11:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126864384):
<p>yep, universities tend to have all kind of stupid administrative rules like that</p>

#### [ Kevin Buzzard (May 21 2018 at 11:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126864386):
<p>I am much keener on Lean marking their scripts</p>

#### [ Kevin Buzzard (May 21 2018 at 11:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126864391):
<p>When they're done I might well write a blog post about how Lean does the question</p>

#### [ Patrick Massot (May 21 2018 at 11:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126864393):
<p>Do you know which ones are from Kenny and Chris or are there anonymous?</p>

#### [ Kevin Buzzard (May 21 2018 at 11:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126864395):
<p>yes and yes</p>

#### [ Patrick Massot (May 21 2018 at 11:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126864410):
<p>Do you mean two out of 100 gave answer in Lean written on paper, and you guessed?</p>

#### [ Kevin Buzzard (May 21 2018 at 11:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126864414):
<p>I recognise their handwriting and I know enough about where they were sitting in the room to be able to work it out</p>

#### [ Kevin Buzzard (May 21 2018 at 11:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126864474):
<p>In fact I missed Chris' script for Q1</p>

#### [ Kevin Buzzard (May 21 2018 at 11:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126864480):
<p>so I don't really know</p>

#### [ Kevin Buzzard (May 21 2018 at 11:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126864487):
<p>but I did notice Kenny's, a combination of the handwriting, the way he presented the arguments, and the fact that I did unfortunately know that his script would be "around this point in the pile"</p>

#### [ Kevin Buzzard (May 21 2018 at 11:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126864489):
<p>I could be wrong though</p>

#### [ Kevin Buzzard (May 21 2018 at 11:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126864497):
<p>I have no formal proof that it was Kenny's</p>

#### [ Kevin Buzzard (May 21 2018 at 11:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126864505):
<p>In fact it was the fact that I recognised Kenny's handwriting that I realised I must have missed Chris' script</p>

#### [ Kenny Lau (May 21 2018 at 11:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126864552):
<p>where did you get my handwriting sample from?</p>

#### [ Kevin Buzzard (May 21 2018 at 11:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126864557):
<p>You have sent me lots of handwriting in private zulip chats</p>

#### [ Kevin Buzzard (May 21 2018 at 11:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126864558):
<p>and I am sort of a bit weird about handwriting for some reason</p>

#### [ Kevin Buzzard (May 21 2018 at 11:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126864561):
<p>I am quite good at recognising it</p>

#### [ Kenny Lau (May 21 2018 at 11:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126864564):
<p>very interesting</p>

#### [ Kevin Buzzard (May 21 2018 at 11:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126864580):
<p>I guess I should be clear: I have no way of verifying that the script I strongly suspected was Kenny's, was Kenny's</p>

#### [ Kevin Buzzard (May 21 2018 at 11:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126864629):
<p>which of course is a good thing</p>

#### [ Kenny Lau (May 21 2018 at 11:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126864633):
<p>how many questions have you marked?</p>

#### [ Kevin Buzzard (May 21 2018 at 11:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126864634):
<p>1.3</p>

#### [ Kenny Lau (May 21 2018 at 11:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126864638):
<p>did you mark the sup(A+B)=sup(A)+sup(B)?</p>

#### [ Kevin Buzzard (May 21 2018 at 11:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126864644):
<p>doing that one today</p>

#### [ Kevin Buzzard (May 21 2018 at 11:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126864647):
<p>or more of it</p>

#### [ Kenny Lau (May 21 2018 at 11:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126864648):
<p>I see</p>

#### [ Kevin Buzzard (May 21 2018 at 11:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126864650):
<p>Hope to get another 0.3 of it done</p>

#### [ Kevin Buzzard (May 21 2018 at 11:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126864661):
<p>indeed I am just off now</p>

#### [ Mario Carneiro (May 21 2018 at 11:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126864704):
<p>Sometimes you get those <code>apply_instance</code> goals when you use <code>apply</code> with underscores, due to some strange elaboration order stuff. Essentially those goals are unknown at the time when instance resolution normally happens</p>

#### [ Mario Carneiro (May 21 2018 at 11:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126864707):
<p>using <code>refine</code> instead may help</p>

#### [ Patrick Massot (May 21 2018 at 12:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126865634):
<p>Do you get a student teacher collusion law suit if some other student realize Kenny answered "This function is continuous because it goes from R to R" as a signal to trigger special marking?</p>

#### [ Andrew Ashworth (May 21 2018 at 12:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126865906):
<p>I always appreciated automated marking, which you can do for programming assignments (and Lean, too!). Instant feedback if the grader is set up correctly, less need to attend office hours in order to discover that "one special trick professors want you to know about"</p>

#### [ Patrick Massot (May 21 2018 at 12:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126865914):
<p>What do you use for automated marking?</p>

#### [ Andrew Ashworth (May 21 2018 at 12:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126865978):
<p>Our CS department cobbled together a web server and a bunch of Python scripts</p>

#### [ Patrick Massot (May 21 2018 at 12:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126865979):
<p>Is there anything public?</p>

#### [ Andrew Ashworth (May 21 2018 at 12:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126866043):
<p>hmm, doubt it. shell scripts aren't the sort of thing that people would even think to release</p>

#### [ Andrew Ashworth (May 21 2018 at 12:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/126866277):
<p>they all tend to be custom solutions based on whatever your institution's favorite content management system is... for example, this one links with Canvas: <a href="https://github.com/arthuraa/sf-grader" target="_blank" title="https://github.com/arthuraa/sf-grader">https://github.com/arthuraa/sf-grader</a></p>

#### [ Kevin Buzzard (May 25 2018 at 19:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/127092646):
<blockquote>
<p>Do you know which ones are from Kenny and Chris or are there anonymous?</p>
</blockquote>
<p>OK so I asked some question about sups. I got about 80 correct solutions, of which 79 were a proof by contradiction, and one was constructive. And in Kenny's handwriting. And using the kind of pen he uses. But really -- it is anonymous!</p>

#### [ Andrew Ashworth (May 25 2018 at 19:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/127092713):
<p>You can tell the difference between pens? Does he have a fountain pen?</p>

#### [ Moses Schönfinkel (May 25 2018 at 19:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/heq%20question/near/127092857):
<p>Perhaps Kenny uses one of those rainbow pencils.</p>


{% endraw %}
