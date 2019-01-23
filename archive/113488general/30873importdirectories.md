---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/30873importdirectories.html
---

## Stream: [general](index.html)
### Topic: [import directories](30873importdirectories.html)

---


{% raw %}
#### [ Kevin Buzzard (Sep 26 2018 at 16:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/import%20directories/near/134678473):
I want to get custom imports (i.e. stuff in `xenalib`) working in cocalc. Here are some dumb questions. Say I have a Lean file whose first line is an import.

1) If I compiled this with `lean --make` on the command line, which directories will Lean look in when looking for the import?

2) If I open this file in VS Code, where will Lean look, and who told it to look there?

3) If I open this file in cocalc, where will Lean look, and who told it to look there?

[The same question exists for emacs, but I don't need to know the answer]

#### [ Sebastian Ullrich (Sep 26 2018 at 18:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/import%20directories/near/134685628):
1) see `lean --path`, which depends on your current working directory
2) same as 1), but the cwd is set to the package root if vscode-lean sees you're in a package
3) I believe @**William Stein** mentioned that CoCalc uses `~/.lean` as the cwd at the moment. Ideally it should use the same logic as the other editors

#### [ William Stein (Sep 26 2018 at 18:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/import%20directories/near/134686203):
```quote
3) I believe @**William Stein** mentioned that CoCalc uses `~/.lean` as the cwd
```

CoCalc currently always starts the lean server in ~.   I think CoCalc should start a separate server somewhere else if you open a file such as `foo/bar/a.lean`, although I'm not 100% clear on the semantics of what to do.

#### [ Sebastian Ullrich (Sep 26 2018 at 18:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/import%20directories/near/134686339):
The Emacs mode uses one server for all stand-alone Lean files and a separate server per Lean package

#### [ Reid Barton (Sep 26 2018 at 19:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/import%20directories/near/134691615):
I tried to describe the behavior of the emacs mode earlier, on the CoCalc thread, I believe.


{% endraw %}
