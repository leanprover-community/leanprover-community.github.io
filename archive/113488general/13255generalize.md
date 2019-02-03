---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/13255generalize.html
---

## Stream: [general](index.html)
### Topic: [generalize](13255generalize.html)

---


{% raw %}
#### [ Kenny Lau (Apr 19 2018 at 11:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize/near/125297691):
<p>Could someone build a tactic that allows us to generalize at hypotheses?</p>

#### [ Simon Hudon (Apr 20 2018 at 00:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize/near/125329985):
<p>Can you give an example?</p>

#### [ Kenny Lau (Apr 20 2018 at 07:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize/near/125342330):
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">(</span><span class="n">m</span> <span class="n">n</span> <span class="n">p</span> <span class="n">q</span> <span class="o">:</span> <span class="n">nat</span><span class="o">)</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="n">m</span> <span class="bp">+</span> <span class="n">n</span> <span class="bp">=</span> <span class="n">p</span><span class="o">)</span> <span class="o">:</span> <span class="n">m</span> <span class="bp">+</span> <span class="n">n</span> <span class="bp">=</span> <span class="n">q</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">generalize</span> <span class="n">h</span> <span class="o">:</span> <span class="n">m</span> <span class="bp">+</span> <span class="n">n</span> <span class="bp">=</span> <span class="n">x</span> <span class="n">at</span> <span class="n">h</span> <span class="err">⊢</span><span class="o">,</span>
  <span class="n">guard_hyp</span> <span class="n">h</span> <span class="o">:=</span> <span class="n">m</span> <span class="bp">+</span> <span class="n">n</span> <span class="bp">=</span> <span class="n">x</span><span class="o">,</span>
  <span class="n">guard_hyp</span> <span class="n">H</span> <span class="o">:=</span> <span class="n">x</span> <span class="bp">=</span> <span class="n">p</span><span class="o">,</span>
  <span class="n">guard_target</span> <span class="n">x</span> <span class="bp">=</span> <span class="n">q</span><span class="o">,</span>
  <span class="n">admit</span>
<span class="kn">end</span>
</pre></div>

#### [ Kenny Lau (Apr 20 2018 at 07:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize/near/125342331):
<p><span class="user-mention" data-user-id="110026">@Simon Hudon</span></p>

#### [ Simon Hudon (Apr 20 2018 at 13:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize/near/125445414):
<p>I see. So it reverts your hypotheses for you. That should be doable. I'll look into it. Any idea what it should be called?</p>

#### [ Kenny Lau (Apr 20 2018 at 13:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize/near/125445638):
<p>I think one can extend generalize?</p>

#### [ Kenny Lau (Apr 20 2018 at 13:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize/near/125445648):
<p>i.e. still call it generalize, since it builds upon the current generalize (so there won’t be beackwards compatibility problem)</p>

#### [ Simon Hudon (Apr 20 2018 at 13:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize/near/125445755):
<p><code>generalize</code> is defined in the core library and they usually don't take pull requests there. We may have to give it a different name and put it in <code>mathlib</code></p>

#### [ Kenny Lau (Apr 20 2018 at 14:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize/near/125447182):
<p>I’m not sure what I would call it. What do you think?</p>

#### [ Simon Hudon (Apr 20 2018 at 14:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize/near/125447233):
<p><code>generalized_generalize</code></p>

#### [ Johan Commelin (Apr 20 2018 at 14:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize/near/125447264):
<p>Can't you have tactic modifying tactics? Then you could just write <code>generalize simp</code> or <code>generalize wlog</code> and of course also <code>generalize generalize</code>.<br>
Life would be so much <code>simp</code>ler.</p>

#### [ Simon Hudon (Apr 20 2018 at 14:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize/near/125447272):
<p>Or <code>ageneralize</code>. <code>a</code> for assumption. We can also call it <code>generalizea</code> (not to be confused with the Canadian <code>generalize</code>, eh?)</p>

#### [ Simon Hudon (Apr 20 2018 at 14:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize/near/125447334):
<p>some tactics have <code>generalizing</code> clauses like <code>induction xs generalizing h</code></p>

#### [ Simon Hudon (Apr 20 2018 at 14:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize/near/125447851):
<p>(kudos for the hockey stick, <span class="user-mention" data-user-id="110045">@Sean Leather</span> <span class="emoji emoji-1f923" title="rolling on the floor laughing">:rolling_on_the_floor_laughing:</span> )</p>

#### [ Sean Leather (Apr 20 2018 at 14:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize/near/125447949):
<p>Bienvenue, eh!</p>

#### [ Kenny Lau (Apr 20 2018 at 16:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize/near/125450421):
<p>I have a truly marvelous idea</p>

#### [ Kenny Lau (Apr 20 2018 at 16:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize/near/125450422):
<p>I have a truly marvelous idea</p>

#### [ Kenny Lau (Apr 20 2018 at 16:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize/near/125450423):
<p>we can call it <code>generalise</code></p>

#### [ Simon Hudon (Apr 20 2018 at 16:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize/near/125450448):
<p>You are truly evil, <span class="user-mention" data-user-id="110064">@Kenny Lau</span></p>

#### [ Patrick Massot (Apr 20 2018 at 17:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize/near/125452634):
<blockquote>
<p>You are truly evil, <span class="user-mention" data-user-id="110064">@Kenny Lau</span></p>
</blockquote>
<p>Don't forget we learned this morning that Kenny is nothing but Kevin's evil part.</p>

