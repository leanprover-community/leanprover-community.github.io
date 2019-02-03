---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/71650tidyholecommand.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [tidy hole command](https://leanprover-community.github.io/archive/113488general/71650tidyholecommand.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Johan Commelin (Sep 03 2018 at 19:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20hole%20command/near/133272160):
<p><span class="user-mention" data-user-id="110524">@Scott Morrison</span> The tidy hole command is really marvellous. Here are some trivialities that might give epsilon improvement:<br>
(1) If <code>tidy</code> generates the proof <code>begin refl end</code>, generate <code>rfl</code> instead.<br>
(2) If <code>tidy</code> generates the proof <code>begin exact foo end</code>, generate <code>foo</code> instead.</p>

#### [ Scott Morrison (Sep 03 2018 at 22:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20hole%20command/near/133276810):
<p><span class="user-mention" data-user-id="112680">@Johan Commelin</span>, the first is impossible, or rather useless: Lean actually decides _in the parser_ whether you not you proved by <code>rfl</code>, rather than inspecting the proof term!</p>

#### [ Scott Morrison (Sep 03 2018 at 22:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20hole%20command/near/133276820):
<p>But (2) will go on my todo list. (i.e. I'll leave your message starred :-)</p>

#### [ Johan Commelin (Sep 03 2018 at 22:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20hole%20command/near/133276825):
<p>No, I mean that you inspect the string you are about to return.</p>

#### [ Johan Commelin (Sep 03 2018 at 22:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20hole%20command/near/133276866):
<p>The hole command returns some string, and VScode substitutes that for the hole. Is that right?</p>

#### [ Scott Morrison (Sep 03 2018 at 22:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20hole%20command/near/133276869):
<p>Ah, okay. Absolutely, I can do that.</p>

#### [ Johan Commelin (Sep 03 2018 at 22:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20hole%20command/near/133276870):
<p>If that string is exactly <code>begin refl end</code>, then you might as well output <code>rfl</code> instead.</p>

#### [ Kenny Lau (Sep 03 2018 at 22:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20hole%20command/near/133276875):
<p>by induction convert tactic proofs to term proofs</p>

#### [ Scott Morrison (Sep 03 2018 at 22:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20hole%20command/near/133276879):
<p>I can also have "begin just_one_tactic end" into "by just_one_tactic".</p>

#### [ Patrick Massot (Sep 03 2018 at 22:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20hole%20command/near/133276880):
<p>I think <code>refl</code> tries slightly harder than <code>rfl</code></p>

#### [ Johan Commelin (Sep 03 2018 at 22:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20hole%20command/near/133276882):
<p>That's somewhere on the VScode extension wishlist</p>

#### [ Johan Commelin (Sep 03 2018 at 22:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20hole%20command/near/133276940):
<blockquote>
<p>I think <code>refl</code> tries slightly harder than <code>rfl</code></p>
</blockquote>
<p>Hmmm... that might be true. So maybe we need to slightly patch tidy, to first try <code>exact rfl</code>. Then (1) will be a special case of (2).</p>

#### [ Johan Commelin (Sep 03 2018 at 22:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20hole%20command/near/133276948):
<p>Anyway, this is not high priority stuff.</p>

#### [ Chris Hughes (Sep 03 2018 at 22:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20hole%20command/near/133277149):
<p><code>refl</code> works for any reflexive relation I think. <code>rfl</code> is just equality.</p>

#### [ Patrick Massot (Sep 03 2018 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20hole%20command/near/133277163):
<p>I think it also does more definitional reduction</p>

#### [ Chris Hughes (Sep 03 2018 at 22:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tidy%20hole%20command/near/133277646):
<p>Can you give an example? If I prove something with <code>by refl</code>, the proof term is just <code>eq.refl _</code> which is <code>rfl</code></p>


{% endraw %}
