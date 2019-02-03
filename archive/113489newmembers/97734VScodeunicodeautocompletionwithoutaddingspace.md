---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/97734VScodeunicodeautocompletionwithoutaddingspace.html
---

## Stream: [new members](index.html)
### Topic: [VS code unicode autocompletion without adding space](97734VScodeunicodeautocompletionwithoutaddingspace.html)

---


{% raw %}
#### [ Bryan Gin-ge Chen (Aug 15 2018 at 17:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/VS%20code%20unicode%20autocompletion%20without%20adding%20space/near/132179797):
<p>Currently if I want to type <code>α₁</code> in VS Code, I type <code>\a</code> then hit space, and then hit backspace before typing <code>\1</code>+space again. Is there a way to do this without having to hit backspace all the time?</p>

#### [ Gabriel Ebner (Aug 15 2018 at 17:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/VS%20code%20unicode%20autocompletion%20without%20adding%20space/near/132180057):
<p>You can type <code>\a\1 </code>, and <code>(\a\1: Type)</code> works as well.</p>

#### [ Gabriel Ebner (Aug 15 2018 at 17:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/VS%20code%20unicode%20autocompletion%20without%20adding%20space/near/132180112):
<ul>
<li>Used to work, somehow it doesn't now.</li>
</ul>

#### [ Patrick Massot (Aug 15 2018 at 17:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/VS%20code%20unicode%20autocompletion%20without%20adding%20space/near/132180357):
<p>This is why I tried to ask the same question a while ago. It's clearly the single most annoying thing in VScode</p>

#### [ Patrick Massot (Aug 15 2018 at 17:14)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/VS%20code%20unicode%20autocompletion%20without%20adding%20space/near/132180446):
<p>Do you use this when using the vim plugin?</p>

#### [ Bryan Gin-ge Chen (Aug 15 2018 at 17:18)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/VS%20code%20unicode%20autocompletion%20without%20adding%20space/near/132180667):
<blockquote>
<p>Do you use this when using the vim plugin?</p>
</blockquote>
<p>Yep, and for me that would be harder to give up than dealing with this annoyance.</p>

#### [ Patrick Massot (Aug 15 2018 at 17:18)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/VS%20code%20unicode%20autocompletion%20without%20adding%20space/near/132180678):
<p>I have this annoyance without the vim plugin</p>

#### [ Patrick Massot (Aug 15 2018 at 17:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/VS%20code%20unicode%20autocompletion%20without%20adding%20space/near/132180709):
<p>I once tried the vim plugin and decided it was unusable, but maybe I hesitate to give it another try. Since Gabriel didn't seem to know about this problem I suddenly hoped it wasn't there with the vim plugin</p>

#### [ Gabriel Ebner (Aug 15 2018 at 17:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/VS%20code%20unicode%20autocompletion%20without%20adding%20space/near/132180771):
<p>I only use the vim plugin and observe this problem as well.</p>

#### [ Bryan Gin-ge Chen (Aug 15 2018 at 17:23)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/VS%20code%20unicode%20autocompletion%20without%20adding%20space/near/132180923):
<p>An ideal solution for me would be some way to trigger the replacement without moving the cursor. I would like it if either "space" would not add a space when performing a replacement, or if there were some other keybinding that did precisely that.</p>

#### [ Gabriel Ebner (Aug 15 2018 at 17:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/VS%20code%20unicode%20autocompletion%20without%20adding%20space/near/132181558):
<p>So, <code>\alpha\1\2\3</code> works again now.  I believe this was silently broken due to an upstream change in vscode.  Thanks for pointing it out!</p>

#### [ Gabriel Ebner (Aug 15 2018 at 17:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/VS%20code%20unicode%20autocompletion%20without%20adding%20space/near/132181588):
<blockquote>
<p>An ideal solution for me would be some way to trigger the replacement without moving the cursor.</p>
</blockquote>
<p>I am reluctant to reuse space for this.  Ideas for other keybindings?</p>

#### [ Bryan Gin-ge Chen (Aug 15 2018 at 17:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/VS%20code%20unicode%20autocompletion%20without%20adding%20space/near/132181669):
<blockquote>
<p>I am reluctant to reuse space for this.  Ideas for other keybindings?</p>
</blockquote>
<p>shift+space maybe?</p>

