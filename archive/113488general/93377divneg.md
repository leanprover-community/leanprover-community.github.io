---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/93377divneg.html
---

## Stream: [general](index.html)
### Topic: ["div_neg"](93377divneg.html)

---


{% raw %}
#### [ Kenny Lau (Sep 25 2018 at 20:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134617532):
<p>algebra/field.lean L95:</p>
<div class="codehilite"><pre><span></span>lemma div_neg (a : α) (hb : b ≠ 0) : a / -b = -(a / b) :=
by rw [← division_ring.neg_div_neg_eq _ (neg_ne_zero.2 hb), neg_neg, neg_div]
</pre></div>

#### [ Kenny Lau (Sep 25 2018 at 20:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134617540):
<p>but <code>div_neg_eq_neg_div</code> is the exact same</p>

#### [ Kevin Buzzard (Sep 26 2018 at 09:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134652104):
<p>it's not the same, it's over twice as hard to type</p>

#### [ Sean Leather (Sep 26 2018 at 09:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134652157):
<p>Especially if you're using a <a href="#narrow/stream/113488-general/subject/caching.20proofs/near/134214831" title="#narrow/stream/113488-general/subject/caching.20proofs/near/134214831">typewriter</a>. <span class="emoji emoji-1f5a8" title="printer">:printer:</span></p>

#### [ Mario Carneiro (Sep 26 2018 at 09:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134652158):
<p>I imagine I was annoyed with the lean core name and duplicated it with a new name</p>

#### [ Kenny Lau (Sep 26 2018 at 09:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134652162):
<p>then why don't you prove it just using that?</p>

#### [ Mario Carneiro (Sep 26 2018 at 09:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134652165):
<p>probably the proof is shorter too?</p>

#### [ Kenny Lau (Sep 26 2018 at 09:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134652234):
<p>I think you're misunderstanding me. See <a href="https://github.com/leanprover-community/mathlib/commit/6b2ee1dd45fedc0d04a4c9df76b3d0ce1ec084ed#diff-6bbbc7fb99ee6d3f77c06e4b7ad403a1L97" target="_blank" title="https://github.com/leanprover-community/mathlib/commit/6b2ee1dd45fedc0d04a4c9df76b3d0ce1ec084ed#diff-6bbbc7fb99ee6d3f77c06e4b7ad403a1L97">this edit of mine</a>.</p>

#### [ Mario Carneiro (Sep 26 2018 at 09:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134652262):
<p>No, I know exactly what you mean. I am saying the proof is shorter than the original proof</p>

#### [ Mario Carneiro (Sep 26 2018 at 09:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134652353):
<p>you've also revealed to me that your compile times change is doing more than just improving compile times :}</p>

#### [ Kenny Lau (Sep 26 2018 at 09:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134652412):
<p>that's not true. my term mode proof is faster than <code>rw</code></p>

#### [ Mario Carneiro (Sep 26 2018 at 09:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134652426):
<p>the point is not to be significantly refactoring the proofs while you do it though</p>

#### [ Kenny Lau (Sep 26 2018 at 09:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134652431):
<p>but that would reduce the time by like at least 90%</p>

#### [ Mario Carneiro (Sep 26 2018 at 09:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134652435):
<p>because that brings in more controversial aspects of the work</p>

#### [ Kenny Lau (Sep 26 2018 at 09:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134652439):
<p>I don't see why proofs are relevant</p>

#### [ Mario Carneiro (Sep 26 2018 at 09:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134652447):
<p>you aren't making it easy for me to merge this PR</p>

#### [ Kenny Lau (Sep 26 2018 at 09:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134652449):
<p>also don't you like shorter proofs?</p>

#### [ Mario Carneiro (Sep 26 2018 at 09:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134652517):
<p>yes, that's why I want the original proof there</p>

#### [ Kenny Lau (Sep 26 2018 at 09:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134652528):
<p>because the original proof <code>by rw [← division_ring.neg_div_neg_eq _ (neg_ne_zero.2 hb), neg_neg, neg_div]</code> is longer and slower?</p>

#### [ Mario Carneiro (Sep 26 2018 at 09:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134652530):
<p>I expect that the core theorem will disappear shortly, and I don't want to forget that it's already been minimized</p>

#### [ Mario Carneiro (Sep 26 2018 at 09:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134652591):
<p>Don't sweat the small stuff. I'm hoping that your work is focusing on the actual worst offenders</p>

#### [ Mario Carneiro (Sep 26 2018 at 09:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134652604):
<p>Did you test your proofs for actual time saved?</p>

#### [ Kenny Lau (Sep 26 2018 at 09:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134652606):
<p>of course</p>

#### [ Mario Carneiro (Sep 26 2018 at 09:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134652621):
<p>what method are you using?</p>

#### [ Kenny Lau (Sep 26 2018 at 09:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134652623):
<p><code>set_option profiler true</code></p>

