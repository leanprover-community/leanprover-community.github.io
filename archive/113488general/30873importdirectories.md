---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/30873importdirectories.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [import directories](https://leanprover-community.github.io/archive/113488general/30873importdirectories.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kevin Buzzard (Sep 26 2018 at 16:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/import%20directories/near/134678473):
<p>I want to get custom imports (i.e. stuff in <code>xenalib</code>) working in cocalc. Here are some dumb questions. Say I have a Lean file whose first line is an import.</p>
<p>1) If I compiled this with <code>lean --make</code> on the command line, which directories will Lean look in when looking for the import?</p>
<p>2) If I open this file in VS Code, where will Lean look, and who told it to look there?</p>
<p>3) If I open this file in cocalc, where will Lean look, and who told it to look there?</p>
<p>[The same question exists for emacs, but I don't need to know the answer]</p>

#### [ Sebastian Ullrich (Sep 26 2018 at 18:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/import%20directories/near/134685628):
<p>1) see <code>lean --path</code>, which depends on your current working directory<br>
2) same as 1), but the cwd is set to the package root if vscode-lean sees you're in a package<br>
3) I believe <span class="user-mention" data-user-id="116034">@William Stein</span> mentioned that CoCalc uses <code>~/.lean</code> as the cwd at the moment. Ideally it should use the same logic as the other editors</p>

#### [ William Stein (Sep 26 2018 at 18:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/import%20directories/near/134686203):
<blockquote>
<p>3) I believe <span class="user-mention" data-user-id="116034">@William Stein</span> mentioned that CoCalc uses <code>~/.lean</code> as the cwd</p>
</blockquote>
<p>CoCalc currently always starts the lean server in ~.   I think CoCalc should start a separate server somewhere else if you open a file such as <code>foo/bar/a.lean</code>, although I'm not 100% clear on the semantics of what to do.</p>

#### [ Sebastian Ullrich (Sep 26 2018 at 18:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/import%20directories/near/134686339):
<p>The Emacs mode uses one server for all stand-alone Lean files and a separate server per Lean package</p>

#### [ Reid Barton (Sep 26 2018 at 19:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/import%20directories/near/134691615):
<p>I tried to describe the behavior of the emacs mode earlier, on the CoCalc thread, I believe.</p>


{% endraw %}
