---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/73983Magicdotinplaceofproof.html
---

## Stream: [new members](https://leanprover-community.github.io/archive/113489newmembers/index.html)
### Topic: [Magic dot in place of proof?](https://leanprover-community.github.io/archive/113489newmembers/73983Magicdotinplaceofproof.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Mark Dickinson (Nov 05 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Magic%20dot%20in%20place%20of%20proof%3F/near/146826913):
<p>Looking through the standard library, I see this in <code>basic.lean</code>:</p>
<div class="codehilite"><pre><span></span><span class="kn">lemma</span> <span class="n">not_succ_le_zero</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">),</span> <span class="n">succ</span> <span class="n">n</span> <span class="bp">≤</span> <span class="mi">0</span> <span class="bp">→</span> <span class="n">false</span>
<span class="bp">.</span>
</pre></div>


<p>What's the magic dot on the second line? Is this syntactic sugar for a particular tactic or set of tactics?</p>
<p>Source : <a href="https://github.com/leanprover/lean/blob/ceacfa7445953cbc8860ddabc55407430a9ca5c3/library/init/data/nat/basic.lean#L84-L85" target="_blank" title="https://github.com/leanprover/lean/blob/ceacfa7445953cbc8860ddabc55407430a9ca5c3/library/init/data/nat/basic.lean#L84-L85">https://github.com/leanprover/lean/blob/ceacfa7445953cbc8860ddabc55407430a9ca5c3/library/init/data/nat/basic.lean#L84-L85</a></p>

#### [ Scott Morrison (Nov 05 2018 at 22:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Magic%20dot%20in%20place%20of%20proof%3F/near/146826965):
<p>no, it just says "this is the end of the definition", and causes lean to realise that there are no cases to prove!</p>

#### [ Scott Morrison (Nov 05 2018 at 22:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Magic%20dot%20in%20place%20of%20proof%3F/near/146826976):
<p>magic. :-)</p>

#### [ Patrick Massot (Nov 05 2018 at 22:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Magic%20dot%20in%20place%20of%20proof%3F/near/146827317):
<p>See also <a href="#narrow/stream/113489-new-members/topic/what.20does.20.2E.20mean.20here.3F" title="#narrow/stream/113489-new-members/topic/what.20does.20.2E.20mean.20here.3F">https://leanprover.zulipchat.com/#narrow/stream/113489-new-members/topic/what.20does.20.2E.20mean.20here.3F</a></p>

#### [ Mark Dickinson (Nov 05 2018 at 22:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Magic%20dot%20in%20place%20of%20proof%3F/near/146827412):
<p>Ah, thank you! I did try searching the archives, but it's not easy to figure out how to search for a single period.</p>

#### [ Patrick Massot (Nov 05 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Magic%20dot%20in%20place%20of%20proof%3F/near/146827436):
<p>I searched for the name of this lemma, because I was pretty sure it was already discussed</p>

#### [ Mark Dickinson (Nov 05 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Magic%20dot%20in%20place%20of%20proof%3F/near/146827446):
<p>Yep, I should have thought to use <code>not_succ_le_zero</code> as a search term ..</p>

#### [ Patrick Massot (Nov 05 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Magic%20dot%20in%20place%20of%20proof%3F/near/146827451):
<p>And there are very few opportunities to use this trick</p>

#### [ Patrick Massot (Nov 05 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Magic%20dot%20in%20place%20of%20proof%3F/near/146827459):
<p>No problem</p>

#### [ Bryan Gin-ge Chen (Nov 06 2018 at 00:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Magic%20dot%20in%20place%20of%20proof%3F/near/146832913):
<p>I've sometimes found it useful when rewriting a proof,  e.g. instead of temporarily commenting out the rest of a proof, I just insert a <code>.</code>.</p>

#### [ Kevin Buzzard (Nov 06 2018 at 00:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Magic%20dot%20in%20place%20of%20proof%3F/near/146833077):
<p>I usually insert a <code>#exit</code></p>


{% endraw %}
