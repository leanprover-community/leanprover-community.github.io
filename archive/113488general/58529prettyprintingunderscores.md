---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/58529prettyprintingunderscores.html
---

## Stream: [general](index.html)
### Topic: [pretty printing underscores](58529prettyprintingunderscores.html)

---


{% raw %}
#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Nov 27 2018 at 00:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pretty%20printing%20underscores/near/148406464):
Is there a good way to pretty print expressions, so metavariables get replaced by `_` characters?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Nov 27 2018 at 00:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pretty%20printing%20underscores/near/148406530):
I see there is `pp.use_holes` which prints metavariables as `{! !}`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Nov 27 2018 at 00:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pretty%20printing%20underscores/near/148406776):
or perhaps more simply --- does anyone know how I do substring replacement? (e.g. `{! !}` to `_`)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Nov 27 2018 at 00:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pretty%20printing%20underscores/near/148406884):
It might be easier to replace the metavars with `pexpr.mk_placeholder` before printing.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Nov 27 2018 at 00:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pretty%20printing%20underscores/near/148407075):
I see. Any suggestions on how to do the replacement? I tried just folding, but I need to turn `expr`s back into `pexpr`s.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Nov 27 2018 at 00:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pretty%20printing%20underscores/near/148407086):
of, pexpr.of_expr

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Rob Lewis (Nov 27 2018 at 00:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pretty%20printing%20underscores/near/148407113):
No promises that this works beyond the two little examples I just tried, but give it a shot.
```lean
meta def replace_mvars (e : expr) : expr :=
e.replace (λ e' _, if e'.is_meta_var then some (unchecked_cast pexpr.mk_placeholder) else none)
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Nov 27 2018 at 00:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pretty%20printing%20underscores/near/148407167):
Looking good!!

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Nov 27 2018 at 00:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pretty%20printing%20underscores/near/148407267):
I still need to learn how to do string munging in Lean, I'm flailing about trying to decide is a string contains a given character... :-(

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Nov 27 2018 at 00:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pretty%20printing%20underscores/near/148407316):
`'_' ∈ s.to_list`?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Nov 27 2018 at 00:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pretty%20printing%20underscores/near/148407320):
Seems to work, but presumably there's something more natural.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Keeley Hoek (Nov 27 2018 at 01:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pretty%20printing%20underscores/near/148408767):
Just on the strings scott
Resist the temptation to use `string.iterator`s
I thought they were the future (they are VM implemented), and changed the `expr` deserialiser to use them
About a 5% slowdown


{% endraw %}
