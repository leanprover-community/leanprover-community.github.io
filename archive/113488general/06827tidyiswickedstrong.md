---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/06827tidyiswickedstrong.html
---

## Stream: [general](index.html)
### Topic: [tidy is wicked strong](06827tidyiswickedstrong.html)

---


{% raw %}
#### [ Johan Commelin (Aug 03 2018 at 09:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20is%20wicked%20strong/near/130822631):
<p>Kudos to Scott!</p>
<div class="codehilite"><pre><span></span><span class="kn">instance</span> <span class="n">LeftMod__has_ZeroObject</span> <span class="o">:</span> <span class="bp">@</span><span class="n">universal</span><span class="bp">.</span><span class="n">has_ZeroObject</span> <span class="o">(</span><span class="n">R</span><span class="bp">-</span><span class="n">Mod</span><span class="o">)</span> <span class="n">LeftMod_</span><span class="bp">.</span><span class="n">foo</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">zero_object</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">zero_object</span> <span class="o">:=</span> <span class="n">zero_module</span> <span class="n">R</span><span class="o">,</span>
  <span class="n">is_initial</span>  <span class="o">:=</span> <span class="bp">⟨λ</span> <span class="n">M</span> <span class="o">:</span> <span class="n">R</span><span class="bp">-</span><span class="n">Mod</span><span class="o">,</span> <span class="bp">⟨λ</span> <span class="bp">_</span><span class="o">,</span> <span class="mi">0</span><span class="o">,</span> <span class="n">is_linear_map</span><span class="bp">.</span><span class="n">map_zero</span><span class="bp">⟩</span><span class="o">,</span>
  <span class="k">begin</span>
    <span class="n">intros</span> <span class="n">M</span> <span class="n">f</span> <span class="n">g</span><span class="o">,</span>
    <span class="n">tidy</span><span class="o">,</span>
    <span class="n">rw</span> <span class="o">[</span><span class="err">←</span> <span class="n">zero_is_star</span><span class="o">,</span> <span class="n">is_linear_map</span><span class="bp">.</span><span class="n">zero</span> <span class="n">f_property</span><span class="o">,</span> <span class="n">is_linear_map</span><span class="bp">.</span><span class="n">zero</span> <span class="n">g_property</span><span class="o">]</span>
  <span class="kn">end</span> <span class="bp">⟩</span><span class="o">,</span>
  <span class="n">is_terminal</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">tidy</span>
<span class="o">}</span> <span class="o">}</span>
</pre></div>

#### [ Johan Commelin (Aug 03 2018 at 09:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20is%20wicked%20strong/near/130822638):
<p>I just told Lean the definition of the zero-module. And it figured out on its own that it is the terminal object in the category of left modules!<br>
Mind you: I wrote only 1 <code>rfl</code>-lemma to help it:</p>
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">zero_is_star</span> <span class="o">:</span> <span class="o">(</span><span class="mi">0</span> <span class="o">:</span> <span class="o">(</span><span class="n">zero_module</span> <span class="n">R</span><span class="o">))</span> <span class="bp">=</span> <span class="n">star</span> <span class="o">:=</span> <span class="n">rfl</span>
</pre></div>

#### [ Johan Commelin (Aug 03 2018 at 09:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20is%20wicked%20strong/near/130822683):
<p>It needs a bit of hand-holding for the initial object, but I guess this is only because <code>is_linear_map</code> is not a class.</p>

#### [ Johan Commelin (Aug 03 2018 at 09:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20is%20wicked%20strong/near/130822696):
<p>Long live <span class="user-mention" data-user-id="110087">@Scott Morrison</span>! Blacksmith of hammer tactics!</p>

#### [ Johan Commelin (Aug 03 2018 at 09:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20is%20wicked%20strong/near/130824101):
<p>Ooh, and <code>obviously</code> also does the job.</p>

#### [ Kevin Buzzard (Aug 03 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20is%20wicked%20strong/near/130824817):
<p>It's slowly dawning on me that my initial impression ("<code>tidy</code> is something Scott wrote to help with his category theory stuff, and it does category theory stuff") is completely wrong, and that <code>tidy</code> and <code>obviously</code> are really all-purpose tools which will help us all. But they are not even part of a PR, right? Is there some kind of plan to get them PR'ed somehow, and what are the obstructions to getting them into mathlib?</p>

#### [ Scott Morrison (Aug 03 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20is%20wicked%20strong/near/130824972):
<p>Hi Kevin, <code>tidy</code> doesn't do all that much, but I agree it's helpful. Really we need to carefully read &lt;<a href="https://arxiv.org/abs/1309.4501" target="_blank" title="https://arxiv.org/abs/1309.4501">https://arxiv.org/abs/1309.4501</a>&gt; and translate it all into Lean, and then we'll really have the start of a hammer that mathematicians appreciate.</p>

