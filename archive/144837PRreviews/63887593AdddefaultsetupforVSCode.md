---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/144837PRreviews/63887593AdddefaultsetupforVSCode.html
---

## Stream: [PR reviews](https://leanprover-community.github.io/archive/144837PRreviews/index.html)
### Topic: [#593 Add default setup for VS Code](https://leanprover-community.github.io/archive/144837PRreviews/63887593AdddefaultsetupforVSCode.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Johannes Hölzl (Jan 14 2019 at 17:32)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23593%20Add%20default%20setup%20for%20VS%20Code/near/155096087):
<p>I would like to propose to add a <code>.vscode/settings.json</code> file. <span class="user-mention" data-user-id="110043">@Gabriel Ebner</span> mentioned that this may be a problem if somebody uses this file for their own personal <code>mathlib</code> settings. Is anybody using it?</p>

#### [ Patrick Massot (Jan 14 2019 at 20:45)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23593%20Add%20default%20setup%20for%20VS%20Code/near/155110758):
<p>I don't use this. I do have a snippet file in my  <code>~/.config/Code/User/snippets/lean.json</code>. The things I use most often is my <code>proof</code> snippet that I posted last week, and snippets that write options for me, like <code>#implicit</code> that writes <code>"set_option pp.implicit true</code>. An important thing while choosing the prefix is to choose something that we wouldn't normally type, so that the snippet is VScode's first proposal. For instance <code>begin</code> is not a good prefix in order to insert a proof snippet because VScode then has to choose between completing the word "begin" and inserting the prefix. That's why I started my set_option prefixes <code>#implicit</code>, <code>#rewrite</code>, <code>#all</code>, <code>#instance</code> with a "#".</p>

#### [ Patrick Massot (Jan 15 2019 at 09:12)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23593%20Add%20default%20setup%20for%20VS%20Code/near/155153055):
<p>Reading the actual PR discussion I'm confused. Would this <code>mathlib/.vscode/settings.json</code> take precedence over my <code>$HOME/.config/Code/User/settings.json</code>? If yes then of course we can't do that.</p>

#### [ Gabriel Ebner (Jan 15 2019 at 09:43)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23593%20Add%20default%20setup%20for%20VS%20Code/near/155154267):
<p>Yes, the folder configuration in <code>mathlib/.vscode/settings.json</code> takes precedence.  That's the whole point of it: you can override your default settings with project-specific settings.<br>
I have no idea if it also overrides workspace settings.</p>

#### [ Patrick Massot (Jan 15 2019 at 09:45)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23593%20Add%20default%20setup%20for%20VS%20Code/near/155154368):
<p>Ok, then we need to be very careful. But in the PR I see only things that are mathlib's style rules, nothing setting the leader key (<code>\</code> vs <code>,</code>) or custom translations, so we should be ok, right?</p>

#### [ Reid Barton (Jan 15 2019 at 09:46)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23593%20Add%20default%20setup%20for%20VS%20Code/near/155154413):
<p>Patrick, are there specific settings you don't want overridden? Maybe <code>tabSize</code> or <code>rulers</code>?<br>
I guess we agree that overriding <code>files.encoding</code> is correct, for example?</p>

#### [ Patrick Massot (Jan 15 2019 at 09:49)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23593%20Add%20default%20setup%20for%20VS%20Code/near/155154519):
<p>I guess we should have only stuff that alter what is sent to mathlib, but nothing about how we produce it. So enforcing end of lines and encoding is ok, but <code>editor.rulers</code> isn't. I'm not sure what <code>tabSize</code> does. Is it only about how tab are displayed? Or do tabs get physically replaced by spaces?</p>

#### [ Reid Barton (Jan 15 2019 at 09:49)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23593%20Add%20default%20setup%20for%20VS%20Code/near/155154532):
<p>I was wondering about what <code>tabSize</code> does too</p>

#### [ Johannes Hölzl (Jan 15 2019 at 10:27)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23593%20Add%20default%20setup%20for%20VS%20Code/near/155156255):
<p><code>tabSize</code> is the amount of spaces inserted when pressing tab. Which is also the indentation we use in mathlib</p>

#### [ Patrick Massot (Jan 15 2019 at 11:30)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23593%20Add%20default%20setup%20for%20VS%20Code/near/155159566):
<p>Ok, then this should be in the enforced things. But I think rulers shouldn't</p>

#### [ Johannes Hölzl (Jan 23 2019 at 12:52)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23593%20Add%20default%20setup%20for%20VS%20Code/near/156682868):
<p>Okay, I just needed to merge another PR which had the wrong file endings. I will merge the current setup, and adopt it when people start complaining about it</p>


{% endraw %}