#### [ Mario Carneiro (Sep 26 2018 at 09:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134652671):
<p>You should focus on proofs that take &gt;1s to compile</p>

#### [ Kenny Lau (Sep 26 2018 at 09:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134652679):
<p>every <code>simp</code> proof takes &gt;1s to compile</p>

#### [ Mario Carneiro (Sep 26 2018 at 09:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134652720):
<p>this is not my experience</p>

#### [ Kevin Buzzard (Sep 26 2018 at 09:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134652779):
<p>Maybe Kenny has a slower machine, which I guess in this context is in some weird sense quite helpful</p>

#### [ Kevin Buzzard (Sep 26 2018 at 09:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134652792):
<p>I remember Kenny complaining that some proof took 7 seconds to compile, and I tried it on my 1 year old laptop and it took 3 seconds</p>

#### [ Kenny Lau (Sep 26 2018 at 09:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134652810):
<p><a href="/user_uploads/3121/OtOLeoaVolATyey-qF9KFNpx/2018-09-26-5.png" target="_blank" title="2018-09-26-5.png">2018-09-26-5.png</a></p>
<div class="message_inline_image"><a href="/user_uploads/3121/OtOLeoaVolATyey-qF9KFNpx/2018-09-26-5.png" target="_blank" title="2018-09-26-5.png"><img src="/user_uploads/3121/OtOLeoaVolATyey-qF9KFNpx/2018-09-26-5.png"></a></div>

#### [ Kevin Buzzard (Sep 26 2018 at 09:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134652815):
<p>Kenny -- Mario is right. Attack the stuff which takes &gt; 1 second for you. Don't worry about div_neg being 0.04 or 0.03</p>

#### [ Kevin Buzzard (Sep 26 2018 at 09:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134652876):
<p>Your screenshot is eye-opening by the way</p>

#### [ Mario Carneiro (Sep 26 2018 at 09:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134652908):
<p>it's also not good news at all</p>

#### [ Mario Carneiro (Sep 26 2018 at 09:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134652913):
<p>we may need to rewrite simp</p>

#### [ Kenny Lau (Sep 26 2018 at 09:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134652921):
<p>so do I have the green light?</p>

#### [ Mario Carneiro (Sep 26 2018 at 09:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134652999):
<p>I am still a bit uncomfortable about this, like we should retain the original proofs</p>

#### [ Mario Carneiro (Sep 26 2018 at 09:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134653015):
<p>this is of course the same story as with <code>tidy</code></p>

#### [ Kenny Lau (Sep 26 2018 at 09:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134653018):
<blockquote>
<p>I expect that the core theorem will disappear shortly, and I don't want to forget that it's already been minimized</p>
</blockquote>
<p>are you referring to Lean 4?</p>

#### [ Mario Carneiro (Sep 26 2018 at 09:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134653024):
<p>yes, basically</p>

#### [ Kenny Lau (Sep 26 2018 at 09:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134653030):
<p>but you can't copy the files to Lean 4 anyway</p>

#### [ Kenny Lau (Sep 26 2018 at 09:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134653035):
<p>why bother that this particular proof can't be copied to Lean 4</p>

#### [ Mario Carneiro (Sep 26 2018 at 09:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134653047):
<p>kenny, focus</p>

#### [ Kenny Lau (Sep 26 2018 at 09:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134653097):
<p>ok ok</p>

#### [ Mario Carneiro (Sep 26 2018 at 09:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134653107):
<p>suffice it to say that you have the green light to do changes expressly for the purpose of improving compile times by e.g. replacing <code>simp</code> with <code>simp only</code> or <code>rw</code></p>

#### [ Mario Carneiro (Sep 26 2018 at 09:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134653111):
<p>If you want to do something else, put it in a different PR</p>

#### [ Kevin Buzzard (Sep 26 2018 at 09:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134653113):
<p>If you want to do two different things Kenny then you could do them in two different branches</p>

#### [ Kenny Lau (Sep 26 2018 at 09:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134653114):
<p>ok</p>