#### [ Scott Morrison (Aug 03 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20is%20wicked%20strong/near/130825014):
<p><code>tidy</code> is relatively easy to PR to mathlib, and hopefully I will have time soon to start doing this</p>

#### [ Scott Morrison (Aug 03 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20is%20wicked%20strong/near/130825017):
<p>many of the gross aspects of it have become cleaner in the last month</p>

#### [ Scott Morrison (Aug 03 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20is%20wicked%20strong/near/130825043):
<p><code>obviously</code> is just <code>tidy</code> equipped with an extra tactic, called <code>rewrite_search</code>, which uses edit-distance based heuristics to search for chains of rewrites to prove equational results.</p>

#### [ Scott Morrison (Aug 03 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20is%20wicked%20strong/near/130825061):
<p>it is harder to PR, both because the implementation is really awful, and a student is actively working on cleverer (i.e. using machine learning in the heuristics) versions, so it's a moving target</p>

#### [ Scott Morrison (Aug 03 2018 at 10:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20is%20wicked%20strong/near/130825112):
<p>(actually, secretly I'm hoping that he will rewrite <code>rewrite_search</code> from scratch for me, when he realises how awful it is)</p>

#### [ Minchao Wu (Aug 03 2018 at 10:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20is%20wicked%20strong/near/130825305):
<p><span class="user-mention" data-user-id="110087">@Scott Morrison</span>  who is the student? I'm also interested in applying machine learning to heuristics</p>

#### [ Kenny Lau (Aug 03 2018 at 10:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20is%20wicked%20strong/near/130825314):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> did one of your students mention machine learning?</p>

#### [ Johan Commelin (Aug 03 2018 at 10:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20is%20wicked%20strong/near/130825391):
<p>It seems that Mohan Ganesalingam completely left the field.</p>

#### [ Scott Morrison (Aug 03 2018 at 10:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20is%20wicked%20strong/near/130825447):
<p><span class="user-mention" data-user-id="110187">@Minchao Wu</span> , it's Keeley Hoek, who is sometimes around here. (Also, as we're all in the same building, we should really meet up --- my apologies that I screwed up our last attempt to do so.)</p>

#### [ Scott Morrison (Aug 03 2018 at 10:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20is%20wicked%20strong/near/130825465):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span>, have you ever read that Ganesalingam-Gowers paper? If not, you really should. :-)</p>

#### [ Minchao Wu (Aug 03 2018 at 10:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20is%20wicked%20strong/near/130825523):
<p>No worries :) Is the student also from the math department?</p>

#### [ Johan Commelin (Aug 03 2018 at 10:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20is%20wicked%20strong/near/130825616):
<p>It's really a pity that the "future work" never materialised. I think Gowers also changed subject...</p>

#### [ Scott Morrison (Aug 03 2018 at 10:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20is%20wicked%20strong/near/130825624):
<p>Well... Gowers was only ever a visitor... :-)</p>

#### [ Minchao Wu (Aug 03 2018 at 10:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20is%20wicked%20strong/near/130825634):
<p>If he's coming next week we can just schedule a group meeting maybe</p>

#### [ Scott Morrison (Aug 03 2018 at 10:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20is%20wicked%20strong/near/130825682):
<p>It is such a pity that they did their work in their own private interactive theorem prover, so it's not usable by the rest of us.</p>

#### [ Scott Morrison (Aug 03 2018 at 10:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20is%20wicked%20strong/near/130825683):
<p>(Typical mathematicians! :-)</p>

#### [ Rob Lewis (Aug 03 2018 at 13:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20is%20wicked%20strong/near/130832892):
<p><span class="user-mention" data-user-id="110087">@Scott Morrison</span> Are you/your student familiar with the work on TacticToe? <a href="http://cl-informatik.uibk.ac.at/users/cek/docs/17/tgckju-lpar17.pdf" target="_blank" title="http://cl-informatik.uibk.ac.at/users/cek/docs/17/tgckju-lpar17.pdf">http://cl-informatik.uibk.ac.at/users/cek/docs/17/tgckju-lpar17.pdf</a> They've been relatively successful with ML-guided tactic proofs in HOL4. One of the more impressive results at AITP this year, in my opinion.</p>

#### [ Scott Morrison (Aug 03 2018 at 13:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20is%20wicked%20strong/near/130832996):
<p>Thanks <span class="user-mention" data-user-id="110596">@Rob Lewis</span> for the reference. This is very different than what we're trying.</p>


{% endraw %}
