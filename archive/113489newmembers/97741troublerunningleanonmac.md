---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/97741troublerunningleanonmac.html
---

## Stream: [new members](index.html)
### Topic: [trouble running lean on mac](97741troublerunningleanonmac.html)

---


{% raw %}
#### [ Yuhan Du (Aug 13 2018 at 13:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/trouble%20running%20lean%20on%20mac/near/132038880):
<div class="codehilite"><pre><span></span>dyn3218-19:bin apple$ ls
lean        leanchecker leanpkg
dyn3218-19:bin apple$ ./lean
dyld: Library not loaded: /usr/local/opt/gmp/lib/libgmp.10.dylib
  Referenced from: /Users/apple/Desktop/lean-3.4.2-nightly-2018-06-21-darwin/bin/./lean
  Reason: image not found
Abort trap: 6
</pre></div>


<p>can someone help with this</p>

#### [ Mario Carneiro (Aug 13 2018 at 13:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/trouble%20running%20lean%20on%20mac/near/132038910):
<p>I think if you are compiling it yourself there is some line to install <code>libgmp</code> in the readme?</p>

#### [ Kevin Buzzard (Aug 13 2018 at 13:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/trouble%20running%20lean%20on%20mac/near/132038915):
<p>This is the current nightly</p>

#### [ Kevin Buzzard (Aug 13 2018 at 13:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/trouble%20running%20lean%20on%20mac/near/132038956):
<p>I just don't know how to install gmp on a mac</p>

#### [ Kevin Buzzard (Aug 13 2018 at 13:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/trouble%20running%20lean%20on%20mac/near/132038958):
<p>(or indeed how to do anything on a mac)</p>

#### [ Yulia Zaplatina (Aug 13 2018 at 13:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/trouble%20running%20lean%20on%20mac/near/132038960):
<p>Homebrew solves the problem</p>

#### [ Yulia Zaplatina (Aug 13 2018 at 13:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/trouble%20running%20lean%20on%20mac/near/132038964):
<p><a href="https://brew.sh" target="_blank" title="https://brew.sh">https://brew.sh</a></p>

#### [ Kevin Buzzard (Aug 13 2018 at 13:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/trouble%20running%20lean%20on%20mac/near/132038971):
<p>I think Homebrew solved a problem like this before. I should write this in the docs</p>

#### [ Kevin Buzzard (Aug 13 2018 at 13:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/trouble%20running%20lean%20on%20mac/near/132039153):
<p>Can one install Lean through homebrew? I'm guessing no</p>

#### [ Sean Leather (Aug 13 2018 at 13:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/trouble%20running%20lean%20on%20mac/near/132039278):
<p>I used to do it with Lean 2. I don't know if it's been kept up to date, though.</p>

#### [ Sean Leather (Aug 13 2018 at 13:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/trouble%20running%20lean%20on%20mac/near/132039866):
<p>I just read the rest of the thread before Kevin's message. I believe Yulia is referring to installing <code>libgmp</code> via <code>brew install gmp</code>, which will probably fix Yuhan's problem.</p>

#### [ Patrick Massot (Aug 13 2018 at 13:31)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/trouble%20running%20lean%20on%20mac/near/132040275):
<p>Since Lean is currently frozen, it seems like a very good time to update that brew thing</p>

#### [ Kevin Buzzard (Aug 13 2018 at 13:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/trouble%20running%20lean%20on%20mac/near/132040340):
<p>FWIW we have everything up and running now. On MacOS High Sierra we installed brew, and then <code>brew install gmp</code> (to get <code>lean</code> running) and <code>brew install coreutils</code> (to get <code>leanpkg</code> running).</p>

#### [ Kevin Buzzard (Aug 13 2018 at 13:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/trouble%20running%20lean%20on%20mac/near/132040348):
<p>Yuhan also installed git somehow, or had git already, but that was before I arrived.</p>

#### [ Sean Leather (Aug 13 2018 at 13:43)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/trouble%20running%20lean%20on%20mac/near/132040849):
<p>IIRC, <code>git</code> comes with the Xcode command line tools.</p>


{% endraw %}
