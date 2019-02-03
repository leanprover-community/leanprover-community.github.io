---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/46360rewritesearch.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [rewrite_search](https://leanprover-community.github.io/archive/113488general/46360rewritesearch.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Scott Morrison (Nov 10 2018 at 07:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite_search/near/147422501):
<p>Hi <span class="user-mention" data-user-id="110111">@Keeley Hoek</span>, I think I'm getting <code>"XXX" is not a valid rewrite lemma!</code> errors which I shouldn't be. I think in this case the problem is you need to unfold a step before the lemma looks right. Can we make <code>rewrite_search</code> more forgiving?</p>

#### [ Scott Morrison (Nov 10 2018 at 08:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite_search/near/147422576):
<p>There are examples in my branch &lt;<a href="https://github.com/semorrison/monoidal-categories-reboot/tree/monoidal_functor.comp" target="_blank" title="https://github.com/semorrison/monoidal-categories-reboot/tree/monoidal_functor.comp">https://github.com/semorrison/monoidal-categories-reboot/tree/monoidal_functor.comp</a>&gt; of <span class="user-mention" data-user-id="128547">@Michael Jendrusch</span>'s new monoidal categories development.</p>

#### [ Keeley Hoek (Nov 10 2018 at 11:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite_search/near/147428564):
<p><span class="user-mention" data-user-id="110087">@Scott Morrison</span> I can't see anything there which doesn't compile (on the monoidal_functor.comp branch), am I meant to try to remove the <code>sorry</code>s?</p>

#### [ Keeley Hoek (Nov 10 2018 at 13:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite_search/near/147431664):
<p>Nonetheless, off a fuzzy memory of something like this happening to me with projections or local variables or something, I've made a total shot in the dark and hopefully <code>whnf</code>'d the problem away</p>

#### [ Scott Morrison (Nov 10 2018 at 22:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite_search/near/147448566):
<p>Hmm, doesn't seem to have helped. Here's the problem: &lt;<a href="https://github.com/semorrison/monoidal-categories-reboot/blob/monoidal_functor.comp/src/monoidal_categories_reboot/monoidal_category.lean#L52" target="_blank" title="https://github.com/semorrison/monoidal-categories-reboot/blob/monoidal_functor.comp/src/monoidal_categories_reboot/monoidal_category.lean#L52">https://github.com/semorrison/monoidal-categories-reboot/blob/monoidal_functor.comp/src/monoidal_categories_reboot/monoidal_category.lean#L52</a>&gt;</p>

#### [ Keeley Hoek (Nov 11 2018 at 04:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite_search/near/147461212):
<p>Gotcha, I'll take a look</p>

#### [ Keeley Hoek (Nov 11 2018 at 05:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite_search/near/147462126):
<p>ok I've just turned it the checks off for now. Does anyone know how to do something similar to <code>#reduce</code>, but to an <code>expr</code> in tactic-mode?</p>

#### [ Keeley Hoek (Nov 11 2018 at 05:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite_search/near/147462183):
<p>I'd just like to unfold some definitions, to be able to tell certain things (e.g. of type <code>monoidal_category.associator_naturality'</code>) are secretly just equalities</p>

#### [ Keeley Hoek (Nov 11 2018 at 05:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite_search/near/147462189):
<p>I thought <code>whnf</code> maybe did this? Is there a problem if the expression being passed is after binders?</p>

#### [ Keeley Hoek (Nov 11 2018 at 05:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite_search/near/147462347):
<p>ah, I see I want <code>dsimp</code></p>

#### [ Keeley Hoek (Nov 11 2018 at 05:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/rewrite_search/near/147462547):
<p>Hmm... it seems to unfold projections when I pass in arguments, but it doesn't deduce their type</p>


{% endraw %}
