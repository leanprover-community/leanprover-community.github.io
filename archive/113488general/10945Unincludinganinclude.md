---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/10945Unincludinganinclude.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [Un-including an include](https://leanprover-community.github.io/archive/113488general/10945Unincludinganinclude.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Keeley Hoek (Sep 29 2018 at 12:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Un-including%20an%20include/near/134878195):
<p>If <code>include blah</code> occurs in my current namespace, is there a way to make a special definition which doesn't take <code>blah</code> as an argument?</p>

#### [ Patrick Massot (Sep 29 2018 at 12:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Un-including%20an%20include/near/134878197):
<p><code>omit blah</code></p>

#### [ Patrick Massot (Sep 29 2018 at 12:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Un-including%20an%20include/near/134878199):
<p>and then reinclude</p>

#### [ Keeley Hoek (Sep 29 2018 at 13:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Un-including%20an%20include/near/134878790):
<p>awesome cheers!</p>

#### [ Keeley Hoek (Sep 29 2018 at 13:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Un-including%20an%20include/near/134878828):
<p>how about turning a <code>list α</code> into an <code>expr</code>?</p>

#### [ Mario Carneiro (Sep 29 2018 at 13:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Un-including%20an%20include/near/134879034):
<p>I think <code>reflect</code> is what you want?</p>

#### [ Keeley Hoek (Sep 29 2018 at 13:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Un-including%20an%20include/near/134879356):
<p>Sweet!</p>

#### [ Keeley Hoek (Sep 29 2018 at 13:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Un-including%20an%20include/near/134879364):
<p>Has anyone ever gotten the error <code>VM does not have code for 'xyz.abc'</code> after trying to use something they <code>environment.add</code>ed?</p>

#### [ Kevin Buzzard (Sep 29 2018 at 13:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Un-including%20an%20include/near/134879479):
<p>The only time I get that error is when I've accidentally used <code>theorem</code> to make a definition</p>

#### [ Keeley Hoek (Sep 29 2018 at 14:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Un-including%20an%20include/near/134880407):
<p>it turned out to be a really obscure problem, where if you call user_attribute.get_param with someone who doesn't have the attribute set, the vm un-gracefully shoots you down without a catchable <code>fail</code></p>

#### [ Keeley Hoek (Sep 29 2018 at 14:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Un-including%20an%20include/near/134881168):
<p>If this ever comes up for anyone else, <code>environment.add</code> is a little messed up if you want to later add attributes<br>
Instead use <code>tactic.add_decl</code> (both are implemented in C++)</p>

#### [ Simon Hudon (Sep 29 2018 at 22:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Un-including%20an%20include/near/134895695):
<blockquote>
<p>it turned out to be a really obscure problem, where if you call user_attribute.get_param with someone who doesn't have the attribute set, the vm un-gracefully shoots you down without a catchable <code>fail</code></p>
</blockquote>
<p>Are you sure? <code>get_param</code> has issues because it uses <code>eval_expr</code> which is kind of broken. Try <code>get_param_untyped</code> instead to see if it crashes uglily, still</p>


{% endraw %}
