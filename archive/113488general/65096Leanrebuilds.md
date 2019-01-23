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
@**Sebastian Ullrich** What criterion does `leanpkg` use to decide whether a certain file has to be rebuilt or not? I'm caching `.olean` files on travis and the whole thing gets rebuilt anyway. If I also cache `.lean` files, then the rebuild is more conservative.

#### [ Gabriel Ebner (Jul 12 2018 at 00:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20re-builds/near/129504063):
It's modification time.

#### [ Simon Hudon (Jul 12 2018 at 00:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20re-builds/near/129504133):
It's curious that caching doesn't play well with that.

#### [ Simon Hudon (Jul 12 2018 at 00:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20re-builds/near/129504141):
Is the `.lean` modification time recorded inside the `.olean` file?

#### [ Gabriel Ebner (Jul 12 2018 at 00:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20re-builds/near/129504298):
No, but we also compare the olean modification times with the imports.  So the olean files need to be newer than the lean files and also in the same temporal order as the import order.

#### [ Simon Hudon (Jul 12 2018 at 01:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20re-builds/near/129506308):
Yes, I noticed that. Caching `~/.elan` became necessary for any `.olean` files to be reused at all

#### [ Mario Carneiro (Jul 17 2018 at 03:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20re-builds/near/129786566):
@**Simon Hudon** Do you know what is up with the latest build failure? https://travis-ci.org/leanprover/mathlib/jobs/404668129 It seems like `travis_long` is messing with some kind of change detection

#### [ Simon Hudon (Jul 17 2018 at 03:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20re-builds/near/129786753):
what might be happening is a sort of race condition: some builds share the same cache  (for example, the builds of the same branch) so it's possible that one build finishes its stage one, uploads its new version of the cache, then the other build does the same and then the first build tries to start its stage two. I have guarded stage two so that it fails when the binaries in the cache were built from a different commit. The only thing to do is to restart the build.

#### [ Simon Hudon (Jul 17 2018 at 03:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20re-builds/near/129786773):
One may try to remove that guard but what would happen then is that Travis would try to redo all the work of stage 1 only to fail at the end.

#### [ Simon Hudon (Jul 17 2018 at 03:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20re-builds/near/129786777):
I chose to make it fail as quickly as possible

#### [ Simon Hudon (Jul 17 2018 at 03:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20re-builds/near/129787237):
That will probably happen at time of high affluence. It's annoying but it should still be better than before. Would it make it better if it sent you an email when it happens?

#### [ Mario Carneiro (Jul 17 2018 at 03:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20re-builds/near/129787294):
I always get an email when it fails

#### [ Mario Carneiro (Jul 17 2018 at 03:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20re-builds/near/129787309):
but I've reset the build a few times and it's still not working

#### [ Simon Hudon (Jul 17 2018 at 03:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20re-builds/near/129787310):
This email would tell you its a race condition. Nothing you can't check yourself, that's true

#### [ Simon Hudon (Jul 17 2018 at 03:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20re-builds/near/129787319):
The whole build or only stage two?

#### [ Simon Hudon (Jul 17 2018 at 03:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20re-builds/near/129787399):
I'm starting to consider it might be worth letting the build restart in stage two when there's a race condition. With the cache, the build time sometimes gets much shorter than 45 minutes; it might just succeed

#### [ Mario Carneiro (Jul 17 2018 at 03:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20re-builds/near/129787441):
Does stage 1 ever use the cache?

#### [ Mario Carneiro (Jul 17 2018 at 03:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20re-builds/near/129787454):
If we give the old oleans to lean and let it sort them out we may gain a big improvement on many commits

#### [ Simon Hudon (Jul 17 2018 at 03:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20re-builds/near/129787471):
It does. but that doesn't cause significant trouble. The cache contains code and binaries. Stage 1 just discards the code from the cache and ensure the right code from `git` is used.

#### [ Simon Hudon (Jul 17 2018 at 03:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20re-builds/near/129787477):
That's actually what has been happening

#### [ Simon Hudon (Jul 17 2018 at 03:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20re-builds/near/129787579):
Ok, I'll remove the guard. That will be easier to handle.

#### [ Simon Hudon (Jul 17 2018 at 03:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Lean%20re-builds/near/129787582):
When stage 2 fails, be sure to restart the whole thing


{% endraw %}
