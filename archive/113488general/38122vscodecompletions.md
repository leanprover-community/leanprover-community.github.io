---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/38122vscodecompletions.html
---

## [general](index.html)
### [[vscode] completions](38122vscodecompletions.html)

#### [Edward Ayers (Aug 12 2018 at 12:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/[vscode] completions/near/131991476):
Sometimes I will type `\langle` or whatever and vscode won't underline it and I will have to delete it all and keep typing `\` until eventually the underline appears. Then when I click space it will complete. This is extremely annoying and happens every other time seemingly randomly. Are there some settings that will prevent this?

#### [Edward Ayers (Aug 12 2018 at 12:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/[vscode] completions/near/131991542):
Also is there a way to increase the delay when the completion underline dissappears? I just spent about a minute trying to get `\McC` to complete.

#### [Edward Ayers (Aug 12 2018 at 12:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/[vscode] completions/near/131991550):
Also is there a way to get the list of available completions to appear?

#### [Edward Ayers (Aug 12 2018 at 12:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/[vscode] completions/near/131991557):
Also is there a way of making tab complete the symbols?

#### [Edward Ayers (Aug 12 2018 at 12:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/[vscode] completions/near/131991606):
Is there a way of turning off the Lean inbuilt completions so I can just maintain my own snippets file?

#### [Mario Carneiro (Aug 12 2018 at 12:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/[vscode] completions/near/131991669):
VSCode will not underline the `\` if you had a selection immediately before you started typing

#### [Edward Ayers (Aug 12 2018 at 12:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/[vscode] completions/near/131991681):
I'm not observing this behavior

#### [Mario Carneiro (Aug 12 2018 at 12:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/[vscode] completions/near/131991685):
there is no delay for the completion underline - it is not time-based

#### [Mario Carneiro (Aug 12 2018 at 12:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/[vscode] completions/near/131991743):
The answer to all of your questions is "no" without hacking the extension itself

#### [Mario Carneiro (Aug 12 2018 at 12:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/[vscode] completions/near/131991752):
which might not be a bad idea, if you have a concrete plan for how to improve the situation

#### [Edward Ayers (Aug 12 2018 at 12:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/[vscode] completions/near/131991753):
[completions.mov](/user_uploads/3121/oP99rwB3Qg2dbE2Lkg6Cu6e-/completions.mov)

#### [Mario Carneiro (Aug 12 2018 at 12:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/[vscode] completions/near/131991812):
I can't replicate those behaviors

#### [Edward Ayers (Aug 12 2018 at 12:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/[vscode] completions/near/131991864):
ok I wiped my settings.json and the behaviour went away

#### [Mario Carneiro (Aug 12 2018 at 12:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/[vscode] completions/near/131991868):
what was in there?

#### [Mario Carneiro (Aug 12 2018 at 12:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/[vscode] completions/near/131991872):
do you have any other extensions?

#### [Edward Ayers (Aug 12 2018 at 12:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/[vscode] completions/near/131991875):
so something's interfering... let me slowly add the settings back in and see what the issue is

#### [Mario Carneiro (Aug 12 2018 at 12:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/[vscode] completions/near/131991888):
particularly one that messes with editor interaction like a vim mode

#### [Edward Ayers (Aug 12 2018 at 12:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/[vscode] completions/near/131992164):
`"editor.wordBasedSuggestions": false,` causes it

#### [Edward Ayers (Aug 12 2018 at 12:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/[vscode] completions/near/131992216):
`"editor.wordBasedSuggestions": true,    ` also causes it!

#### [Edward Ayers (Aug 12 2018 at 12:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/[vscode] completions/near/131992231):
So does `"editor.acceptSuggestionOnEnter": "smart",` set to any value

#### [Edward Ayers (Aug 12 2018 at 12:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/[vscode] completions/near/131992263):
setting these in `settings.json` is clobbering something that the extension needs

#### [Edward Ayers (Aug 12 2018 at 12:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/[vscode] completions/near/131992450):
Shall I open a github issue?

#### [Mario Carneiro (Aug 12 2018 at 12:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/[vscode] completions/near/131992581):
I can't replicate any effect of `editor.wordBasedSuggestions`

#### [Mario Carneiro (Aug 12 2018 at 13:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/[vscode] completions/near/131992705):
nor `editor.acceptSuggestionOnEnter`

#### [Edward Ayers (Aug 12 2018 at 13:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/[vscode] completions/near/131992714):
I figured it out. `files.autoSaveDelay : x` also needs to be set. The delay for the underline to dissappear is the same as the autosave delay

#### [Mario Carneiro (Aug 12 2018 at 13:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/[vscode] completions/near/131992781):
yeah, I'm getting that

#### [Edward Ayers (Aug 12 2018 at 13:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/[vscode] completions/near/131992786):
weird. Sorry it seemed correlated with `editor.wordBasedSuggestions` but it was just my mind playing tricks.

#### [Edward Ayers (Aug 12 2018 at 13:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/[vscode] completions/near/131992988):
I made a github issue: https://github.com/leanprover/vscode-lean/issues/80

#### [Edward Ayers (Aug 12 2018 at 13:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/[vscode] completions/near/131993069):
I thought the 500ms delay was put in intentionally and you were just supposed to type really fast!

#### [Mario Carneiro (Aug 12 2018 at 13:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/[vscode] completions/near/131993242):
I usually don't need to save so aggressively, since vscode can quit and restart without losing unsaved data

#### [Edward Ayers (Aug 12 2018 at 13:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/[vscode] completions/near/131993551):
Ok I've wopped a zero to the end of the delay time and it's utterly fabulous.

#### [Gabriel Ebner (Aug 12 2018 at 19:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/[vscode] completions/near/132004573):
Fixed in vscode-lean 0.11.14, coming to a vscode installation near you any moment now.
BTW, the vim plugin is officially supported and tested since the main extension developer uses it exclusively.

