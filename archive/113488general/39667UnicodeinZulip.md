---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/39667UnicodeinZulip.html
---

## [general](index.html)
### [Unicode in Zulip](39667UnicodeinZulip.html)

#### [Johan Commelin (Apr 11 2018 at 20:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unicode in Zulip/near/124944729):
Quick question: how do I comfortably input unicode in Zulip? So far I have used copy-paste to write alphas and betas. In VS code these are magically replaced with unicode... in the rest of my life TeX does this for me. How do I get them here?

#### [Mario Carneiro (Apr 11 2018 at 20:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unicode in Zulip/near/124944838):
You can use tex here, although it gets math font: $\alpha$

#### [Johan Commelin (Apr 11 2018 at 20:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unicode in Zulip/near/124945053):
Ok, thanks.

#### [Johan Commelin (Apr 11 2018 at 20:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unicode in Zulip/near/124945057):
Test: `$\alpha$` $\alpha$

#### [Johan Commelin (Apr 11 2018 at 20:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unicode in Zulip/near/124945064):
Hmm, neither do what I want...

#### [Johan Commelin (Apr 11 2018 at 20:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unicode in Zulip/near/124945076):
How do you input an alpha in code? So between back-ticks?

#### [Johan Commelin (Apr 11 2018 at 20:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unicode in Zulip/near/124945123):
Test: $$\alpha$$

#### [Patrick Massot (Apr 11 2018 at 21:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unicode in Zulip/near/124945238):
I use https://github.com/docwhat/itsalltext/tree/release-1.9.3#readme It gives me a small "edit" button near textareas in firefox. Clicking this button fires vim and you can type whatever you want

#### [Patrick Massot (Apr 11 2018 at 21:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unicode in Zulip/near/124945245):
Of course you can also configure it to fire emacs if that's your religion

#### [Johan Commelin (Apr 11 2018 at 21:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unicode in Zulip/near/124945289):
No, I'm a vimmer. But I never input alphas directly into vim...

#### [Johan Commelin (Apr 11 2018 at 21:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unicode in Zulip/near/124945292):
I was an ascii-only guy, until I met Lean

#### [Johan Commelin (Apr 11 2018 at 21:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unicode in Zulip/near/124945364):
At some point, someone will formalise Fermat's last theorem in Lean

#### [Patrick Massot (Apr 11 2018 at 21:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unicode in Zulip/near/124945365):
Then you should go and configure your vim to make you a unicode guy

#### [Johan Commelin (Apr 11 2018 at 21:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unicode in Zulip/near/124945366):
And it will take us 5 years to figure out that they spoofed us with an punycode attack: https://en.wikipedia.org/wiki/IDN_homograph_attack

#### [Johan Commelin (Apr 11 2018 at 21:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unicode in Zulip/near/124945386):
Importing some library whose name looks completely familiar, but inside the library they do just assume false...

#### [Patrick Massot (Apr 11 2018 at 21:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unicode in Zulip/near/124945909):
I think Kevin decided we weren't formalizing FLT in the end

#### [Patrick Massot (Apr 11 2018 at 21:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unicode in Zulip/near/124945950):
This is too old

#### [Patrick Massot (Apr 11 2018 at 21:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unicode in Zulip/near/124945952):
He works on perfectoid spaces

#### [Johan Commelin (Apr 11 2018 at 21:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unicode in Zulip/near/124946277):
The problem remains... whether you are formalising the latest hotness in the Langlands program, or some hardcore $$\infty$$-stuff, or something from quantisation-blabla... unicode is ambiguous and susceptible to social attacks...

#### [Johan Commelin (Apr 11 2018 at 21:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unicode in Zulip/near/124946280):
Anyway, I will stuff away my tinfoil hat... enough other problems to focus on right now (^;

#### [Kevin Buzzard (Apr 11 2018 at 21:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unicode in Zulip/near/124946716):
I don't think it's too difficult to formalise. The proof might be harder though.

#### [Kevin Buzzard (Apr 11 2018 at 21:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unicode in Zulip/near/124946769):
The thing about the proof is that there is a huge amount of analysis that goes into the trace formula

#### [Kevin Buzzard (Apr 11 2018 at 21:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unicode in Zulip/near/124946776):
and I know of no proof which ultimately avoids the trace formula

#### [Kevin Buzzard (Apr 11 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unicode in Zulip/near/124946781):
in the non-compact case I should add -- SL(2).

#### [Patrick Massot (Apr 11 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unicode in Zulip/near/124946789):
https://github.com/formalabstracts/formalabstracts/blob/master/fabstract/Wiles_A_and_Taylor_R_FermatLast/fabstract.lean

#### [Kevin Buzzard (Apr 11 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unicode in Zulip/near/124946791):
It's the one part of the proof I've not read and it would not surprise me if I went to my grave not having read it.

#### [Kevin Buzzard (Apr 11 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unicode in Zulip/near/124946794):
Unless EPSRC give me several million quid to formalise it.

#### [Patrick Massot (Apr 11 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unicode in Zulip/near/124946796):
Statement is already done :smile:

#### [Kevin Buzzard (Apr 11 2018 at 21:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unicode in Zulip/near/124946798):
Oh OK that's great, we're half way there.

#### [Patrick Massot (Apr 11 2018 at 21:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unicode in Zulip/near/124946836):
Indeed

#### [Johan Commelin (Apr 11 2018 at 21:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unicode in Zulip/near/124946850):
Lol, they have a type called `document`

#### [Johan Commelin (Apr 11 2018 at 21:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Unicode in Zulip/near/124946855):
That's fantastic (^;

