---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/28727simpasrw.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [simp as rw](https://leanprover-community.github.io/archive/113488general/28727simpasrw.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Ali Sever (Sep 15 2018 at 00:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20as%20rw/near/133984046):
<p>Recently I have come across many cases where rw cannot rewrite the thing I need it to. Usually simp can do the trick, but I know it's bad practice to not close a goal after using simp. I was wondering if it's ok to use <code>simp only</code> and not close a goal?<br>
Also, is there a reason rw cannot rewrite under lambdas, or stuff with type class inference (there probably is a good reason, most likely one I won't understand)?</p>

#### [ Ali Sever (Sep 15 2018 at 11:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20as%20rw/near/134003836):
<p>Same question for if <code>dsimp</code> is ok.</p>

#### [ Kevin Buzzard (Sep 15 2018 at 11:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20as%20rw/near/134003846):
<p>with <code>dsimp</code> there's a trick which Chris told me: you run <code>dsimp</code>, you see what it gives you, and then you remove the <code>dsimp</code> and replace it with <code>show &lt;output&gt;</code></p>

#### [ Kevin Buzzard (Sep 15 2018 at 11:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20as%20rw/near/134003890):
<p>Related: I am currently learning to turn my tactic mode proofs into term mode, because mathlib prefers brevity and I am trying to write code which can be put into mathlib. In term mode the <code>show</code> stuff can often be deleted completely.</p>

#### [ Kevin Buzzard (Sep 15 2018 at 11:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20as%20rw/near/134003901):
<p>I was inspired by watching Mario writing <code>noetherian.lean</code> in real time; I saw him finish a proof and then instead of moving on he would start editing it to make it as small as possible.</p>

#### [ Ali Sever (Sep 15 2018 at 11:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20as%20rw/near/134004035):
<p>Doesn't that make it harder to go back and change it if necessary?</p>

#### [ Kevin Buzzard (Sep 15 2018 at 11:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20as%20rw/near/134004170):
<p>the shorter it is, the less likely it will need to be changed</p>

#### [ Mario Carneiro (Sep 15 2018 at 11:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20as%20rw/near/134004180):
<p>a bit, depending on what needs changing. It's also a good skill to learn to take a term proof and insert probes and tactic blocks in the middle to find out what's going on</p>

#### [ Kevin Buzzard (Sep 15 2018 at 11:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20as%20rw/near/134004230):
<p>With this <code>simp</code> thing, the extra line that you're not happy about is exactly the clue that Lean needs in order to minimise the chances that it will need to be changed later.</p>

#### [ Kevin Buzzard (Sep 15 2018 at 11:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20as%20rw/near/134004238):
<p>Mario has a lot of experience in something I'm a complete novice at -- maintaining code. That's the next level up for me.</p>

#### [ Kevin Buzzard (Sep 15 2018 at 11:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/simp%20as%20rw/near/134004250):
<p>Currently I'm learning how to write code which is maintainable. But I'm trying to preach the basics to people like you Ali.</p>


{% endraw %}
