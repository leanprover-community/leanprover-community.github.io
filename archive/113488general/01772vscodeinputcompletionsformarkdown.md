---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/01772vscodeinputcompletionsformarkdown.html
---

## Stream: [general](index.html)
### Topic: [vscode input completions for markdown](01772vscodeinputcompletionsformarkdown.html)

---

#### [Edward Ayers (Sep 17 2018 at 11:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20input%20completions%20for%20markdown/near/134090703):
I love the way that Lean does unicode completions so much that I copied the vscode-lean project and made it also work for markdown. Could markdown unicode completions be added as a feature to the vscode-lean extension? Or is it better being a separate extension? Happy to submit a PR doing this.

#### [Edward Ayers (Sep 17 2018 at 11:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20input%20completions%20for%20markdown/near/134090778):
Seems like @**Gabriel Ebner** is the one to ask about this.

#### [Gabriel Ebner (Sep 17 2018 at 11:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/vscode%20input%20completions%20for%20markdown/near/134091160):
I'd prefer to keep it all in one extension if possible.  Ideally you could enable the unicode completions for specific file types and also specific files (via a command).  I'm happy about a PR for this feature.  That said, I'm on vacation until October.

