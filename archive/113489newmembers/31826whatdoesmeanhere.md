---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/31826whatdoesmeanhere.html
---

## Stream: [new members](index.html)
### Topic: [what does . mean here?](31826whatdoesmeanhere.html)

---


{% raw %}
#### [ Bryan Gin-ge Chen (Aug 30 2018 at 16:26)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/what%20does%20.%20mean%20here%3F/near/133063613):
<p>I copied this from <a href="https://github.com/leanprover/lean/blob/master/library/init/data/nat/basic.lean#L84" target="_blank" title="https://github.com/leanprover/lean/blob/master/library/init/data/nat/basic.lean#L84">library/init/data/nat/basic.lean</a>.</p>
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">not_succ_le_zero</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">),</span> <span class="n">nat</span><span class="bp">.</span><span class="n">succ</span> <span class="n">n</span> <span class="bp">≤</span> <span class="mi">0</span> <span class="bp">→</span> <span class="n">false</span>
<span class="bp">.</span>
</pre></div>

#### [ cbailey (Aug 30 2018 at 16:29)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/what%20does%20.%20mean%20here%3F/near/133063790):
<p>It's syntax to execute a method inside a module (the nat module). If you do </p>
<div class="codehilite"><pre><span></span><span class="kn">open</span> <span class="n">nat</span>
</pre></div>


<p>you can access succ without the nat. prefix by opening the nat namespace. There's a section in "Theorem Proving in Lean" about the module/namespace keywords.</p>

#### [ Bryan Gin-ge Chen (Aug 30 2018 at 16:30)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/what%20does%20.%20mean%20here%3F/near/133063859):
<p>Sorry, I meant the . on the line all by itself, which somehow suffices as a proof of this lemma.</p>

#### [ Patrick Massot (Aug 30 2018 at 16:31)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/what%20does%20.%20mean%20here%3F/near/133063917):
<p>Usually an dot at the end of something is there only to help the parser</p>

#### [ Bryan Gin-ge Chen (Aug 30 2018 at 16:38)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/what%20does%20.%20mean%20here%3F/near/133064379):
<p>What do you mean by "help the parser" here? Is the dot shorthand for something?</p>

#### [ Patrick Massot (Aug 30 2018 at 16:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/what%20does%20.%20mean%20here%3F/near/133064406):
<p>I mean it tells the parser that something ends here.</p>

#### [ Patrick Massot (Aug 30 2018 at 16:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/what%20does%20.%20mean%20here%3F/near/133064419):
<p>But really I don't know why there is something to end here. The statement is trivial but many other trivial things still require a proof</p>

#### [ Rob Lewis (Aug 30 2018 at 16:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/what%20does%20.%20mean%20here%3F/near/133064512):
<p>It's being used to indicate that this is an empty pattern match. Structurally, there's no <code>n</code> for which you can have a proof of <code>succ n ≤ 0</code>.</p>

#### [ Rob Lewis (Aug 30 2018 at 16:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/what%20does%20.%20mean%20here%3F/near/133064535):
<p>So you're proving the lemma by induction on <code>n</code>, except there are no cases because none of them make sense.</p>

#### [ Rob Lewis (Aug 30 2018 at 16:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/what%20does%20.%20mean%20here%3F/near/133064601):
<p>You need the <code>.</code> so that Lean knows the proof is over and doesn't confuse the next line with a continuation of the lemma statement.</p>

#### [ Bryan Gin-ge Chen (Aug 30 2018 at 16:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/what%20does%20.%20mean%20here%3F/near/133064617):
<p>OK, that makes sense, thanks!</p>

#### [ cbailey (Aug 30 2018 at 16:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/what%20does%20.%20mean%20here%3F/near/133064965):
<p>Oh I was way off lol. My apologies.</p>


{% endraw %}
