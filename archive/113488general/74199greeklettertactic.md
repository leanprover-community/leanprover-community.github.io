---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/74199greeklettertactic.html
---

## Stream: [general](index.html)
### Topic: [greek letter tactic](74199greeklettertactic.html)

---


{% raw %}
#### [ Patrick Massot (May 28 2018 at 13:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/greek%20letter%20tactic/near/127201952):
<p>Is there a tactic doing only that greek letter which transforms <code>(λ  a, f a) x</code> to <code>f x</code>?</p>

#### [ Andrew Ashworth (May 28 2018 at 13:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/greek%20letter%20tactic/near/127202121):
<p>I think <code>dsimp</code> with one of its special options does it, but I don't remember exactly what it is</p>

#### [ Kenny Lau (May 28 2018 at 13:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/greek%20letter%20tactic/near/127202123):
<p>that's eta reduction</p>

#### [ Kenny Lau (May 28 2018 at 13:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/greek%20letter%20tactic/near/127202126):
<p>no</p>

#### [ Andrew Ashworth (May 28 2018 at 13:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/greek%20letter%20tactic/near/127202127):
<p>beta</p>

#### [ Kenny Lau (May 28 2018 at 13:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/greek%20letter%20tactic/near/127202128):
<p>that's delta reduction</p>

#### [ Kenny Lau (May 28 2018 at 13:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/greek%20letter%20tactic/near/127202129):
<p>oh</p>

#### [ Kenny Lau (May 28 2018 at 13:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/greek%20letter%20tactic/near/127202131):
<p>beta it is then</p>

#### [ Patrick Massot (May 28 2018 at 13:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/greek%20letter%20tactic/near/127202136):
<p>I say alpha!</p>

#### [ Kenny Lau (May 28 2018 at 13:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/greek%20letter%20tactic/near/127202143):
<p>no, that's also eta reduction</p>

#### [ Patrick Massot (May 28 2018 at 13:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/greek%20letter%20tactic/near/127202148):
<p>We need printable DTT cheat sheets</p>

#### [ Kenny Lau (May 28 2018 at 13:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/greek%20letter%20tactic/near/127202151):
<p>it's not even DTT</p>

#### [ Kenny Lau (May 28 2018 at 13:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/greek%20letter%20tactic/near/127202391):
<div class="codehilite"><pre><span></span><span class="c1">-- (λ (a : X), f a) x = f x</span>
<span class="kn">example</span> <span class="o">:</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">a</span><span class="o">,</span> <span class="n">f</span> <span class="n">a</span><span class="o">)</span> <span class="n">x</span> <span class="bp">=</span> <span class="n">f</span> <span class="n">x</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">dsimp</span> <span class="o">{</span> <span class="n">eta</span> <span class="o">:=</span> <span class="n">false</span><span class="o">,</span> <span class="n">beta</span> <span class="o">:=</span> <span class="n">false</span> <span class="o">}</span>

<span class="c1">-- (λ (a : X), f a) x = f x</span>
<span class="kn">example</span> <span class="o">:</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">a</span><span class="o">,</span> <span class="n">f</span> <span class="n">a</span><span class="o">)</span> <span class="n">x</span> <span class="bp">=</span> <span class="n">f</span> <span class="n">x</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">dsimp</span> <span class="o">{</span> <span class="n">eta</span> <span class="o">:=</span> <span class="n">true</span><span class="o">,</span> <span class="n">beta</span> <span class="o">:=</span> <span class="n">false</span> <span class="o">}</span>

<span class="c1">-- f x = f x</span>
<span class="kn">example</span> <span class="o">:</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">a</span><span class="o">,</span> <span class="n">f</span> <span class="n">a</span><span class="o">)</span> <span class="n">x</span> <span class="bp">=</span> <span class="n">f</span> <span class="n">x</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">dsimp</span> <span class="o">{</span> <span class="n">eta</span> <span class="o">:=</span> <span class="n">false</span><span class="o">,</span> <span class="n">beta</span> <span class="o">:=</span> <span class="n">true</span> <span class="o">}</span>
</pre></div>

#### [ Kenny Lau (May 28 2018 at 13:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/greek%20letter%20tactic/near/127202394):
<p>why isn't it eta?</p>

#### [ Kenny Lau (May 28 2018 at 13:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/greek%20letter%20tactic/near/127202400):
<p><span class="user-mention" data-user-id="110025">@Andrew Ashworth</span></p>

#### [ Andrew Ashworth (May 28 2018 at 13:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/greek%20letter%20tactic/near/127202649):
<p>i don't know how dsimp does it, but I remember it as eta is the sorta useless thing that turns <code>lam x, f x --&gt; f</code>, while beta is <code>(lam x, f x) y --&gt; f y</code></p>

#### [ Andrew Ashworth (May 28 2018 at 13:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/greek%20letter%20tactic/near/127202697):
<p>basically eta only cleans up useless lambdas</p>

#### [ Reid Barton (May 28 2018 at 19:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/greek%20letter%20tactic/near/127213902):
<p>An amazing feature I only discovered recently: <code>set_option pp.beta true</code> will hide those useless <code>(λ a, f a) x</code> in displayed types</p>

#### [ Chris Hughes (May 28 2018 at 19:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/greek%20letter%20tactic/near/127214374):
<p>The slightly annoying thing about that is sometimes it won't rewrite because it's not reduced, and you get frustrated trying to work out why.</p>

#### [ Kevin Buzzard (May 28 2018 at 23:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/greek%20letter%20tactic/near/127222466):
<p>You need to set pp.beta true in rw as well :-)</p>


{% endraw %}
