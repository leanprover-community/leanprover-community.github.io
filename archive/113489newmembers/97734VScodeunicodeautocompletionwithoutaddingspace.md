---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/97734VScodeunicodeautocompletionwithoutaddingspace.html
---

## Stream: [new members](index.html)
### Topic: [VS code unicode autocompletion without adding space](97734VScodeunicodeautocompletionwithoutaddingspace.html)

---

#### [Bryan Gin-ge Chen (Aug 15 2018 at 17:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/VS%20code%20unicode%20autocompletion%20without%20adding%20space/near/132179797):
Currently if I want to type `α₁` in VS Code, I type `\a` then hit space, and then hit backspace before typing `\1`+space again. Is there a way to do this without having to hit backspace all the time?

#### [Gabriel Ebner (Aug 15 2018 at 17:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/VS%20code%20unicode%20autocompletion%20without%20adding%20space/near/132180057):
You can type `\a\1 `, and `(\a\1: Type)` works as well.

#### [Gabriel Ebner (Aug 15 2018 at 17:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/VS%20code%20unicode%20autocompletion%20without%20adding%20space/near/132180112):
* Used to work, somehow it doesn't now.

#### [Patrick Massot (Aug 15 2018 at 17:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/VS%20code%20unicode%20autocompletion%20without%20adding%20space/near/132180357):
This is why I tried to ask the same question a while ago. It's clearly the single most annoying thing in VScode

#### [Patrick Massot (Aug 15 2018 at 17:14)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/VS%20code%20unicode%20autocompletion%20without%20adding%20space/near/132180446):
Do you use this when using the vim plugin?

#### [Bryan Gin-ge Chen (Aug 15 2018 at 17:18)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/VS%20code%20unicode%20autocompletion%20without%20adding%20space/near/132180667):
```quote
Do you use this when using the vim plugin?
```
Yep, and for me that would be harder to give up than dealing with this annoyance.

#### [Patrick Massot (Aug 15 2018 at 17:18)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/VS%20code%20unicode%20autocompletion%20without%20adding%20space/near/132180678):
I have this annoyance without the vim plugin

#### [Patrick Massot (Aug 15 2018 at 17:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/VS%20code%20unicode%20autocompletion%20without%20adding%20space/near/132180709):
I once tried the vim plugin and decided it was unusable, but maybe I hesitate to give it another try. Since Gabriel didn't seem to know about this problem I suddenly hoped it wasn't there with the vim plugin

#### [Gabriel Ebner (Aug 15 2018 at 17:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/VS%20code%20unicode%20autocompletion%20without%20adding%20space/near/132180771):
I only use the vim plugin and observe this problem as well.

#### [Bryan Gin-ge Chen (Aug 15 2018 at 17:23)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/VS%20code%20unicode%20autocompletion%20without%20adding%20space/near/132180923):
An ideal solution for me would be some way to trigger the replacement without moving the cursor. I would like it if either "space" would not add a space when performing a replacement, or if there were some other keybinding that did precisely that.

#### [Gabriel Ebner (Aug 15 2018 at 17:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/VS%20code%20unicode%20autocompletion%20without%20adding%20space/near/132181558):
So, `\alpha\1\2\3` works again now.  I believe this was silently broken due to an upstream change in vscode.  Thanks for pointing it out!

#### [Gabriel Ebner (Aug 15 2018 at 17:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/VS%20code%20unicode%20autocompletion%20without%20adding%20space/near/132181588):
```quote
An ideal solution for me would be some way to trigger the replacement without moving the cursor.
```
I am reluctant to reuse space for this.  Ideas for other keybindings?

#### [Bryan Gin-ge Chen (Aug 15 2018 at 17:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/VS%20code%20unicode%20autocompletion%20without%20adding%20space/near/132181669):
```quote
I am reluctant to reuse space for this.  Ideas for other keybindings?
```
shift+space maybe?

#### [Patrick Massot (Aug 15 2018 at 17:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/VS%20code%20unicode%20autocompletion%20without%20adding%20space/near/132181736):
why not tab, like in shell completion?

#### [Gabriel Ebner (Aug 15 2018 at 17:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/VS%20code%20unicode%20autocompletion%20without%20adding%20space/near/132181741):
shift+space is crazy enough that hopefully nobody uses it yet. I'll try to add it.

#### [Gabriel Ebner (Aug 15 2018 at 17:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/VS%20code%20unicode%20autocompletion%20without%20adding%20space/near/132181753):
@**Patrick Massot** tab already produces a... tab.

#### [Gabriel Ebner (Aug 15 2018 at 17:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/VS%20code%20unicode%20autocompletion%20without%20adding%20space/near/132181835):
More seriously, it's hard to hijack a key just when the input mode is active.  I can add a global keybinding for tab, but this is probably not what you want.

#### [Bryan Gin-ge Chen (Aug 15 2018 at 17:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/VS%20code%20unicode%20autocompletion%20without%20adding%20space/near/132182138):
I checked the default keybinds and shift+space seems to be unused. 

Tab would of course be nicer if you can somehow get it working. However, often the autocomplete menu is active as well, and that would eat the tab as well.  My guess is that in most situations, unicode input should win over autocomplete, but dealing with all this might be more trouble than it's worth.

#### [Patrick Massot (Aug 15 2018 at 17:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/VS%20code%20unicode%20autocompletion%20without%20adding%20space/near/132182306):
Gabriel, did you write anything about Lean+vim plugin, or do you simply activate both plugin and there is nothing more to know?

#### [Gabriel Ebner (Aug 15 2018 at 18:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/VS%20code%20unicode%20autocompletion%20without%20adding%20space/near/132183068):
I just install both plugins separately.  No configuration required.

#### [Patrick Massot (Aug 15 2018 at 18:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/VS%20code%20unicode%20autocompletion%20without%20adding%20space/near/132183084):
thanks

#### [Gabriel Ebner (Aug 15 2018 at 18:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/VS%20code%20unicode%20autocompletion%20without%20adding%20space/near/132183178):
Since everybody loves tab so much, you get tab.  Apparently you can set any property on the vscode "context" and then make keybindings conditional on these properties.  The tab keybinding is now conditional on `lean.input.isActive`.  Hope this doesn't break anything...

#### [Mario Carneiro (Aug 15 2018 at 18:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/VS%20code%20unicode%20autocompletion%20without%20adding%20space/near/132183317):
I hope that pressing tab gives you a tab (equivalent) when the underline is not active

#### [Gabriel Ebner (Aug 15 2018 at 18:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/VS%20code%20unicode%20autocompletion%20without%20adding%20space/near/132183369):
I'm not sure.  Can you check this?

#### [Mario Carneiro (Aug 15 2018 at 18:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/VS%20code%20unicode%20autocompletion%20without%20adding%20space/near/132183375):
I certainly use tab for indentation and block indentation currently

#### [Gabriel Ebner (Aug 15 2018 at 18:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/VS%20code%20unicode%20autocompletion%20without%20adding%20space/near/132183387):
Yes, of course, it works.  Tab produces a tab when there's no underline (at least on Linux)

#### [Gabriel Ebner (Aug 15 2018 at 18:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/VS%20code%20unicode%20autocompletion%20without%20adding%20space/near/132183416):
That was the whole point about the undocumented`setContext` command.

#### [Bryan Gin-ge Chen (Aug 15 2018 at 19:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/VS%20code%20unicode%20autocompletion%20without%20adding%20space/near/132186642):
Thanks again Gabriel!

