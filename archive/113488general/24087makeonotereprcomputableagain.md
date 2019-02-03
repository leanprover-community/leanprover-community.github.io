---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/24087makeonotereprcomputableagain.html
---

## Stream: [general](index.html)
### Topic: [make onote.repr computable again](24087makeonotereprcomputableagain.html)

---


{% raw %}
#### [ Kenny Lau (Apr 20 2018 at 11:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/make%20onote.repr%20computable%20again/near/125412217):
<div class="codehilite"><pre><span></span><span class="c">/-</span><span class="cm">- The ordinal denoted by a notation -/</span>
<span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="n">noncomputable</span> <span class="n">def</span> <span class="n">repr</span> <span class="o">:</span> <span class="n">onote</span> <span class="bp">→</span> <span class="n">ordinal</span><span class="bp">.</span><span class="o">{</span><span class="mi">0</span><span class="o">}</span>
<span class="bp">|</span> <span class="mi">0</span> <span class="o">:=</span> <span class="mi">0</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">oadd</span> <span class="n">e</span> <span class="n">n</span> <span class="n">a</span><span class="o">)</span> <span class="o">:=</span> <span class="n">ω</span> <span class="err">^</span> <span class="n">repr</span> <span class="n">e</span> <span class="bp">*</span> <span class="n">n</span> <span class="bp">+</span> <span class="n">repr</span> <span class="n">a</span>
</pre></div>


<p>This is in <code>set_theory/ordinal_notation.lean</code>. This definition is currently noncomputable. Should I start working on it to make it computable? (I believe I know how to make it computable, my only worry is that my PR will be rejected)</p>

#### [ Kenny Lau (Apr 20 2018 at 11:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/make%20onote.repr%20computable%20again/near/125412264):
<p>(cc <span class="user-mention" data-user-id="110049">@Mario Carneiro</span>)</p>

#### [ Kenny Lau (Apr 20 2018 at 11:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/make%20onote.repr%20computable%20again/near/125413219):
<p>(cc <span class="user-mention" data-user-id="110294">@Johannes Hölzl</span> )</p>

#### [ Kenny Lau (Apr 20 2018 at 11:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/make%20onote.repr%20computable%20again/near/125419192):
<p>maybe I'll do some analysis to show that I know how to make it computable</p>

#### [ Kenny Lau (Apr 20 2018 at 11:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/make%20onote.repr%20computable%20again/near/125419783):
<p><code>ω</code> depends on <code>nat.lt.is_well_order</code>, which depends on <code>has_lt.lt.is_strict_total_order'</code>, which depends on <code>lt_trichotomy</code>, which depends on <code>lt_or_eq_of_le</code>, which uses <code>classical.by_cases</code>, so we only need to change one of them</p>

#### [ Gabriel Ebner (Apr 20 2018 at 11:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/make%20onote.repr%20computable%20again/near/125420264):
<p><code>classical.by_cases</code> is in <code>Prop</code>, so it has zero effect on noncomputability.</p>

#### [ Kenny Lau (Apr 20 2018 at 12:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/make%20onote.repr%20computable%20again/near/125421754):
<p>you're right. I need to redo my analysis.</p>

#### [ Kenny Lau (Apr 20 2018 at 12:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/make%20onote.repr%20computable%20again/near/125422169):
<p><span class="user-mention" data-user-id="110043">@Gabriel Ebner</span> do you have any idea which part is noncomputable?</p>

#### [ Gabriel Ebner (Apr 20 2018 at 12:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/make%20onote.repr%20computable%20again/near/125424751):
<p><code>ord.has_pow</code> is noncomputable because it 1) has an if-then-else on <code>a=0</code>, and 2) uses <code>limit_rec_on</code></p>

#### [ Gabriel Ebner (Apr 20 2018 at 12:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/make%20onote.repr%20computable%20again/near/125425296):
<p>I wonder if there is a cheap trick where you "eta-expand" an arbitrary ordinal to make it computable.  All components of ordinals are props or types after all.</p>

#### [ Mario Carneiro (Apr 21 2018 at 00:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/make%20onote.repr%20computable%20again/near/125471318):
<p>Ordinals are a noncomputable theory, so there isn't much point. Furthermore, as Gabriel observes, ordinals are "cheaply noncomputable" since they contain only erasable data, so the VM never computes with them anyway. I think a future version of lean may mark this function computable simply because it doesn't compute anything.</p>

#### [ Mario Carneiro (Apr 21 2018 at 00:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/make%20onote.repr%20computable%20again/near/125471438):
<p>You may wonder why so many things are noncomputable, when the choice usage is only in things like <code>ord</code>; the reason is because there is a lot of use of "unique choice", which is okay in ZF but not in lean. For example, can you even decide <code>a = 0</code>? This is easy in ZF, where everything is decidable by unique choice, but to do in lean you would have to decide if an arbitrary type is empty, for example <code>plift p</code> where <code>p</code> is a nondecidable proposition.</p>

#### [ Mario Carneiro (Apr 21 2018 at 00:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/make%20onote.repr%20computable%20again/near/125471516):
<p>My question to you: why do you care that <code>repr</code> is noncomputable? If the goal is to compute with ordinals, that's the whole reason I wrote the <code>ordinal_notation</code> file - it gives computational analogues of the ordinal functions. You will note that <code>onote.add</code> and such are all computable. <code>repr</code> is only there to make it possible to state correctness results, assuming full choice.</p>


{% endraw %}
