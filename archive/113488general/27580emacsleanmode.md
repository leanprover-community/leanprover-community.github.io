---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/27580emacsleanmode.html
---

## Stream: [general](index.html)
### Topic: [emacs lean-mode](27580emacsleanmode.html)

---

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Feb 27 2018 at 23:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/emacs%20lean-mode/near/123062251):
I am going to switch to using emacs for writing lean files for a while; I am now competent with VS Code and sort of believe it to be a better end user experience than emacs. The reason I'm switching to emacs is because there is a risk that it will be the best option for some of my undergraduates in October. I think that I can offer them (via cocalc) blisteringly fast Lean plus group editing of files etc, except that they will have to use emacs.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Feb 27 2018 at 23:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/emacs%20lean-mode/near/123062321):
emacs CUA mode isn't so bad, and I say this as a dirty windows user

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Moses Schönfinkel (Feb 27 2018 at 23:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/emacs%20lean-mode/near/123062380):
Windows hate is amusing in here considering a lot of Lean comes from MS Research :).

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Feb 27 2018 at 23:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/emacs%20lean-mode/near/123062386):
Here is something I find much easier to do in VS Code. I have completion running with company-lean, and I can get shift space to give me a big list of cool stuff (possible completions of what I've typed) plus types of the completions. I just want to cut and paste from one of these types

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Feb 27 2018 at 23:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/emacs%20lean-mode/near/123062403):
I select the correct completion and the type disappears. I then stop what I'm doing and type `#check (the thing whose type I was interested in)` and even then I can't access the output. So I then have to change buffers and cut and paste from there and then change back.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Feb 27 2018 at 23:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/emacs%20lean-mode/near/123062405):
Am I missing a trick?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Feb 27 2018 at 23:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/emacs%20lean-mode/near/123062406):
downside: you may be one of three people using company-lean

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Feb 27 2018 at 23:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/emacs%20lean-mode/near/123062497):
```quote
Windows hate is amusing in here considering a lot of Lean comes from MS Research :).
```
Windows is an interesting cute project but I'm not sure it will amount to much :stuck_out_tongue:

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Moses Schönfinkel (Feb 27 2018 at 23:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/emacs%20lean-mode/near/123062503):
I *love* windows.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Moses Schönfinkel (Feb 27 2018 at 23:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/emacs%20lean-mode/near/123062551):
Honestly the amount of headaches I've had with various Linux distros. Ever since probably Win7 I've never really run into any sort of an issue with win.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Feb 27 2018 at 23:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/emacs%20lean-mode/near/123062555):
But seriously, I love to hate windows but it got harder when they came up with the Slam checker. It kind of makes it look like they take software engineering and modularity more seriously than Apple

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Simon Hudon (Feb 27 2018 at 23:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/emacs%20lean-mode/near/123062569):
```quote
I *love* windows.
```
Have you had to turn on your computer since installing Windows 7?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Joey Dodds (Feb 27 2018 at 23:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/emacs%20lean-mode/near/123062576):
Have you seen vscode live editing?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Moses Schönfinkel (Feb 27 2018 at 23:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/emacs%20lean-mode/near/123062577):
Yes, my Win 7 8 and 10 have been running close to flawlessly.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Joey Dodds (Feb 27 2018 at 23:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/emacs%20lean-mode/near/123062625):
live share I guess

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Joey Dodds (Feb 27 2018 at 23:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/emacs%20lean-mode/near/123062650):
(I'd be completely windows native is windows subsystem for Linux worked with Haskell)

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Moses Schönfinkel (Feb 27 2018 at 23:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/emacs%20lean-mode/near/123062658):
Que?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Feb 27 2018 at 23:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/emacs%20lean-mode/near/123062723):
why does haskell need wsfl? 
even before windows subsystem | docker for windows there was mingw, cygwin, virtual box, i've been happy developing on a windows host for decades now
despite this, i know way more about pthreads than about CreateProcess...

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Moses Schönfinkel (Feb 27 2018 at 23:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/emacs%20lean-mode/near/123062780):
You mean you don't know by heart what all those 49 parameters do?

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Feb 27 2018 at 23:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/emacs%20lean-mode/near/123062796):
maybe std::threads and modules will arrive before i'm an old man

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Andrew Ashworth (Feb 27 2018 at 23:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/emacs%20lean-mode/near/123062837):
and then i'll never need to know

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Moses Schönfinkel (Feb 27 2018 at 23:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/emacs%20lean-mode/near/123062858):
Nope, we need new fancy ways to initialize stuff. Call it uniform so at least something gives you the right to call it so.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Moses Schönfinkel (Feb 27 2018 at 23:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/emacs%20lean-mode/near/123062891):
And then mix the syntax up with initializer lists. Then give up on the language.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Joey Dodds (Feb 27 2018 at 23:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/emacs%20lean-mode/near/123063046):
I use virtualbox, but that's probably heavyweight to consider it developing on windows

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Joey Dodds (Feb 27 2018 at 23:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/emacs%20lean-mode/near/123063070):
I'm using Haskell tools that depend on C code that is challenging to build on windows

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Sebastian Ullrich (Feb 28 2018 at 00:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/emacs%20lean-mode/near/123064520):
@**Kevin Buzzard** I'm not sure if you can copy company candidates, but for those in the decl search window (`C-c C-d`) you can use `C-c C-y`.

#### [![Click to go to Zulip](../../assets/img/zulip2.png) Kevin Buzzard (Feb 28 2018 at 01:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/emacs%20lean-mode/near/123066283):
I shall star that reply and consider it later when I have an emacs open. Yay for non-gitter things.

