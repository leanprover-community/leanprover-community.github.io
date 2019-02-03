---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/38122vscodecompletions.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [[vscode] completions](https://leanprover-community.github.io/archive/113488general/38122vscodecompletions.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Edward Ayers (Aug 12 2018 at 12:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%5Bvscode%5D%20completions/near/131991476):
<p>Sometimes I will type <code>\langle</code> or whatever and vscode won't underline it and I will have to delete it all and keep typing <code>\</code> until eventually the underline appears. Then when I click space it will complete. This is extremely annoying and happens every other time seemingly randomly. Are there some settings that will prevent this?</p>

#### [ Edward Ayers (Aug 12 2018 at 12:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%5Bvscode%5D%20completions/near/131991542):
<p>Also is there a way to increase the delay when the completion underline dissappears? I just spent about a minute trying to get <code>\McC</code> to complete.</p>

#### [ Edward Ayers (Aug 12 2018 at 12:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%5Bvscode%5D%20completions/near/131991550):
<p>Also is there a way to get the list of available completions to appear?</p>

#### [ Edward Ayers (Aug 12 2018 at 12:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%5Bvscode%5D%20completions/near/131991557):
<p>Also is there a way of making tab complete the symbols?</p>

#### [ Edward Ayers (Aug 12 2018 at 12:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%5Bvscode%5D%20completions/near/131991606):
<p>Is there a way of turning off the Lean inbuilt completions so I can just maintain my own snippets file?</p>

#### [ Mario Carneiro (Aug 12 2018 at 12:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%5Bvscode%5D%20completions/near/131991669):
<p>VSCode will not underline the <code>\</code> if you had a selection immediately before you started typing</p>

#### [ Edward Ayers (Aug 12 2018 at 12:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%5Bvscode%5D%20completions/near/131991681):
<p>I'm not observing this behavior</p>

#### [ Mario Carneiro (Aug 12 2018 at 12:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%5Bvscode%5D%20completions/near/131991685):
<p>there is no delay for the completion underline - it is not time-based</p>

#### [ Mario Carneiro (Aug 12 2018 at 12:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%5Bvscode%5D%20completions/near/131991743):
<p>The answer to all of your questions is "no" without hacking the extension itself</p>

#### [ Mario Carneiro (Aug 12 2018 at 12:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%5Bvscode%5D%20completions/near/131991752):
<p>which might not be a bad idea, if you have a concrete plan for how to improve the situation</p>

#### [ Edward Ayers (Aug 12 2018 at 12:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%5Bvscode%5D%20completions/near/131991753):
<p><a href="/user_uploads/3121/oP99rwB3Qg2dbE2Lkg6Cu6e-/completions.mov" target="_blank" title="completions.mov">completions.mov</a></p>

#### [ Mario Carneiro (Aug 12 2018 at 12:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%5Bvscode%5D%20completions/near/131991812):
<p>I can't replicate those behaviors</p>

#### [ Edward Ayers (Aug 12 2018 at 12:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%5Bvscode%5D%20completions/near/131991864):
<p>ok I wiped my settings.json and the behaviour went away</p>

#### [ Mario Carneiro (Aug 12 2018 at 12:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%5Bvscode%5D%20completions/near/131991868):
<p>what was in there?</p>

#### [ Mario Carneiro (Aug 12 2018 at 12:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%5Bvscode%5D%20completions/near/131991872):
<p>do you have any other extensions?</p>

#### [ Edward Ayers (Aug 12 2018 at 12:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%5Bvscode%5D%20completions/near/131991875):
<p>so something's interfering... let me slowly add the settings back in and see what the issue is</p>

#### [ Mario Carneiro (Aug 12 2018 at 12:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%5Bvscode%5D%20completions/near/131991888):
<p>particularly one that messes with editor interaction like a vim mode</p>

#### [ Edward Ayers (Aug 12 2018 at 12:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%5Bvscode%5D%20completions/near/131992164):
<p><code>"editor.wordBasedSuggestions": false,</code> causes it</p>

#### [ Edward Ayers (Aug 12 2018 at 12:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%5Bvscode%5D%20completions/near/131992216):
<p><code>"editor.wordBasedSuggestions": true,    </code> also causes it!</p>

#### [ Edward Ayers (Aug 12 2018 at 12:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%5Bvscode%5D%20completions/near/131992231):
<p>So does <code>"editor.acceptSuggestionOnEnter": "smart",</code> set to any value</p>

#### [ Edward Ayers (Aug 12 2018 at 12:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%5Bvscode%5D%20completions/near/131992263):
<p>setting these in <code>settings.json</code> is clobbering something that the extension needs</p>

#### [ Edward Ayers (Aug 12 2018 at 12:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%5Bvscode%5D%20completions/near/131992450):
<p>Shall I open a github issue?</p>

#### [ Mario Carneiro (Aug 12 2018 at 12:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%5Bvscode%5D%20completions/near/131992581):
<p>I can't replicate any effect of <code>editor.wordBasedSuggestions</code></p>

#### [ Mario Carneiro (Aug 12 2018 at 13:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%5Bvscode%5D%20completions/near/131992705):
<p>nor <code>editor.acceptSuggestionOnEnter</code></p>

#### [ Edward Ayers (Aug 12 2018 at 13:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%5Bvscode%5D%20completions/near/131992714):
<p>I figured it out. <code>files.autoSaveDelay : x</code> also needs to be set. The delay for the underline to dissappear is the same as the autosave delay</p>

#### [ Mario Carneiro (Aug 12 2018 at 13:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%5Bvscode%5D%20completions/near/131992781):
<p>yeah, I'm getting that</p>

#### [ Edward Ayers (Aug 12 2018 at 13:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%5Bvscode%5D%20completions/near/131992786):
<p>weird. Sorry it seemed correlated with <code>editor.wordBasedSuggestions</code> but it was just my mind playing tricks.</p>

#### [ Edward Ayers (Aug 12 2018 at 13:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%5Bvscode%5D%20completions/near/131992988):
<p>I made a github issue: <a href="https://github.com/leanprover/vscode-lean/issues/80" target="_blank" title="https://github.com/leanprover/vscode-lean/issues/80">https://github.com/leanprover/vscode-lean/issues/80</a></p>

#### [ Edward Ayers (Aug 12 2018 at 13:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%5Bvscode%5D%20completions/near/131993069):
<p>I thought the 500ms delay was put in intentionally and you were just supposed to type really fast!</p>

#### [ Mario Carneiro (Aug 12 2018 at 13:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%5Bvscode%5D%20completions/near/131993242):
<p>I usually don't need to save so aggressively, since vscode can quit and restart without losing unsaved data</p>

#### [ Edward Ayers (Aug 12 2018 at 13:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%5Bvscode%5D%20completions/near/131993551):
<p>Ok I've wopped a zero to the end of the delay time and it's utterly fabulous.</p>

#### [ Gabriel Ebner (Aug 12 2018 at 19:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/%5Bvscode%5D%20completions/near/132004573):
<p>Fixed in vscode-lean 0.11.14, coming to a vscode installation near you any moment now.<br>
BTW, the vim plugin is officially supported and tested since the main extension developer uses it exclusively.</p>


{% endraw %}
