---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/66627lean4branch.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [lean 4 branch](https://leanprover-community.github.io/archive/113488general/66627lean4branch.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Mario Carneiro (Apr 11 2018 at 04:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%204%20branch/near/124913759):
<p>For those who are interested: Leo just added a bunch of commits to a new lean 4 branch, primarily just removing lean 3 cruft, and you can see a taste of what it means for the size of corelib.</p>
<ul>
<li>He's already taken a hatchet to most of the math in the corelib library, leaving only definitions of stuff like <code>int.mul</code> without proving it's a comm_ring, etc.</li>
<li><code>norm_num</code> (the core tactic) is also removed, which eliminates the other main dependency on the algebraic hierarchy.</li>
<li><code>coinductive</code> and <code>transfer</code> were removed, but that's not much of a surprise since they were pure lean anyway.</li>
<li>I'm a bit surprised <code>mk_has_sizeof_instance</code> got the axe, unless <code>sizeof</code> itself is going away. But again, it's pure lean so easily replaceable.</li>
<li>unification hints were removed? I'm not sure what's going on here, but it's true that these got essentially no use since they were introduced, and I think the API was not well thought out. But maybe this is a concern for Tom Hales, who has been planning to use unification hints to resolve some typeclass problems. I'll wait to see what's Leo's plan for algebra before making a judgment on this.</li>
<li>SMT is gone, we knew that was coming. Maybe we'll get something better later, but I think it's fair to say that the next thing will be significantly different.</li>
</ul>
<p>I've mentioned this before, but the removal of most of these things from core lib is good news from my point of view, because they can just be reinstated in mathlib, in a place where PRs are not unwelcome. Bad news here would involve things that essentially require lean C support being removed, which can't just be coded up in lean itself, like the SMT stuff. But as Jeremy points out to me, Leo is a world expert when it comes to doing automated theorem proving with equations, and furthermore this is one of the major things that MS will want from any internal uses of Lean, so I'm not unduly worried about this.</p>

#### [ Simon Hudon (Apr 11 2018 at 04:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%204%20branch/near/124913812):
<p>Thanks for the cliff notes</p>

#### [ Patrick Massot (Apr 11 2018 at 08:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%204%20branch/near/124920412):
<p>Thank you very much for taking the time to report on this in a way everybody can understand at least vaguely.</p>

#### [ Sebastian Ullrich (Apr 11 2018 at 09:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%204%20branch/near/124922587):
<blockquote>
<p>I'm a bit surprised mk_has_sizeof_instance got the axe, unless sizeof itself is going away. But again, it's pure lean so easily replaceable.</p>
</blockquote>
<p>There _is_ a pretty big surprise hidden here: Lean 4 will support nested and mutual inductives in the kernel, exactly to get rid of the mess that is <code>sizeof</code> etc</p>

#### [ Mario Carneiro (Apr 11 2018 at 10:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%204%20branch/near/124922656):
<p>If you have any say in it, is there any chance of getting structural recursion in definitions? I want my inductive predicates</p>

#### [ Sebastian Ullrich (Apr 11 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%204%20branch/near/124922808):
<p>You mean like induction-recursion or...?</p>

#### [ Mario Carneiro (Apr 11 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%204%20branch/near/124922814):
<p>No, just plain structural induction, you know, the one that lean does natively?</p>

#### [ Mario Carneiro (Apr 11 2018 at 10:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%204%20branch/near/124922818):
<p>For some reason that's the one kind of induction you <em>can't</em> do using the equation compiler</p>

#### [ Mario Carneiro (Apr 11 2018 at 10:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%204%20branch/near/124922831):
<p>It's not as big a problem here, but this is the same reason why <code>nat.add</code>, defined in the current "obvious way", compiles to a 30-line monster</p>

#### [ Sebastian Ullrich (Apr 11 2018 at 10:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%204%20branch/near/124922991):
<p>Okay, I was confused about the connection to ginductives. But yes, the equation compiler would have to be touched anyway, so... maybe? I don't know why it's not implemented right now, or if it would be hard to do so.</p>

#### [ Mario Carneiro (Apr 11 2018 at 10:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%204%20branch/near/124923057):
<p>Cool, just wanted to make sure you are aware of this</p>

#### [ Gabriel Ebner (Apr 11 2018 at 11:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%204%20branch/near/124924647):
<blockquote>
<p>Lean 4 will support nested and mutual inductives in the kernel</p>
</blockquote>
<p>Wow, it would be awesome if nested inductives worked nicely.  Will Lean 4 still use recursors?  It's probably obvious, but how would the recursor for <code>term</code> look like?</p>
<div class="codehilite"><pre><span></span><span class="kn">inductive</span> <span class="n">term</span>
<span class="bp">|</span> <span class="n">fn</span> <span class="o">(</span><span class="n">args</span> <span class="o">:</span> <span class="n">list</span> <span class="n">term</span><span class="o">)</span>
</pre></div>

#### [ Sebastian Ullrich (Apr 11 2018 at 11:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%204%20branch/near/124924696):
<p>Heh, good question. We've only talked about how to implement mutual inductives so far, to be honest.</p>

#### [ Sebastian Ullrich (Apr 11 2018 at 11:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%204%20branch/near/124924746):
<p>Well, if you interpret it as a mutual definition of <code>term</code> and <code>list term</code>, I suppose you should get three motives? Would that work?</p>

#### [ Gabriel Ebner (Apr 11 2018 at 11:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%204%20branch/near/124925368):
<p>Two motives, but it would work.  So no recursing through <code>map</code>, apparently. <span class="emoji emoji-1f61e" title="disappointed">:disappointed:</span></p>

#### [ Sebastian Ullrich (Apr 30 2018 at 10:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/lean%204%20branch/near/125884409):
<p><span class="user-mention" data-user-id="110043">@Gabriel Ebner</span> I talked with Leo about nested recursion again yesterday and we want to keep using well-founded recursion for this for now. I.e. you should be able to recursive through a dependently-typed <code>pmap</code> variant of <code>map</code>, which hopefully the default <code>dec_tac</code> should make easy to do. Perhaps a future equation compiler, probably written in Lean, will do cleverer things like transforming <code>map</code> automatically.</p>


{% endraw %}
