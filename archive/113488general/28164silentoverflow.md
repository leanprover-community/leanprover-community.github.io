---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/28164silentoverflow.html
---

## Stream: [general](index.html)
### Topic: [silent overflow](28164silentoverflow.html)

---


{% raw %}
#### [ Kevin Buzzard (Apr 09 2018 at 18:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/silent%20overflow/near/124842273):
<div class="codehilite"><pre><span></span><span class="bp">#</span><span class="kn">check</span> <span class="n">id</span> <span class="c1">-- all seems fine</span>

<span class="kn">example</span> <span class="o">:</span> <span class="mi">1000</span> <span class="bp">*</span> <span class="mi">1000</span> <span class="bp">=</span> <span class="mi">123456</span> <span class="o">:=</span> <span class="n">rfl</span> <span class="c1">-- no error reported</span>

<span class="bp">#</span><span class="kn">check</span> <span class="n">id</span> <span class="c1">-- all still seems fine</span>
</pre></div>

#### [ Kevin Buzzard (Apr 09 2018 at 18:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/silent%20overflow/near/124842287):
<p>changing <code>example</code> to <code>theorem X</code> shows that there is a problem</p>

#### [ Kevin Buzzard (Apr 09 2018 at 18:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/silent%20overflow/near/124842294):
<p><code> deep recursion was detected at 'replace' (potential solution: increase stack space in your system) </code></p>

#### [ Kevin Buzzard (Apr 09 2018 at 18:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/silent%20overflow/near/124842302):
<p>but the error is not triggered if we use <code>example</code></p>

#### [ Kenny Lau (Apr 09 2018 at 18:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/silent%20overflow/near/124842353):
<p>no error reported!</p>

#### [ Kevin Buzzard (Apr 09 2018 at 18:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/silent%20overflow/near/124842357):
<p>Changing example to theorem also gives us the <code> not a rfl-lemma, even though marked as rfl </code> error</p>

#### [ Kevin Buzzard (Apr 09 2018 at 18:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/silent%20overflow/near/124842368):
<p>and perhaps this is relevant</p>

#### [ Kevin Buzzard (Apr 09 2018 at 18:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/silent%20overflow/near/124842378):
<p>because <code>example : 1000  *  1000  =  123456  :=  by refl</code> gives the recursion error</p>

#### [ Kevin Buzzard (Apr 09 2018 at 18:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/silent%20overflow/near/124842389):
<p>no error reported! So maybe we can prove 0=1</p>

#### [ Kevin Buzzard (Apr 09 2018 at 18:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/silent%20overflow/near/124842394):
<p>but it's hard to work with</p>

#### [ Kevin Buzzard (Apr 09 2018 at 18:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/silent%20overflow/near/124842396):
<p>I guess proving 1000000 = 123456 is just as good</p>

#### [ Kevin Buzzard (Apr 09 2018 at 18:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/silent%20overflow/near/124842398):
<p>Do you know how to run this through Lean with max paranoia options on?</p>

#### [ Kevin Buzzard (Apr 09 2018 at 18:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/silent%20overflow/near/124842637):
<div class="codehilite"><pre><span></span>buzzard@bob:~$ more wrong.lean
example : 1000 * 1000 = 123456 := rfl -- no error reported
buzzard@bob:~$ lean --trust=0 wrong.lean
buzzard@bob:~$
</pre></div>

#### [ Kevin Buzzard (Apr 09 2018 at 18:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/silent%20overflow/near/124842681):
<p>looks good to me</p>

#### [ Kevin Buzzard (Apr 09 2018 at 18:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/silent%20overflow/near/124842908):
<p>dammit <code>example : 0 = 1 := @nat.add_left_cancel (1000 * 1000) 0 1 rfl
</code> doesn't work :-(</p>

#### [ Kevin Buzzard (Apr 09 2018 at 18:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/silent%20overflow/near/124842921):
<p>you get the recursion error</p>

#### [ Kevin Buzzard (Apr 09 2018 at 18:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/silent%20overflow/near/124843274):
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">W</span> <span class="o">:</span> <span class="mi">0</span> <span class="bp">=</span> <span class="mi">1</span> <span class="bp">→</span> <span class="n">false</span> <span class="o">:=</span> <span class="n">dec_trivial</span>

