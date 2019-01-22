---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/58529prettyprintingunderscores.html
---

## [general](index.html)
### [pretty printing underscores](58529prettyprintingunderscores.html)

#### [Scott Morrison (Nov 27 2018 at 00:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pretty%20printing%20underscores/near/148406464):
Is there a good way to pretty print expressions, so metavariables get replaced by `_` characters?

#### [Scott Morrison (Nov 27 2018 at 00:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pretty%20printing%20underscores/near/148406530):
I see there is `pp.use_holes` which prints metavariables as `{! !}`.

#### [Scott Morrison (Nov 27 2018 at 00:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pretty%20printing%20underscores/near/148406776):
or perhaps more simply --- does anyone know how I do substring replacement? (e.g. `{! !}` to `_`)

#### [Rob Lewis (Nov 27 2018 at 00:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pretty%20printing%20underscores/near/148406884):
It might be easier to replace the metavars with `pexpr.mk_placeholder` before printing.

#### [Scott Morrison (Nov 27 2018 at 00:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pretty%20printing%20underscores/near/148407075):
I see. Any suggestions on how to do the replacement? I tried just folding, but I need to turn `expr`s back into `pexpr`s.

#### [Scott Morrison (Nov 27 2018 at 00:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pretty%20printing%20underscores/near/148407086):
of, pexpr.of_expr

#### [Rob Lewis (Nov 27 2018 at 00:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pretty%20printing%20underscores/near/148407113):
No promises that this works beyond the two little examples I just tried, but give it a shot.
```lean
meta def replace_mvars (e : expr) : expr :=
e.replace (λ e' _, if e'.is_meta_var then some (unchecked_cast pexpr.mk_placeholder) else none)
```

#### [Scott Morrison (Nov 27 2018 at 00:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pretty%20printing%20underscores/near/148407167):
Looking good!!

#### [Scott Morrison (Nov 27 2018 at 00:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pretty%20printing%20underscores/near/148407267):
I still need to learn how to do string munging in Lean, I'm flailing about trying to decide is a string contains a given character... :-(

#### [Scott Morrison (Nov 27 2018 at 00:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pretty%20printing%20underscores/near/148407316):
`'_' ∈ s.to_list`?

#### [Scott Morrison (Nov 27 2018 at 00:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pretty%20printing%20underscores/near/148407320):
Seems to work, but presumably there's something more natural.

#### [Keeley Hoek (Nov 27 2018 at 01:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/pretty%20printing%20underscores/near/148408767):
Just on the strings scott
Resist the temptation to use `string.iterator`s
I thought they were the future (they are VM implemented), and changed the `expr` deserialiser to use them
About a 5% slowdown