#### [ Patrick Massot (Aug 15 2018 at 17:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/VS%20code%20unicode%20autocompletion%20without%20adding%20space/near/132181736):
<p>why not tab, like in shell completion?</p>

#### [ Gabriel Ebner (Aug 15 2018 at 17:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/VS%20code%20unicode%20autocompletion%20without%20adding%20space/near/132181741):
<p>shift+space is crazy enough that hopefully nobody uses it yet. I'll try to add it.</p>

#### [ Gabriel Ebner (Aug 15 2018 at 17:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/VS%20code%20unicode%20autocompletion%20without%20adding%20space/near/132181753):
<p><span class="user-mention" data-user-id="110031">@Patrick Massot</span> tab already produces a... tab.</p>

#### [ Gabriel Ebner (Aug 15 2018 at 17:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/VS%20code%20unicode%20autocompletion%20without%20adding%20space/near/132181835):
<p>More seriously, it's hard to hijack a key just when the input mode is active.  I can add a global keybinding for tab, but this is probably not what you want.</p>

#### [ Bryan Gin-ge Chen (Aug 15 2018 at 17:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/VS%20code%20unicode%20autocompletion%20without%20adding%20space/near/132182138):
<p>I checked the default keybinds and shift+space seems to be unused. </p>
<p>Tab would of course be nicer if you can somehow get it working. However, often the autocomplete menu is active as well, and that would eat the tab as well.  My guess is that in most situations, unicode input should win over autocomplete, but dealing with all this might be more trouble than it's worth.</p>

#### [ Patrick Massot (Aug 15 2018 at 17:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/VS%20code%20unicode%20autocompletion%20without%20adding%20space/near/132182306):
<p>Gabriel, did you write anything about Lean+vim plugin, or do you simply activate both plugin and there is nothing more to know?</p>

#### [ Gabriel Ebner (Aug 15 2018 at 18:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/VS%20code%20unicode%20autocompletion%20without%20adding%20space/near/132183068):
<p>I just install both plugins separately.  No configuration required.</p>

#### [ Patrick Massot (Aug 15 2018 at 18:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/VS%20code%20unicode%20autocompletion%20without%20adding%20space/near/132183084):
<p>thanks</p>

#### [ Gabriel Ebner (Aug 15 2018 at 18:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/VS%20code%20unicode%20autocompletion%20without%20adding%20space/near/132183178):
<p>Since everybody loves tab so much, you get tab.  Apparently you can set any property on the vscode "context" and then make keybindings conditional on these properties.  The tab keybinding is now conditional on <code>lean.input.isActive</code>.  Hope this doesn't break anything...</p>

#### [ Mario Carneiro (Aug 15 2018 at 18:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/VS%20code%20unicode%20autocompletion%20without%20adding%20space/near/132183317):
<p>I hope that pressing tab gives you a tab (equivalent) when the underline is not active</p>

#### [ Gabriel Ebner (Aug 15 2018 at 18:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/VS%20code%20unicode%20autocompletion%20without%20adding%20space/near/132183369):
<p>I'm not sure.  Can you check this?</p>

#### [ Mario Carneiro (Aug 15 2018 at 18:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/VS%20code%20unicode%20autocompletion%20without%20adding%20space/near/132183375):
<p>I certainly use tab for indentation and block indentation currently</p>

#### [ Gabriel Ebner (Aug 15 2018 at 18:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/VS%20code%20unicode%20autocompletion%20without%20adding%20space/near/132183387):
<p>Yes, of course, it works.  Tab produces a tab when there's no underline (at least on Linux)</p>

#### [ Gabriel Ebner (Aug 15 2018 at 18:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/VS%20code%20unicode%20autocompletion%20without%20adding%20space/near/132183416):
<p>That was the whole point about the undocumented<code>setContext</code> command.</p>

#### [ Bryan Gin-ge Chen (Aug 15 2018 at 19:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/VS%20code%20unicode%20autocompletion%20without%20adding%20space/near/132186642):
<p>Thanks again Gabriel!</p>


{% endraw %}
