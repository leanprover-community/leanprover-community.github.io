---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/65096Leanrebuilds.html
---

## Stream: [general](index.html)
### Topic: [Lean re-builds](65096Leanrebuilds.html)

---


{% raw %}
#### [ Simon Hudon (Jul 12 2018 at 00:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20re-builds/near/129503329):
<p><span class="user-mention" data-user-id="110024">@Sebastian Ullrich</span> What criterion does <code>leanpkg</code> use to decide whether a certain file has to be rebuilt or not? I'm caching <code>.olean</code> files on travis and the whole thing gets rebuilt anyway. If I also cache <code>.lean</code> files, then the rebuild is more conservative.</p>

#### [ Gabriel Ebner (Jul 12 2018 at 00:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20re-builds/near/129504063):
<p>It's modification time.</p>

#### [ Simon Hudon (Jul 12 2018 at 00:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20re-builds/near/129504133):
<p>It's curious that caching doesn't play well with that.</p>

#### [ Simon Hudon (Jul 12 2018 at 00:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20re-builds/near/129504141):
<p>Is the <code>.lean</code> modification time recorded inside the <code>.olean</code> file?</p>

#### [ Gabriel Ebner (Jul 12 2018 at 00:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20re-builds/near/129504298):
<p>No, but we also compare the olean modification times with the imports.  So the olean files need to be newer than the lean files and also in the same temporal order as the import order.</p>

#### [ Simon Hudon (Jul 12 2018 at 01:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20re-builds/near/129506308):
<p>Yes, I noticed that. Caching <code>~/.elan</code> became necessary for any <code>.olean</code> files to be reused at all</p>

#### [ Mario Carneiro (Jul 17 2018 at 03:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20re-builds/near/129786566):
<p><span class="user-mention" data-user-id="110026">@Simon Hudon</span> Do you know what is up with the latest build failure? <a href="https://travis-ci.org/leanprover/mathlib/jobs/404668129" target="_blank" title="https://travis-ci.org/leanprover/mathlib/jobs/404668129">https://travis-ci.org/leanprover/mathlib/jobs/404668129</a> It seems like <code>travis_long</code> is messing with some kind of change detection</p>

#### [ Simon Hudon (Jul 17 2018 at 03:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20re-builds/near/129786753):
<p>what might be happening is a sort of race condition: some builds share the same cache  (for example, the builds of the same branch) so it's possible that one build finishes its stage one, uploads its new version of the cache, then the other build does the same and then the first build tries to start its stage two. I have guarded stage two so that it fails when the binaries in the cache were built from a different commit. The only thing to do is to restart the build.</p>

#### [ Simon Hudon (Jul 17 2018 at 03:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20re-builds/near/129786773):
<p>One may try to remove that guard but what would happen then is that Travis would try to redo all the work of stage 1 only to fail at the end.</p>

#### [ Simon Hudon (Jul 17 2018 at 03:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20re-builds/near/129786777):
<p>I chose to make it fail as quickly as possible</p>

#### [ Simon Hudon (Jul 17 2018 at 03:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20re-builds/near/129787237):
<p>That will probably happen at time of high affluence. It's annoying but it should still be better than before. Would it make it better if it sent you an email when it happens?</p>

#### [ Mario Carneiro (Jul 17 2018 at 03:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20re-builds/near/129787294):
<p>I always get an email when it fails</p>

#### [ Mario Carneiro (Jul 17 2018 at 03:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20re-builds/near/129787309):
<p>but I've reset the build a few times and it's still not working</p>

#### [ Simon Hudon (Jul 17 2018 at 03:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20re-builds/near/129787310):
<p>This email would tell you its a race condition. Nothing you can't check yourself, that's true</p>

#### [ Simon Hudon (Jul 17 2018 at 03:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20re-builds/near/129787319):
<p>The whole build or only stage two?</p>

#### [ Simon Hudon (Jul 17 2018 at 03:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20re-builds/near/129787399):
<p>I'm starting to consider it might be worth letting the build restart in stage two when there's a race condition. With the cache, the build time sometimes gets much shorter than 45 minutes; it might just succeed</p>

#### [ Mario Carneiro (Jul 17 2018 at 03:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20re-builds/near/129787441):
<p>Does stage 1 ever use the cache?</p>

#### [ Mario Carneiro (Jul 17 2018 at 03:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20re-builds/near/129787454):
<p>If we give the old oleans to lean and let it sort them out we may gain a big improvement on many commits</p>

#### [ Simon Hudon (Jul 17 2018 at 03:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20re-builds/near/129787471):
<p>It does. but that doesn't cause significant trouble. The cache contains code and binaries. Stage 1 just discards the code from the cache and ensure the right code from <code>git</code> is used.</p>

#### [ Simon Hudon (Jul 17 2018 at 03:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20re-builds/near/129787477):
<p>That's actually what has been happening</p>

#### [ Simon Hudon (Jul 17 2018 at 03:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20re-builds/near/129787579):
<p>Ok, I'll remove the guard. That will be easier to handle.</p>

#### [ Simon Hudon (Jul 17 2018 at 03:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20re-builds/near/129787582):
<p>When stage 2 fails, be sure to restart the whole thing</p>


{% endraw %}
