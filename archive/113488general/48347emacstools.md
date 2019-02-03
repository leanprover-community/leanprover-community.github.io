---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/48347emacstools.html
---

## Stream: [general](index.html)
### Topic: [emacs tools](48347emacstools.html)

---


{% raw %}
#### [ Simon Hudon (Jun 03 2018 at 02:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/emacs%20tools/near/127482729):
<p>Is it possible in emacs lisp to use <code>lean-server-session-send-command</code> to get the text of a definition? Failing that, is it possible to use it with the command <code>'info</code> to get the line info of the next command in the file that contains it? I'm trying to create a command to display the definition of the symbol the cursor is currently on.</p>

#### [ Sebastian Ullrich (Jun 03 2018 at 20:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/emacs%20tools/near/127510536):
<p>No, I can't think of any way to do that</p>

#### [ Simon Hudon (Jun 03 2018 at 20:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/emacs%20tools/near/127511408):
<p>What I ended up doing is use the list of keywords in <code>lean-syntax</code> and only keep the ones that are commands, use <code>lean-find-definition</code> to find the location of the definition and <code>re-search-forward</code> to find the next command. That's pretty primitive because it doesn't account for user command but it might just be good enough.</p>

#### [ Sebastian Ullrich (Jun 03 2018 at 20:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/emacs%20tools/near/127511513):
<p>Good enough I guess :)</p>

#### [ Simon Hudon (Jun 04 2018 at 01:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/emacs%20tools/near/127518889):
<p>I'm wondering if it would be more useful to just go with find definition and have an option to go back. What do you think? The easiest way to do it is provide one slot memory for finding definition but it would be nicer to have many slots. I just don't want it to grow without bounds.</p>

#### [ Reid Barton (Jun 04 2018 at 01:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/emacs%20tools/near/127519166):
<p>How about setting the mark to the old location if the definition is in the same file?</p>

#### [ Simon Hudon (Jun 04 2018 at 01:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/emacs%20tools/near/127519210):
<p>What does that solve?</p>

#### [ Reid Barton (Jun 04 2018 at 01:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/emacs%20tools/near/127519219):
<p>then you can C-x C-x to go back</p>

#### [ Reid Barton (Jun 04 2018 at 01:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/emacs%20tools/near/127519227):
<p>for example, isearch (C-s) does this</p>

#### [ Simon Hudon (Jun 04 2018 at 01:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/emacs%20tools/near/127519340):
<p>Ah I see! But then when you go to another file, you have a different shortcut than when you stay in the same file</p>

#### [ Reid Barton (Jun 04 2018 at 01:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/emacs%20tools/near/127519418):
<p>Apparently there's also C-x C-SPC which will pop marks off a global stack, between files</p>

#### [ Reid Barton (Jun 04 2018 at 01:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/emacs%20tools/near/127519469):
<p>So that would always work as a "go back" key</p>

#### [ Reid Barton (Jun 04 2018 at 01:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/emacs%20tools/near/127519533):
<p><a href="https://stackoverflow.com/questions/4918707/in-emacs-how-to-go-back-to-previous-line-position-after-using-semantic-jump-to" target="_blank" title="https://stackoverflow.com/questions/4918707/in-emacs-how-to-go-back-to-previous-line-position-after-using-semantic-jump-to">https://stackoverflow.com/questions/4918707/in-emacs-how-to-go-back-to-previous-line-position-after-using-semantic-jump-to</a></p>

#### [ Simon Hudon (Jun 04 2018 at 01:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/emacs%20tools/near/127519595):
<p>Nice! So you suggest that in <code>lean-find-definition</code> (which is called when you press <code>M-.</code>) I first push the mark and then set the mark to <code>(point)</code> and then the user will simply have access to those features?</p>

#### [ Simon Hudon (Jun 04 2018 at 01:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/emacs%20tools/near/127519597):
<p>Is there a limit to the number of slots on that stack?</p>

#### [ Reid Barton (Jun 04 2018 at 01:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/emacs%20tools/near/127519603):
<p>I don't know. I just found out the limit is more than one <span class="emoji emoji-1f642" title="simple smile">:simple_smile:</span></p>

#### [ Reid Barton (Jun 04 2018 at 01:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/emacs%20tools/near/127519650):
<p>I think you just need to call <code>(push-mark)</code> before doing the navigation</p>

#### [ Reid Barton (Jun 04 2018 at 01:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/emacs%20tools/near/127519710):
<div class="codehilite"><pre><span></span>mark-ring-max is a variable defined in ‘simple.el’.
Its value is 16

Documentation:
Maximum size of mark ring.  Start discarding off end if gets this big.
</pre></div>

#### [ Simon Hudon (Jun 04 2018 at 01:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/emacs%20tools/near/127519766):
<blockquote>
<p>I think you just need to call <code>(push-mark)</code> before doing the navigation</p>
</blockquote>
<p>Inside of <code>lean-mode</code> or as a user of <code>lean-mode</code>?</p>

#### [ Reid Barton (Jun 04 2018 at 01:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/emacs%20tools/near/127519772):
<p><code>lean-find-definition</code> should call it (I guess, haven't looked at the code)</p>

#### [ Reid Barton (Jun 04 2018 at 01:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/emacs%20tools/near/127519825):
<p>Hmm. I see there is already this, in <code>lean-find-definition-cont</code></p>
<div class="codehilite"><pre><span></span><span class="p">(</span><span class="nb">cl-defun</span> <span class="nv">lean-find-definition-cont</span> <span class="p">(</span><span class="kp">&amp;key</span> <span class="nv">file</span> <span class="nv">line</span> <span class="nv">column</span><span class="p">)</span>
  <span class="p">(</span><span class="nb">when</span> <span class="p">(</span><span class="nf">fboundp</span> <span class="ss">&#39;xref-push-marker-stack</span><span class="p">)</span> <span class="p">(</span><span class="nv">xref-push-marker-stack</span><span class="p">))</span>
<span class="o">...</span>
</pre></div>

#### [ Simon Hudon (Jun 04 2018 at 01:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/emacs%20tools/near/127519832):
<p>This is so nice! It's working very well!</p>

#### [ Simon Hudon (Jun 04 2018 at 01:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/emacs%20tools/near/127519836):
<p>Thanks!</p>

#### [ Simon Hudon (Jun 04 2018 at 01:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/emacs%20tools/near/127519894):
<p>I can PR it if you'd like to have it too</p>

#### [ Reid Barton (Jun 04 2018 at 01:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/emacs%20tools/near/127519900):
<p>Yes please</p>

#### [ Reid Barton (Jun 04 2018 at 01:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/emacs%20tools/near/127519907):
<p>I've been wanting this feature too, but the mark thing just occurred to me now</p>

#### [ Reid Barton (Jun 04 2018 at 01:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/emacs%20tools/near/127519969):
<p>It looks like maybe M-, already does the same thing? but I have that mapped to autocomplete</p>

#### [ Simon Hudon (Jun 04 2018 at 01:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/emacs%20tools/near/127520133):
<p>You're right! I undid my changes and <code>M-.</code> <code>M-.</code> <code>M-,</code> <code>M-,</code> brings me back to the beginning. It looks like my pull request will be the empty set. I hope it's approved!</p>


{% endraw %}
