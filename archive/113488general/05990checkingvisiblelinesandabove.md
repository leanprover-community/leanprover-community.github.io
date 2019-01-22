---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/05990checkingvisiblelinesandabove.html
---

## [general](index.html)
### [checking visible lines and above](05990checkingvisiblelinesandabove.html)

#### [Kevin Buzzard (Jul 11 2018 at 16:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/checking visible lines and above/near/129473320):
Whilst the VS Code option "checking visible lines and above" is probably a useful mode to be in if you're working on a large file, for my users it causes more problems than it solves. I know how to change it to "checking visible files", but every time I open a new folder it changes back. Is there a way to globally change the default once and for all?

#### [Gabriel Ebner (Jul 11 2018 at 18:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/checking visible lines and above/near/129481006):
There is a setting to change the default.  Open user settings and search for lean to see the configuration options.

#### [Gabriel Ebner (Jul 11 2018 at 18:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/checking visible lines and above/near/129481027):
Maybe we should change the default as well given the troubles it causes.

#### [Elliott Macneil (Jul 12 2018 at 11:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/checking visible lines and above/near/129526984):
I'm looking at the user settings to change the default.
```lean 
// Set the default region of interest mode (nothing, visible, lines, linesAndAbove, open, or project) for the Lean extension.
  "lean.roiModeDefault": "linesAndAbove",
```
It doesn't seem to say what the "checking visible files" option would be - could anyone tell me what that would be?

#### [Mario Carneiro (Jul 12 2018 at 12:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/checking visible lines and above/near/129527279):
`visible` is the visible files option

