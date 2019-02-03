---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/57510Henselslemma.html
---

## Stream: [maths](https://leanprover-community.github.io/archive/116395maths/index.html)
### Topic: [Hensel's lemma](https://leanprover-community.github.io/archive/116395maths/57510Henselslemma.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Johan Commelin (Sep 11 2018 at 19:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Hensel%27s%20lemma/near/133747941):
<p><span class="user-mention" data-user-id="110596">@Rob Lewis</span> has PR'd Hensel's lemma for the p-adics! <span class="emoji emoji-1f389" title="tada">:tada:</span> <span class="emoji emoji-1f419" title="octopus">:octopus:</span> <span class="emoji emoji-1f4aa" title="muscle">:muscle:</span><br>
<a href="https://github.com/leanprover/mathlib/pull/337/files?w=1" target="_blank" title="https://github.com/leanprover/mathlib/pull/337/files?w=1">https://github.com/leanprover/mathlib/pull/337/files?w=1</a></p>

#### [ Johan Commelin (Sep 11 2018 at 19:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Hensel%27s%20lemma/near/133747982):
<p>Rob, would you mind sharing a bit of your long term plans? It seems like you project and the perfectoid project could strengthen each other.</p>

#### [ Johan Commelin (Sep 11 2018 at 19:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Hensel%27s%20lemma/near/133748063):
<p>I'm really excited to see all this stuff materialising.</p>

#### [ Kevin Buzzard (Sep 11 2018 at 19:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Hensel%27s%20lemma/near/133748199):
<p>In terms of what is needed to do modern mathematics I guess one has to plough through Serre's book on local fields</p>

#### [ Rob Lewis (Sep 11 2018 at 20:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Hensel%27s%20lemma/near/133750674):
<p>There's not so much of a long term plan right now. I've just been talking to Sander Dahmen about what we'll need to start formalizing his work, like we promised in the Lean Forward project. This seemed like a good place to start.</p>

#### [ Johan Commelin (Sep 11 2018 at 20:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Hensel%27s%20lemma/near/133750700):
<p>It definitely is.</p>

#### [ Rob Lewis (Sep 11 2018 at 20:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Hensel%27s%20lemma/near/133750750):
<p>Short term, I want to see what I can do about cleaning up some of the annoying inequality proofs in that PR.</p>

#### [ Johan Commelin (Sep 11 2018 at 20:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Hensel%27s%20lemma/near/133750776):
<p>I am not intimately familiar with Sanders work, but I do worry a tiny little bit that in the near future you might need to do a lot of this again for completions of number fields.</p>

#### [ Rob Lewis (Sep 11 2018 at 20:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Hensel%27s%20lemma/near/133750781):
<p>I'm sure there's plenty of overlap between Lean Forward and the perfectoid project, maybe we could get everyone together and chat sometime.</p>

#### [ Johan Commelin (Sep 11 2018 at 20:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Hensel%27s%20lemma/near/133750813):
<p>I think starting from a slightly more general perspective might pay off in the long run.</p>

#### [ Johan Commelin (Sep 11 2018 at 20:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Hensel%27s%20lemma/near/133750841):
<p>Let me put it like this: I would be very surprised if the only local rings in Sanders work are p-adics. I would expect to also find finite extensions of those.</p>

#### [ Johan Commelin (Sep 11 2018 at 20:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Hensel%27s%20lemma/near/133750853):
<p>And usually the proofs are almost the same difficulty.</p>

#### [ Johan Commelin (Sep 11 2018 at 20:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Hensel%27s%20lemma/near/133750906):
<p>This is absolutely not meant as criticism.</p>

#### [ Patrick Massot (Sep 11 2018 at 22:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Hensel%27s%20lemma/near/133757316):
<blockquote>
<p>Short term, I want to see what I can do about cleaning up some of the annoying inequality proofs in that PR.</p>
</blockquote>
<p>Did you have a look at Simon's mono tactic? It's not yet merged but it's in the nursery</p>

#### [ Patrick Massot (Sep 11 2018 at 22:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Hensel%27s%20lemma/near/133757562):
<p><span class="user-mention" data-user-id="110596">@Rob Lewis</span> would you mind documenting your p-adic work somewhere in <a href="https://github.com/leanprover/mathlib/tree/master/docs/theories" target="_blank" title="https://github.com/leanprover/mathlib/tree/master/docs/theories">https://github.com/leanprover/mathlib/tree/master/docs/theories</a>?</p>

#### [ Johan Commelin (Sep 12 2018 at 11:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Hensel%27s%20lemma/near/133786975):
<p><span class="user-mention" data-user-id="110596">@Rob Lewis</span> Thanks for the documentation!</p>


{% endraw %}
