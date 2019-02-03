---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/77414wlogexample.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [wlog example](https://leanprover-community.github.io/archive/113488general/77414wlogexample.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Simon Hudon (Apr 02 2018 at 17:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/wlog%20example/near/124531148):
<p>What about: </p>
<div class="codehilite"><pre><span></span>Lean: 28f4143be31b7aa3c63a907be5443ca100025ef1
mathlib: d84af03bdb8ec4e02c96b6262e7b78c8f3de412b
</pre></div>

#### [ Patrick Massot (Apr 02 2018 at 17:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/wlog%20example/near/124531422):
<p>Thanks</p>

#### [ Patrick Massot (Apr 02 2018 at 17:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/wlog%20example/near/124531475):
<p>In the mean time I've found that March 27th nightly seems to allow compiling mathlib HEAD</p>

#### [ Patrick Massot (Apr 02 2018 at 17:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/wlog%20example/near/124531479):
<p>But now <code>rcases</code> doesn't work in my code</p>

#### [ Patrick Massot (Apr 02 2018 at 17:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/wlog%20example/near/124531492):
<p>I see <code>tactic.rcases_patt.has_reflect._rec_2: trying to evaluate sorry </code> each time I  use <code>rcases</code></p>

#### [ Patrick Massot (Apr 02 2018 at 17:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/wlog%20example/near/124531500):
<p>Sorry</p>

#### [ Patrick Massot (Apr 02 2018 at 17:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/wlog%20example/near/124531501):
<p>It's gone now</p>

#### [ Patrick Massot (Apr 02 2018 at 17:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/wlog%20example/near/124531502):
<p>I missed one server restart</p>

#### [ Simon Hudon (Apr 02 2018 at 17:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/wlog%20example/near/124531517):
<blockquote>
<p>Sorry</p>
</blockquote>
<p>I can't evaluate that</p>

#### [ Patrick Massot (Apr 02 2018 at 17:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/wlog%20example/near/124531558):
<p>Now I need to figure out how <code>wlog</code> is meant to be used</p>

#### [ Patrick Massot (Apr 02 2018 at 17:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/wlog%20example/near/124531583):
<p>My naive attempt leads to <code> failed to revert '_inst_3', it is a frozen local instance (possible solution: use tactic </code>tactic.unfreeze_local_instances<code> to reset the set of local instances) </code></p>

#### [ Patrick Massot (Apr 02 2018 at 17:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/wlog%20example/near/124531634):
<p>context is</p>
<div class="codehilite"><pre><span></span><span class="n">X</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">,</span>
<span class="bp">_</span><span class="n">inst_3</span> <span class="o">:</span> <span class="n">topological_space</span> <span class="n">X</span><span class="o">,</span>
<span class="n">f</span> <span class="n">g</span> <span class="o">:</span> <span class="n">homeo</span> <span class="n">X</span> <span class="n">X</span><span class="o">,</span>
<span class="n">H</span> <span class="o">:</span> <span class="n">supp</span> <span class="n">f</span> <span class="err">∩</span> <span class="n">supp</span> <span class="n">g</span> <span class="bp">=</span> <span class="err">∅</span><span class="o">,</span>
<span class="n">x</span> <span class="o">:</span> <span class="n">X</span><span class="o">,</span>
<span class="n">h</span> <span class="o">:</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">supp</span> <span class="n">f</span> <span class="err">∪</span> <span class="n">supp</span> <span class="n">g</span>
<span class="err">⊢</span> <span class="o">(</span><span class="n">f</span> <span class="err">∘</span> <span class="n">g</span><span class="o">)</span> <span class="n">x</span> <span class="bp">=</span> <span class="o">(</span><span class="n">g</span> <span class="err">∘</span> <span class="n">f</span><span class="o">)</span> <span class="n">x</span>
</pre></div>

#### [ Patrick Massot (Apr 02 2018 at 17:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/wlog%20example/near/124531657):
<p>I'm trying to use <code>wlog</code> (without knowing anything about it, only hoping from the name) to say it suffices to prove the statement when <code>x</code> is in the support of <code>f</code></p>

#### [ Simon Hudon (Apr 02 2018 at 17:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/wlog%20example/near/124531658):
<p>Is that instance used in your proof?</p>

#### [ Patrick Massot (Apr 02 2018 at 17:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/wlog%20example/near/124531664):
<p>What proof?</p>

#### [ Patrick Massot (Apr 02 2018 at 17:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/wlog%20example/near/124531666):
<p>I have no proof yet</p>

#### [ Patrick Massot (Apr 02 2018 at 17:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/wlog%20example/near/124531671):
<p>(actually I have one but without <code>wlog</code>)</p>

#### [ Simon Hudon (Apr 02 2018 at 17:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/wlog%20example/near/124531719):
<p>Right ... and does the part that <code>wlog</code> would replace make use of <code>_inst_3</code>?</p>

#### [ Patrick Massot (Apr 02 2018 at 17:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/wlog%20example/near/124531726):
<p>Of course</p>

#### [ Patrick Massot (Apr 02 2018 at 17:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/wlog%20example/near/124531728):
<p>everything makes use of that</p>

#### [ Patrick Massot (Apr 02 2018 at 17:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/wlog%20example/near/124531732):
<p>it's the topological space structure on X</p>

#### [ Patrick Massot (Apr 02 2018 at 17:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/wlog%20example/near/124531739):
<p><a href="https://github.com/PatrickMassot/lean-scratchpad/blob/master/src/support.lean#L133" target="_blank" title="https://github.com/PatrickMassot/lean-scratchpad/blob/master/src/support.lean#L133">https://github.com/PatrickMassot/lean-scratchpad/blob/master/src/support.lean#L133</a></p>

#### [ Simon Hudon (Apr 02 2018 at 17:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/wlog%20example/near/124531833):
<p>It's curious because <code>wlog</code> shouldn't need to revert anything but <code>f</code>, <code>g</code>, <code>H</code> and <code>h</code></p>

#### [ Simon Hudon (Apr 02 2018 at 17:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/wlog%20example/near/124531843):
<p>Can you show me the command that you're using?</p>

#### [ Patrick Massot (Apr 02 2018 at 17:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/wlog%20example/near/124531924):
<p>I'm trying to replace the proof with:</p>
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">fundamental&#39;</span> <span class="o">(</span><span class="n">f</span> <span class="n">g</span> <span class="o">:</span> <span class="n">homeo</span> <span class="n">X</span> <span class="n">X</span><span class="o">)</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="n">supp</span> <span class="n">f</span> <span class="err">∩</span> <span class="n">supp</span> <span class="n">g</span> <span class="bp">=</span> <span class="err">∅</span><span class="o">)</span> <span class="o">:</span> <span class="n">f</span> <span class="err">∘</span> <span class="n">g</span> <span class="bp">=</span> <span class="n">g</span> <span class="err">∘</span> <span class="n">f</span>  <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">funext</span><span class="o">,</span>
  <span class="n">by_cases</span> <span class="n">h</span> <span class="o">:</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">supp</span> <span class="n">f</span> <span class="err">∪</span> <span class="n">supp</span> <span class="n">g</span><span class="o">,</span>
  <span class="o">{</span> <span class="n">wlog</span>  <span class="n">h</span> <span class="o">:</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">supp</span> <span class="n">f</span> <span class="kn">using</span> <span class="n">x</span> <span class="n">y</span><span class="o">,</span>
    <span class="o">},</span>
  <span class="o">{</span> <span class="n">replace</span> <span class="n">h</span> <span class="o">:</span> <span class="n">x</span> <span class="err">∈</span> <span class="bp">-</span><span class="o">(</span><span class="n">supp</span> <span class="n">f</span> <span class="err">∪</span> <span class="n">supp</span> <span class="n">g</span><span class="o">)</span> <span class="o">:=</span> <span class="n">h</span><span class="o">,</span>
    <span class="n">rw</span> <span class="n">compl_union</span> <span class="o">(</span><span class="n">supp</span> <span class="n">f</span><span class="o">)</span> <span class="o">(</span><span class="n">supp</span> <span class="n">g</span><span class="o">)</span> <span class="n">at</span> <span class="n">h</span><span class="o">,</span>

    <span class="k">have</span> <span class="n">f_x</span> <span class="o">:</span> <span class="n">f</span> <span class="n">x</span> <span class="bp">=</span> <span class="n">x</span> <span class="o">:=</span> <span class="n">compl_supp_subset_fix</span> <span class="n">f</span> <span class="n">h</span><span class="bp">.</span><span class="mi">1</span><span class="o">,</span>
    <span class="k">have</span> <span class="n">g_x</span> <span class="o">:</span> <span class="n">g</span> <span class="n">x</span> <span class="bp">=</span> <span class="n">x</span> <span class="o">:=</span> <span class="n">compl_supp_subset_fix</span> <span class="n">g</span> <span class="n">h</span><span class="bp">.</span><span class="mi">2</span><span class="o">,</span>


    <span class="n">exact</span> <span class="k">calc</span> <span class="o">(</span><span class="n">f</span> <span class="err">∘</span> <span class="n">g</span><span class="o">)</span> <span class="n">x</span> <span class="bp">=</span> <span class="n">f</span> <span class="o">(</span><span class="n">g</span> <span class="n">x</span><span class="o">)</span> <span class="o">:</span> <span class="n">rfl</span>
        <span class="bp">...</span> <span class="bp">=</span> <span class="n">f</span> <span class="n">x</span> <span class="o">:</span> <span class="k">by</span> <span class="n">rw</span> <span class="n">g_x</span>
        <span class="bp">...</span> <span class="bp">=</span> <span class="n">x</span> <span class="o">:</span> <span class="k">by</span>  <span class="n">rw</span> <span class="n">f_x</span>
        <span class="bp">...</span> <span class="bp">=</span> <span class="n">g</span> <span class="n">x</span> <span class="o">:</span> <span class="k">by</span> <span class="n">rw</span> <span class="n">g_x</span>
        <span class="bp">...</span> <span class="bp">=</span> <span class="n">g</span> <span class="o">(</span><span class="n">f</span> <span class="n">x</span><span class="o">)</span> <span class="o">:</span> <span class="k">by</span> <span class="n">rw</span> <span class="n">f_x</span> <span class="o">}</span>
<span class="kn">end</span>
</pre></div>

#### [ Patrick Massot (Apr 02 2018 at 17:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/wlog%20example/near/124531932):
<p>I only remove everything inside the first branch of the <code>by_cases</code> and <code>wlog</code> there</p>

#### [ Patrick Massot (Apr 02 2018 at 17:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/wlog%20example/near/124531980):
<p>Maybe I completely misunderstood what <code>wlog</code> is meant to do</p>

#### [ Patrick Massot (Apr 02 2018 at 17:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/wlog%20example/near/124532067):
<p>I also don't manage to change the topic of messages that should be elsewhere</p>

#### [ Patrick Massot (Apr 02 2018 at 17:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/wlog%20example/near/124532099):
<p>How did you do that?</p>

#### [ Simon Hudon (Apr 02 2018 at 17:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/wlog%20example/near/124532157):
<p>I went to one of my messages preceding most of this conversation, I changed its topic and selected the option "change the topic of everything that came later"</p>

#### [ Simon Hudon (Apr 02 2018 at 17:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/wlog%20example/near/124532168):
<blockquote>
<p>Maybe I completely misunderstood what <code>wlog</code> is meant to do</p>
</blockquote>
<p>I think I misled you. Try <code>wlog h : x ∈ supp f using f g</code> instead.</p>

#### [ Patrick Massot (Apr 02 2018 at 17:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/wlog%20example/near/124532230):
<div class="codehilite"><pre><span></span><span class="n">intron</span> <span class="n">tactic</span> <span class="n">failed</span><span class="o">,</span> <span class="n">insufficient</span> <span class="n">binders</span>
<span class="n">state</span><span class="o">:</span>
<span class="n">X</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">,</span>
<span class="bp">_</span><span class="n">inst_3</span> <span class="o">:</span> <span class="n">topological_space</span> <span class="n">X</span><span class="o">,</span>
<span class="n">x</span> <span class="o">:</span> <span class="n">X</span><span class="o">,</span>
<span class="n">f</span> <span class="n">g</span> <span class="o">:</span> <span class="n">homeo</span> <span class="n">X</span> <span class="n">X</span><span class="o">,</span>
<span class="n">this</span> <span class="o">:</span>
  <span class="bp">∀</span> <span class="o">(</span><span class="n">f</span> <span class="n">g</span> <span class="o">:</span> <span class="n">homeo</span> <span class="n">X</span> <span class="n">X</span><span class="o">),</span>
    <span class="n">x</span> <span class="err">∈</span> <span class="n">supp</span> <span class="n">f</span> <span class="bp">→</span> <span class="n">supp</span> <span class="n">f</span> <span class="err">∩</span> <span class="n">supp</span> <span class="n">g</span> <span class="bp">=</span> <span class="err">∅</span> <span class="bp">→</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">supp</span> <span class="n">f</span> <span class="err">∪</span> <span class="n">supp</span> <span class="n">g</span> <span class="bp">→</span> <span class="o">(</span><span class="n">f</span> <span class="err">∘</span> <span class="n">g</span><span class="o">)</span> <span class="n">x</span> <span class="bp">=</span> <span class="o">(</span><span class="n">g</span> <span class="err">∘</span> <span class="n">f</span><span class="o">)</span> <span class="n">x</span><span class="o">,</span>
<span class="n">h</span> <span class="o">:</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">supp</span> <span class="n">f</span>
<span class="err">⊢</span> <span class="n">homeo</span> <span class="n">X</span> <span class="n">X</span>
</pre></div>

#### [ Simon Hudon (Apr 02 2018 at 17:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/wlog%20example/near/124532399):
<p>Is that the only goal being printed?</p>

#### [ Patrick Massot (Apr 02 2018 at 17:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/wlog%20example/near/124532471):
<p>yes</p>

#### [ Simon Hudon (Apr 02 2018 at 18:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/wlog%20example/near/124532600):
<p>Ok I'm going to clone your repo and see what I can do</p>

#### [ Patrick Massot (Apr 02 2018 at 18:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/wlog%20example/near/124532607):
<p>Thanks a lot!</p>

#### [ Simon Hudon (Apr 02 2018 at 18:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/wlog%20example/near/124534063):
<p>No worries! I found a serious bug in wlog. I'll let you know when I figured out a fix. In the mean time, I hope this is not stopping you</p>

#### [ Patrick Massot (Apr 02 2018 at 18:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/wlog%20example/near/124534127):
<p>No I'm not stopped, I have a working proof (with lot of duplication, hence I thought that would be a good opportunity to learn <code>wlog</code>)</p>

#### [ Kenny Lau (Apr 19 2018 at 06:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/wlog%20example/near/125287082):
<p>how is wlog now?</p>

#### [ Kenny Lau (Apr 19 2018 at 06:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/wlog%20example/near/125287125):
<p>I don't really think one can use wlog</p>

#### [ Kenny Lau (Apr 19 2018 at 06:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/wlog%20example/near/125287129):
<p>I mean, it passed those simple examples in the tests</p>

#### [ Simon Hudon (Apr 20 2018 at 00:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/wlog%20example/near/125330112):
<p>Can you show what you tried?</p>


{% endraw %}
