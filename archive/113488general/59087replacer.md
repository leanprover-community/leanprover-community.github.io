---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/59087replacer.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [replacer](https://leanprover-community.github.io/archive/113488general/59087replacer.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Mario Carneiro (Sep 11 2018 at 02:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/replacer/near/133700764):
<p>By the suggestion of Simon, I've extended <code>replacer</code> to support parameters in its type. That is, you can define a replaceable definition <code>foo : A -&gt; tactic B</code> where you have arbitrary input and output, rather than just <code>tactic unit</code>. Incidentally, implementing this required my first attempt at meta-metaprogramming, since the defined tactics are written programmatically.</p>

#### [ Simon Hudon (Sep 11 2018 at 02:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/replacer/near/133700886):
<p>Does it accept any number of parameters?</p>

#### [ Mario Carneiro (Sep 11 2018 at 02:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/replacer/near/133700888):
<p>yes</p>

#### [ Mario Carneiro (Sep 11 2018 at 02:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/replacer/near/133700895):
<p>just one output, but we always bundle that anyway</p>

#### [ Mario Carneiro (Sep 11 2018 at 02:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/replacer/near/133700963):
<p>It doesn't support monads other than <code>tactic</code>, and the prev tactic access does not allow changing parameters</p>

#### [ Simon Hudon (Sep 11 2018 at 03:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/replacer/near/133701331):
<p>This supercalifragilisticexpialidocious!</p>

#### [ Simon Hudon (Sep 11 2018 at 03:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/replacer/near/133701427):
<p>To let other people in on the idea, I wanted this so that we can write a tactic at the same as we write a proof, even if the tactic is a core tactic, we can put them in the same file and stop recompiling everything every time we change the tactic</p>

#### [ Simon Hudon (Sep 11 2018 at 03:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/replacer/near/133701435):
<p>This is a bit similar to hot code loading</p>

#### [ Mario Carneiro (Sep 11 2018 at 03:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/replacer/near/133701521):
<p>you don't mean "core" as in "core lean" though. Like time travel, you can't go back before the time machine was invented</p>

#### [ Simon Hudon (Sep 11 2018 at 03:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/replacer/near/133701529):
<p>That is correct :)</p>

#### [ Simon Hudon (Sep 11 2018 at 03:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/replacer/near/133701549):
<p>You can only replace definitions in files where you can import this replacer tactic.</p>

#### [ Simon Hudon (Sep 11 2018 at 03:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/replacer/near/133701974):
<p>What do you use from <code>tactic.basic</code>?</p>

#### [ Mario Carneiro (Sep 11 2018 at 03:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/replacer/near/133702266):
<p>just the <code>has_reflect</code> instance for binder_info</p>

#### [ Simon Hudon (Sep 11 2018 at 03:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/replacer/near/133702353):
<p>Cool, I left you a comment on the commit. I think it should be moved to <code>tactic.replacer</code> so that <code>tactic.basic</code> can import <code>tactic.replacer</code> (since it's a tool for writing tactics)</p>

#### [ Mario Carneiro (Sep 11 2018 at 03:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/replacer/near/133702529):
<p>I don't think anything in mathlib uses it though</p>

#### [ Simon Hudon (Sep 11 2018 at 03:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/replacer/near/133702652):
<p>That's ok. What i intend to do with it when I write tactics for mathlib is to temporarily have <code>tactic.basic</code> import <code>tactic.replacer</code>, make all the routines I use replaceable, go write an example and, next to it, keep a version of the functions and tactics that I modify. When I'm done, I remove the <code>def_replacers</code> and the <code>import tactic.basic</code> statement.</p>

#### [ Simon Hudon (Sep 11 2018 at 03:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/replacer/near/133703035):
<p>Btw, there is a way we could go back in time passed the creation of our machine: using meta programming, we create a <code>dynamic</code> namespace in which we copy all the visible declarations that depend on what we want to replace and and we rewrite their definitions to insert the replacer instead of the original definition.</p>

#### [ Mario Carneiro (Sep 11 2018 at 03:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/replacer/near/133703136):
<p>that's more like alternate universe time travel</p>

#### [ Simon Hudon (Sep 11 2018 at 03:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/replacer/near/133703163):
<p>I'm happy with multi-universe interpretations</p>


{% endraw %}
