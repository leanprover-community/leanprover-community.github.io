---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/85208contextlikeexprlists.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [context like expr lists?](https://leanprover-community.github.io/archive/113488general/85208contextlikeexprlists.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Jakob von Raumer (Mar 13 2018 at 14:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/context%20like%20expr%20lists%3F/near/123654389):
<p>How do I construct a list of expressions where later entries can depend on earlier ones? Like <code>(A : Sort u) (a : A)</code> as a minimal example... Do I have to use local constants?</p>

#### [ Mario Carneiro (Mar 13 2018 at 14:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/context%20like%20expr%20lists%3F/near/123654415):
<p>when you say list of expressions, are you working in <code>meta</code> land?</p>

#### [ Jakob von Raumer (Mar 13 2018 at 14:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/context%20like%20expr%20lists%3F/near/123654423):
<p>Yes</p>

#### [ Mario Carneiro (Mar 13 2018 at 14:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/context%20like%20expr%20lists%3F/near/123654424):
<p>it's just <code>list expr</code></p>

#### [ Mario Carneiro (Mar 13 2018 at 14:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/context%20like%20expr%20lists%3F/near/123654473):
<p>all that binding stuff is handled by you</p>

#### [ Jakob von Raumer (Mar 13 2018 at 14:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/context%20like%20expr%20lists%3F/near/123654481):
<p>Yes, but how is the above example represented for example?</p>

#### [ Mario Carneiro (Mar 13 2018 at 14:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/context%20like%20expr%20lists%3F/near/123654502):
<p>the first expr is <code>`(Sort u)</code>, the second is either <code> `(A)</code> or <code>#0</code> depending on whether <code>A</code> is in context</p>

#### [ Jakob von Raumer (Mar 13 2018 at 14:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/context%20like%20expr%20lists%3F/near/123654671):
<p>Well at the time I define the list, <code>A</code> is clearly not in context, right?</p>

#### [ Mario Carneiro (Mar 13 2018 at 14:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/context%20like%20expr%20lists%3F/near/123654676):
<p>Maybe; perhaps you are planning for when it is. What's your use case?</p>

#### [ Jakob von Raumer (Mar 13 2018 at 14:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/context%20like%20expr%20lists%3F/near/123654723):
<p>Just experimenting with the <code>add_inductive</code> API a bit... which is where it should be used as list of parameters or such</p>

#### [ Jakob von Raumer (Mar 13 2018 at 14:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/context%20like%20expr%20lists%3F/near/123654735):
<p>And <code>meta example : list expr := [\</code>(Sort 1), \`(A)]` immediately gives me "unknown identifier A"..</p>

#### [ Jakob von Raumer (Mar 13 2018 at 14:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/context%20like%20expr%20lists%3F/near/123654737):
<p><em>sigh</em> How do I escape backticks here?</p>

#### [ Mario Carneiro (Mar 13 2018 at 14:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/context%20like%20expr%20lists%3F/near/123654777):
<p><code>add_inductive</code> doesn't take a list of parameters, it takes <code>ty : expr</code> that specifies the whole type</p>

#### [ Mario Carneiro (Mar 13 2018 at 14:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/context%20like%20expr%20lists%3F/near/123654787):
<p>Since it's a single expression, all the binding is done via <code>expr.pi</code>, and dependencies are done with <code>var</code> (de bruijn variables)</p>

#### [ Mario Carneiro (Mar 13 2018 at 14:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/context%20like%20expr%20lists%3F/near/123654810):
<p>That is, <code>ty</code> should be a closed term</p>

#### [ Mario Carneiro (Mar 13 2018 at 14:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/context%20like%20expr%20lists%3F/near/123654857):
<p>escape backticks with more backticks <code> `` `escaped` `` </code></p>

#### [ Jakob von Raumer (Mar 13 2018 at 14:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/context%20like%20expr%20lists%3F/near/123654861):
<p>But it takes a list of constructtors, right?</p>

#### [ Mario Carneiro (Mar 13 2018 at 14:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/context%20like%20expr%20lists%3F/near/123654865):
<p>The constructor types are also closed terms</p>

#### [ Mario Carneiro (Mar 13 2018 at 14:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/context%20like%20expr%20lists%3F/near/123654868):
<p>they repeat all the parameters, with the same types</p>

#### [ Jakob von Raumer (Mar 13 2018 at 14:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/context%20like%20expr%20lists%3F/near/123654914):
<p>Hm, I'd still like to have a data structure like that...</p>

#### [ Mario Carneiro (Mar 13 2018 at 14:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/context%20like%20expr%20lists%3F/near/123654915):
<p>(this is done because constructors may change the binding type, like making things implicit)</p>

#### [ Mario Carneiro (Mar 13 2018 at 14:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/context%20like%20expr%20lists%3F/near/123654921):
<p>Usually, we work in a context, and then it's a <code>list expr</code></p>

#### [ Mario Carneiro (Mar 13 2018 at 14:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/context%20like%20expr%20lists%3F/near/123654928):
<p>the whole tactic state is built around that</p>

#### [ Mario Carneiro (Mar 13 2018 at 14:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/context%20like%20expr%20lists%3F/near/123654931):
<p>that's where local constants come in</p>

#### [ Jakob von Raumer (Mar 13 2018 at 14:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/context%20like%20expr%20lists%3F/near/123654988):
<p><code>expr</code> could use a bit more documentation somehow, it's really hard to figure out what local constants are</p>

#### [ Kevin Buzzard (Mar 13 2018 at 14:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/context%20like%20expr%20lists%3F/near/123655582):
<p><span class="user-mention" data-user-id="110789">@Jakob von Raumer</span> Write what you know and PR it to mathlib/docs/</p>

#### [ Kevin Buzzard (Mar 13 2018 at 14:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/context%20like%20expr%20lists%3F/near/123655583):
<p>and then ask about what you don't know</p>

#### [ Kevin Buzzard (Mar 13 2018 at 14:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/context%20like%20expr%20lists%3F/near/123655594):
<p>we're trying to make some community-based docs in there</p>

#### [ Kevin Buzzard (Mar 13 2018 at 14:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/context%20like%20expr%20lists%3F/near/123655599):
<p>informal and hopefully useful</p>

#### [ Jakob von Raumer (Mar 13 2018 at 14:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/context%20like%20expr%20lists%3F/near/123655600):
<p>I'll try :)</p>

#### [ Kevin Buzzard (Mar 13 2018 at 14:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/context%20like%20expr%20lists%3F/near/123655643):
<p>The rule I usually go for is "if it's not in the reference manual, and it's either not in TPIL/Programming In Lean or it's hard to find, then stick it in mathlib/docs"</p>

#### [ Jakob von Raumer (Mar 13 2018 at 14:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/context%20like%20expr%20lists%3F/near/123655655):
<p>I think it <em>should</em> be in PIL but it's noted as a TODO there</p>

#### [ Kevin Buzzard (Mar 13 2018 at 15:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/context%20like%20expr%20lists%3F/near/123655712):
<p>Then I would urge you to create a short text file called expr.md and simply write some background and then what you're stuck on and PR it to that docs dir. You can assume people have read PIL.</p>

#### [ Jakob von Raumer (Mar 14 2018 at 16:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/context%20like%20expr%20lists%3F/near/123705964):
<p>What is the purpose of the second <code>name</code> argument to <code>expr.local_const</code>?</p>

#### [ Jakob von Raumer (Mar 14 2018 at 16:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/context%20like%20expr%20lists%3F/near/123706023):
<p>Ah, got it, pretty printer name...</p>


{% endraw %}
