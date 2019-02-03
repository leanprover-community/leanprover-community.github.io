---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/70396Provefalsefromnottrue.html
---

## Stream: [new members](index.html)
### Topic: [Prove false from not true?](70396Provefalsefromnottrue.html)

---


{% raw %}
#### [ Abhimanyu Pallavi Sudhir (Oct 05 2018 at 23:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Prove%20false%20from%20not%20true%3F/near/135283394):
<p>Hi, I have an elementary question -- I'm proving something, and am down to having the proved statement "¬true", and the goal is "false". Is there a quick way to finish this?</p>

#### [ Andrew Ashworth (Oct 05 2018 at 23:38)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Prove%20false%20from%20not%20true%3F/near/135283461):
<p>are you in term mode or tactic mode?</p>

#### [ Kenny Lau (Oct 05 2018 at 23:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Prove%20false%20from%20not%20true%3F/near/135283469):
<p>if <code>h : ¬true</code> then <code>exact h trivial</code></p>

#### [ Abhimanyu Pallavi Sudhir (Oct 05 2018 at 23:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Prove%20false%20from%20not%20true%3F/near/135283500):
<p>Oh ok -- thanks, that works.</p>

#### [ Abhimanyu Pallavi Sudhir (Oct 05 2018 at 23:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Prove%20false%20from%20not%20true%3F/near/135284011):
<p>By the way, is there a statement that automatically proves the goal "true"?</p>

#### [ Abhimanyu Pallavi Sudhir (Oct 05 2018 at 23:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Prove%20false%20from%20not%20true%3F/near/135284074):
<p>I.e. "anything -&gt; true" just like ex falso is "false -&gt; anything"</p>

#### [ Kenny Lau (Oct 05 2018 at 23:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Prove%20false%20from%20not%20true%3F/near/135284181):
<p><code>trivial</code></p>

#### [ Andrew Ashworth (Oct 05 2018 at 23:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Prove%20false%20from%20not%20true%3F/near/135284285):
<p>as an aside, I think <code>trivial</code> is named weirdly. Why does it exist when <code>true.intro</code> is the canonical name?</p>

#### [ Abhimanyu Pallavi Sudhir (Oct 05 2018 at 23:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Prove%20false%20from%20not%20true%3F/near/135284287):
<p>Thanks. Didn't know that could be used as a standalone statement.</p>

#### [ Abhimanyu Pallavi Sudhir (Oct 05 2018 at 23:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Prove%20false%20from%20not%20true%3F/near/135284298):
<p>Re:true.intro Doesn't that apply to exfalso too? false.elim having a special name.</p>

#### [ Andrew Ashworth (Oct 05 2018 at 23:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Prove%20false%20from%20not%20true%3F/near/135284312):
<p><code>exfalso</code> is an eliminator</p>

#### [ Andrew Ashworth (Oct 05 2018 at 23:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Prove%20false%20from%20not%20true%3F/near/135284384):
<p>but yes, i also prefer using <code>false.elim</code> ;)</p>

#### [ Chris Hughes (Oct 05 2018 at 23:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Prove%20false%20from%20not%20true%3F/near/135284568):
<p>My favourite is <code>induction h</code> if <code>h : false</code></p>

#### [ Kenny Lau (Oct 05 2018 at 23:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Prove%20false%20from%20not%20true%3F/near/135284579):
<p>my favourite is <code>cases h</code></p>

#### [ Charles Rezk (Oct 06 2018 at 02:31)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Prove%20false%20from%20not%20true%3F/near/135290869):
<p>Where can I get help for installing lean?</p>

#### [ Bryan Gin-ge Chen (Oct 06 2018 at 02:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Prove%20false%20from%20not%20true%3F/near/135290928):
<p>Feel free to ask in this chat! But we may want to use a different "thread".</p>

#### [ Charles Rezk (Oct 06 2018 at 02:33)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Prove%20false%20from%20not%20true%3F/near/135290937):
<p>OK how do I do that?</p>


{% endraw %}
