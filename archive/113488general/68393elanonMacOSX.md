---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/68393elanonMacOSX.html
---

## Stream: [general](index.html)
### Topic: [elan on MacOSX](68393elanonMacOSX.html)

---

#### [Simon Hudon (Apr 15 2018 at 20:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elan%20on%20MacOSX/near/125118341):
I'm giving another try for elan and here is what happens when I install `nightly`:

```
$ elan toolchain install nightly
info: syncing channel updates for 'nightly'
error: failed to resolve latest version of 'nightly'
info: caused by: failed to parse latest release tag
```

#### [Simon Hudon (Apr 15 2018 at 20:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elan%20on%20MacOSX/near/125118388):
Is this because of OSX or because of the latest nightly?

#### [Sebastian Ullrich (Apr 16 2018 at 09:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elan%20on%20MacOSX/near/125138749):
@**Simon Hudon** Oops... should be fixed in 0.3.4

#### [Simon Hudon (Apr 16 2018 at 13:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elan%20on%20MacOSX/near/125145662):
Thanks! I'm really like elan by the way

#### [Kenny Lau (Apr 16 2018 at 13:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elan%20on%20MacOSX/near/125145665):
my antivirus doesn't like elan though

#### [Sebastian Ullrich (Apr 16 2018 at 13:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elan%20on%20MacOSX/near/125145666):
Well, elan doesn't like your antivirus either

#### [Sebastian Ullrich (Apr 16 2018 at 13:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/elan%20on%20MacOSX/near/125145673):
Like, there is literally nothing I can do :) . You could try to send them the executable as a false positive and tell them to get their act together.

