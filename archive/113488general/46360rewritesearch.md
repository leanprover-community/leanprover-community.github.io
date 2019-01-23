---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/46360rewritesearch.html
---

## Stream: [general](index.html)
### Topic: [rewrite_search](46360rewritesearch.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Nov 10 2018 at 07:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite_search/near/147422501):
Hi @**Keeley Hoek**, I think I'm getting `"XXX" is not a valid rewrite lemma!` errors which I shouldn't be. I think in this case the problem is you need to unfold a step before the lemma looks right. Can we make `rewrite_search` more forgiving?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Nov 10 2018 at 08:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite_search/near/147422576):
There are examples in my branch <https://github.com/semorrison/monoidal-categories-reboot/tree/monoidal_functor.comp> of @**Michael Jendrusch**'s new monoidal categories development.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Keeley Hoek (Nov 10 2018 at 11:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite_search/near/147428564):
@**Scott Morrison|110087** I can't see anything there which doesn't compile (on the monoidal_functor.comp branch), am I meant to try to remove the `sorry`s?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Keeley Hoek (Nov 10 2018 at 13:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite_search/near/147431664):
Nonetheless, off a fuzzy memory of something like this happening to me with projections or local variables or something, I've made a total shot in the dark and hopefully `whnf`'d the problem away

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Scott Morrison (Nov 10 2018 at 22:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite_search/near/147448566):
Hmm, doesn't seem to have helped. Here's the problem: <https://github.com/semorrison/monoidal-categories-reboot/blob/monoidal_functor.comp/src/monoidal_categories_reboot/monoidal_category.lean#L52>

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Keeley Hoek (Nov 11 2018 at 04:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite_search/near/147461212):
Gotcha, I'll take a look

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Keeley Hoek (Nov 11 2018 at 05:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite_search/near/147462126):
ok I've just turned it the checks off for now. Does anyone know how to do something similar to `#reduce`, but to an `expr` in tactic-mode?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Keeley Hoek (Nov 11 2018 at 05:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite_search/near/147462183):
I'd just like to unfold some definitions, to be able to tell certain things (e.g. of type `monoidal_category.associator_naturality'`) are secretly just equalities

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Keeley Hoek (Nov 11 2018 at 05:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite_search/near/147462189):
I thought `whnf` maybe did this? Is there a problem if the expression being passed is after binders?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Keeley Hoek (Nov 11 2018 at 05:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite_search/near/147462347):
ah, I see I want `dsimp`

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Keeley Hoek (Nov 11 2018 at 05:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite_search/near/147462547):
Hmm... it seems to unfold projections when I pass in arguments, but it doesn't deduce their type

