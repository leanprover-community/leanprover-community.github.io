---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/64142aorborcord.html
---

## Stream: [general](index.html)
### Topic: [a or b or c or d](64142aorborcord.html)

---


{% raw %}
#### [ Chris Hughes (Aug 04 2018 at 21:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20or%20b%20or%20c%20or%20d/near/130900638):
<p>If I have <code>a or b or c or d</code>, can I split into four goals in one go?</p>

#### [ Kenny Lau (Aug 04 2018 at 21:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20or%20b%20or%20c%20or%20d/near/130900640):
<p><code>rcases [identifier] with H | H | H | H</code></p>

#### [ Kenny Lau (Aug 04 2018 at 21:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20or%20b%20or%20c%20or%20d/near/130900647):
<p>I can't interpret "split into four goals". If it's a hypothesis then you get four hypotheses. If it's a goal then you get one goal.</p>

#### [ Simon Hudon (Aug 04 2018 at 21:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20or%20b%20or%20c%20or%20d/near/130900700):
<p>Alternatively, <code>casesm* [_ ∨ _]</code> also helps.</p>

#### [ Chris Hughes (Aug 04 2018 at 21:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20or%20b%20or%20c%20or%20d/near/130900707):
<p>Thanks</p>

#### [ Mario Carneiro (Aug 04 2018 at 21:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20or%20b%20or%20c%20or%20d/near/130900812):
<p>there is no brackets in <code>rcases</code></p>

#### [ Kenny Lau (Aug 04 2018 at 21:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20or%20b%20or%20c%20or%20d/near/130900816):
<p><code>[identifier]</code> is a placeholder</p>

#### [ Mario Carneiro (Aug 04 2018 at 21:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20or%20b%20or%20c%20or%20d/near/130900836):
<p>hm, it's hard to tell the difference between meta notation and lean notation... we need more brackets</p>
<div class="codehilite"><pre><span></span>rcases ⟅identifier⟆ with H | H | H | H
</pre></div>

#### [ Ali Sever (Aug 05 2018 at 00:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20or%20b%20or%20c%20or%20d/near/130906775):
<p>On a similar note, if you want to prove <code>∃ a b c,  ...</code> is there a way to do something like <code>existsi a b c</code>? I tried<code>repeat {constructor}</code> for fun, and I was surprised to see lean perfectly guess what a, b and c were.</p>

#### [ Ali Sever (Aug 05 2018 at 00:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20or%20b%20or%20c%20or%20d/near/130906828):
<p>Also, when I used <code>constructor,</code> three times, lean did not guess them.</p>

#### [ Simon Hudon (Aug 05 2018 at 00:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20or%20b%20or%20c%20or%20d/near/130906831):
<p>you could also do <code>existsi [a,b,c]</code> if you want to specify the witnesses yourself.</p>

#### [ Ali Sever (Aug 05 2018 at 01:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20or%20b%20or%20c%20or%20d/near/130907028):
<p>Ah thank you, I had not tried those brackets. Is there a rule to know which type is used where?</p>

#### [ Simon Hudon (Aug 05 2018 at 01:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20or%20b%20or%20c%20or%20d/near/130907038):
<p>Which types do you mean?</p>

#### [ Kevin Buzzard (Aug 05 2018 at 01:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20or%20b%20or%20c%20or%20d/near/130907080):
<p>which type of bracket?</p>

#### [ Kevin Buzzard (Aug 05 2018 at 01:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20or%20b%20or%20c%20or%20d/near/130907085):
<p>I guess you can look at the documentation for the tactic...</p>

#### [ Kevin Buzzard (Aug 05 2018 at 01:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20or%20b%20or%20c%20or%20d/near/130907087):
<p>(by hovering over it)</p>

#### [ Nicholas Scheel (Aug 05 2018 at 01:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20or%20b%20or%20c%20or%20d/near/130907138):
<p>brackets are syntax, so I don‘t think they can have _types_, nor kinds, nor sorts ... must be varieties, I guess? ;)</p>

#### [ Nicholas Scheel (Aug 05 2018 at 01:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20or%20b%20or%20c%20or%20d/near/130907192):
<p>we’re going to run out of variants of words soon to describe these things</p>


{% endraw %}
