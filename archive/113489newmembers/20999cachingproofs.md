---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/20999cachingproofs.html
---

## Stream: [new members](https://leanprover-community.github.io/archive/113489newmembers/index.html)
### Topic: [caching proofs](https://leanprover-community.github.io/archive/113489newmembers/20999cachingproofs.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Johan Commelin (Sep 18 2018 at 09:14)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/caching%20proofs/near/134149890):
<p>Re <span class="user-mention" data-user-id="110111">@Keeley Hoek</span>'s dream. ( <span class="emoji emoji-26a0" title="warning">:warning:</span> everything that follows should be taken with a fair amount of <span class="emoji emoji-1f340" title="four leaf clover">:four_leaf_clover:</span>)<br>
We now have two crawlers that spit out dependency graphs of statements in mathlib. What I wish is that this would be integrated with Lean. I don't think it is unreasonable that Lean could have some <code>cache.sqlite</code> in the root of every project. It could store dependencies there (not per file, but per statement!) and also cache proofs that have been computed by hammer/big-gun tactics.<br>
This would have the side benefit that Lean could use more fine-grained dependency management on recompilation. Currently if someone <em>adds</em> a lemma to some basic file like <code>data/list/basic.lean</code> almost half of mathlib has to be recompiled. But nothing changed! We only added a lemma!<br>
I understand that if you want reproducible builds, this might require some modification of the binary format, but that shouldn't be impossible.<br>
This recompilation could also combine this cache and proof-irrelevance. If someone changed the <em>proof</em> of a <code>Prop</code>, but left the statement alone, then one only needs to chech that the new proof is in fact a proof. But it isn't necessary to recompile everything that depended on it.<br>
Basically, when someone adds a lemma to <code>data/list/basic.lean</code> I want the recompile to be done in 5 seconds.</p>

#### [ Sean Leather (Sep 18 2018 at 09:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/caching%20proofs/near/134150071):
<p>I definitely think dependency tracking should be per-theorem and per-definition. I think the proof changing bit could probably be taken care by tracking changes to the theorem's interface (i.e. what you see with <code>set_option pp.all true</code>, <code>#check @theorem</code>).</p>

#### [ Scott Morrison (Sep 18 2018 at 09:21)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/caching%20proofs/near/134150093):
<p>Unfortunately too much proof caching becomes dangerous, especially when combined with hammers.</p>

#### [ Johan Commelin (Sep 18 2018 at 09:21)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/caching%20proofs/near/134150095):
<p>Why?</p>

#### [ Scott Morrison (Sep 18 2018 at 09:21)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/caching%20proofs/near/134150096):
<p>The problem can be that of course merely adding a lemma can't break a proof, but it can very much break a hammer.</p>

#### [ Scott Morrison (Sep 18 2018 at 09:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/caching%20proofs/near/134150141):
<p>Perhaps my hammer spends a certain amount of time searching a graph of rewrites, but has heuristics for aborting if things starting looking too bad.</p>

#### [ Sean Leather (Sep 18 2018 at 09:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/caching%20proofs/near/134150144):
<p>For example, adding a <code>@[simp]</code> theorem can change the way <code>simp</code> works?</p>

#### [ Johan Commelin (Sep 18 2018 at 09:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/caching%20proofs/near/134150145):
<p>Right, I see where this is going...</p>

#### [ Sean Leather (Sep 18 2018 at 09:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/caching%20proofs/near/134150148):
<p>That's true.</p>

#### [ Scott Morrison (Sep 18 2018 at 09:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/caching%20proofs/near/134150153):
<p>An innocuous extra lemma can cause it to waste time searching consequences of that lemma, and not only cause it to run longer, but to actually fail.</p>

#### [ Scott Morrison (Sep 18 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/caching%20proofs/near/134150166):
<p>We want to allow people to leave the big hammers in their proofs, but also to be confident these proof scripts are still correct.</p>

#### [ Scott Morrison (Sep 18 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/caching%20proofs/near/134150170):
<p>I can imagine a "two pass" compilation, which we could display e.g. with two colours of sidebars instead of the current yellow one.</p>

#### [ Scott Morrison (Sep 18 2018 at 09:24)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/caching%20proofs/near/134150213):
<p>On a first pass, we very aggressively use cached proofs, and if they work completely ignore the "expensive to check" tactic scripts.</p>

#### [ Sean Leather (Sep 18 2018 at 09:24)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/caching%20proofs/near/134150214):
<p>This leads to something I've been thinking about for a while: storing the proof structure directly to allow for fast builds.</p>

#### [ Scott Morrison (Sep 18 2018 at 09:24)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/caching%20proofs/near/134150216):
<p>On the second pass we actually check the tactic scripts still work.</p>

#### [ Scott Morrison (Sep 18 2018 at 09:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/caching%20proofs/near/134150218):
<p>By the way --- this discussion, which is great, definitely doesn't belong on this thread.</p>

#### [ Johan Commelin (Sep 18 2018 at 09:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/caching%20proofs/near/134150221):
<p>But that second pass has to go all over mathlib. Not just the 5 files that I have open.</p>

#### [ Johan Commelin (Sep 18 2018 at 09:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/caching%20proofs/near/134151223):
<p>Discussion continued here: <a href="#narrow/stream/113488-general/subject/caching.20proofs" title="#narrow/stream/113488-general/subject/caching.20proofs">https://leanprover.zulipchat.com/#narrow/stream/113488-general/subject/caching.20proofs</a></p>


{% endraw %}
