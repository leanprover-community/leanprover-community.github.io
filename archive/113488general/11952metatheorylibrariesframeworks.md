---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/11952metatheorylibrariesframeworks.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [metatheory libraries/frameworks](https://leanprover-community.github.io/archive/113488general/11952metatheorylibrariesframeworks.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Brendan Zabarauskas (May 17 2018 at 06:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/metatheory%20libraries/frameworks/near/126680432):
<p>Hello, I was wondering if anybody was working on libraries/frameworks for making defining metatheory stuff in Lean easier. I'm thinking like LN for Coq: <a href="http://www.chargueraud.org/softs/ln/" target="_blank" title="http://www.chargueraud.org/softs/ln/">http://www.chargueraud.org/softs/ln/</a> - Context is that I'd like to prove some properties about my language Pikelet. See this issue: <a href="https://github.com/brendanzab/pikelet/issues/39" target="_blank" title="https://github.com/brendanzab/pikelet/issues/39">https://github.com/brendanzab/pikelet/issues/39</a></p>

#### [ Sean Leather (May 17 2018 at 08:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/metatheory%20libraries/frameworks/near/126682736):
<p>Hi <span class="user-mention" data-user-id="117066">@Brendan Zabarauskas</span>!</p>
<p>I'm currently working on a Lean proof of part of the Coq locally nameless library predecessor to the one you've linked to. I've forked <a href="https://github.com/spl/formal_binders" target="_blank" title="https://github.com/spl/formal_binders">that library</a> for my own reference. The reason I'm using the predecessor is because it had the Core ML typing formalization example, which seems to have been lost. (Also, are you familiar with <a href="https://github.com/plclub/metalib" target="_blank" title="https://github.com/plclub/metalib">Metalib</a>, a successor to that library?)</p>
<p><a href="https://github.com/spl/tts/" target="_blank" title="https://github.com/spl/tts/">My own work</a> is currently strictly focused on what I need to get working for my research. However, I have certainly thought about making it useful more generally. As it is, I try to push into <a href="https://github.com/leanprover/mathlib/" target="_blank" title="https://github.com/leanprover/mathlib/">mathlib</a> small improvements/additions that have helped me as I go. I think that the better mathlib gets — and it is well-maintained! — the less one needs another library.</p>
<p>All that said, it will probably be a lot of work to formalize what you need in Lean. There's a lot of existing knowledge, including libraries/frameworks, of how to do it in Coq. But I do find Lean easier to use, faster to compile, and more enjoyable. If you do plan on trying it out, you may want to take at look at <a href="https://github.com/spl/tts/" target="_blank" title="https://github.com/spl/tts/">my work</a>. It's still in progress, but I'll do my best to answer questions or help out.</p>

#### [ Brendan Zabarauskas (May 17 2018 at 08:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/metatheory%20libraries/frameworks/near/126682850):
<p>Oh cool, glad to know work is being done! I'll check out your stuff.</p>
<p>I definitely find the ergonomics of Lean much more pleasant than Coq, but the ecosystem is still lacking. In the future I will definitely start needing some kind of separation logic, but earlier on I can probably get by without (need to tackle the higher level metatheory before then).</p>

#### [ Brendan Zabarauskas (May 17 2018 at 08:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/metatheory%20libraries/frameworks/near/126682930):
<p>What in particular is interesting to look at in mathlib? I saw it before but didn't make the connection that it might have interesting things for metatheory in it.</p>

#### [ Sean Leather (May 17 2018 at 08:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/metatheory%20libraries/frameworks/near/126682973):
<p>Mathlib has a lot of basic theories and data structures. It's really like a standard library for Lean.</p>

#### [ Brendan Zabarauskas (May 17 2018 at 08:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/metatheory%20libraries/frameworks/near/126682981):
<p>Oh that's good to know. I'm guessing folks like it because it can move faster than the builtin libs?</p>

#### [ Sean Leather (May 17 2018 at 08:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/metatheory%20libraries/frameworks/near/126682982):
<p>In particular <code>data.finset</code> is very useful for my work. But the wealth of  list-related proofs (<code>data.list</code>) also make it easy to work with lists.</p>

#### [ Sean Leather (May 17 2018 at 08:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/metatheory%20libraries/frameworks/near/126683036):
<blockquote>
<p>Oh that's good to know. I'm guessing folks like it because it can move faster than the builtin libs?</p>
</blockquote>
<p>Yeah... Currently, the developers of Lean are working on the next version. They're not too keen on other changes right now. But mathlib, on the other hand, has had a lot of changes and is constantly growing.</p>

#### [ Brendan Zabarauskas (May 17 2018 at 08:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/metatheory%20libraries/frameworks/near/126683045):
<p>Are you using a locally nameless representation in tts? Also would be handy to get a quick description of what tts is. Is the README opaque by design? :P</p>

#### [ Sean Leather (May 17 2018 at 08:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/metatheory%20libraries/frameworks/near/126683047):
<p>Mathlib used to <em>be</em> the standard library before it was extracted from the Lean core.</p>

#### [ Sean Leather (May 17 2018 at 08:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/metatheory%20libraries/frameworks/near/126683052):
<p>Not by design, just by fact of me focusing on proofs and less on evangelism. <span class="emoji emoji-1f609" title="wink">:wink:</span></p>

#### [ Sean Leather (May 17 2018 at 08:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/metatheory%20libraries/frameworks/near/126683108):
<p>It's based on a let-polymorphic lambda-calculus.</p>

#### [ Sean Leather (May 17 2018 at 08:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/metatheory%20libraries/frameworks/near/126683111):
<p>Core ML is another term for it.</p>

#### [ Sean Leather (May 17 2018 at 08:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/metatheory%20libraries/frameworks/near/126683112):
<p><code>exp</code> has the expression language.</p>

#### [ Brendan Zabarauskas (May 17 2018 at 08:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/metatheory%20libraries/frameworks/near/126683114):
<p>Ah, right! Still, can be handy for folks like me searching for Lean examples on Github. I did a survey a few weeks ago, but had a hard time finding examples that I could learn off. Your work would have been super handy! &lt;3</p>

#### [ Sean Leather (May 17 2018 at 08:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/metatheory%20libraries/frameworks/near/126683126):
<p>Sorry. I've just been too busy to make it usable for others to read. I still have a lot to do.</p>

#### [ Sean Leather (May 17 2018 at 08:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/metatheory%20libraries/frameworks/near/126683180):
<p>When I'm closer to writing about it, the documentation will be a paper and/or thesis, I hope.</p>

#### [ Sean Leather (May 17 2018 at 08:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/metatheory%20libraries/frameworks/near/126683188):
<p>But, just FYI, every <code>core.lean</code> file has the definitions. Every other <code>.lean</code> file (except <code>default.lean</code>) has proofs.</p>

#### [ Brendan Zabarauskas (May 17 2018 at 08:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/metatheory%20libraries/frameworks/near/126683229):
<p>Yeah, perfectly understandable that it's a WIP. I'm cool if it's messy - don't let me looking put any pressure on your stuff. Thanks a bunch for linking! Would be neat to extract some common stuff at some stage though!</p>

#### [ Brendan Zabarauskas (May 17 2018 at 08:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/metatheory%20libraries/frameworks/near/126683233):
<p>Have you put it under a License?</p>

#### [ Sean Leather (May 17 2018 at 08:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/metatheory%20libraries/frameworks/near/126683242):
<blockquote>
<p>Would be neat to extract some common stuff at some stage though!</p>
</blockquote>
<p>Indeed. I try to put as much common stuff as I can in mathlib. There's still more of that I have planned.</p>

#### [ Brendan Zabarauskas (May 17 2018 at 08:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/metatheory%20libraries/frameworks/near/126683246):
<p>Oooh, this is super handy <span class="emoji emoji-1f44f" title="clap">:clap:</span>  <a href="https://github.com/spl/tts/blob/master/src/exp/core.lean" target="_blank" title="https://github.com/spl/tts/blob/master/src/exp/core.lean">https://github.com/spl/tts/blob/master/src/exp/core.lean</a></p>

#### [ Sean Leather (May 17 2018 at 08:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/metatheory%20libraries/frameworks/near/126683288):
<blockquote>
<p>Have you put it under a License?</p>
</blockquote>
<p>Not at the moment. I suppose I should. Apache 2.0 since that what mathlib uses? I don't feel strongly about it.</p>

#### [ Brendan Zabarauskas (May 17 2018 at 08:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/metatheory%20libraries/frameworks/near/126683359):
<p>Yeah, I normally go with Apache 2.0. Sometimes I dual license with MIT. But that's cause I'm used to the Rust ecosystem. I tend to adapt to whatever is generally accepted in the ecosystem</p>

#### [ Sean Leather (May 17 2018 at 08:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/metatheory%20libraries/frameworks/near/126683483):
<p>LICENSE added.</p>

#### [ Brendan Zabarauskas (May 17 2018 at 08:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/metatheory%20libraries/frameworks/near/126683544):
<p>Thanks! Might be a while till I actually get around to getting started on formalisation, but it's handy to have your stuff around as reference.</p>


{% endraw %}
