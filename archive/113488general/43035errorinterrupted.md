---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/43035errorinterrupted.html
---

## Stream: [general](index.html)
### Topic: [error: interrupted](43035errorinterrupted.html)

---


{% raw %}
#### [ Reid Barton (Jun 02 2018 at 02:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/error%3A%20interrupted/near/127445373):
<p>Does anyone know why this often happens when using jump-to-definition? (I'm in emacs if it matters.)</p>

#### [ Simon Hudon (Jun 02 2018 at 02:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/error%3A%20interrupted/near/127445391):
<p>I get the same error.</p>

#### [ Simon Hudon (Jun 02 2018 at 02:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/error%3A%20interrupted/near/127445442):
<p>I thought it might be a problem with <code>company-mode</code> but I wasn't able to find anything. Are you also on a Mac?</p>

#### [ Reid Barton (Jun 02 2018 at 02:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/error%3A%20interrupted/near/127445454):
<p>Linux here</p>

#### [ Simon Hudon (Jun 02 2018 at 02:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/error%3A%20interrupted/near/127445516):
<p><span class="user-mention" data-user-id="110024">@Sebastian Ullrich</span> also I think and I remember he didn't have the same error so I thought it might be because of mac. It must be something else</p>

#### [ Simon Hudon (Jun 02 2018 at 02:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/error%3A%20interrupted/near/127445523):
<p>Are you well versed in Emacs Lisp?</p>

#### [ Reid Barton (Jun 02 2018 at 02:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/error%3A%20interrupted/near/127445624):
<p>Not especially, but I would try to debug it if the issue is not already understood.</p>

#### [ Reid Barton (Jun 02 2018 at 02:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/error%3A%20interrupted/near/127445625):
<p>It's quite irritating</p>

#### [ Simon Hudon (Jun 02 2018 at 02:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/error%3A%20interrupted/near/127446322):
<p>it is indeed. I just added print statements in  <code>lean-find-definition</code> in <code>lean-mode</code> but I can't get it to fail now ... :/</p>

#### [ Simon Hudon (Jun 02 2018 at 03:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/error%3A%20interrupted/near/127446785):
<p>Do you have:</p>
<div class="codehilite"><pre><span></span>(global-set-key (kbd &quot;S-SPC&quot;) #&#39;company-complete)
</pre></div>


<p>in your init file? I found a thread on the github repo (<a href="https://github.com/company-mode/company-mode/issues/69" target="_blank" title="https://github.com/company-mode/company-mode/issues/69">https://github.com/company-mode/company-mode/issues/69</a>) that suggests replacing it with:</p>
<div class="codehilite"><pre><span></span>(define-key company-mode-map (kbd &quot;S-SPC&quot;) #&#39;company-complete)
</pre></div>


<p>It seems to help but the bug has been showing up inconsistently. Can you try it and tell me if it helps?</p>

#### [ Reid Barton (Jun 02 2018 at 03:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/error%3A%20interrupted/near/127446911):
<p>I got <code>Symbol's value as variable is void: company-mode-map</code></p>

#### [ Reid Barton (Jun 02 2018 at 03:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/error%3A%20interrupted/near/127446917):
<p>Is that the right issue?</p>

#### [ Reid Barton (Jun 02 2018 at 03:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/error%3A%20interrupted/near/127446984):
<p>okay, a <code>(require 'company)</code> fixed that</p>

#### [ Simon Hudon (Jun 02 2018 at 03:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/error%3A%20interrupted/near/127446986):
<p>That's the one that helped me. Do you have <code>(require 'company)</code> before that line?</p>

#### [ Reid Barton (Jun 02 2018 at 03:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/error%3A%20interrupted/near/127446989):
<p>Well, it's working at the moment, but it usually does after restarting emacs :)</p>

#### [ Reid Barton (Jun 02 2018 at 03:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/error%3A%20interrupted/near/127447104):
<p>Oh, it already stopped working</p>

#### [ Simon Hudon (Jun 02 2018 at 03:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/error%3A%20interrupted/near/127447116):
<p>Darn! I was hoping!</p>

#### [ Simon Hudon (Jun 02 2018 at 03:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/error%3A%20interrupted/near/127447977):
<p>In <code>lean-input.el</code>, in <code>lean-find-definition</code>, can you try adding print statements inside the lambda expression? Like this:</p>
<div class="codehilite"><pre><span></span><span class="p">(</span><span class="nb">defun</span> <span class="nv">lean-find-definition</span> <span class="p">()</span>
  <span class="s">&quot;Jump to definition of thing at point&quot;</span>
  <span class="p">(</span><span class="k">interactive</span><span class="p">)</span>
  <span class="p">(</span><span class="nv">lean-get-info-record-at-point</span>
   <span class="p">(</span><span class="nb">lambda</span> <span class="p">(</span><span class="nv">info-record</span><span class="p">)</span>
     <span class="p">(</span><span class="nf">print</span> <span class="s">&quot;begin&quot;</span><span class="p">)</span>
     <span class="p">(</span><span class="nv">-if-let</span> <span class="p">(</span><span class="nv">source-record</span> <span class="p">(</span><span class="nf">plist-get</span> <span class="nv">info-record</span> <span class="nb">:source</span><span class="p">))</span>
         <span class="p">(</span><span class="nf">apply</span> <span class="nf">#&#39;</span><span class="nv">lean-find-definition-cont</span> <span class="nv">source-record</span><span class="p">)</span>
       <span class="p">(</span><span class="nv">-if-let</span> <span class="p">(</span><span class="nv">id</span> <span class="p">(</span><span class="nf">plist-get</span> <span class="nv">info-record</span> <span class="nb">:full-id</span><span class="p">))</span>
           <span class="p">(</span><span class="nf">message</span> <span class="s">&quot;no source location available for %s&quot;</span> <span class="nv">id</span><span class="p">)</span>
         <span class="p">(</span><span class="nf">message</span> <span class="s">&quot;unknown thing at point&quot;</span><span class="p">)))</span>
     <span class="p">(</span><span class="nf">print</span> <span class="s">&quot;end&quot;</span><span class="p">))))</span>
</pre></div>

#### [ Reid Barton (Jun 02 2018 at 03:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/error%3A%20interrupted/near/127448179):
<p>Well... I tried adding those and it's working again.<br>
Did editing the <code>.el</code> file cause emacs to reload the mode automatically?</p>

#### [ Simon Hudon (Jun 02 2018 at 03:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/error%3A%20interrupted/near/127448391):
<p>I don't know. I wonder if the printing introduces a delay. Let's try removing the print statements</p>

#### [ Reid Barton (Jun 02 2018 at 03:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/error%3A%20interrupted/near/127448441):
<p>Unfortunately I finished proving the thing I was trying to prove</p>

#### [ Simon Hudon (Jun 02 2018 at 04:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/error%3A%20interrupted/near/127448556):
<p>I guess we'll never know</p>

#### [ Sebastian Ullrich (Jun 02 2018 at 09:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/error%3A%20interrupted/near/127456608):
<p>This is a known issue (to me :) ) where go-to-definition doesn't work while the goal display is open</p>

#### [ Simon Hudon (Jun 02 2018 at 13:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/error%3A%20interrupted/near/127462600):
<p>That's very good to know! Is this on the emacs side or on the Lean side?</p>

#### [ Sebastian Ullrich (Jun 03 2018 at 20:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/error%3A%20interrupted/near/127510537):
<p>That requests are interrupted by unrelated requests is an issue with the Lean server. But lean-mode could try to work around that by not sending a goal request directly after a find definition request.</p>

#### [ Simon Hudon (Jun 03 2018 at 20:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/error%3A%20interrupted/near/127511362):
<p>Do you think if we set a timer for masking requests for half a second after find definition that might be good enough?</p>

#### [ Sebastian Ullrich (Jun 03 2018 at 20:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/error%3A%20interrupted/near/127511592):
<p>It should be sufficient to suppress the next execution of <code>lean-show-goal--handler</code> after <code>lean-find-definition</code> has run, probably?</p>

#### [ Simon Hudon (Jun 03 2018 at 22:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/error%3A%20interrupted/near/127514811):
<p>That seems to be enough. Do you want a PR for it?</p>

#### [ Sebastian Ullrich (Jun 03 2018 at 22:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/error%3A%20interrupted/near/127514912):
<p>Sure, thanks</p>

#### [ Simon Hudon (Jun 03 2018 at 23:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/error%3A%20interrupted/near/127515061):
<p>Done</p>


{% endraw %}
