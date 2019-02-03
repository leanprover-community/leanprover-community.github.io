---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/39667UnicodeinZulip.html
---

## Stream: [general](index.html)
### Topic: [Unicode in Zulip](39667UnicodeinZulip.html)

---


{% raw %}
#### [ Johan Commelin (Apr 11 2018 at 20:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unicode%20in%20Zulip/near/124944729):
<p>Quick question: how do I comfortably input unicode in Zulip? So far I have used copy-paste to write alphas and betas. In VS code these are magically replaced with unicode... in the rest of my life TeX does this for me. How do I get them here?</p>

#### [ Mario Carneiro (Apr 11 2018 at 20:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unicode%20in%20Zulip/near/124944838):
<p>You can use tex here, although it gets math font: $\alpha$</p>

#### [ Johan Commelin (Apr 11 2018 at 20:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unicode%20in%20Zulip/near/124945053):
<p>Ok, thanks.</p>

#### [ Johan Commelin (Apr 11 2018 at 20:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unicode%20in%20Zulip/near/124945057):
<p>Test: <code>$\alpha$</code> $\alpha$</p>

#### [ Johan Commelin (Apr 11 2018 at 20:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unicode%20in%20Zulip/near/124945064):
<p>Hmm, neither do what I want...</p>

#### [ Johan Commelin (Apr 11 2018 at 20:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unicode%20in%20Zulip/near/124945076):
<p>How do you input an alpha in code? So between back-ticks?</p>

#### [ Johan Commelin (Apr 11 2018 at 20:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unicode%20in%20Zulip/near/124945123):
<p>Test: <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>α</mi></mrow><annotation encoding="application/x-tex">\alpha</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.43056em;"></span><span class="strut bottom" style="height:0.43056em;vertical-align:0em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.0037em;">α</span></span></span></span></p>

#### [ Patrick Massot (Apr 11 2018 at 21:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unicode%20in%20Zulip/near/124945238):
<p>I use <a href="https://github.com/docwhat/itsalltext/tree/release-1.9.3#readme" target="_blank" title="https://github.com/docwhat/itsalltext/tree/release-1.9.3#readme">https://github.com/docwhat/itsalltext/tree/release-1.9.3#readme</a> It gives me a small "edit" button near textareas in firefox. Clicking this button fires vim and you can type whatever you want</p>

#### [ Patrick Massot (Apr 11 2018 at 21:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unicode%20in%20Zulip/near/124945245):
<p>Of course you can also configure it to fire emacs if that's your religion</p>

#### [ Johan Commelin (Apr 11 2018 at 21:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unicode%20in%20Zulip/near/124945289):
<p>No, I'm a vimmer. But I never input alphas directly into vim...</p>

#### [ Johan Commelin (Apr 11 2018 at 21:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unicode%20in%20Zulip/near/124945292):
<p>I was an ascii-only guy, until I met Lean</p>

#### [ Johan Commelin (Apr 11 2018 at 21:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unicode%20in%20Zulip/near/124945364):
<p>At some point, someone will formalise Fermat's last theorem in Lean</p>

#### [ Patrick Massot (Apr 11 2018 at 21:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unicode%20in%20Zulip/near/124945365):
<p>Then you should go and configure your vim to make you a unicode guy</p>

#### [ Johan Commelin (Apr 11 2018 at 21:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unicode%20in%20Zulip/near/124945366):
<p>And it will take us 5 years to figure out that they spoofed us with an punycode attack: <a href="https://en.wikipedia.org/wiki/IDN_homograph_attack" target="_blank" title="https://en.wikipedia.org/wiki/IDN_homograph_attack">https://en.wikipedia.org/wiki/IDN_homograph_attack</a></p>

#### [ Johan Commelin (Apr 11 2018 at 21:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unicode%20in%20Zulip/near/124945386):
<p>Importing some library whose name looks completely familiar, but inside the library they do just assume false...</p>

