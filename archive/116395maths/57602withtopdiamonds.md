---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/57602withtopdiamonds.html
---

## Stream: [maths](index.html)
### Topic: [with_top "diamonds"](57602withtopdiamonds.html)

---


{% raw %}
#### [ Chris Hughes (Oct 25 2018 at 09:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/with_top%20%22diamonds%22/near/136461132):
<p>The following equality isn't <code>rfl</code>. I think it should be. I tried redefining the instances, because I thought it might have something to do with the issue that stopped <code>(0 : with_bot nat) = some 0</code> being definitional, but I couldn't get it to work </p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">:</span> <span class="bp">@</span><span class="n">with_top</span><span class="bp">.</span><span class="n">add_monoid</span> <span class="bp">ℕ</span> <span class="bp">_</span> <span class="bp">=</span> <span class="n">add_comm_monoid</span><span class="bp">.</span><span class="n">to_add_monoid</span> <span class="bp">_</span> <span class="o">:=</span> <span class="n">rfl</span>
</pre></div>

#### [ Johan Commelin (Oct 27 2018 at 07:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/with_top%20%22diamonds%22/near/136592348):
<p>Hmmm, since when is <code>(0 : with_bot nat) = some 0</code> no longer defeq? I know that things like that worked for <code>with_zero</code> a couple of weeks ago. You are just using a wrapper around <code>option</code> and the obvious coercion. This seems a bit surprising.</p>

#### [ Chris Hughes (Oct 27 2018 at 10:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/with_top%20%22diamonds%22/near/136598822):
<p>Ages ago it didn't work, but it's now fixed.</p>

#### [ Johan Commelin (Oct 27 2018 at 10:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/with_top%20%22diamonds%22/near/136598865):
<p>Ok, good!</p>

#### [ Chris Hughes (Oct 27 2018 at 13:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/with_top%20%22diamonds%22/near/136603200):
<p>Found a fix and PRed. <a href="https://github.com/leanprover/mathlib/issues/442" target="_blank" title="https://github.com/leanprover/mathlib/issues/442">#442</a></p>


{% endraw %}
