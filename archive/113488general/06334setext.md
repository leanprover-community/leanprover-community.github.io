---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/06334setext.html
---

## Stream: [general](index.html)
### Topic: [setext](06334setext.html)

---


{% raw %}
#### [ Patrick Massot (Apr 16 2018 at 18:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/setext/near/125155122):
<p>Core lib has a <code>funext</code> tactic which allows to replace <code>apply funext, intro x</code> by <code>funext x</code>. Would it be a good idea to copy the definition of this tactic to get a <code>setext</code> tactic?</p>

#### [ Kenny Lau (Apr 16 2018 at 18:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/setext/near/125155142):
<p>the <code>funext</code> tactic is really <code>repeat {apply funext, intro x}</code> though</p>

#### [ Kenny Lau (Apr 16 2018 at 18:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/setext/near/125155159):
<p>but right, <code>set.ext</code> can only be used once</p>

#### [ Kenny Lau (Apr 16 2018 at 18:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/setext/near/125155166):
<p>well you can just set <code>setext</code> to be <code>apply set.ext; intro x</code></p>

#### [ Patrick Massot (Apr 16 2018 at 18:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/setext/near/125155173):
<p>I want <code>x</code> to be an argument of the tactic</p>

#### [ Kenny Lau (Apr 16 2018 at 18:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/setext/near/125155215):
<p>sure</p>

#### [ Patrick Massot (Apr 16 2018 at 18:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/setext/near/125155220):
<p>It's mostly a cosmetic question, but also about consistency</p>

#### [ Patrick Massot (Apr 16 2018 at 18:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/setext/near/125155225):
<p>Because I keep trying <code>setext x</code> before remembering it doesn't work yet</p>

#### [ Mario Carneiro (Apr 16 2018 at 19:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/setext/near/125158190):
<p><span class="user-mention" data-user-id="110026">@Simon Hudon</span> I recall discussing a generic <code>ext</code> tactic as a complement to the <code>monotonicity</code> tactic, perhaps it would help here</p>

#### [ Simon Hudon (Apr 16 2018 at 19:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/setext/near/125158338):
<p>Yes, I have it in <code>lean-lib</code>. I can create a pull request. I have a <code>extensionality</code> attribute that I used to tag extentionality on sets, stream and maybe other things too</p>

#### [ Patrick Massot (Apr 16 2018 at 22:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/setext/near/125164007):
<p>nice</p>

#### [ Simon Hudon (Apr 16 2018 at 22:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/setext/near/125166265):
<p>I just submitted a pull request: <a href="https://github.com/leanprover/mathlib/pull/104" target="_blank" title="https://github.com/leanprover/mathlib/pull/104">https://github.com/leanprover/mathlib/pull/104</a></p>

#### [ Simon Hudon (Apr 16 2018 at 22:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/setext/near/125166322):
<p>In tests/examples.lean you should see a bunch of situations where <code>ext</code> is useful.</p>

#### [ Simon Hudon (Apr 16 2018 at 22:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/setext/near/125166324):
<p>Let me know if you think there should be more extensionality lemmas</p>

#### [ Patrick Massot (Apr 16 2018 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/setext/near/125166339):
<p>Thanks!</p>

#### [ Patrick Massot (Apr 16 2018 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/setext/near/125166347):
<p>Can you give it names like with funext?</p>

#### [ Patrick Massot (Apr 16 2018 at 22:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/setext/near/125166423):
<p>Oh, you put sorries in tests again <span class="emoji emoji-1f61e" title="disappointed">:disappointed:</span></p>

#### [ Simon Hudon (Apr 16 2018 at 22:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/setext/near/125166431):
<p>Yes. <code>ext</code> will apply all extensionality lemmas that make sense while <code>ext a b c</code> will only apply three (not necessarily the same) and name the introduced locals <code>a</code>,<code>b</code>, <code>c</code>,</p>

#### [ Patrick Massot (Apr 16 2018 at 22:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/setext/near/125166439):
<p>What is this <code>ext1</code> I see in tests? Apply it only once?</p>

#### [ Patrick Massot (Apr 16 2018 at 22:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/setext/near/125166442):
<p>like <code>congr_n 1</code>?</p>

#### [ Simon Hudon (Apr 16 2018 at 22:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/setext/near/125166443):
<p>It shouldn't affect the built because the final proof is just <code>trivial</code></p>

#### [ Patrick Massot (Apr 16 2018 at 22:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/setext/near/125166448):
<p>Ahah</p>

#### [ Simon Hudon (Apr 16 2018 at 22:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/setext/near/125166506):
<p>I don't know of <code>congr_n 1</code> but it sounds like you got the right idea</p>