#### [ Patrick Massot (Apr 11 2018 at 21:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unicode%20in%20Zulip/near/124945909):
<p>I think Kevin decided we weren't formalizing FLT in the end</p>

#### [ Patrick Massot (Apr 11 2018 at 21:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unicode%20in%20Zulip/near/124945950):
<p>This is too old</p>

#### [ Patrick Massot (Apr 11 2018 at 21:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unicode%20in%20Zulip/near/124945952):
<p>He works on perfectoid spaces</p>

#### [ Johan Commelin (Apr 11 2018 at 21:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unicode%20in%20Zulip/near/124946277):
<p>The problem remains... whether you are formalising the latest hotness in the Langlands program, or some hardcore <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi mathvariant="normal">∞</mi></mrow><annotation encoding="application/x-tex">\infty</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.43056em;"></span><span class="strut bottom" style="height:0.43056em;vertical-align:0em;"></span><span class="base"><span class="mord mathrm">∞</span></span></span></span>-stuff, or something from quantisation-blabla... unicode is ambiguous and susceptible to social attacks...</p>

#### [ Johan Commelin (Apr 11 2018 at 21:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unicode%20in%20Zulip/near/124946280):
<p>Anyway, I will stuff away my tinfoil hat... enough other problems to focus on right now (^;</p>

#### [ Kevin Buzzard (Apr 11 2018 at 21:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unicode%20in%20Zulip/near/124946716):
<p>I don't think it's too difficult to formalise. The proof might be harder though.</p>

#### [ Kevin Buzzard (Apr 11 2018 at 21:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unicode%20in%20Zulip/near/124946769):
<p>The thing about the proof is that there is a huge amount of analysis that goes into the trace formula</p>

#### [ Kevin Buzzard (Apr 11 2018 at 21:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unicode%20in%20Zulip/near/124946776):
<p>and I know of no proof which ultimately avoids the trace formula</p>

#### [ Kevin Buzzard (Apr 11 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unicode%20in%20Zulip/near/124946781):
<p>in the non-compact case I should add -- SL(2).</p>

#### [ Patrick Massot (Apr 11 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unicode%20in%20Zulip/near/124946789):
<p><a href="https://github.com/formalabstracts/formalabstracts/blob/master/fabstract/Wiles_A_and_Taylor_R_FermatLast/fabstract.lean" target="_blank" title="https://github.com/formalabstracts/formalabstracts/blob/master/fabstract/Wiles_A_and_Taylor_R_FermatLast/fabstract.lean">https://github.com/formalabstracts/formalabstracts/blob/master/fabstract/Wiles_A_and_Taylor_R_FermatLast/fabstract.lean</a></p>

#### [ Kevin Buzzard (Apr 11 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unicode%20in%20Zulip/near/124946791):
<p>It's the one part of the proof I've not read and it would not surprise me if I went to my grave not having read it.</p>

#### [ Kevin Buzzard (Apr 11 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unicode%20in%20Zulip/near/124946794):
<p>Unless EPSRC give me several million quid to formalise it.</p>

#### [ Patrick Massot (Apr 11 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unicode%20in%20Zulip/near/124946796):
<p>Statement is already done <span class="emoji emoji-1f604" title="smile">:smile:</span></p>

#### [ Kevin Buzzard (Apr 11 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unicode%20in%20Zulip/near/124946798):
<p>Oh OK that's great, we're half way there.</p>

#### [ Patrick Massot (Apr 11 2018 at 21:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unicode%20in%20Zulip/near/124946836):
<p>Indeed</p>

#### [ Johan Commelin (Apr 11 2018 at 21:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unicode%20in%20Zulip/near/124946850):
<p>Lol, they have a type called <code>document</code></p>

#### [ Johan Commelin (Apr 11 2018 at 21:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unicode%20in%20Zulip/near/124946855):
<p>That's fantastic (^;</p>


{% endraw %}