#### [ Kenny Lau (Sep 26 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134653168):
<p>so I don't have the green light to change:</p>
<div class="codehilite"><pre><span></span><span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="kn">lemma</span> <span class="n">coe_singleton</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="err">↑</span><span class="o">(</span><span class="n">ι</span> <span class="n">a</span><span class="o">)</span> <span class="bp">=</span> <span class="o">({</span><span class="n">a</span><span class="o">}</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">simp</span> <span class="o">[</span><span class="n">set</span><span class="bp">.</span><span class="n">ext_iff</span><span class="o">]</span>
</pre></div>


<p>to:</p>
<div class="codehilite"><pre><span></span><span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="kn">lemma</span> <span class="n">coe_singleton</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="err">↑</span><span class="o">(</span><span class="n">ι</span> <span class="n">a</span><span class="o">)</span> <span class="bp">=</span> <span class="o">({</span><span class="n">a</span><span class="o">}</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">)</span> <span class="o">:=</span>
<span class="n">rfl</span>
</pre></div>


<p>?</p>

#### [ Kenny Lau (Sep 26 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134653179):
<p>just to confirm</p>

#### [ Mario Carneiro (Sep 26 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134653180):
<p>I would accept that if it's actually much faster</p>

#### [ Kenny Lau (Sep 26 2018 at 09:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134653190):
<p>of course it's much faster</p>

#### [ Mario Carneiro (Sep 26 2018 at 09:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134653193):
<p><code>refl</code> is also among the things you can replace <code>simp</code> with</p>

#### [ Mario Carneiro (Sep 26 2018 at 09:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134653195):
<p>definitional unfolding is not always fast</p>

#### [ Mario Carneiro (Sep 26 2018 at 09:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134653199):
<p>hint: <code>10 + 10 = 20 := rfl</code></p>

#### [ Kenny Lau (Sep 26 2018 at 09:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134653202):
<p>alright</p>

#### [ Kenny Lau (Sep 26 2018 at 09:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134653257):
<p><a href="/user_uploads/3121/12xknWSPMLmfvRnGOp0UDVj4/2018-09-26-6.png" target="_blank" title="2018-09-26-6.png">2018-09-26-6.png</a></p>
<div class="message_inline_image"><a href="/user_uploads/3121/12xknWSPMLmfvRnGOp0UDVj4/2018-09-26-6.png" target="_blank" title="2018-09-26-6.png"><img src="/user_uploads/3121/12xknWSPMLmfvRnGOp0UDVj4/2018-09-26-6.png"></a></div>

#### [ Mario Carneiro (Sep 26 2018 at 09:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134653280):
<p>I would still prefer <code>simp</code> over <code>simp only</code> if it is not a significant improvement</p>

#### [ Kenny Lau (Sep 26 2018 at 09:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134653292):
<p>is 3 orders of magnitude significant enough?</p>

#### [ Scott Morrison (Sep 26 2018 at 09:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134653294):
<p>I wonder if it is worth writing a hole command for generating <code>simp only</code> tactics.</p>

#### [ Mario Carneiro (Sep 26 2018 at 09:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134653298):
<p>like if you can't improve by more than .1s then leave it</p>

#### [ Mario Carneiro (Sep 26 2018 at 09:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134653303):
<p>a hole command sounds like a great idea</p>

#### [ Kenny Lau (Sep 26 2018 at 09:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134653304):
<p>maybe you missed the unit</p>

#### [ Mario Carneiro (Sep 26 2018 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134653356):
<p>no, I saw, that's a phenomenal improvement and I don't doubt that you will find many such things</p>

#### [ Scott Morrison (Sep 26 2018 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134653378):
<p>or even just a wrapper for simp, that calls <code>simp</code>, looks at the result, and works out automatically a <code>simp only</code> command that will work, and outputs that as a trace message.</p>

#### [ Kenny Lau (Sep 26 2018 at 09:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134653386):
<blockquote>
<p>or even just a wrapper for simp, that calls <code>simp</code>, looks at the result, and works out automatically a <code>simp only</code> command that will work, and outputs that as a trace message.</p>
</blockquote>
<p>that's exaclty what's in my mind</p>

#### [ Scott Morrison (Sep 26 2018 at 09:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134653392):
<p>... and this all emphasises how much we need multiple levels of caching.</p>

#### [ Kenny Lau (Sep 26 2018 at 09:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134653410):
<p>I think caching is a bad idea</p>

#### [ Mario Carneiro (Sep 26 2018 at 09:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134653420):
<p>I think caching of the sort scott is talking about is a very good idea</p>

#### [ Kenny Lau (Sep 26 2018 at 09:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134653438):
<p>in terms of the trust of the correctness</p>

#### [ Mario Carneiro (Sep 26 2018 at 10:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134653484):
<p>?</p>

#### [ Mario Carneiro (Sep 26 2018 at 10:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134653503):
<p>a proof is a proof</p>

#### [ Kenny Lau (Sep 26 2018 at 10:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134653515):
<p>never mind</p>

#### [ Kenny Lau (Sep 26 2018 at 10:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134653525):
<p>also what Scott said is what I'm doing manually</p>

#### [ Kenny Lau (Sep 26 2018 at 10:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134653537):
<p>look at the output for <code>trace.simplify.rewrite</code> and write a correspondingly <code>simp only</code> or <code>rw</code></p>

#### [ Kenny Lau (Sep 26 2018 at 10:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134653539):
<p>(or term mode proof)</p>

#### [ Mario Carneiro (Sep 26 2018 at 10:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134653561):
<p>Unfortunately I don't know if tactics can capture trace output</p>

#### [ Kevin Buzzard (Sep 26 2018 at 10:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134653630):
<blockquote>
<blockquote>
<p>or even just a wrapper for simp, that calls <code>simp</code>, looks at the result, and works out automatically a <code>simp only</code> command that will work, and outputs that as a trace message.</p>
</blockquote>
<p>that's exaclty what's in my mind</p>
</blockquote>
<p>Kenny why don't you look at how Scott got <code>tidy</code> to print out its proofs, and then write code which does what you're doing, or at least does part of it? It will make you a more powerful Lean programmer. Chris might be able to help you with this when you're back in London -- he knows some tactic stuff now.</p>

#### [ Kenny Lau (Sep 26 2018 at 10:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134653667):
<p>or you all can help me with my project so we can have a faster build sooner</p>

#### [ Mario Carneiro (Sep 26 2018 at 10:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134653688):
<p>maybe we can look at the proof term that is generated by <code>simp</code> to work out those lemmas</p>

#### [ Kevin Buzzard (Sep 26 2018 at 10:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134653699):
<p>I am not motivated to have a faster build because things build fast for me already :-/</p>

#### [ Mario Carneiro (Sep 26 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134653799):
<p>do holes work inside interactive tactic mode?</p>

#### [ Mario Carneiro (Sep 26 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134653810):
<p>like <code>begin {! !} end</code></p>

#### [ Kenny Lau (Sep 26 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134653817):
<blockquote>
<p>I am not motivated to have a faster build because things build fast for me already :-/</p>
</blockquote>
<p>remember the problems with mathlib that we talked about?</p>

#### [ Johan Commelin (Sep 26 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134653910):
<blockquote>
<p>do holes work inside interactive tactic mode?</p>
</blockquote>
<p>It seems that they do.</p>

#### [ Mario Carneiro (Sep 26 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134653928):
<p>there is a reason I recommended you focus on the worst offenders - not only is it a huge project to change every proof, but I'm not even sure that's a good idea</p>

#### [ Mario Carneiro (Sep 26 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134653953):
<p>you will get most of the benefits with just working on 2 or 3 files in mathlib</p>

#### [ Kenny Lau (Sep 26 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134653956):
<p>I understand</p>

#### [ Kenny Lau (Sep 26 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134653973):
<p>do you know which 3 files those are?</p>

#### [ Mario Carneiro (Sep 26 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134654013):
<p>no</p>

#### [ Kenny Lau (Sep 26 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134654023):
<p>do you know how I can find out?</p>

#### [ Mario Carneiro (Sep 26 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134654028):
<p>I'm hoping that you will find a way to use the profiler for this</p>

#### [ Mario Carneiro (Sep 26 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134654033):
<p>and let me know what you do</p>

#### [ Kenny Lau (Sep 26 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134654071):
<p>ok</p>

#### [ Mario Carneiro (Sep 26 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134654378):
<p>kenny, have you found that <code>simp only</code> is faster or slower than <code>rw</code> when you have to give a list of rewrites?</p>

#### [ Kenny Lau (Sep 26 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134654429):
<p>I think they're roughly the same</p>

#### [ Mario Carneiro (Sep 26 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/134654607):
<p>Also, if you come up with proof shortenings while you are doing this (and I expect you will), you should hold on to them and PR them separately. I'm not opposed to this, but the review is different</p>

#### [ Kenny Lau (Oct 02 2018 at 09:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135019586):
<p><a href="#narrow/stream/113488-general/subject/.22div_neg.22/near/134653199" title="#narrow/stream/113488-general/subject/.22div_neg.22/near/134653199">https://leanprover.zulipchat.com/#narrow/stream/113488-general/subject/.22div_neg.22/near/134653199</a></p>
<blockquote>
<p>Mario Carneiro: definitional unfolding is not always fast<br>
Mario Carneiro: hint: <code>10 + 10 = 20 := rfl</code></p>
</blockquote>
<p><a href="/user_uploads/3121/A-LPlvuMKGXmQM8fHPvu_LW8/2018-10-02.png" target="_blank" title="2018-10-02.png">10+10=20</a></p>
<div class="message_inline_image"><a href="/user_uploads/3121/A-LPlvuMKGXmQM8fHPvu_LW8/2018-10-02.png" target="_blank" title="10+10=20"><img src="/user_uploads/3121/A-LPlvuMKGXmQM8fHPvu_LW8/2018-10-02.png"></a></div>

#### [ Mario Carneiro (Oct 02 2018 at 09:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135019643):
<p>it was a hint, not an answer</p>

#### [ Kenny Lau (Oct 02 2018 at 09:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135019644):
<p>I see</p>

#### [ Chris Hughes (Oct 02 2018 at 09:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135019654):
<p>Try <code>10000 * 10000</code></p>

#### [ Mario Carneiro (Oct 02 2018 at 09:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135019656):
<p>obviously you should put a silly number of zeroes in random places, maybe a <code>^</code> for good measure</p>

#### [ Kenny Lau (Oct 02 2018 at 10:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135020222):
<p>I don't really think that's a good argument though. <code>10000 * 10000</code> would be a lot of layers of definitional unfolding, so what you really mean is that if you have a lot of layers of definitional unfolding then it would be slow. Of course, any fast process repeated 100000000 times will take a long time. That doesn't mean definitional unfolding itself is slow.</p>

#### [ Mario Carneiro (Oct 02 2018 at 10:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135020288):
<p>Okay, how about <code>nat.prime 5 := dec_trivial</code>?</p>

#### [ Kenny Lau (Oct 02 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135020346):
<p>what do I need to import?</p>

#### [ Mario Carneiro (Oct 02 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135020415):
<p><code>data.nat.prime</code></p>

#### [ Kenny Lau (Oct 02 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135020432):
<p>and I also need an instance?</p>

#### [ Mario Carneiro (Oct 02 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135020435):
<p>the default one</p>

#### [ Kenny Lau (Oct 02 2018 at 10:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135020495):
<p>well there are two of them</p>

#### [ Mario Carneiro (Oct 02 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135020524):
<p>Actually the most convincing example is probably <code>ring2</code>. I wrote the same tactic twice, once via computational reflection, aka kernel evaluation, and once using the VM to produce proof terms. It wasn't significantly slower, but it was measurable, like 50% worse</p>

#### [ Kenny Lau (Oct 02 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135020551):
<p>which one was worse?</p>

#### [ Mario Carneiro (Oct 02 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135020563):
<p><code>ring2</code> of course</p>

#### [ Mario Carneiro (Oct 02 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135020570):
<p>Otherwise it would be called <code>ring</code> now</p>

#### [ Kenny Lau (Oct 02 2018 at 18:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135048800):
<p>not every term mode proof is fast</p>

#### [ Kenny Lau (Oct 02 2018 at 18:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135048803):
<p>but every fast proof is in term mode</p>

#### [ Kenny Lau (Oct 02 2018 at 18:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135048809):
<p>every proof that gets below 10 ms is done in term mode</p>

#### [ Kenny Lau (Oct 02 2018 at 19:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135049451):
<p><a href="/user_uploads/3121/zqTn_dKHUTIKI1ujiLPrhKOR/2018-10-02-1.png" target="_blank" title="2018-10-02-1.png">case in point:</a></p>
<div class="message_inline_image"><a href="/user_uploads/3121/zqTn_dKHUTIKI1ujiLPrhKOR/2018-10-02-1.png" target="_blank" title="case in point:"><img src="/user_uploads/3121/zqTn_dKHUTIKI1ujiLPrhKOR/2018-10-02-1.png"></a></div>

#### [ Kenny Lau (Oct 02 2018 at 19:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135049466):
<p>ok bad example, <code>rfl</code> is a special term</p>

#### [ Kenny Lau (Oct 02 2018 at 19:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135049507):
<p><a href="/user_uploads/3121/8XdY6dp5U5mlaOPN-YFCkls_/2018-10-02-4.png" target="_blank" title="2018-10-02-4.png">case in point:</a></p>
<div class="message_inline_image"><a href="/user_uploads/3121/8XdY6dp5U5mlaOPN-YFCkls_/2018-10-02-4.png" target="_blank" title="case in point:"><img src="/user_uploads/3121/8XdY6dp5U5mlaOPN-YFCkls_/2018-10-02-4.png"></a></div>

#### [ Johan Commelin (Oct 02 2018 at 19:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135049582):
<p>"All fast proofs are alike; each slow proof is slow in its own way" — Λeo Tolstoy</p>

#### [ Kenny Lau (Oct 02 2018 at 19:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135049634):
<p>is that a lambda?</p>

#### [ Kevin Buzzard (Oct 02 2018 at 19:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135049689):
<p>Do you get big speed-up if you tell Lean what the missing terms are instead of making it guess them?</p>

#### [ Kenny Lau (Oct 02 2018 at 19:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135049731):
<p>depends on the term</p>

#### [ Kenny Lau (Oct 02 2018 at 19:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135049733):
<p>mostly no.</p>

#### [ Mario Carneiro (Oct 02 2018 at 19:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135050403):
<p>You get a really big speedup if you just write olean files by hand</p>

#### [ Chris Hughes (Oct 02 2018 at 19:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135050694):
<p>It's not really a long term solution. The long term solution is to have an option to import files without proof checking, so that editing is easier. I've been using a ton of <code>linarith</code> when writing my stuff on exp, and it's great that when you have a goal like this, you don't have to think about it, and that's the way it should be, and I think it's hard to sell Lean if you say using these tactics is discouraged because they're slow.</p>

#### [ Johan Commelin (Oct 02 2018 at 19:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135050710):
<p>Right, so we are back to the caching that we have been talking about.</p>

#### [ Johan Commelin (Oct 02 2018 at 19:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135050762):
<p>We need readable (editable?) proofs. But we also need speed.</p>

#### [ Johan Commelin (Oct 02 2018 at 19:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135050772):
<p>So we need several layers of caches, I think.</p>

#### [ Mario Carneiro (Oct 02 2018 at 19:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135050838):
<p>This is one of the reasons I like metamath - there was a very clear middle layer that is easy to verify quickly and compiled-to by higher level IDEs</p>

#### [ Mario Carneiro (Oct 02 2018 at 19:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135050849):
<p>storing only proof scripts forces their reevaluation on a regular basis</p>

#### [ Mario Carneiro (Oct 02 2018 at 19:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135050909):
<p>In principle this should be the olean file, but the current design has these being far too ephemeral</p>

#### [ Mario Carneiro (Oct 02 2018 at 19:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135051025):
<p>Does anyone know how many definitions there are in mathlib? If we were to aim for 5 minutes compilation, how much time does that give each definition on average?</p>

#### [ Mario Carneiro (Oct 02 2018 at 19:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135051061):
<p>(this ignores multithreading, but I'm not sure if travis is even multithreaded)</p>

#### [ Johan Commelin (Oct 02 2018 at 19:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135051179):
<p>I don't really care about the Travis compile time. I care about the compile time on my laptop, and that of Chris, and yours.</p>

#### [ Johan Commelin (Oct 02 2018 at 19:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135051188):
<p>For me it currently takes more than an hour...</p>

#### [ Johan Commelin (Oct 02 2018 at 19:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135051239):
<p>Concerning number of statements: I think this was somewhere in the statistics of Patrick.</p>

#### [ Chris Hughes (Oct 02 2018 at 19:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135051275):
<p>I don't even care about that. I care about the 10 minute - 1 hour wait for the yellow bar to move whenever I change some library file with quite a few dependencies.</p>

#### [ Johan Commelin (Oct 02 2018 at 19:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135051385):
<div class="codehilite"><pre><span></span>for i in def lemma theorem; do git grep &quot;^$i&quot; | wc -l; done
1301
2511
3942
</pre></div>

#### [ Johan Commelin (Oct 02 2018 at 19:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135051432):
<p>That's a rough approximation, because it doesn't match simp-lemmas etc</p>

#### [ Mario Carneiro (Oct 02 2018 at 19:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135051491):
<p>that is 40ms each, sounds tough</p>

#### [ Johan Commelin (Oct 02 2018 at 19:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135051527):
<div class="codehilite"><pre><span></span>for i in def lemma theorem &quot;\\@\\[&quot;; do git grep &quot;^$i&quot; | wc -l; done
1301
2511
3942
3457
</pre></div>

#### [ Mario Carneiro (Oct 02 2018 at 19:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135051565):
<p>There could be some overcounting there though</p>

#### [ Johan Commelin (Oct 02 2018 at 19:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135051615):
<p>Right. To do this properly one should use one of the statistics tools</p>

#### [ Johan Commelin (Oct 02 2018 at 19:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135051628):
<p>But I don't care if I have to compile for 8 hours, once a month.</p>

#### [ Johan Commelin (Oct 02 2018 at 19:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135051634):
<p>I'll just leave my laptop running overnight.</p>

#### [ Johan Commelin (Oct 02 2018 at 19:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135051641):
<p>The rest of the month, some sort of intermediate layer should be sufficient.</p>

#### [ Johan Commelin (Oct 02 2018 at 19:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135051718):
<p>But I guess it doesn't make sense to discuss this all over again. I hope Lean 4 will bring some nice features. The issue about memoisation of tactic blocks sounded good. I hope something like that will be realised.</p>

#### [ Mario Carneiro (Oct 02 2018 at 19:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135051826):
<p>What about "unsafe caching"? In the sense, if A changes and you are modifying C and B is in the dependency path, then A is updated and rechecked, B remains untouched and all its theorems continue to hold in the old A environment, and C uses both, with conflicts resolved in favor of the new A environment</p>

#### [ Mario Carneiro (Oct 02 2018 at 19:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135051870):
<p>This is not sound, but it would be pretty hard to notice the inconsistency unless you are specifically trying to foil it</p>

#### [ Mario Carneiro (Oct 02 2018 at 19:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135051923):
<p>And it would only be for editor interaction anyway</p>

#### [ Johan Commelin (Oct 02 2018 at 19:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135051971):
<p>Right... it is completely fine if the stuff is opportunistic</p>

#### [ Johan Commelin (Oct 02 2018 at 19:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135052005):
<p>If it trips on some edge case you just flag it to rebuild some caches</p>

#### [ Johan Commelin (Oct 02 2018 at 19:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135052022):
<p>But again... this is not something we can currently do, right?</p>

#### [ Mario Carneiro (Oct 02 2018 at 19:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135052070):
<p>no, this requires lean support as does any caching modification</p>

#### [ Johan Commelin (Oct 02 2018 at 20:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135052336):
<p>I should say that even "readable term-mode proofs" (what most people here would call readable) are really bad for showing to newcomers. There was a PhD student who showed quite a bit of interest over lunch. He asked me if I could show him some files on ring theory. So we browsed mathlib a bit. He really liked the interactive proofs. But as soon as a term-mode proof was more than a simple lambda-expression he was completely lost and disappointed.</p>

#### [ Johan Commelin (Oct 02 2018 at 20:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135052346):
<p>Especially some 15-line term-mode proofs that were impossible to explain</p>

#### [ Andrew Ashworth (Oct 02 2018 at 20:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135052510):
<p>What do you think of TPIL's term mode style?</p>

#### [ Johan Commelin (Oct 02 2018 at 20:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135052669):
<p>Can you point me to a specific page?</p>

#### [ Johan Commelin (Oct 02 2018 at 20:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135052770):
<p><span class="user-mention" data-user-id="110025">@Andrew Ashworth</span> Do you mean something like p34?</p>

#### [ Johan Commelin (Oct 02 2018 at 20:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135052778):
<p>I would say that is readable, but it is also extremely long-winded for a really simple goal.</p>

#### [ Johan Commelin (Oct 02 2018 at 20:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135052886):
<p>It helps that the write a lot of types and <code>show</code> that are not strictly necessary.</p>

#### [ Andrew Ashworth (Oct 02 2018 at 20:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135052918):
<p>yes, in general, TPIL's style of using lots of explicit <code>show</code>, <code>have</code>, and <code>calc</code> mode</p>

#### [ Johan Commelin (Oct 02 2018 at 20:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135052991):
<p>But what is the benefit over tactic mode?</p>

#### [ Johan Commelin (Oct 02 2018 at 20:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135053034):
<p>Those proofs have a pretty straight forward analogue in tactic mode. With the benefit that you get interaction, and you can see how the proof state changes.</p>

#### [ Andrew Ashworth (Oct 02 2018 at 20:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135053048):
<p>hmm, well, 1) you may read it without using the Lean editor, 2) organizing proofs around key <code>have</code> statements instead of long chains of <code>apply</code> or <code>rewrite</code> is good practice</p>

#### [ Johan Commelin (Oct 02 2018 at 20:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135053097):
<p>But both of those can be done in tactic mode</p>

#### [ Andrew Ashworth (Oct 02 2018 at 20:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135053159):
<p>sure! and that's great for tactic mode. also I don't want to deny using tactics and advocate for 100% terms</p>

#### [ Johan Commelin (Oct 02 2018 at 20:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135053221):
<div class="codehilite"><pre><span></span>git grep &quot;^begin&quot; | wc -l
800
</pre></div>

#### [ Johan Commelin (Oct 02 2018 at 20:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135053238):
<p>It is clear that tactic mode proofs are a minority in mathlib</p>

#### [ Johan Commelin (Oct 02 2018 at 20:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135053247):
<p>And it is not clear to me why.</p>

#### [ Andrew Ashworth (Oct 02 2018 at 20:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135053264):
<p>Just like in Coq most people write tactic mode proofs, but they could also write them in C-Zar style</p>

#### [ Andrew Ashworth (Oct 02 2018 at 20:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135053266):
<p><a href="https://www-verimag.imag.fr/~corbinea/ftp/programs/sqrt2.v" target="_blank" title="https://www-verimag.imag.fr/~corbinea/ftp/programs/sqrt2.v">https://www-verimag.imag.fr/~corbinea/ftp/programs/sqrt2.v</a></p>

#### [ Andrew Ashworth (Oct 02 2018 at 20:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135053275):
<p>and I prefer to read those kinds of proofs</p>

#### [ Johan Commelin (Oct 02 2018 at 20:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135053306):
<p>Sure, there are expensive tactics... we can try to use those for proof discovery, and remove them later (or have good caching <span class="emoji emoji-1f61c" title="stuck out tongue wink">:stuck_out_tongue_wink:</span>). But just a bunch of <code>have</code> and <code>show</code>, <code>convert</code>, <code>cases</code>, <code>split</code>, etc...</p>

#### [ Johan Commelin (Oct 02 2018 at 20:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135053323):
<p>That shouldn't be much more expensive then term mode, I hope.</p>

#### [ Andrew Ashworth (Oct 02 2018 at 20:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135053366):
<p>it's really not about tactics, I think, just that tactics encourage what I think is a kind of sloppy proof writing</p>

#### [ Andrew Ashworth (Oct 02 2018 at 20:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135053378):
<p>with not much care about reading and understanding the proof later</p>

#### [ Andrew Ashworth (Oct 02 2018 at 20:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135053380):
<p>of course you can do the same thing in term mode</p>

#### [ Johan Commelin (Oct 02 2018 at 20:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135053383):
<p>Huh?</p>

#### [ Johan Commelin (Oct 02 2018 at 20:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135053397):
<p>With every term mode proof I have trouble "reading and understanding the proof later"</p>

#### [ Andrew Ashworth (Oct 02 2018 at 20:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135053398):
<p>I think I jokingly complained about this many months ago to Mario when I was going through Mathlib's analysis section</p>

#### [ Johan Commelin (Oct 02 2018 at 20:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135053404):
<p>It is the tactic proofs that I find easy to follow</p>

#### [ Johan Commelin (Oct 02 2018 at 20:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135053415):
<p>Btw, link is broken over here.</p>

#### [ Andrew Ashworth (Oct 02 2018 at 20:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135053511):
<p><a href="https://gist.github.com/alashworth/0f1446b5b322427cfd42a6ccb5a9df83" target="_blank" title="https://gist.github.com/alashworth/0f1446b5b322427cfd42a6ccb5a9df83">https://gist.github.com/alashworth/0f1446b5b322427cfd42a6ccb5a9df83</a></p>

#### [ Johan Commelin (Oct 02 2018 at 20:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135053534):
<p>Maybe tactic mode makes me sloppy. But I'm sure that I can come back and pretty quickly edit some proof or make little changes. With term mode I just have to start all over again.</p>

#### [ Johan Commelin (Oct 02 2018 at 20:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135053588):
<p>Those proofs in that link are very readable!</p>

#### [ Andrew Ashworth (Oct 02 2018 at 20:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135053659):
<p>yes, I imagine anybody could understand them, even if they don't know any Coq</p>

#### [ Johan Commelin (Oct 02 2018 at 20:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135053773):
<p>In Orsay we spoke about a VScode button that would transform a term-mode proof into a tactic block. Just by silly regex transformations you could get pretty far...</p>

#### [ Johan Commelin (Oct 02 2018 at 20:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135053807):
<p>I haven't figured out how to contribute to the VScode extensions, but I think it would be really helpful for me...</p>

#### [ Andrew Ashworth (Oct 02 2018 at 20:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135053919):
<p>if people wrote their term mode proofs with care, in the style of TPIL or the gist I linked, then you wouldn't need to step through it with Lean :) I guess that's the point I wanted to make</p>

#### [ Andrew Ashworth (Oct 02 2018 at 20:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135053942):
<p>I agree with your friend that most proofs in mathlib, term mode or tactic mode, are impossible to understand without taking them apart by hand...</p>

#### [ Andrew Ashworth (Oct 02 2018 at 20:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135054129):
<p>but as it turns out the concise style seems to be popular no matter the language. In Coq nobody uses C-Zar, but instead SSReflect, which is famously terse</p>

#### [ Andrew Ashworth (Oct 02 2018 at 20:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135054137):
<p>(for math anyway)</p>

#### [ Johan Commelin (Oct 02 2018 at 20:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135054197):
<p>hmmm... is it also faster?</p>

#### [ Andrew Ashworth (Oct 02 2018 at 20:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135054335):
<p>I don't know enough about SSReflect to compare the two</p>

#### [ Andrew Ashworth (Oct 02 2018 at 20:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135054356):
<p>Actually I found out about Lean after struggling with SSReflect in an IRC chatroom... and then I switched</p>

#### [ Johan Commelin (Oct 02 2018 at 20:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135054371):
<p>Lol</p>

#### [ Kenny Lau (Oct 02 2018 at 20:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135055543):
<blockquote>
<p>It is clear that tactic mode proofs are a minority in mathlib</p>
</blockquote>
<p>maybe you forgot <code>by</code></p>

#### [ Kenny Lau (Oct 02 2018 at 20:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135055706):
<blockquote>
<p>that is 40ms each, sounds tough</p>
</blockquote>
<p>20% of the theorems take 80% of the time to compile (Pareto principle)</p>

#### [ Kenny Lau (Oct 02 2018 at 20:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135055715):
<p>many theorems take less than 40ms to compile</p>

#### [ Kevin Buzzard (Oct 03 2018 at 09:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%22div_neg%22/near/135086345):
<p>Everyone seems to have different opinions about readability. People like Larry Paulson in Cambridge seem to believe it is a fundamental principle which should be adhered to at all costs. I had always assumed that Mario's attitude was "hang readability, just get it done in as few characters as possible" -- but then later on I realised that Mario was writing code which he could actually read, it was just that I couldn't read it. No doubt this will come with practice.</p>
<p>My opinion is that actually I don't think anyone reads Bourbaki, people read books which are written to be read so that people could learn the material, and Bourbaki was written to be foundational. There is one Bourbaki that people read -- the stuff on algebraic groups -- because it's a really good refrence for e.g. all the facts and figures for the exceptional groups like E_8, G_2 etc -- but in general my experience is that people only read Bourbaki if they're desperate or if they for some reason want to see the theory built up from scratch (and most mathematicians don't). I've come to the conclusion that when it comes to mathlib I don't care whether the proofs are readable or not, because that is not the point of mathlib. I have occasionally in the past written instructive proofs, and actually this term I will be writing a whole bunch of instructive proofs of basic mathematics, with Lean tactic proofs littered with comments. But that's because I'm concentrating on teaching. In my mind the main criteria for a mathlib proof should be "is it easily maintainable?". I am hoping that compilation times are something which can be solved by technology (code to make it so I only have to compile once a month, speed-ups, better hardware) in the long term.</p>


{% endraw %}