#### [ Simon Hudon (Apr 16 2018 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/setext/near/125166536):
<p>(I'm so glad <code>congr_n</code> exists! I'll be able to use that now!)</p>

#### [ Patrick Massot (Apr 16 2018 at 23:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/setext/near/125166606):
<p>I was looking to my mathlib tactics docs to point to and, shame on me, I didn't include congr_n! <span class="emoji emoji-1f61e" title="disappointed">:disappointed:</span></p>

#### [ Simon Hudon (Apr 16 2018 at 23:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/setext/near/125166620):
<p><em>shake head in  disapproval</em></p>

#### [ Simon Hudon (Apr 16 2018 at 23:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/setext/near/125166733):
<p>Would it be useful to have a <code>monoid</code> and <code>add_monoid</code> instance for <code>fin n</code> in <code>mathlib</code>?</p>

#### [ Patrick Massot (Apr 16 2018 at 23:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/setext/near/125166871):
<p>What would be the law? Again some truncation thing?</p>

#### [ Simon Hudon (Apr 16 2018 at 23:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/setext/near/125166894):
<p>Yes. It would be modulo arithmetic with the modulo baked into the type</p>

#### [ Patrick Massot (Apr 16 2018 at 23:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/setext/near/125166943):
<p>Oh, modulo</p>

#### [ Patrick Massot (Apr 16 2018 at 23:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/setext/near/125166948):
<p>That's a bit sneaky</p>

#### [ Patrick Massot (Apr 16 2018 at 23:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/setext/near/125166951):
<p><a href="https://github.com/leanprover/mathlib/pull/105" target="_blank" title="https://github.com/leanprover/mathlib/pull/105">https://github.com/leanprover/mathlib/pull/105</a></p>

#### [ Simon Hudon (Apr 16 2018 at 23:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/setext/near/125166987):
<p>What kind of sneaky? Evil-sneaky or just effective-sneaky?</p>

#### [ Patrick Massot (Apr 16 2018 at 23:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/setext/near/125167052):
<p>I don't know. People could be taken off guard. But who would want to add elements of <code>fin n</code> anyway?</p>

#### [ Simon Hudon (Apr 16 2018 at 23:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/setext/near/125167066):
<p>After a quick survey, there's me</p>

#### [ Simon Hudon (Apr 16 2018 at 23:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/setext/near/125167146):
<p>The other alternative I see is the <code>p ≡ q [MOD k]</code> notation but that looks more restricted. <code>fin n</code> is usable in other contexts that congruences or equalities.</p>

#### [ Patrick Massot (Apr 16 2018 at 23:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/setext/near/125167210):
<p>I notice your ext PR doesn't include documentation <span class="emoji emoji-1f612" title="unamused">:unamused:</span></p>

#### [ Simon Hudon (Apr 16 2018 at 23:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/setext/near/125167238):
<p>What's this <code>documentation</code> thing?</p>

#### [ Simon Hudon (Apr 16 2018 at 23:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/setext/near/125167272):
<p>Alright, I'll add a comment :)</p>

#### [ Simon Hudon (Apr 16 2018 at 23:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/setext/near/125167274):
<p>Is that better?</p>

#### [ Patrick Massot (Apr 16 2018 at 23:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/setext/near/125167328):
<p>By the way, you told me we found a bug in <code>wlog</code> when I asked questions about it. Did you manage to fix it?</p>

#### [ Simon Hudon (Apr 16 2018 at 23:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/setext/near/125167358):
<p>That's true! I forgot about it. It was pretty tricky. I'll get back to it.</p>

#### [ Simon Hudon (Apr 16 2018 at 23:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/setext/near/125167362):
<p>Sorry for the delay</p>

#### [ Patrick Massot (Apr 16 2018 at 23:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/setext/near/125167372):
<p>Adding a docstring to <code>tactic/interactive.lean</code> would be good enough. Then I can copy it to tactic.md</p>

#### [ Patrick Massot (Apr 16 2018 at 23:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/setext/near/125167378):
<p>But in this case I could also write the docstring I guess</p>

#### [ Patrick Massot (Apr 16 2018 at 23:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/setext/near/125167422):
<p>The problem is I could write nonsense</p>

#### [ Patrick Massot (Apr 16 2018 at 23:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/setext/near/125167447):
<p>There is no delay problem with wlog, I was only asking so you don't forget</p>

#### [ Simon Hudon (Apr 16 2018 at 23:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/setext/near/125167472):
<p>Thanks for reminding me</p>

