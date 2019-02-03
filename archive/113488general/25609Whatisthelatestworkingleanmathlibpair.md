---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/25609Whatisthelatestworkingleanmathlibpair.html
---

## Stream: [general](index.html)
### Topic: [What is the latest working (lean, mathlib) pair?](25609Whatisthelatestworkingleanmathlibpair.html)

---


{% raw %}
#### [ Ching-Tsun Chou (Mar 26 2018 at 01:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%20is%20the%20latest%20working%20%28lean%2C%20mathlib%29%20pair%3F/near/124203602):
<p>A pair of git commit ids would suffice.</p>
<p>Thanks!</p>

#### [ Simon Hudon (Mar 26 2018 at 01:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%20is%20the%20latest%20working%20%28lean%2C%20mathlib%29%20pair%3F/near/124203737):
<p>I haven't had much success updating in the last couple of days so I'm using:</p>
<div class="codehilite"><pre><span></span>Lean: 07bb7d809b6be49f38ce4e427c54a82708ae281f
mathlib: f7977ff5a6bcf7e5c54eec908364ceb40dafc795
</pre></div>


<p>It's from about 10 days ago and it doesn't include the latest monad changes</p>

#### [ Ching-Tsun Chou (Mar 26 2018 at 01:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%20is%20the%20latest%20working%20%28lean%2C%20mathlib%29%20pair%3F/near/124203882):
<p>Thanks!  I'll give them a try.</p>
<p>I wonder if the maintainer of mathlib (Mario?) can keep a record of which mathlib git commit matches which lean commit.  All that is needed is a lean commit id in the mathlib commit messages.</p>

#### [ Mario Carneiro (Mar 26 2018 at 01:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%20is%20the%20latest%20working%20%28lean%2C%20mathlib%29%20pair%3F/near/124203900):
<p>I'm checking out the last nightly (28f414) and I'll revert mathlib to work with it instead of HEAD, at least until the issues on lean repo are fixed</p>

#### [ Simon Hudon (Mar 26 2018 at 01:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%20is%20the%20latest%20working%20%28lean%2C%20mathlib%29%20pair%3F/near/124203943):
<p>It's a bit unusual for Lean and mathlib to be broken for this long. Normally, Mario keeps it working with the nightly build</p>

#### [ Ching-Tsun Chou (Mar 26 2018 at 01:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%20is%20the%20latest%20working%20%28lean%2C%20mathlib%29%20pair%3F/near/124203987):
<p>It doesn't really matter how long they are broken.  All we need is a record of which lean commit works with which mathlib commit.  The user can compile lean him/herself.  Thanks!</p>

#### [ Mario Carneiro (Mar 26 2018 at 01:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%20is%20the%20latest%20working%20%28lean%2C%20mathlib%29%20pair%3F/near/124203991):
<p>I usually keep it working with HEAD, and it doesn't make a big difference from nightly after a day</p>

#### [ Mario Carneiro (Mar 26 2018 at 01:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%20is%20the%20latest%20working%20%28lean%2C%20mathlib%29%20pair%3F/near/124203993):
<p>Usually leo is careful not to push a broken build, and certainly not leave it for several days like that</p>

#### [ Simon Hudon (Mar 26 2018 at 01:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%20is%20the%20latest%20working%20%28lean%2C%20mathlib%29%20pair%3F/near/124204003):
<p>I think they might be preparing for Lean 4</p>

#### [ Ching-Tsun Chou (Mar 26 2018 at 01:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%20is%20the%20latest%20working%20%28lean%2C%20mathlib%29%20pair%3F/near/124204046):
<p>Well, you guys would not have needed to spend the time to answer my questions if there is a record which I can look up myself.</p>

#### [ Mario Carneiro (Mar 26 2018 at 01:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%20is%20the%20latest%20working%20%28lean%2C%20mathlib%29%20pair%3F/near/124204054):
<p>The record is the relative commit times</p>

#### [ Ching-Tsun Chou (Mar 26 2018 at 02:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%20is%20the%20latest%20working%20%28lean%2C%20mathlib%29%20pair%3F/near/124204367):
<p>How do I find out what is the commit id of the latest lean nightly build?  The lean-nightly at <a href="https://leanprover.github.io/download/" target="_blank" title="https://leanprover.github.io/download/">https://leanprover.github.io/download/</a> currently points to something that is 3 weeks old (d6d44a19947e ).  The lean commit history does not say which commits are used in nightly builds.</p>

#### [ Mario Carneiro (Mar 26 2018 at 02:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%20is%20the%20latest%20working%20%28lean%2C%20mathlib%29%20pair%3F/near/124204414):
<p>The nightly build process is soon to change, with a better record of all this, but currently you can go to <a href="https://github.com/leanprover/lean-nightly/tree/gh-pages" target="_blank" title="https://github.com/leanprover/lean-nightly/tree/gh-pages">https://github.com/leanprover/lean-nightly/tree/gh-pages</a> and look at the commit that "bot botson" says in the commit message</p>

#### [ Mario Carneiro (Mar 26 2018 at 02:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%20is%20the%20latest%20working%20%28lean%2C%20mathlib%29%20pair%3F/near/124204420):
<p>I pushed a version of mathlib that works with it, so hopefully we will see the travis <span class="emoji emoji-1f44d" title="thumbs up">:thumbs_up:</span> soon</p>

#### [ Simon Hudon (Mar 26 2018 at 02:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%20is%20the%20latest%20working%20%28lean%2C%20mathlib%29%20pair%3F/near/124204513):
<p>That latest commit is about making it work with the latest nightly instead of HEAD, is that correct?</p>

#### [ Mario Carneiro (Mar 26 2018 at 02:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/What%20is%20the%20latest%20working%20%28lean%2C%20mathlib%29%20pair%3F/near/124204564):
<p>yes</p>


{% endraw %}
