---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/27580emacsleanmode.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [emacs lean-mode](https://leanprover-community.github.io/archive/113488general/27580emacsleanmode.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kevin Buzzard (Feb 27 2018 at 23:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/emacs%20lean-mode/near/123062251):
<p>I am going to switch to using emacs for writing lean files for a while; I am now competent with VS Code and sort of believe it to be a better end user experience than emacs. The reason I'm switching to emacs is because there is a risk that it will be the best option for some of my undergraduates in October. I think that I can offer them (via cocalc) blisteringly fast Lean plus group editing of files etc, except that they will have to use emacs.</p>

#### [ Andrew Ashworth (Feb 27 2018 at 23:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/emacs%20lean-mode/near/123062321):
<p>emacs CUA mode isn't so bad, and I say this as a dirty windows user</p>

#### [ Moses Schönfinkel (Feb 27 2018 at 23:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/emacs%20lean-mode/near/123062380):
<p>Windows hate is amusing in here considering a lot of Lean comes from MS Research :).</p>

#### [ Kevin Buzzard (Feb 27 2018 at 23:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/emacs%20lean-mode/near/123062386):
<p>Here is something I find much easier to do in VS Code. I have completion running with company-lean, and I can get shift space to give me a big list of cool stuff (possible completions of what I've typed) plus types of the completions. I just want to cut and paste from one of these types</p>

#### [ Kevin Buzzard (Feb 27 2018 at 23:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/emacs%20lean-mode/near/123062403):
<p>I select the correct completion and the type disappears. I then stop what I'm doing and type <code>#check (the thing whose type I was interested in)</code> and even then I can't access the output. So I then have to change buffers and cut and paste from there and then change back.</p>

#### [ Kevin Buzzard (Feb 27 2018 at 23:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/emacs%20lean-mode/near/123062405):
<p>Am I missing a trick?</p>

#### [ Andrew Ashworth (Feb 27 2018 at 23:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/emacs%20lean-mode/near/123062406):
<p>downside: you may be one of three people using company-lean</p>

#### [ Simon Hudon (Feb 27 2018 at 23:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/emacs%20lean-mode/near/123062497):
<blockquote>
<p>Windows hate is amusing in here considering a lot of Lean comes from MS Research :).</p>
</blockquote>
<p>Windows is an interesting cute project but I'm not sure it will amount to much <span class="emoji emoji-1f61b" title="stuck out tongue">:stuck_out_tongue:</span></p>

#### [ Moses Schönfinkel (Feb 27 2018 at 23:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/emacs%20lean-mode/near/123062503):
<p>I <em>love</em> windows.</p>

#### [ Moses Schönfinkel (Feb 27 2018 at 23:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/emacs%20lean-mode/near/123062551):
<p>Honestly the amount of headaches I've had with various Linux distros. Ever since probably Win7 I've never really run into any sort of an issue with win.</p>

#### [ Simon Hudon (Feb 27 2018 at 23:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/emacs%20lean-mode/near/123062555):
<p>But seriously, I love to hate windows but it got harder when they came up with the Slam checker. It kind of makes it look like they take software engineering and modularity more seriously than Apple</p>

#### [ Simon Hudon (Feb 27 2018 at 23:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/emacs%20lean-mode/near/123062569):
<blockquote>
<p>I <em>love</em> windows.</p>
</blockquote>
<p>Have you had to turn on your computer since installing Windows 7?</p>

#### [ Joey Dodds (Feb 27 2018 at 23:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/emacs%20lean-mode/near/123062576):
<p>Have you seen vscode live editing?</p>

#### [ Moses Schönfinkel (Feb 27 2018 at 23:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/emacs%20lean-mode/near/123062577):
<p>Yes, my Win 7 8 and 10 have been running close to flawlessly.</p>

#### [ Joey Dodds (Feb 27 2018 at 23:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/emacs%20lean-mode/near/123062625):
<p>live share I guess</p>

#### [ Joey Dodds (Feb 27 2018 at 23:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/emacs%20lean-mode/near/123062650):
<p>(I'd be completely windows native is windows subsystem for Linux worked with Haskell)</p>

#### [ Moses Schönfinkel (Feb 27 2018 at 23:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/emacs%20lean-mode/near/123062658):
<p>Que?</p>

#### [ Andrew Ashworth (Feb 27 2018 at 23:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/emacs%20lean-mode/near/123062723):
<p>why does haskell need wsfl? <br>
even before windows subsystem | docker for windows there was mingw, cygwin, virtual box, i've been happy developing on a windows host for decades now<br>
despite this, i know way more about pthreads than about CreateProcess...</p>

#### [ Moses Schönfinkel (Feb 27 2018 at 23:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/emacs%20lean-mode/near/123062780):
<p>You mean you don't know by heart what all those 49 parameters do?</p>

#### [ Andrew Ashworth (Feb 27 2018 at 23:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/emacs%20lean-mode/near/123062796):
<p>maybe std::threads and modules will arrive before i'm an old man</p>

#### [ Andrew Ashworth (Feb 27 2018 at 23:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/emacs%20lean-mode/near/123062837):
<p>and then i'll never need to know</p>

#### [ Moses Schönfinkel (Feb 27 2018 at 23:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/emacs%20lean-mode/near/123062858):
<p>Nope, we need new fancy ways to initialize stuff. Call it uniform so at least something gives you the right to call it so.</p>

#### [ Moses Schönfinkel (Feb 27 2018 at 23:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/emacs%20lean-mode/near/123062891):
<p>And then mix the syntax up with initializer lists. Then give up on the language.</p>

#### [ Joey Dodds (Feb 27 2018 at 23:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/emacs%20lean-mode/near/123063046):
<p>I use virtualbox, but that's probably heavyweight to consider it developing on windows</p>

#### [ Joey Dodds (Feb 27 2018 at 23:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/emacs%20lean-mode/near/123063070):
<p>I'm using Haskell tools that depend on C code that is challenging to build on windows</p>

#### [ Sebastian Ullrich (Feb 28 2018 at 00:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/emacs%20lean-mode/near/123064520):
<p><span class="user-mention" data-user-email="k.buzzard@imperial.ac.uk" data-user-id="110038">@Kevin Buzzard</span> I'm not sure if you can copy company candidates, but for those in the decl search window (<code>C-c C-d</code>) you can use <code>C-c C-y</code>.</p>

#### [ Kevin Buzzard (Feb 28 2018 at 01:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/emacs%20lean-mode/near/123066283):
<p>I shall star that reply and consider it later when I have an emacs open. Yay for non-gitter things.</p>


{% endraw %}
