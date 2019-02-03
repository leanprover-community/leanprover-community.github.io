---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/06135Anglebrackets.html
---

## Stream: [new members](index.html)
### Topic: [Angle brackets](06135Anglebrackets.html)

---


{% raw %}
#### [ Robert Spencer (Feb 01 2019 at 17:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Angle%20brackets/near/157364494):
<p>Are <code>(| ... |)</code> and <code>⟨ ... ⟩</code> meant to be treated identically by lean?</p>

#### [ Robert Spencer (Feb 01 2019 at 17:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Angle%20brackets/near/157364977):
<p>In particular, I have a case where <code>or.inr ⟨a, b⟩</code> works as expected, but <code>or.inr (|a, b|)</code> does not (it does though if I write <code>or.inr ( (|a, b|) )</code>.</p>

#### [ Simon Hudon (Feb 01 2019 at 17:31)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Angle%20brackets/near/157365234):
<p>That is curious. <span class="user-mention" data-user-id="110024">@Sebastian Ullrich</span>, is this normal?</p>

#### [ Sebastian Ullrich (Feb 01 2019 at 17:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Angle%20brackets/near/157365782):
<p>It looks like <code>(|</code> is missing the precedence from <code>⟨</code></p>

#### [ Sebastian Ullrich (Feb 01 2019 at 17:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Angle%20brackets/near/157365789):
<p>i.e. it's a bug</p>

#### [ Simon Hudon (Feb 01 2019 at 17:44)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Angle%20brackets/near/157366189):
<p>Is it worth fixing?</p>

#### [ Robert Spencer (Feb 01 2019 at 17:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Angle%20brackets/near/157366944):
<p>Well, I'll file an issue, and then people can decide.</p>

#### [ Mario Carneiro (Feb 01 2019 at 21:11)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Angle%20brackets/near/157381995):
<p>issues at lean repo are dead on arrival for the most part. Everything I have seen suggests that lean ascii support is half-hearted at best and has several issues, and seems like one of those things that is more likely to be dropped than fixed in lean 4</p>

#### [ Mario Carneiro (Feb 01 2019 at 21:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Angle%20brackets/near/157382079):
<p>I recommend getting used to the angle brackets</p>

#### [ Patrick Massot (Feb 01 2019 at 21:18)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Angle%20brackets/near/157382482):
<p>This <code>(| ... |)</code> is a nightmare for mathematicians who want to use <code>|</code> for absolute values. I really really hope Lean 4 drops it</p>


{% endraw %}
