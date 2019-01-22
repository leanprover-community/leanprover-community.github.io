---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/07922reflectbool.html
---

## [general](index.html)
### [reflect bool](07922reflectbool.html)

#### [Simon Hudon (Aug 03 2018 at 08:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reflect%20bool/near/130821232):
I'm running the following code:

```lean
run_cmd eval_expr bool (reflect tt) >>= trace
```

`bool` has an instance of `has_reflect` and the above is type correct but when I run it I get the following error:

```
VM does not have code for 'bool.tt'
```

What can I do?

#### [Mario Carneiro (Aug 03 2018 at 12:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reflect%20bool/near/130830241):
There is definitely a bug somewhere in the workings of `eval_expr`

#### [Mario Carneiro (Aug 03 2018 at 12:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reflect%20bool/near/130830284):
workaround:
```
run_cmd eval_expr bool (reflect (id tt)) >>= trace
```

#### [Minchao Wu (Aug 03 2018 at 12:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reflect%20bool/near/130830305):
looks like magic

#### [Simon Hudon (Aug 03 2018 at 15:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reflect%20bool/near/130839532):
Thanks! I was able to use this trick with `user_attribute.get_param_untyped` to replace `user_attribute.get_param`

#### [Simon Hudon (Aug 03 2018 at 15:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/reflect%20bool/near/130839561):
(by wrapping the return with `id`: ```to_expr ``(id %%r)```)

