---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/144837PRreviews/09722598analysisreorganization.html
---

## Stream: [PR reviews](https://leanprover-community.github.io/archive/144837PRreviews/index.html)
### Topic: [#598 analysis reorganization](https://leanprover-community.github.io/archive/144837PRreviews/09722598analysisreorganization.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Sebastien Gouezel (Jan 17 2019 at 17:10)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23598%20analysis%20reorganization/near/155347359):
<p>I am confused: is it normal that there are still several references to <code>general_topology</code>?</p>

#### [ Patrick Massot (Jan 17 2019 at 20:13)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23598%20analysis%20reorganization/near/155360700):
<p>Arggg Lean using olean of deleted lean files is really confusing. I'm sorry about this mess</p>

#### [ Patrick Massot (Jan 17 2019 at 20:13)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23598%20analysis%20reorganization/near/155360707):
<p>I'll try again</p>

#### [ Mario Carneiro (Jan 17 2019 at 20:23)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23598%20analysis%20reorganization/near/155361577):
<p>just delete all .oleans</p>

#### [ Mario Carneiro (Jan 17 2019 at 20:45)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23598%20analysis%20reorganization/near/155363096):
<p>While we're on the topic of renaming and reorganization, is there a better name for the <code>category/</code> folder? It's not obvious what the difference between <code>category/</code> and <code>category_theory/</code> is on a first reading.</p>

#### [ Johan Commelin (Jan 17 2019 at 21:00)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23598%20analysis%20reorganization/near/155364349):
<p><code>cs_category/</code> <span class="emoji emoji-1f648" title="see no evil">:see_no_evil:</span></p>

#### [ Mario Carneiro (Jan 17 2019 at 21:01)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23598%20analysis%20reorganization/near/155364387):
<p>I was actually thinking the same thing</p>

#### [ Mario Carneiro (Jan 17 2019 at 21:02)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23598%20analysis%20reorganization/near/155364494):
<p>it seems a bit crude though, surely there's a better description. "that thing that haskellers think is a category but isn't"</p>

#### [ Johan Commelin (Jan 17 2019 at 21:02)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23598%20analysis%20reorganization/near/155364504):
<p>It also helps with tab-completion (-;</p>

#### [ Bryan Gin-ge Chen (Jan 17 2019 at 21:11)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23598%20analysis%20reorganization/near/155365107):
<p>So is it the same as what they call "Hask"?</p>

#### [ Johan Commelin (Jan 17 2019 at 21:12)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23598%20analysis%20reorganization/near/155365188):
<p>Lol, we can call the directory <code>hask/</code> to troll them (-;</p>

#### [ Mario Carneiro (Jan 17 2019 at 21:13)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23598%20analysis%20reorganization/near/155365233):
<p>yeah, have you ever read Andrej Bauer's rant on why Hask isn't a category and they should stop pretending it exists?</p>

#### [ Kevin Buzzard (Jan 17 2019 at 21:14)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23598%20analysis%20reorganization/near/155365344):
<p><a href="http://math.andrej.com/2016/08/06/hask-is-not-a-category/" target="_blank" title="http://math.andrej.com/2016/08/06/hask-is-not-a-category/">http://math.andrej.com/2016/08/06/hask-is-not-a-category/</a></p>

#### [ Bryan Gin-ge Chen (Jan 17 2019 at 21:17)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23598%20analysis%20reorganization/near/155365532):
<p>Maybe we should call it <code>not_a_category/</code> instead?</p>

#### [ Mario Carneiro (Jan 17 2019 at 21:18)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23598%20analysis%20reorganization/near/155365650):
<p><code>categoroid</code></p>

#### [ Patrick Massot (Jan 17 2019 at 21:23)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23598%20analysis%20reorganization/near/155365973):
<p>I think Travis is fighting its cache again. It complains about errors that don't exist as far as I can see</p>

#### [ Johannes Hölzl (Jan 17 2019 at 21:35)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23598%20analysis%20reorganization/near/155366751):
<p>the import namespace for Monads etc in Haskell is <code>Control</code>, so we could rename it to <code>control</code>?</p>

#### [ Patrick Massot (Jan 17 2019 at 21:55)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23598%20analysis%20reorganization/near/155368296):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> I just merged today's commts. I hope Travis will stop inventing non-existent files, but I don't see what I could do if not</p>

#### [ Mario Carneiro (Jan 17 2019 at 21:56)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23598%20analysis%20reorganization/near/155368363):
<p>I just cleared the cache and restarted the build for your PR, so it should work this time</p>

#### [ Patrick Massot (Jan 17 2019 at 21:56)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23598%20analysis%20reorganization/near/155368377):
<p>Ok, thanks</p>

#### [ Patrick Massot (Jan 18 2019 at 10:02)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23598%20analysis%20reorganization/near/156353639):
<p>Travis is now happy, I think you can merge now</p>

#### [ Johannes Hölzl (Jan 18 2019 at 11:13)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23598%20analysis%20reorganization/near/156357499):
<p>merged</p>

#### [ Johannes Hölzl (Jan 18 2019 at 11:31)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23598%20analysis%20reorganization/near/156358360):
<p>the build failed, but I think this was due to the cache. (I think) I cleared the chache, and restarted it now</p>

#### [ Mario Carneiro (Jan 18 2019 at 11:32)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23598%20analysis%20reorganization/near/156358441):
<p>note: if you clear the PR cache, it falls back on the main cache (master), so you have to clear that too</p>

#### [ Mario Carneiro (Jan 18 2019 at 11:33)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23598%20analysis%20reorganization/near/156358462):
<p>I discovered this after my first attempts to rebuild the PR failed</p>

#### [ Johannes Hölzl (Jan 18 2019 at 11:46)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23598%20analysis%20reorganization/near/156359224):
<p>ah good to now. But I think I cleared the master cache anyway. The failure is happening at the master branch</p>

#### [ Patrick Massot (Jan 18 2019 at 12:50)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23598%20analysis%20reorganization/near/156362168):
<p>Now it works on the main repository, but fails on lean-community...</p>

#### [ Simon Hudon (Jan 18 2019 at 20:46)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23598%20analysis%20reorganization/near/156394463):
<p>On the subject of Hask, I think the point may be valid but what we have in Lean actually looks like a category. We do not need to denounce it here. We could put everything in <code>category_theory.types</code> and generalize over time.</p>

#### [ Simon Hudon (Jan 18 2019 at 20:47)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23598%20analysis%20reorganization/near/156394513):
<p>I have a general definition for monad and applicative functors in my files so it should be coming soon ... right after we agree on a definition of monoidal categories</p>

#### [ Johan Commelin (Jan 18 2019 at 20:47)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23598%20analysis%20reorganization/near/156394520):
<p>Except that your functors aren't functors!</p>

#### [ Simon Hudon (Jan 18 2019 at 20:53)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23598%20analysis%20reorganization/near/156394907):
<p>That's a minor terminology detail. You can <code>functor</code> + <code>is_lawful_functor</code> as our notion of functor and that's fixed</p>

#### [ Mario Carneiro (Jan 18 2019 at 21:01)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23598%20analysis%20reorganization/near/156395489):
<p>The question is what to call the structure built on <code>functor</code> alone</p>

#### [ Simon Hudon (Jan 18 2019 at 21:04)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23598%20analysis%20reorganization/near/156395682):
<p>A while back, you proposed <code>functor_struct</code> (in the context of <code>category</code>, actually)</p>

#### [ Mario Carneiro (Jan 18 2019 at 21:08)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23598%20analysis%20reorganization/near/156395950):
<p>and you want that to be the folder name?</p>


{% endraw %}