<span class="kn">theorem</span> <span class="n">X</span> <span class="o">:</span> <span class="mi">1000</span> <span class="bp">*</span> <span class="mi">1000</span> <span class="bp">+</span> <span class="mi">0</span> <span class="bp">=</span> <span class="mi">1000</span> <span class="bp">*</span> <span class="mi">1000</span> <span class="bp">+</span> <span class="mi">1</span> <span class="bp">→</span> <span class="n">false</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">H</span><span class="o">,</span> <span class="n">W</span> <span class="o">(</span><span class="n">nat</span><span class="bp">.</span><span class="n">add_left_cancel</span> <span class="n">H</span><span class="o">)</span>

<span class="kn">example</span> <span class="o">:</span> <span class="mi">1000</span> <span class="bp">*</span> <span class="mi">1000</span> <span class="bp">+</span> <span class="mi">0</span> <span class="bp">=</span> <span class="mi">1000</span> <span class="bp">*</span> <span class="mi">1000</span> <span class="bp">+</span> <span class="mi">1</span> <span class="o">:=</span> <span class="n">rfl</span> <span class="c1">-- no problem</span>

<span class="kn">example</span> <span class="o">:</span> <span class="n">false</span> <span class="o">:=</span> <span class="n">X</span> <span class="n">rfl</span> <span class="c1">-- recursion error</span>
</pre></div>

#### [ Kevin Buzzard (Apr 09 2018 at 18:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/silent%20overflow/near/124843311):
<p>so near and yet so far</p>

#### [ Kevin Buzzard (Apr 09 2018 at 18:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/silent%20overflow/near/124843350):
<p>" As far as we know, no proof of <code>false</code> has ever been accepted by Lean when using <code>-t0</code>. " (from the FAQ)</p>

#### [ Kenny Lau (Apr 09 2018 at 18:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/silent%20overflow/near/124843354):
<p>who is <code>-t0</code>?</p>

#### [ Kevin Buzzard (Apr 09 2018 at 18:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/silent%20overflow/near/124843359):
<p>same as <code>--trust 0</code></p>

#### [ Kevin Buzzard (Apr 09 2018 at 18:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/silent%20overflow/near/124843363):
<p>"trust no-one"</p>

#### [ Kevin Buzzard (Apr 09 2018 at 18:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/silent%20overflow/near/124843411):
<p><code>0 means do not trust any macro, and type check all imported modules</code></p>

#### [ Kevin Buzzard (Apr 09 2018 at 18:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/silent%20overflow/near/124843433):
<p>My session earlier had Lean accepting wrong.lean even at <code>-t0</code> but it's not a proof of false, it's just a proof of something which is false :-)</p>

#### [ Kevin Buzzard (Apr 09 2018 at 18:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/silent%20overflow/near/124843442):
<p>well, AFAIK it's false</p>

#### [ Gabriel Ebner (Apr 09 2018 at 18:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/silent%20overflow/near/124843924):
<p>This would be really awesome, but I get an error:</p>
<div class="codehilite"><pre><span></span>type mismatch, term
  rfl
has type
  ?m_2 = ?m_2
but is expected to have type
  1000 * 1000 + 0 = 1000 * 1000 + 1
</pre></div>

#### [ Kevin Buzzard (Apr 09 2018 at 18:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/silent%20overflow/near/124843933):
<p>ooh</p>

#### [ Kevin Buzzard (Apr 09 2018 at 18:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/silent%20overflow/near/124843973):
<p>so maybe there's a problem with my set-up</p>

#### [ Kevin Buzzard (Apr 09 2018 at 18:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/silent%20overflow/near/124843980):
<div class="codehilite"><pre><span></span>$ lean --version
Lean (version 3.3.1, nightly-2018-04-06, commit 8f55ec4c5037, Release)
</pre></div>

#### [ Kevin Buzzard (Apr 09 2018 at 18:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/silent%20overflow/near/124843982):
<p>Ubuntu 16.04</p>

#### [ Kevin Buzzard (Apr 09 2018 at 18:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/silent%20overflow/near/124843985):
<p>mathlib HEAD</p>

#### [ Kevin Buzzard (Apr 09 2018 at 18:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/silent%20overflow/near/124843992):
<p>Nothing to do with VS Code because I can reproduce on the command line</p>

#### [ Sebastian Ullrich (Apr 09 2018 at 18:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/silent%20overflow/near/124844000):
<p>I can reproduce the issue</p>

#### [ Gabriel Ebner (Apr 09 2018 at 18:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/silent%20overflow/near/124844011):
<p>I now see it with the nightly as well, but not with my git build from master..</p>

#### [ Sebastian Ullrich (Apr 09 2018 at 18:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/silent%20overflow/near/124844059):
<p>...using my git build :)</p>

