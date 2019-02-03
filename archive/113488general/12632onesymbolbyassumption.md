---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/12632onesymbolbyassumption.html
---

## Stream: [general](index.html)
### Topic: [one-symbol "by assumption"](12632onesymbolbyassumption.html)

---


{% raw %}
#### [ Johan Commelin (Dec 27 2018 at 22:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/one-symbol%20%22by%20assumption%22/near/152620996):
<p>How would people feel about a 1-symbol version of <code>by assumption</code>? I now often have hypotheses with unenlightening names <code>H1</code> ... <code>H5</code>, and these labels are all over the place in my proofs. But they don't really convey any information. I could use the french quotes to tell Lean the type, and it will start looking for a fitting assumption. But often I find that pretty verbose. Because usually, it's just an annoying proof obligation that we want to get rid of. How about <code>!</code>, or maybe the unicode <code>…</code>?</p>

#### [ Patrick Massot (Dec 27 2018 at 22:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/one-symbol%20%22by%20assumption%22/near/152621153):
<p>I can see you are tempted by the SSReflect cabalistic road...</p>

#### [ Patrick Massot (Dec 27 2018 at 22:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/one-symbol%20%22by%20assumption%22/near/152621161):
<p>I think this is part of what SSReflect <code>//</code> does</p>

#### [ Johan Commelin (Dec 27 2018 at 22:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/one-symbol%20%22by%20assumption%22/near/152621256):
<blockquote>
<p>I can see you are tempted by the SSReflect cabalistic road...</p>
</blockquote>
<p>I know of a guild that doesn't write anything when it comes to these proof obligations... it's completely transparent to them.</p>

#### [ Patrick Massot (Dec 27 2018 at 22:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/one-symbol%20%22by%20assumption%22/near/152621713):
<p>Great, let's have a transparent unicode character! Let's take the one we use in real world math papers.</p>

#### [ Andrew Ashworth (Dec 27 2018 at 23:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/one-symbol%20%22by%20assumption%22/near/152623829):
<p>I am not a huge fan of this being a mathlib standard. Maybe in your personal code, you can make your own <code>meta def</code>, and then when you PR, you can search and replace?</p>

#### [ Andrew Ashworth (Dec 27 2018 at 23:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/one-symbol%20%22by%20assumption%22/near/152623896):
<p>Or a VSCode tab-completion when you start writing <code>by a</code></p>

#### [ Reid Barton (Dec 28 2018 at 00:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/one-symbol%20%22by%20assumption%22/near/152626746):
<p>If <code>H3</code> is uninformative, wouldn't <code>!</code> be even more uninformative?</p>

#### [ Reid Barton (Dec 28 2018 at 00:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/one-symbol%20%22by%20assumption%22/near/152626787):
<p>At least with <code>H3</code> the IDE will tell you the type</p>

#### [ Johan Commelin (Dec 28 2018 at 06:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/one-symbol%20%22by%20assumption%22/near/152637610):
<p>After a bit more thought, maybe the most most user-friendly version (both for reading and writing) would be to have a VScode keyboard shortcut that looks at the type of the current <code>_</code> and replaces it with <code>\f&lt; the_type \f&gt;</code>. It really is a pity that we can't invoke hole commands on bare <code>_</code>. Otherwise a hole command would be perfect.</p>

#### [ Mario Carneiro (Dec 28 2018 at 06:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/one-symbol%20%22by%20assumption%22/near/152638100):
<p>a simple available compromise is <code>\f&lt;_\f&gt;</code></p>

#### [ Mario Carneiro (Dec 28 2018 at 06:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/one-symbol%20%22by%20assumption%22/near/152638105):
<p>I would also be happy if <code>\f&lt;\f&gt;</code> worked but I think that requires a bit more parsing magic</p>

#### [ Reid Barton (Dec 28 2018 at 07:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/one-symbol%20%22by%20assumption%22/near/152638307):
<blockquote>
<p>After a bit more thought, maybe the most most user-friendly version (both for reading and writing) would be to have a VScode keyboard shortcut that looks at the type of the current <code>_</code> and replaces it with <code>\f&lt; the_type \f&gt;</code>. It really is a pity that we can't invoke hole commands on bare <code>_</code>. Otherwise a hole command would be perfect.</p>
</blockquote>
<p>I would agree with this. I imagine the VSCode extension could just replace the <code>_</code> with a <code>{! _ !}</code> and then invoke the hole command--we shouldn't be limited by Lean here.</p>

#### [ Mario Carneiro (Dec 28 2018 at 07:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/one-symbol%20%22by%20assumption%22/near/152638439):
<p>I would prefer it just replace the hole with a reference to the actual hypothesis</p>

#### [ Johan Commelin (Dec 28 2018 at 07:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/one-symbol%20%22by%20assumption%22/near/152638457):
<p>Why not the <code>\f&lt; the_type \f&gt;</code> version? It is less "Lean-explicit" but it is a whole lot more "math-explicit".</p>


{% endraw %}
