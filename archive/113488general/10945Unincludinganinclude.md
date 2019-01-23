---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/10945Unincludinganinclude.html
---

## Stream: [general](index.html)
### Topic: [Un-including an include](10945Unincludinganinclude.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Keeley Hoek (Sep 29 2018 at 12:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Un-including%20an%20include/near/134878195):
If `include blah` occurs in my current namespace, is there a way to make a special definition which doesn't take `blah` as an argument?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 29 2018 at 12:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Un-including%20an%20include/near/134878197):
`omit blah`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Sep 29 2018 at 12:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Un-including%20an%20include/near/134878199):
and then reinclude

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Keeley Hoek (Sep 29 2018 at 13:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Un-including%20an%20include/near/134878790):
awesome cheers!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Keeley Hoek (Sep 29 2018 at 13:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Un-including%20an%20include/near/134878828):
how about turning a `list α` into an `expr`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Sep 29 2018 at 13:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Un-including%20an%20include/near/134879034):
I think `reflect` is what you want?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Keeley Hoek (Sep 29 2018 at 13:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Un-including%20an%20include/near/134879356):
Sweet!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Keeley Hoek (Sep 29 2018 at 13:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Un-including%20an%20include/near/134879364):
Has anyone ever gotten the error `VM does not have code for 'xyz.abc'` after trying to use something they `environment.add`ed?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Sep 29 2018 at 13:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Un-including%20an%20include/near/134879479):
The only time I get that error is when I've accidentally used `theorem` to make a definition

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Keeley Hoek (Sep 29 2018 at 14:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Un-including%20an%20include/near/134880407):
it turned out to be a really obscure problem, where if you call user_attribute.get_param with someone who doesn't have the attribute set, the vm un-gracefully shoots you down without a catchable `fail`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Keeley Hoek (Sep 29 2018 at 14:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Un-including%20an%20include/near/134881168):
If this ever comes up for anyone else, `environment.add` is a little messed up if you want to later add attributes
Instead use `tactic.add_decl` (both are implemented in C++)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Sep 29 2018 at 22:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Un-including%20an%20include/near/134895695):
```quote
it turned out to be a really obscure problem, where if you call user_attribute.get_param with someone who doesn't have the attribute set, the vm un-gracefully shoots you down without a catchable `fail`
```
Are you sure? `get_param` has issues because it uses `eval_expr` which is kind of broken. Try `get_param_untyped` instead to see if it crashes uglily, still


{% endraw %}
