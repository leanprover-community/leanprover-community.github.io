---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/06135Anglebrackets.html
---

## Stream: [new members](https://leanprover-community.github.io/archive/113489newmembers/index.html)
### Topic: [Angle brackets](https://leanprover-community.github.io/archive/113489newmembers/06135Anglebrackets.html)

---

<base href="https://leanprover.zulipchat.com">
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

#### [ Robert Spencer (Feb 04 2019 at 08:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Angle%20brackets/near/157504096):
<p>Hmmkay.  That's a little disappointing personally as I am loathe to install an IDE just for unicode support.</p>

#### [ Mario Carneiro (Feb 04 2019 at 08:18)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Angle%20brackets/near/157504689):
<p>I mean, if you can find another means to input the unicode, by all means go ahead, but it's certainly easiest to use an editor that supports unicode</p>

#### [ Mario Carneiro (Feb 04 2019 at 08:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Angle%20brackets/near/157504712):
<p>You don't really need an IDE - I hesitate to call the existing editors IDEs since they are mostly just error reporting and unicode input</p>

#### [ Mario Carneiro (Feb 04 2019 at 08:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Angle%20brackets/near/157504769):
<p>but presumably you use <em>some</em> text editor to write your files, and you can probably set it up to input the lean unicode characters</p>

#### [ Robert Spencer (Feb 04 2019 at 08:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Angle%20brackets/near/157505858):
<p>This is true.  I should just not be lazy and write some vimscript to translate <code>\forall</code> etc into unicode.</p>

#### [ Robert Spencer (Feb 04 2019 at 08:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Angle%20brackets/near/157505951):
<p>Although if it is the opinion of the maintainers that ASCII should not be preferred, it might be worth mentioning this in the tutorial document, and possibly throwing warnings that ASCII is deprecated (a bit more extreme)</p>

#### [ Patrick Massot (Feb 04 2019 at 08:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Angle%20brackets/near/157506093):
<p>You don't need any fancy vimscript, <code>imap</code> is all you need</p>


{% endraw %}
