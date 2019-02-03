---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/88373simpdisplaymode.html
---

## Stream: [new members](index.html)
### Topic: [simp display mode](88373simpdisplaymode.html)

---


{% raw %}
#### [ Andreas Swerdlow (Aug 06 2018 at 12:30)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/simp%20display%20mode/near/130969966):
<p>Is there some way of getting lean to show what lemmas simp used in a particular line? I added an include in my file and suddenly a lot of my simps don't do what they used to. I want to be able to see which lemmas it is now having problems with.</p>

#### [ Chris Hughes (Aug 06 2018 at 12:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/simp%20display%20mode/near/130970048):
<p><code>set_option trace.simplify.rewrite true</code></p>

#### [ Kevin Buzzard (Aug 06 2018 at 12:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/simp%20display%20mode/near/130970060):
<p>see my post from just now about \u m * n :-)</p>

#### [ Mario Carneiro (Aug 06 2018 at 12:33)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/simp%20display%20mode/near/130970090):
<p>you said "just click on <code>simp</code> and see" but I don't know what you mean by that</p>

#### [ Kevin Buzzard (Aug 06 2018 at 12:33)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/simp%20display%20mode/near/130970092):
<p>But that is slightly surprising. It might be that your include contained a lemma tagged <code>@[simp]</code> which is now being applied when it wasn't before. If you can locate the lemma then...I'm not sure you can untag it actually, but you can stop <code>simp</code> from using it and then hopefully sanity will be restored</p>

#### [ Kevin Buzzard (Aug 06 2018 at 12:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/simp%20display%20mode/near/130970096):
<p>Oh -- I'd put the <code>set_option</code> earlier</p>

#### [ Mario Carneiro (Aug 06 2018 at 12:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/simp%20display%20mode/near/130970153):
<p>you can only locally untag a simp lemma</p>

#### [ Andreas Swerdlow (Aug 06 2018 at 12:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/simp%20display%20mode/near/130970368):
<p><span class="user-mention" data-user-id="110044">@Chris Hughes</span>  thanks</p>

#### [ Andreas Swerdlow (Aug 06 2018 at 12:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/simp%20display%20mode/near/130970448):
<p>The offending include file is one of my own. So I tried untagging all of the simp lemmas in the source file but this did not solve the problem</p>

#### [ Kevin Buzzard (Aug 06 2018 at 12:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/simp%20display%20mode/near/130970698):
<p><a href="https://github.com/leanprover/mathlib/blob/master/docs/extras/simp.md#when-it-is-unadvisable-to-use-simp" target="_blank" title="https://github.com/leanprover/mathlib/blob/master/docs/extras/simp.md#when-it-is-unadvisable-to-use-simp">https://github.com/leanprover/mathlib/blob/master/docs/extras/simp.md#when-it-is-unadvisable-to-use-simp</a></p>

#### [ Kevin Buzzard (Aug 06 2018 at 12:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/simp%20display%20mode/near/130970809):
<p>If you're using <code>simp</code> in the middle of a proof, then you're asking for trouble. You should only use <code>simp</code> to close a goal. Although it's kind of annoying, if your goal is <code>A</code> and then <code>simp</code> turns it into <code>B</code>, you're supposed to write <code>suffices : B, simpa using this</code> or <code>simp [this]</code> or <code>simp!</code> or some other random incantation until <code>simp</code> eventually is convinced that it can prove that <code>B</code> implies <code>A</code>, and then go on. This makes imports far less likely to break code.</p>


{% endraw %}