#### [ Kevin Buzzard (Apr 09 2018 at 18:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/silent%20overflow/near/124844068):
<p>Let me know if you want me to open an issue</p>

#### [ Sebastian Ullrich (Apr 09 2018 at 18:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/silent%20overflow/near/124844077):
<p>...in release mode, could be relevant</p>

#### [ Gabriel Ebner (Apr 09 2018 at 18:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/silent%20overflow/near/124844096):
<p>I'm always running relwithdebinfo.</p>

#### [ Sebastian Ullrich (Apr 09 2018 at 19:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/silent%20overflow/near/124845066):
<p><span class="user-mention" data-user-id="110043">@Gabriel Ebner</span> Some initial observations:<br>
1) the exception is not reported by <a href="https://github.com/leanprover/lean/blob/bdea7d420dbcdb7cce700eb62c129387707016fc/src/frontends/lean/definition_cmds.cpp#L711" target="_blank" title="https://github.com/leanprover/lean/blob/bdea7d420dbcdb7cce700eb62c129387707016fc/src/frontends/lean/definition_cmds.cpp#L711">check_example</a> because <code>stack_space_exception</code> is not a <code>lean::exception</code><br>
2) It's then caught by <a href="https://github.com/leanprover/lean/blob/69322cd523e4087530af7cefe3198a1315f6379d/src/util/task.cpp#L60" target="_blank" title="https://github.com/leanprover/lean/blob/69322cd523e4087530af7cefe3198a1315f6379d/src/util/task.cpp#L60">task_queue::execute</a> but never reported, apparently</p>

#### [ Gabriel Ebner (Apr 09 2018 at 19:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/silent%20overflow/near/124845166):
<p>Yeah, <code>task_queue::execute</code> doesn't report errors.</p>

#### [ Gabriel Ebner (Apr 09 2018 at 19:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/silent%20overflow/near/124845241):
<p>I guess we should catch all exceptions in <code>check_example</code> to be consistent with <code>add</code> in <code>module.cpp</code>.</p>

#### [ Gabriel Ebner (Apr 09 2018 at 19:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/silent%20overflow/near/124845319):
<p>I can now reproduce the error as well.  It just takes a slightly larger number:</p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">:</span> <span class="mi">1000</span><span class="bp">*</span><span class="mi">1000</span><span class="bp">*</span><span class="mi">100</span> <span class="bp">+</span> <span class="mi">0</span> <span class="bp">=</span> <span class="mi">1000</span><span class="bp">*</span><span class="mi">1000</span><span class="bp">*</span><span class="mi">100</span> <span class="bp">+</span> <span class="mi">1</span> <span class="o">:=</span> <span class="n">rfl</span> <span class="c1">-- no problem</span>
</pre></div>

#### [ Sebastian Ullrich (Apr 09 2018 at 19:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/silent%20overflow/near/124845399):
<p>Surely we should try and report the caught exception at some point...?</p>

#### [ Gabriel Ebner (Apr 09 2018 at 19:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/silent%20overflow/near/124845410):
<p>Yes, in <code>check_example</code>.  We just need to add <code>std::</code> in front of the exception, and add a second catch-all <code>...</code> case like in <code>add</code>.</p>

#### [ Sebastian Ullrich (Apr 09 2018 at 19:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/silent%20overflow/near/124845431):
<p>That too, but the task_queue shouldn't just swallow exceptions silently</p>

#### [ Gabriel Ebner (Apr 09 2018 at 19:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/silent%20overflow/near/124845501):
<p><del>Mmh, good point.  At least some debugging output on stderr would be good.  For exceptions inheriting <code>std::exception</code> we can even print the error message.</del></p>

#### [ Gabriel Ebner (Apr 09 2018 at 19:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/silent%20overflow/near/124845565):
<p>That won't work, many tasks end in an exceptional state.  And these exceptions are eventually reported.  We wouldn't want to print something to stderr for every red squiggle the user sees.</p>

#### [ Gabriel Ebner (Apr 09 2018 at 19:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/silent%20overflow/near/124845579):
<p>This is similar to the failed promise issue in javascript.  There, a promise can also fail without throwing an exception or printing anything, you only get notified of the error if you listen to it.</p>

#### [ Sebastian Ullrich (Apr 09 2018 at 19:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/silent%20overflow/near/124845952):
<p>In the sane promise APIs I know, not extracting the exception will make the promise throw it in its destructor. Which may kill the process if the exception is not caught in a background thread.</p>

#### [ Sebastian Ullrich (Apr 09 2018 at 19:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/silent%20overflow/near/124845954):
<p>We could do the same</p>


{% endraw %}