#### [ Patrick Massot (Apr 16 2018 at 23:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/setext/near/125167513):
<p>Speaking of documentation, I wonder if <span class="user-mention" data-user-id="110024">@Sebastian Ullrich</span>  of <span class="user-mention" data-user-id="110043">@Gabriel Ebner</span>  could answer Kevin's questions in <a href="https://github.com/leanprover/mathlib/blob/master/docs/extras/calc.md" target="_blank" title="https://github.com/leanprover/mathlib/blob/master/docs/extras/calc.md">https://github.com/leanprover/mathlib/blob/master/docs/extras/calc.md</a> (you only need to search for "Kevin" in this file)</p>

#### [ Simon Hudon (Apr 16 2018 at 23:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/setext/near/125167526):
<p>I'll write both no worries. I was joking.</p>

#### [ Kevin Buzzard (Apr 16 2018 at 23:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/setext/near/125167620):
<p>I'm not at a computer right now, but IIRC I think <code>fin n</code> already has an <code>+</code> but it is not very well behaved!</p>

#### [ Simon Hudon (Apr 16 2018 at 23:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/setext/near/125167632):
<p>Actually, I think <code>-</code> is more problematic. And we don't have laws for them</p>

#### [ Kevin Buzzard (Apr 16 2018 at 23:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/setext/near/125167676):
<p>My memory is that these structures on <code>fin n</code> are defined in core and didn't make it into a sensible mathematical object</p>

#### [ Kevin Buzzard (Apr 16 2018 at 23:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/setext/near/125167682):
<p>I think 2+2 wasn't 2-2 in fin 4 for example</p>

#### [ Kevin Buzzard (Apr 16 2018 at 23:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/setext/near/125167702):
<p>Docs -- yes I'd forgotten I'd left those in!</p>

#### [ Patrick Massot (Apr 16 2018 at 23:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/setext/near/125167708):
<p><code>#reduce (2 : fin 4) - (2 : fin 4)  -- ⟨0, _⟩</code></p>

#### [ Patrick Massot (Apr 16 2018 at 23:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/setext/near/125167749):
<p><code>#reduce (2 : fin 4) + (2 : fin 4)  -- ⟨0, _⟩</code></p>

#### [ Kevin Buzzard (Apr 16 2018 at 23:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/setext/near/125167753):
<p>Try 1+2 and 1-2</p>

#### [ Kevin Buzzard (Apr 16 2018 at 23:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/setext/near/125167755):
<p>Maybe that was it</p>

#### [ Patrick Massot (Apr 16 2018 at 23:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/setext/near/125167764):
<p>1+2 is 3 and 1 - 2 is 0</p>

#### [ Kevin Buzzard (Apr 16 2018 at 23:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/setext/near/125167765):
<p>2+2=0 so adding 2 and subtracting 2 should be the same</p>

#### [ Kevin Buzzard (Apr 16 2018 at 23:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/setext/near/125167772):
<p>Thanks</p>

#### [ Patrick Massot (Apr 16 2018 at 23:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/setext/near/125167773):
<p>hard to tell what is the rule here</p>

#### [ Patrick Massot (Apr 16 2018 at 23:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/setext/near/125167779):
<p>it seems substration is truncated at zero</p>

#### [ Kevin Buzzard (Apr 16 2018 at 23:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/setext/near/125167781):
<p>Subtracting is just subtraction on nat I think</p>

#### [ Patrick Massot (Apr 16 2018 at 23:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/setext/near/125167782):
<p>and addition wraps</p>

#### [ Kevin Buzzard (Apr 16 2018 at 23:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/setext/near/125167821):
<p>Right</p>

#### [ Kevin Buzzard (Apr 16 2018 at 23:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/setext/near/125167829):
<p>Does that make it a monoid?</p>

#### [ Kevin Buzzard (Apr 16 2018 at 23:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/setext/near/125167831):
<p><span class="emoji emoji-1f642" title="simple smile">:simple_smile:</span></p>

#### [ Patrick Massot (Apr 16 2018 at 23:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/setext/near/125167835):
<p>I think I remember reading this discussion in the past</p>

#### [ Kevin Buzzard (Apr 16 2018 at 23:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/setext/near/125167837):
<p>Right</p>

#### [ Simon Hudon (Apr 16 2018 at 23:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/setext/near/125167845):
<p>What was the conclusion?</p>

#### [ Patrick Massot (Apr 16 2018 at 23:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/setext/near/125167896):
<p>Current definitions are... odd</p>

#### [ Kenny Lau (Apr 20 2018 at 07:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/setext/near/125341724):
<p><a href="https://github.com/leanprover/mathlib/pull/109/commits" target="_blank" title="https://github.com/leanprover/mathlib/pull/109/commits">https://github.com/leanprover/mathlib/pull/109/commits</a></p>

#### [ Kenny Lau (Apr 20 2018 at 07:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/setext/near/125341725):
<p>ext is in PR</p>


{% endraw %}
