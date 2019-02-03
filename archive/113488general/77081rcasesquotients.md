---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/77081rcasesquotients.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [rcases + quotients](https://leanprover-community.github.io/archive/113488general/77081rcasesquotients.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Reid Barton (Sep 09 2018 at 11:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rcases%20%2B%20quotients/near/133602376):
<p>I just saw this a moment ago but I think this commit by Johannes needs to be advertised: <a href="https://github.com/leanprover/mathlib/commit/5613d2ecc92ce8fae9555745bd94756dec61a323" target="_blank" title="https://github.com/leanprover/mathlib/commit/5613d2ecc92ce8fae9555745bd94756dec61a323">https://github.com/leanprover/mathlib/commit/5613d2ecc92ce8fae9555745bd94756dec61a323</a></p>

#### [ Kevin Buzzard (Sep 09 2018 at 12:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rcases%20%2B%20quotients/near/133604475):
<p>I look at that commit and I see (1) a commit (2) a title which I don't quite understand and no examples (3) 11 changed files so it's very difficult for me to see the wood from the trees. I find this with many commits to be honest -- things have changed a bit, I don't really know what has happened, I don't have time to look in detail and don't even know whether I will understand what I find. So many commits happen and I get emails about them all but this is not a viable system for me, I need something more digestible. I propose a new thread "this week's commits in mathlib" in the #maths stream, where people can summarise things which they think the community might find useful. I'm not suggesting that people should post to this thread when they make a commit -- on the contrary -- in fact I think I'm suggesting that every few days when I delete a bunch more emails I post myself to the thread trying to summarise what happened and then people who know better correct me. Do you think this sounds workable? I don't see any harm in trying.</p>

#### [ Reid Barton (Sep 09 2018 at 13:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rcases%20%2B%20quotients/near/133604818):
<p>In this case most of those changed files are the examples. I was going to copy an example diff here, but it was hard to find one which would be immediately understandable without context. The basic idea is that you can use <code>rcases</code> (instead of <code>quot.induction_on</code> and its variants) to extract a representative from a value of a quotient type (as long as you're proving a Prop).<br>
I do agree that some kind of periodical "what's new" announcements would be great to have--maybe not restricted to mathlib, but also other projects going on in the community like perfectoid spaces.</p>

#### [ Johannes Hölzl (Sep 09 2018 at 13:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rcases%20%2B%20quotients/near/133605832):
<p>In this case I hoped it would be enough to just look into the changes to the documentation. The idea is very simple: We see quotient types as type you can do cases on, like datatypes. A quotient types only stores one element from the base type, this is what you match on.</p>
<p>Now instead of writing:</p>
<div class="codehilite"><pre><span></span><span class="k">assume</span> <span class="n">x</span><span class="o">,</span> <span class="n">quotient</span><span class="bp">.</span><span class="n">induction_on</span> <span class="n">x</span> <span class="err">$</span> <span class="k">assume</span> <span class="n">a</span><span class="o">,</span> <span class="bp">...</span>
</pre></div>


<p>you just write</p>
<div class="codehilite"><pre><span></span><span class="k">by</span> <span class="n">rintro</span> <span class="bp">⟨</span><span class="n">a</span><span class="bp">⟩;</span> <span class="n">exact</span> <span class="bp">...</span>
</pre></div>


<p>(or even shorter if you stay in tactic mode.</p>
<p>The biggest difference to usual the usual case on datatypes is that this only works in proofs.</p>

#### [ Johannes Hölzl (Sep 09 2018 at 13:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rcases%20%2B%20quotients/near/133605888):
<p>And of course it gets much more important when you have multiple variables:</p>
<div class="codehilite"><pre><span></span><span class="k">assume</span> <span class="n">x</span> <span class="n">y</span> <span class="n">z</span><span class="o">,</span> <span class="n">quotient</span><span class="bp">.</span><span class="n">induction_on</span> <span class="n">x</span> <span class="err">$</span> <span class="k">assume</span> <span class="n">a</span><span class="o">,</span> <span class="n">quotient</span><span class="bp">.</span><span class="n">induction_on</span> <span class="n">y</span> <span class="err">$</span> <span class="k">assume</span> <span class="n">b</span><span class="o">,</span> <span class="n">quotient</span><span class="bp">.</span><span class="n">induction_on</span> <span class="n">z</span> <span class="err">$</span> <span class="k">assume</span> <span class="n">c</span><span class="o">,</span> <span class="bp">...</span>
</pre></div>


<p>is just</p>
<div class="codehilite"><pre><span></span><span class="k">by</span> <span class="n">rintro</span> <span class="bp">⟨</span><span class="n">a</span><span class="bp">⟩</span> <span class="bp">⟨</span><span class="n">b</span><span class="bp">⟩</span> <span class="bp">⟨</span><span class="n">c</span><span class="bp">⟩;</span> <span class="n">exact</span> <span class="bp">...</span>
</pre></div>

#### [ Kevin Buzzard (Sep 09 2018 at 13:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rcases%20%2B%20quotients/near/133605932):
<p>I'm sure it's easy to find out what's going on if you know where to look. One issue with the system is that whilst I get email notifications for all PR's, I don't think I get notifications when you or Mario make commits (and if memory serves I think I raised this issue before and I don't think anyone knew how to make this happen). So in practice I find these things easy to miss. </p>
<p>Thanks for the summary Johannes!</p>

#### [ Johannes Hölzl (Sep 09 2018 at 13:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rcases%20%2B%20quotients/near/133606111):
<p>Hm, yeah direct commits are hard to follow. The announcement channel you just started is a good idea, I will try to announce stuff there.</p>

#### [ Kevin Buzzard (Sep 09 2018 at 14:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rcases%20%2B%20quotients/near/133606375):
<p>Let's see how it goes. Reid's comment about perfectoids made me realise that I am not the only one who realises that they can't see the big picture. There has been no chat in the perfectoid stream for a while but all my recent work on Noetherian stuff is all related and I didn't even mention that my first non-trivial PR had been accepted because currently the direct link to the perfectoid stuff is weak -- what we are aiming for is integral closure of a ring and there's still some way to go.</p>

#### [ Mario Carneiro (Sep 09 2018 at 18:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rcases%20%2B%20quotients/near/133617771):
<p>Re email notifications, RSS has basically emerged as a standard for this kind of thing. I have an RSS reader installed in my browser, and just about every website offers RSS, including github projects. There are also RSS to email services available on the internet</p>


{% endraw %}