#### [ Simon Hudon (Apr 20 2018 at 17:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize/near/125452831):
<p>I wasn't there for that. It all adds up ... his constructivism should really have been a dead give away</p>

#### [ Simon Hudon (Apr 20 2018 at 17:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize/near/125452840):
<p>Btw <span class="user-mention" data-user-id="110064">@Kenny Lau</span> I just made a pull request with your requested feature:</p>
<p><a href="https://github.com/leanprover/mathlib/pull/110" target="_blank" title="https://github.com/leanprover/mathlib/pull/110">https://github.com/leanprover/mathlib/pull/110</a></p>
<p>Let me know if you like it!</p>

#### [ Kenny Lau (Apr 20 2018 at 17:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize/near/125453447):
<p><span class="user-mention" data-user-id="110026">@Simon Hudon</span> does it work with more than one local hypothesis?</p>

#### [ Simon Hudon (Apr 20 2018 at 17:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize/near/125453452):
<p>Yes it does</p>

#### [ Kenny Lau (Apr 20 2018 at 17:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize/near/125453456):
<p>I like it, thanks</p>

#### [ Kenny Lau (Apr 20 2018 at 17:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize/near/125453463):
<p>let's test if it works with induction</p>

#### [ Kenny Lau (Apr 20 2018 at 17:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize/near/125453469):
<p>could you test if you can generalize a list and then do induction?</p>

#### [ Simon Hudon (Apr 20 2018 at 17:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize/near/125453519):
<p>Can you show me what you have in mind?</p>

#### [ Kenny Lau (Apr 20 2018 at 17:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize/near/125453523):
<p>yes, wait a minute</p>

#### [ Kenny Lau (Apr 20 2018 at 17:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize/near/125453683):
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="n">Sort</span><span class="bp">*</span><span class="o">)</span> <span class="o">(</span><span class="n">L₁</span> <span class="n">L₂</span> <span class="n">L₃</span> <span class="o">:</span> <span class="n">list</span> <span class="n">α</span><span class="o">)</span>
  <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="n">L₁</span> <span class="bp">++</span> <span class="n">L₂</span> <span class="bp">=</span> <span class="n">L₃</span><span class="o">)</span> <span class="o">:</span> <span class="n">L₁</span> <span class="bp">++</span> <span class="n">L₂</span> <span class="bp">=</span> <span class="n">L₂</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">generalize_a</span> <span class="n">h</span> <span class="o">:</span> <span class="n">L₁</span> <span class="bp">++</span> <span class="n">L₂</span> <span class="bp">=</span> <span class="n">L</span> <span class="n">at</span> <span class="n">H</span><span class="o">,</span>
  <span class="n">induction</span> <span class="n">L</span> <span class="k">with</span> <span class="n">hd</span> <span class="n">tl</span> <span class="n">ih</span><span class="o">,</span>
  <span class="n">case</span> <span class="n">list</span><span class="bp">.</span><span class="n">nil</span>
  <span class="o">{</span> <span class="n">guard_hyp</span> <span class="n">H</span> <span class="o">:=</span> <span class="n">list</span><span class="bp">.</span><span class="n">nil</span> <span class="bp">=</span> <span class="n">L₃</span> <span class="o">},</span>
  <span class="n">case</span> <span class="n">list</span><span class="bp">.</span><span class="n">cons</span>
  <span class="o">{</span> <span class="n">guard_hyp</span> <span class="n">H</span> <span class="o">:=</span> <span class="n">hd</span> <span class="bp">::</span> <span class="n">tl</span> <span class="bp">=</span> <span class="n">L₃</span> <span class="o">},</span>
  <span class="n">admit</span>
<span class="kn">end</span>
</pre></div>

#### [ Kenny Lau (Apr 20 2018 at 17:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize/near/125453686):
<p><span class="user-mention" data-user-id="110026">@Simon Hudon</span> there you go</p>

#### [ Simon Hudon (Apr 20 2018 at 17:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize/near/125453952):
<p>I had to change it to: </p>
<div class="codehilite"><pre><span></span>example (α : Sort*) (L₁ L₂ L₃ : list α)
  (H : L₁ ++ L₂ = L₃) : L₁ ++ L₂ = L₂ :=
begin
  generalize_a h : L₁ ++ L₂ = L at H,
  induction L with hd tl ih,
  case list.nil
  { tactic.cleanup,
    change list.nil = L₃ at H,
    admit },
  case list.cons
  { change hd :: tl = L₃ at H,
    admit },
end
</pre></div>


<p>but it worked</p>

#### [ Kenny Lau (Apr 20 2018 at 17:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize/near/125453958):
<p>why?</p>

#### [ Kenny Lau (Apr 20 2018 at 17:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize/near/125453963):
<p>but thanks</p>

#### [ Simon Hudon (Apr 20 2018 at 17:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize/near/125454026):
<p><code>guard_hyp</code> and <code>guard_target</code> are fairly intolerant. If your expressions contain meta variables and that they don't match, it will fail. At least, I believe that's the reason</p>

#### [ Kenny Lau (Apr 20 2018 at 17:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize/near/125454027):
<p>I see</p>

#### [ Simon Hudon (Apr 20 2018 at 17:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/generalize/near/125454034):
<p>And you're welcome :)</p>


{% endraw %}
