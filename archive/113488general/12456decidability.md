---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/12456decidability.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [decidability](https://leanprover-community.github.io/archive/113488general/12456decidability.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kenny Lau (Mar 30 2018 at 22:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/decidability/near/124428848):
<p>Are there things that are decidable but not yet proven?</p>

#### [ Kenny Lau (Mar 30 2018 at 22:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/decidability/near/124428850):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span></p>

#### [ Mario Carneiro (Mar 30 2018 at 22:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/decidability/near/124428860):
<p>Not sure I understand the meta level of the question</p>

#### [ Kenny Lau (Mar 30 2018 at 22:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/decidability/near/124428902):
<p>that means, things that should be decidable, but nobody has proved it in Lean yet</p>

#### [ Mario Carneiro (Mar 30 2018 at 22:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/decidability/near/124428905):
<p>of course</p>

#### [ Kenny Lau (Mar 30 2018 at 22:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/decidability/near/124428906):
<p>could you list some</p>

#### [ Mario Carneiro (Mar 30 2018 at 22:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/decidability/near/124428908):
<p>that's like asking if there are any not yet proven theorems</p>

#### [ Kenny Lau (Mar 30 2018 at 22:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/decidability/near/124428920):
<p>well there are only finitely many predicates that have been created in Lean</p>

#### [ Mario Carneiro (Mar 30 2018 at 22:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/decidability/near/124428942):
<p>Hm, none comes to mind... I have a definition that I don't have on mathlib yet that is waiting for a proof of decidability</p>

#### [ Kenny Lau (Mar 30 2018 at 22:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/decidability/near/124428945):
<p>what is it</p>

#### [ Mario Carneiro (Mar 30 2018 at 22:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/decidability/near/124428987):
<p>namely that level (in)equality in lean is decidable</p>

#### [ Kenny Lau (Mar 30 2018 at 22:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/decidability/near/124428992):
<p>hmm...</p>

#### [ Mario Carneiro (Mar 30 2018 at 22:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/decidability/near/124429012):
<p>that is, for expressions made up of <code>max</code>, <code>imax</code> and variables, you can determine if for all values of the variables in <code>nat</code>, one is &lt;= the other or not</p>

#### [ Mario Carneiro (Mar 30 2018 at 22:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/decidability/near/124429027):
<p>The proof uses case splitting on any <code>imax</code> expressions that come up</p>

#### [ Kenny Lau (Mar 30 2018 at 22:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/decidability/near/124429032):
<p>oh, I should build a decidable version of <code>finsupp</code></p>

#### [ Mario Carneiro (Mar 30 2018 at 22:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/decidability/near/124429086):
<p>I think Johannes had a proposal for that on here, where you use a <code>fintype</code> instead of <code>finite</code></p>

#### [ Kenny Lau (Mar 30 2018 at 22:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/decidability/near/124429095):
<p>oh wait, I don't work with finite things</p>

#### [ Kenny Lau (Mar 30 2018 at 22:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/decidability/near/124429096):
<p>lol</p>

#### [ Kenny Lau (Mar 30 2018 at 22:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/decidability/near/124429371):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> no examples from <code>nat</code> and <code>int</code>?</p>

#### [ Kenny Lau (Mar 30 2018 at 22:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/decidability/near/124429372):
<p>i.e. everything about them that should be decidable have been proven to be decidable?</p>

#### [ Mario Carneiro (Mar 30 2018 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/decidability/near/124429446):
<p>yes, there aren't that many interesting predicate to start with</p>

#### [ Kenny Lau (Mar 30 2018 at 22:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/decidability/near/124429495):
<p>nice</p>

#### [ Andrew Ashworth (Mar 30 2018 at 23:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/decidability/near/124430652):
<p><span class="user-mention" data-user-id="110064">@Kenny Lau</span> out of curiousity what's up with your commutative algebra pr on mathlib</p>

#### [ Kenny Lau (Mar 30 2018 at 23:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/decidability/near/124430671):
<p>I just started reworking it a few minutes ago, what a coincidence</p>

#### [ Kevin Buzzard (Mar 31 2018 at 00:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/decidability/near/124433277):
<p>Kenny feel free to PR some of the comm alg stuff in stacks project. Did UMP get PR'd? That's a really important tool I see now.</p>

#### [ Kenny Lau (Mar 31 2018 at 00:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/decidability/near/124433281):
<p>I can't PR anything until mathlib builds</p>

#### [ Kevin Buzzard (Mar 31 2018 at 00:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/decidability/near/124433282):
<p>Oh I see.</p>

#### [ Kevin Buzzard (Mar 31 2018 at 00:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/decidability/near/124433283):
<p>Why don't you roll back?</p>

#### [ Kenny Lau (Mar 31 2018 at 00:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/decidability/near/124433324):
<p>I mean, the PR will have a cross</p>

#### [ Kevin Buzzard (Mar 31 2018 at 00:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/decidability/near/124433326):
<p>I know it's a bore. Whenever Lean head and mathlib head don't play well together you're suddenly having to look up commits.</p>

#### [ Kevin Buzzard (Mar 31 2018 at 00:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/decidability/near/124433332):
<p>I just never upgrade unless I have no red cross and also a thumbs up here</p>

#### [ Kevin Buzzard (Mar 31 2018 at 00:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/decidability/near/124433342):
<p>I think Sebastian is seriously looking at making this kind of thing easier with leanpkg.</p>

#### [ Kenny Lau (Mar 31 2018 at 00:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/decidability/near/124433346):
<p>I still don't know why the latest build fails</p>


{% endraw %}
