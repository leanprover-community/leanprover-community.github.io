---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/03807mathlibisbroken.html
---

## Stream: [general](index.html)
### Topic: [mathlib is broken](03807mathlibisbroken.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jan 12 2019 at 16:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20is%20broken/near/154987864):
The new Lean (merged just yesterday) breaks mathlib

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 12 2019 at 16:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20is%20broken/near/154987876):
naturally

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jan 12 2019 at 16:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20is%20broken/near/154987880):
what should we do then?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 12 2019 at 16:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20is%20broken/near/154987884):
the breakage is mostly just theorems that moved from here to there or vice versa

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 12 2019 at 16:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20is%20broken/near/154987937):
travis seems to disagree

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jan 12 2019 at 16:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20is%20broken/near/154987962):
```
$ cd /c/lean

Kenny Lau@DESKTOP-F01EMD3 MINGW64 /c/lean
$ git log -1 --pretty=oneline
92826917a252a6092cffaf5fc5f1acb1f8cef379 fix(library/module_mgr): ignore '\r' changes

Kenny Lau@DESKTOP-F01EMD3 MINGW64 /c/lean
$ cd /c/mathlib

Kenny Lau@DESKTOP-F01EMD3 MINGW64 /c/mathlib
$ git pull
Already up-to-date.

Kenny Lau@DESKTOP-F01EMD3 MINGW64 /c/mathlib
$ winpty /c/lean/bin/lean --make
C:\mathlib\tactic\mk_iff_of_inductive_prop.lean:50:9: error: unknown identifier
'drop_pis'
[...]
```

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jan 12 2019 at 16:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20is%20broken/near/154988008):
I think travis uses the old lean

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Gabriel Ebner (Jan 12 2019 at 16:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20is%20broken/near/154988014):
Travis uses the Lean version specified in leanpkg.toml.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jan 12 2019 at 16:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20is%20broken/near/154988024):
which is 3.4.1

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 12 2019 at 16:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20is%20broken/near/154988027):
in that case I think we're fine

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 12 2019 at 16:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20is%20broken/near/154988030):
we can just make an update commit at some point

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jan 12 2019 at 16:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20is%20broken/near/154988031):
so I need to refrain from using 3.4.2? I really like the `\r` fix though...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 12 2019 at 16:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20is%20broken/near/154988078):
adapting to 3.4.2 isn't totally trivial, at least we have to import the removed things and remove any mathlib patches for the bugs

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jan 12 2019 at 16:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20is%20broken/near/154988090):
https://github.com/leanprover/lean/compare/17fe3de...master

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jan 12 2019 at 16:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20is%20broken/near/154988092):
changes

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jan 12 2019 at 16:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20is%20broken/near/154988093):
I'll just go back to 3.4.1 then

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 12 2019 at 16:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20is%20broken/near/154988149):
I can't find a 3.4.2 on lean repo

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 12 2019 at 16:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20is%20broken/near/154988150):
are you sure it's released?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Jan 12 2019 at 16:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20is%20broken/near/154988152):
It's not. The nightly is.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jan 12 2019 at 16:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20is%20broken/near/154988195):
I build Lean myself

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Jan 12 2019 at 16:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20is%20broken/near/154988205):
I'm ready to release 3.4.2, but maybe someone wants to port mathlib first and make sure everything works out. With the intended branch layout, that would happen on the `master` branch while regular mathlib stays on the `3.4.1` default branch :) ...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jan 12 2019 at 16:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20is%20broken/near/154988460):
oh man imagine when Lean 4 comes out

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kenny Lau (Jan 12 2019 at 19:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20is%20broken/near/154994675):
@**Mario Carneiro** I think coinductive was removed, and I think `tactic/mk_iff_of_inductive_prop.lean` depends on it

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Bryan Gin-ge Chen (Jan 13 2019 at 23:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20is%20broken/near/155049149):
[The branch `3.4.2` in `leanprover-community/mathlib`](https://github.com/leanprover-community/mathlib/tree/3.4.2) compiles with the latest nightly Lean. I didn't commit any changes to `leanpkg.toml` so if you want to try it out, you'll have to change `3.4.1` to `nightly` after you checkout.

For reference, here are the relevant commits to base Lean [removing coinductive_predicates](https://github.com/leanprover/lean/commit/e79cb3f2c4987dcfbec8e3e15eb83837cabe1058) and [removing relators and transfer](https://github.com/leanprover/lean/commit/95fa4cfb0a8774570d67bb231c1ab088a94e12bb).

All I did was copy the old `coinductive_predicates` to `meta`, merge the old `relator` into `logic/relator`, copy `transfer` to `tactics`, and then add the necessary `import` statements. I think the only thing that was removed that hasn't been added back in this branch is the transfer-related stuff in `library/data/dlist` since it only seemed to be used in the code in `int` that was removed.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Mario Carneiro (Jan 14 2019 at 02:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20is%20broken/near/155054930):
Looks good. @**Sebastian Ullrich** , I think we are go for launch

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Bryan Gin-ge Chen (Jan 14 2019 at 15:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20is%20broken/near/155088895):
@**Mario Carneiro** I forgot to mention that the file [`tests/coinductive`](https://github.com/leanprover-community/mathlib/blob/3.4.2/tests/coinductive.lean) currently uses `#check`, `#print` and `admit`, which seems to be against mathlib style.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Abhimanyu Pallavi Sudhir (Jan 18 2019 at 16:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20is%20broken/near/156375247):
```quote
so I need to refrain from using 3.4.2? I really like the `\r` fix though...
```
 What's the `\r` fix?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Bryan Gin-ge Chen (Jan 18 2019 at 16:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20is%20broken/near/156375747):
@**Abhimanyu Pallavi Sudhir** It's a fix for an issue that windows users were having with unnecessary recompilation: see https://github.com/leanprover/lean/pull/1986

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Bryan Gin-ge Chen (Jan 18 2019 at 16:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/mathlib%20is%20broken/near/156375774):
I've PR'd the 3.4.2 branch: https://github.com/leanprover/mathlib/pull/610

