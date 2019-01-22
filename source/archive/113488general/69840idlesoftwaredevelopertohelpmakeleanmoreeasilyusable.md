---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/69840idlesoftwaredevelopertohelpmakeleanmoreeasilyusable.html
---

## [general](index.html)
### [idle software developer to help make lean more easily usable](69840idlesoftwaredevelopertohelpmakeleanmoreeasilyusable.html)

#### [Adam Kurkiewicz (Aug 09 2018 at 15:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idle%20software%20developer%20to%20help%20make%20lean%20more%20easily%20usable/near/131173267):
Hey guys, one of my student software developers (bright and hard-working, the type I like!) is going idle from today (we've just finished a project). He doesn't do any lean, but he's very good with windows installers, linux packaging, iOS apps, android apps and all sorts of boring software engineering fluff (actually he doesn't think it's boring, which is why I like him even more!). I think lean could use some help in that regard. Happy to chat more if anybody's interested. I vaguely remember @**Kevin Buzzard**  in particular raising some issues with windows installers for lean or something along the lines.

#### [Patrick Massot (Aug 09 2018 at 16:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idle%20software%20developer%20to%20help%20make%20lean%20more%20easily%20usable/near/131176306):
The challenge is extremely easy to state: say you have a colleague who wants to try maths in Lean, either on Linux, MacOS or Windows. We want him to download one file, execute it, wait at most 3 minutes, and be ready to fire either emacs or VScode and  play.

#### [Patrick Massot (Aug 09 2018 at 16:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idle%20software%20developer%20to%20help%20make%20lean%20more%20easily%20usable/near/131176329):
That would be a hugely useful achievement

#### [Johan Commelin (Aug 09 2018 at 16:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idle%20software%20developer%20to%20help%20make%20lean%20more%20easily%20usable/near/131176341):
Make that VScode please...

#### [Johan Commelin (Aug 09 2018 at 16:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idle%20software%20developer%20to%20help%20make%20lean%20more%20easily%20usable/near/131176352):
If they know emacs, they know how to do the rest themselves as well...

#### [Patrick Massot (Aug 09 2018 at 16:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idle%20software%20developer%20to%20help%20make%20lean%20more%20easily%20usable/near/131176409):
I meant the colleague should be able to choose between emacs and VScode.

#### [Patrick Massot (Aug 09 2018 at 16:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idle%20software%20developer%20to%20help%20make%20lean%20more%20easily%20usable/near/131176455):
I guess it's fair to assume emacs is already installed if the colleague want to use emacs, but the default stuff should be to install VScode along the way, unless the user explicitly refuses to get it.

#### [Adam Kurkiewicz (Aug 09 2018 at 16:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idle%20software%20developer%20to%20help%20make%20lean%20more%20easily%20usable/near/131176586):
I realise that this is something, which is badly needed, and happy to put some work to make it happen (especially working with Marcell, he's a really a brilliant software dev), but I'm afraid there would have to be a stream of funding for this. Marcell uses these kinds of jobs to pay for his rent, etc. and I don't think we could have him volunteer to do this.

#### [Patrick Massot (Aug 09 2018 at 16:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idle%20software%20developer%20to%20help%20make%20lean%20more%20easily%20usable/near/131176670):
Oh, I didn't get that from your first message.

#### [Adam Kurkiewicz (Aug 09 2018 at 16:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idle%20software%20developer%20to%20help%20make%20lean%20more%20easily%20usable/near/131176704):
Sorry, should have been more clear.

#### [Patrick Massot (Aug 09 2018 at 16:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idle%20software%20developer%20to%20help%20make%20lean%20more%20easily%20usable/near/131176730):
 No idea who could have money for that, except MS of course

#### [Patrick Massot (Aug 09 2018 at 16:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idle%20software%20developer%20to%20help%20make%20lean%20more%20easily%20usable/near/131176751):
But I'm pretty sure Leo won't be interested right now

#### [Adam Kurkiewicz (Aug 09 2018 at 16:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idle%20software%20developer%20to%20help%20make%20lean%20more%20easily%20usable/near/131176806):
I could maybe ask for some money from SICSA, but it's a bit hard given that this isn't, strictly speaking, research: http://www.sicsa.ac.uk/funding/

#### [Adam Kurkiewicz (Aug 09 2018 at 16:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idle%20software%20developer%20to%20help%20make%20lean%20more%20easily%20usable/near/131176830):
I don't think any of the clients we normally work with would care enough to fund this type of work either.

#### [Adam Kurkiewicz (Aug 09 2018 at 16:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idle%20software%20developer%20to%20help%20make%20lean%20more%20easily%20usable/near/131176927):
I realise that Leo has very different priorities, and I actually think this is entirely justifiable.

#### [Adam Kurkiewicz (Aug 09 2018 at 16:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idle%20software%20developer%20to%20help%20make%20lean%20more%20easily%20usable/near/131176972):
Another idea, which comes to mind is Google Summer of Code, but this is a lot of work, lean would have to become an affiliated partner, etc.

#### [Adam Kurkiewicz (Aug 09 2018 at 16:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idle%20software%20developer%20to%20help%20make%20lean%20more%20easily%20usable/near/131177076):
I don't think I'd be able to commit to such a big task as coordinating GSoC.

#### [Patrick Massot (Aug 09 2018 at 16:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idle%20software%20developer%20to%20help%20make%20lean%20more%20easily%20usable/near/131177136):
I don't think GSoC would be interested in helping packaging, and actual contributions to Lean are far beyond the scope of GSoC

#### [Adam Kurkiewicz (Aug 09 2018 at 16:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idle%20software%20developer%20to%20help%20make%20lean%20more%20easily%20usable/near/131177222):
The thing is, I'm pretty sure, if we get all the pipelines with all the installers nicely polished, swapping the binary from Lean 3 to Lean 4 would be no problem at all.

#### [Adam Kurkiewicz (Aug 09 2018 at 16:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idle%20software%20developer%20to%20help%20make%20lean%20more%20easily%20usable/near/131177257):
True.

#### [Adam Kurkiewicz (Aug 09 2018 at 16:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idle%20software%20developer%20to%20help%20make%20lean%20more%20easily%20usable/near/131177336):
Well, anyway, let's keep thinking about these options, maybe somebody will get a good idea for a funding stream.

#### [Patrick Massot (Aug 09 2018 at 16:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idle%20software%20developer%20to%20help%20make%20lean%20more%20easily%20usable/near/131177403):
There are also intermediate goals that should be reachable, like having Travis building mathlib nightly olean, copying what works for lean nightlies

#### [Adam Kurkiewicz (Aug 09 2018 at 16:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idle%20software%20developer%20to%20help%20make%20lean%20more%20easily%20usable/near/131177485):
Marcell's done plenty of travis builds, both before and after we've started working together.

#### [Adam Kurkiewicz (Aug 09 2018 at 16:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idle%20software%20developer%20to%20help%20make%20lean%20more%20easily%20usable/near/131177512):
There's this website, which lists some possibilities: https://www.software.ac.uk/how-fund-research-software-development

#### [Adam Kurkiewicz (Aug 09 2018 at 16:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/idle%20software%20developer%20to%20help%20make%20lean%20more%20easily%20usable/near/131177601):
I'll investigate and let you guys know what I've found

