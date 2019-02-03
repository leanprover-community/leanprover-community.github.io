---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/45095assumptions.html
---

## Stream: [new members](index.html)
### Topic: [assumptions](45095assumptions.html)

---


{% raw %}
#### [ Geoffrey Yeung (Jan 21 2019 at 21:11)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/assumptions/near/156558856):
<p>is there something similar to <code>meta def assumptions : tactic unit := `[ repeat { assumption } ]</code> somewhere in the library?</p>

#### [ Chris Hughes (Jan 21 2019 at 21:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/assumptions/near/156560625):
<p><code>; assumption</code></p>

#### [ Bryan Gin-ge Chen (Jan 21 2019 at 22:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/assumptions/near/156561395):
<p>What about <code>assumption'</code>?</p>

#### [ Wojciech Nawrocki (Jan 21 2019 at 22:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/assumptions/near/156562900):
<p>Isn't <code>; assumption</code>, which applies once to every goal different from <code>repeat {assumption}</code>, which applies until it fails? <code>assumption'</code> also seems to do the former</p>

#### [ Geoffrey Yeung (Jan 21 2019 at 22:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/assumptions/near/156563787):
<p>I just learned about <code>;</code>. In mosts cases I can replace <code>assumptions</code> with <code>; assumption</code>, but in a few places I need <code>; try {assumption}</code> instead, because some branches need furthur processing</p>

#### [ Rob Lewis (Jan 21 2019 at 22:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/assumptions/near/156563836):
<p><code>assumption</code> fails when the goal can't be closed by something in the local context. So <code>repeat {assumption}</code> will close the first goals until it finds one that can't be closed. <code>; assumption</code> will succeed if every subgoal produced by the previous tactic can be closed by <code>assumption</code>, and fail otherwise. <code>assumption'</code> will close all open goals that can be closed by <code>assumption</code>, and fail if none of them can be closed.</p>

#### [ Rob Lewis (Jan 21 2019 at 22:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/assumptions/near/156563928):
<p>They're all subtly different. But I guess <code>repeat {assumption}</code> is rarely the one you want.</p>

#### [ Geoffrey Yeung (Jan 21 2019 at 22:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/assumptions/near/156564007):
<p>yeah <code>assumption'</code> seems to be the solution</p>

#### [ Rob Lewis (Jan 21 2019 at 22:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/assumptions/near/156564011):
<p><code>; assumption'</code> should have the same effect as <code>; try {assumption}</code>.</p>

#### [ Geoffrey Yeung (Jan 21 2019 at 22:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/assumptions/near/156564038):
<p>side question: why does<br>
<code>example {a b c : Prop} : a → b → c → (a ∧ b) ∧ c := by { intros , repeat{ split } ; assumption }</code> work, but<br>
<code>example {a b c : Prop} : a → b → c → (a ∧ b) ∧ c := by { intros , split , split ; assumption }</code> doesn't?</p>

#### [ Geoffrey Yeung (Jan 21 2019 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/assumptions/near/156564127):
<p>oh never mind figured it out, the <code>;</code> is only applying to the second split</p>


{% endraw %}
