---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/26246Kleenenormalformtheorem.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [Kleene normal form theorem](https://leanprover-community.github.io/archive/113488general/26246Kleenenormalformtheorem.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Mario Carneiro (May 21 2018 at 17:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Kleene%20normal%20form%20theorem/near/126877954):
<p>Yay, milestone achieved. The statement that I actually proved shows that <code>eval : code -&gt; N -&gt;. N</code> which evaluates a partial recursive function given by a code, is itself a partial recursive function. This is also known as a universal Turing machine in the language of Turing machines.</p>

#### [ Patrick Massot (May 21 2018 at 18:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Kleene%20normal%20form%20theorem/near/126878601):
<p>Congratulations!</p>

#### [ Patrick Massot (May 21 2018 at 18:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Kleene%20normal%20form%20theorem/near/126878604):
<p>Do you plan to return to maths now?</p>

#### [ Mario Carneiro (May 21 2018 at 18:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Kleene%20normal%20form%20theorem/near/126878738):
<p>Lol this is math</p>

#### [ Mario Carneiro (May 21 2018 at 18:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Kleene%20normal%20form%20theorem/near/126878775):
<p>I'm aiming for proper computability theory at the moment, with r.e. sets and such</p>

#### [ Patrick Massot (May 21 2018 at 18:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Kleene%20normal%20form%20theorem/near/126878826):
<p>What is "r.e. sets"?</p>

#### [ Mario Carneiro (May 21 2018 at 18:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Kleene%20normal%20form%20theorem/near/126878833):
<p>recursively enumerable</p>

#### [ Mario Carneiro (May 21 2018 at 18:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Kleene%20normal%20form%20theorem/near/126878851):
<p>the set of turing machines that halt is a r.e. set</p>

#### [ Mario Carneiro (May 21 2018 at 18:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Kleene%20normal%20form%20theorem/near/126878866):
<p>but its complement isn't</p>

#### [ Sebastian Ullrich (May 21 2018 at 18:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Kleene%20normal%20form%20theorem/near/126878932):
<p>IOW the set of machines that reset is a r.e.set</p>

#### [ Patrick Massot (May 21 2018 at 18:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Kleene%20normal%20form%20theorem/near/126878969):
<p>Thanks</p>

#### [ Sebastian Ullrich (May 21 2018 at 18:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Kleene%20normal%20form%20theorem/near/126879054):
<p>This looks like a really nice development. Though I have to wonder what we did wrong when building leanpkg to encourage putting everything in a single monolithic package <span class="emoji emoji-1f604" title="smile">:smile:</span> .</p>

#### [ Mario Carneiro (May 21 2018 at 18:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Kleene%20normal%20form%20theorem/near/126879058):
<p>I want to finish the MDRP theorem I started last year</p>

#### [ Patrick Massot (May 21 2018 at 18:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Kleene%20normal%20form%20theorem/near/126880128):
<p>Sebastian: do you refer to mathlib here?</p>

#### [ Sebastian Ullrich (May 21 2018 at 21:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Kleene%20normal%20form%20theorem/near/126888386):
<p><span class="user-mention" data-user-id="110031">@Patrick Massot</span> Yes. Not that it's a real issue until we start prebuilding dependencies on <code>leanpkg configure</code>.</p>

#### [ Patrick Massot (May 21 2018 at 21:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Kleene%20normal%20form%20theorem/near/126888402):
<p>It seems it makes it easier for Mario and Johannes to guarantee a consistent mathlib</p>

#### [ Patrick Massot (May 21 2018 at 21:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Kleene%20normal%20form%20theorem/near/126888415):
<p>But I think we really need precompiled mathlib nightlies</p>


{% endraw %}
