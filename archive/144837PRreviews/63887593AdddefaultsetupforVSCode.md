---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/144837PRreviews/63887593AdddefaultsetupforVSCode.html
---

## Stream: [PR reviews](index.html)
### Topic: [#593 Add default setup for VS Code](63887593AdddefaultsetupforVSCode.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Jan 14 2019 at 17:32)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23593%20Add%20default%20setup%20for%20VS%20Code/near/155096087):
I would like to propose to add a `.vscode/settings.json` file. @**Gabriel Ebner** mentioned that this may be a problem if somebody uses this file for their own personal `mathlib` settings. Is anybody using it?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jan 14 2019 at 20:45)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23593%20Add%20default%20setup%20for%20VS%20Code/near/155110758):
I don't use this. I do have a snippet file in my  `~/.config/Code/User/snippets/lean.json`. The things I use most often is my `proof` snippet that I posted last week, and snippets that write options for me, like `#implicit` that writes `"set_option pp.implicit true`. An important thing while choosing the prefix is to choose something that we wouldn't normally type, so that the snippet is VScode's first proposal. For instance `begin` is not a good prefix in order to insert a proof snippet because VScode then has to choose between completing the word "begin" and inserting the prefix. That's why I started my set_option prefixes `#implicit`, `#rewrite`, `#all`, `#instance` with a "#".

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jan 15 2019 at 09:12)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23593%20Add%20default%20setup%20for%20VS%20Code/near/155153055):
Reading the actual PR discussion I'm confused. Would this `mathlib/.vscode/settings.json` take precedence over my `$HOME/.config/Code/User/settings.json`? If yes then of course we can't do that.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Gabriel Ebner (Jan 15 2019 at 09:43)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23593%20Add%20default%20setup%20for%20VS%20Code/near/155154267):
Yes, the folder configuration in `mathlib/.vscode/settings.json` takes precedence.  That's the whole point of it: you can override your default settings with project-specific settings.
I have no idea if it also overrides workspace settings.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jan 15 2019 at 09:45)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23593%20Add%20default%20setup%20for%20VS%20Code/near/155154368):
Ok, then we need to be very careful. But in the PR I see only things that are mathlib's style rules, nothing setting the leader key (`\` vs `,`) or custom translations, so we should be ok, right?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jan 15 2019 at 09:46)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23593%20Add%20default%20setup%20for%20VS%20Code/near/155154413):
Patrick, are there specific settings you don't want overridden? Maybe `tabSize` or `rulers`?
I guess we agree that overriding `files.encoding` is correct, for example?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jan 15 2019 at 09:49)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23593%20Add%20default%20setup%20for%20VS%20Code/near/155154519):
I guess we should have only stuff that alter what is sent to mathlib, but nothing about how we produce it. So enforcing end of lines and encoding is ok, but `editor.rulers` isn't. I'm not sure what `tabSize` does. Is it only about how tab are displayed? Or do tabs get physically replaced by spaces?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Reid Barton (Jan 15 2019 at 09:49)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23593%20Add%20default%20setup%20for%20VS%20Code/near/155154532):
I was wondering about what `tabSize` does too

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Jan 15 2019 at 10:27)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23593%20Add%20default%20setup%20for%20VS%20Code/near/155156255):
`tabSize` is the amount of spaces inserted when pressing tab. Which is also the indentation we use in mathlib

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Patrick Massot (Jan 15 2019 at 11:30)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23593%20Add%20default%20setup%20for%20VS%20Code/near/155159566):
Ok, then this should be in the enforced things. But I think rulers shouldn't

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Johannes Hölzl (Jan 23 2019 at 12:52)](https://leanprover.zulipchat.com/#narrow/stream/144837-PR%20reviews/topic/%23593%20Add%20default%20setup%20for%20VS%20Code/near/156682868):
Okay, I just needed to merge another PR which had the wrong file endings. I will merge the current setup, and adopt it when people start complaining about it

