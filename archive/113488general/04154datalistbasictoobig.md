---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/04154datalistbasictoobig.html
---

## Stream: [general](index.html)
### Topic: [data/list/basic too big?](04154datalistbasictoobig.html)

---


{% raw %}
#### [ Scott Morrison (Jun 22 2018 at 01:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/data/list/basic%20too%20big%3F/near/128444963):
<p>Is this output from travis:</p>
<div class="codehilite"><pre><span></span>/home/travis/build/semorrison/lean-tidy/_target/deps/mathlib/data/list/basic.lean: list.last_append
No output has been received in the last 10m0s, this potentially indicates a stalled build or something wrong with the build itself.
Check the details on how to adjust your build configuration on: https://docs.travis-ci.com/user/common-build-problems/#Build-times-out-because-no-output-was-received
</pre></div>


<p>(taken from <a href="https://travis-ci.org/semorrison/lean-tidy/builds/395245684?utm_source=email&amp;utm_medium=notification" target="_blank" title="https://travis-ci.org/semorrison/lean-tidy/builds/395245684?utm_source=email&amp;utm_medium=notification">https://travis-ci.org/semorrison/lean-tidy/builds/395245684?utm_source=email&amp;utm_medium=notification</a>) an indication that <code>data/list/basic.lean</code> has grown too big?</p>

#### [ Scott Morrison (Jun 22 2018 at 01:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/data/list/basic%20too%20big%3F/near/128445006):
<p>Another piece of evidence of this is that when a I compile all of mathlib on a many core machine, there seems to be a bottleneck in data/list/basic, when most of the cores have to pause to wait for the thread dealing with this file to finish.</p>

#### [ Reid Barton (Jun 22 2018 at 02:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/data/list/basic%20too%20big%3F/near/128447691):
<p>AFAIK the unit of granularity for threading is a single declaration, so I don't think the file size itself is the issue.<br>
Of course there could be bottlenecks in the dependency graph of declarations, individual declarations which take a long time to compile, etc.</p>

#### [ Sean Leather (Jun 22 2018 at 08:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/data/list/basic%20too%20big%3F/near/128459145):
<p>I think Reid is right. We would need to look at which declaration is causing the slowdown and optimize that. I've seen it myself but haven't taken the time to look into it. I wonder if it's as simple as looking at the printed declaration (<code>list.last_append</code> as you have it), or if there is another culprit.</p>
<p>Perhaps a Lean expert would want to commit a little time here?</p>

#### [ Reid Barton (Jun 22 2018 at 16:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/data/list/basic%20too%20big%3F/near/128475720):
<p>I think that usually when lean's output seems to get "stuck" on one declaration for a long time, that declaration usually is the one that's taking all the time. In the past there were a couple of uses of <code>finish</code> which were very expensive, and easy to spot if you watched the build output.<br>
I notice that <code>list.last_append</code> uses <code>rsimp</code>, which I didn't even know existed; maybe it can also be very slow?</p>

#### [ Sean Leather (Jun 25 2018 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/data/list/basic%20too%20big%3F/near/128588093):
<p>I just sped up the build by simplifying <code>list.last_append</code>. <code>rsimp</code> was definitely the problem and turned out to be unnecessary. <code>list.last_append</code> now builds very quickly. PR forthcoming. <span class="emoji emoji-1f389" title="tada">:tada:</span></p>

#### [ Mario Carneiro (Jun 25 2018 at 09:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/data/list/basic%20too%20big%3F/near/128588103):
<p>I already fixed this in my local copy</p>

#### [ Mario Carneiro (Jun 25 2018 at 10:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/data/list/basic%20too%20big%3F/near/128588142):
<p>not sure if there are any other issues, I'm working on better profiling</p>

#### [ Mario Carneiro (Jun 25 2018 at 10:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/data/list/basic%20too%20big%3F/near/128588153):
<p>(I just replaced <code>rsimp</code> with <code>simp</code> and the proof went through)</p>

#### [ Sean Leather (Jun 25 2018 at 10:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/data/list/basic%20too%20big%3F/near/128588164):
<p><a href="https://github.com/leanprover/mathlib/pull/167" target="_blank" title="https://github.com/leanprover/mathlib/pull/167">https://github.com/leanprover/mathlib/pull/167</a></p>

#### [ Sean Leather (Jun 25 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/data/list/basic%20too%20big%3F/near/128588331):
<blockquote>
<p>I already fixed this in my local copy</p>
</blockquote>
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> So I wasted my time. In the future, can you please communicate this to the rest of us? It would be most helpful if you or anyone else created GitHub issues for such things. They tend to get lost in Zulip.</p>

#### [ Mario Carneiro (Jun 25 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/data/list/basic%20too%20big%3F/near/128588335):
<p>Sorry, been busy these days</p>

#### [ Sean Leather (Jun 25 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/data/list/basic%20too%20big%3F/near/128588346):
<p>... which is why I offered to help maintain mathlib. <span class="emoji emoji-1f604" title="smile">:smile:</span></p>

#### [ Mario Carneiro (Jun 25 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/data/list/basic%20too%20big%3F/near/128588395):
<p>of course it's not necessarily a waste of time, depending on how you discovered that theorem</p>

#### [ Sean Leather (Jun 25 2018 at 10:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/data/list/basic%20too%20big%3F/near/128588521):
<blockquote>
<p>of course it's not necessarily a waste of time, depending on how you discovered that theorem</p>
</blockquote>
<p>I discovered it because I saw the same issue mentioned above in this thread (which means that it was taking a long time to compile <code>last_append</code>, which means I wasted time waited for it to compile <span class="emoji emoji-1f609" title="wink">:wink:</span>).</p>

#### [ Simon Hudon (Jun 25 2018 at 15:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/data/list/basic%20too%20big%3F/near/128600209):
<p>I think one thing that might help streamline maintenance is write a lint tool. I was thinking of using grep to spot the most obvious stylistic mistakes and that you we could add as a git hook</p>

#### [ Simon Hudon (Jun 25 2018 at 15:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/data/list/basic%20too%20big%3F/near/128600221):
<p>It might help use the maintainers' time more sparingly</p>

#### [ Sean Leather (Jun 25 2018 at 17:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/data/list/basic%20too%20big%3F/near/128605048):
<p>Yet another speedup by replacing an <code>rsimp</code> proof with something else: <a href="https://github.com/leanprover/mathlib/pull/169" target="_blank" title="https://github.com/leanprover/mathlib/pull/169">https://github.com/leanprover/mathlib/pull/169</a></p>
<p>I like this <a href="https://github.com/spl/mathlib/blob/16c1915e22d62d29f0a2a8a15d31d93ce1372b03/order/boolean_algebra.lean#L42-L47" target="_blank" title="https://github.com/spl/mathlib/blob/16c1915e22d62d29f0a2a8a15d31d93ce1372b03/order/boolean_algebra.lean#L42-L47">proof</a>. I think it's very readable, unlike many of my other proofs. <span class="emoji emoji-1f61c" title="stuck out tongue winking eye">:stuck_out_tongue_winking_eye:</span> </p>
<div class="codehilite"><pre><span></span><span class="k">calc</span> <span class="bp">-</span><span class="n">x</span> <span class="bp">=</span> <span class="bp">-</span><span class="n">x</span> <span class="err">⊓</span> <span class="o">(</span><span class="n">x</span> <span class="err">⊔</span> <span class="n">y</span><span class="o">)</span>    <span class="o">:</span> <span class="k">by</span> <span class="n">simp</span> <span class="o">[</span><span class="n">s</span><span class="o">]</span>
    <span class="bp">...</span> <span class="bp">=</span> <span class="bp">-</span><span class="n">x</span> <span class="err">⊓</span> <span class="n">x</span> <span class="err">⊔</span> <span class="bp">-</span><span class="n">x</span> <span class="err">⊓</span> <span class="n">y</span> <span class="o">:</span> <span class="n">inf_sup_left</span>
    <span class="bp">...</span> <span class="bp">=</span> <span class="n">y</span> <span class="err">⊓</span> <span class="n">x</span> <span class="err">⊔</span> <span class="n">y</span> <span class="err">⊓</span> <span class="bp">-</span><span class="n">x</span>  <span class="o">:</span> <span class="k">by</span> <span class="n">simp</span> <span class="o">[</span><span class="n">i</span><span class="o">,</span> <span class="n">inf_comm</span><span class="o">]</span>
    <span class="bp">...</span> <span class="bp">=</span> <span class="n">y</span> <span class="err">⊓</span> <span class="o">(</span><span class="n">x</span> <span class="err">⊔</span> <span class="bp">-</span><span class="n">x</span><span class="o">)</span>    <span class="o">:</span> <span class="n">inf_sup_left</span><span class="bp">.</span><span class="n">symm</span>
    <span class="bp">...</span> <span class="bp">=</span> <span class="n">y</span>               <span class="o">:</span> <span class="k">by</span> <span class="n">simp</span>
</pre></div>

#### [ Sean Leather (Jun 25 2018 at 17:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/data/list/basic%20too%20big%3F/near/128605112):
<p>I don't often write <code>calc</code> proofs, so that probably has something to do with it.</p>


{% endraw %}
