---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/144837PRreviews/89535480Yonedafixes.html
---

## Stream: [PR reviews](https://leanprover-community.github.io/archive/144837PRreviews/index.html)
### Topic: [#480 Yoneda fixes](https://leanprover-community.github.io/archive/144837PRreviews/89535480Yonedafixes.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Scott Morrison (Nov 28 2018 at 04:29)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23480%20Yoneda%20fixes/near/148686856):
<p>Travis seems to be screwing something up with <a href="https://github.com/leanprover/mathlib/pull/480" target="_blank" title="https://github.com/leanprover/mathlib/pull/480">https://github.com/leanprover/mathlib/pull/480</a>. It’s complaining about invalid imports in files that aren’t even in this PR anymore. <span class="user-mention" data-user-id="110049">@Mario Carneiro</span>, are you able to reset it somehow?</p>

#### [ Keeley Hoek (Nov 28 2018 at 04:45)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23480%20Yoneda%20fixes/near/148687461):
<p><span class="user-mention" data-user-id="110087">@Scott Morrison</span> have you tried clearing the cache for that branch? I think I can do it</p>

#### [ Scott Morrison (Nov 28 2018 at 04:46)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23480%20Yoneda%20fixes/near/148687515):
<p>Ah, I thought only some people could do that. If you see how to do it, teach me. :-)</p>

#### [ Keeley Hoek (Nov 28 2018 at 04:46)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23480%20Yoneda%20fixes/near/148687524):
<p><a href="https://travis-ci.org/leanprover-community/mathlib/caches" target="_blank" title="https://travis-ci.org/leanprover-community/mathlib/caches">https://travis-ci.org/leanprover-community/mathlib/caches</a></p>

#### [ Keeley Hoek (Nov 28 2018 at 04:46)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23480%20Yoneda%20fixes/near/148687526):
<p>And just click the lil bin</p>

#### [ Keeley Hoek (Nov 28 2018 at 04:46)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23480%20Yoneda%20fixes/near/148687529):
<p>I retriggered a build</p>

#### [ Keeley Hoek (Nov 28 2018 at 04:46)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23480%20Yoneda%20fixes/near/148687531):
<p>after</p>

#### [ Keeley Hoek (Nov 28 2018 at 04:50)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23480%20Yoneda%20fixes/near/148687643):
<p>We can because everything is really on mathlib-community, which we can push to</p>

#### [ Scott Morrison (Nov 28 2018 at 07:11)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23480%20Yoneda%20fixes/near/148692162):
<p>Thanks <span class="user-mention" data-user-id="110111">@Keeley Hoek</span>. Curiously this doesn't seem to have fixed the PR, however. :-(</p>

#### [ Keeley Hoek (Nov 28 2018 at 07:11)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23480%20Yoneda%20fixes/near/148692163):
<p>Ah yes<br>
But it did build successfully<br>
<a href="https://travis-ci.org/leanprover-community/mathlib/builds/460592170" target="_blank" title="https://travis-ci.org/leanprover-community/mathlib/builds/460592170">https://travis-ci.org/leanprover-community/mathlib/builds/460592170</a></p>

#### [ Keeley Hoek (Nov 28 2018 at 07:11)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23480%20Yoneda%20fixes/near/148692164):
<p>I was wrong about it updating the thingo for the main repo though</p>

#### [ Scott Morrison (Nov 28 2018 at 07:13)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23480%20Yoneda%20fixes/near/148692210):
<p>Okay, I'll just push a whitespace change and see if that fixes things.</p>

#### [ Scott Morrison (Nov 28 2018 at 07:58)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23480%20Yoneda%20fixes/near/148693645):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> could you restart the build for <a href="https://github.com/leanprover/mathlib/issues/480" target="_blank" title="https://github.com/leanprover/mathlib/issues/480">#480</a> on travis? I've tried deleting caches, force pushing again, etc. but it won't rebuild and the error message is nonsense (because of the cache).</p>

#### [ Scott Morrison (Nov 28 2018 at 09:05)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23480%20Yoneda%20fixes/near/148696110):
<p>Ok, this is ready.<br>
It just does two small things: a few lemmas about</p>
<div class="codehilite"><pre><span></span>def ulift_functor : (Type u) ⥤ (Type (max u v))
</pre></div>


<p>and states as a separate lemma the componentwise version of the Yoneda lemma:</p>
<div class="codehilite"><pre><span></span>@[simp] def yoneda_sections (X : C) (F : Cᵒᵖ ⥤ Type v₁) : (yoneda.obj X ⟹ F) ≅ ulift.{u₁} (F.obj X)
</pre></div>


<p>Oh -- and adds the definition of <code>representable</code>, which will be needed shortly for the limits PRs.</p>


{% endraw %}
