---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/37188newwlog.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [new wlog](https://leanprover-community.github.io/archive/113488general/37188newwlog.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Patrick Massot (May 28 2018 at 11:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/new%20wlog/near/127197261):
<p>Johannes, I'm sorry I didn't properly follow the new wlog discussion, I've been caught by real world. But I really think like it's less powerful than Simon's version. Today I noticed that it doesn't  even try <code>assumption</code> to discharge auxiliary goals.</p>

#### [ Patrick Massot (May 28 2018 at 11:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/new%20wlog/near/127197327):
<p>for instance (I know this is already proven much more efficiently in mathlib, but I was testing stuff):</p>
<div class="codehilite"><pre><span></span><span class="kn">open</span> <span class="n">set</span>
<span class="kn">example</span> <span class="o">(</span><span class="n">X</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">(</span><span class="n">A</span> <span class="n">B</span> <span class="n">C</span> <span class="o">:</span> <span class="n">set</span> <span class="n">X</span><span class="o">)</span> <span class="o">:</span> <span class="n">A</span> <span class="err">∩</span> <span class="o">(</span><span class="n">B</span> <span class="err">∪</span> <span class="n">C</span><span class="o">)</span> <span class="bp">=</span> <span class="o">(</span><span class="n">A</span> <span class="err">∩</span> <span class="n">B</span><span class="o">)</span> <span class="err">∪</span> <span class="o">(</span><span class="n">A</span> <span class="err">∩</span> <span class="n">C</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">ext</span> <span class="n">x</span><span class="o">,</span>
  <span class="n">split</span><span class="o">,</span>
  <span class="o">{</span> <span class="n">intro</span> <span class="n">hyp</span><span class="o">,</span>
    <span class="n">cases</span> <span class="n">hyp</span><span class="o">,</span>
    <span class="n">wlog</span> <span class="n">x_in</span> <span class="o">:</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">B</span> <span class="kn">using</span> <span class="n">B</span> <span class="n">C</span><span class="o">,</span>
    <span class="o">{</span> <span class="n">assumption</span> <span class="o">},</span>
    <span class="o">{</span> <span class="n">exact</span> <span class="n">or</span><span class="bp">.</span><span class="n">inl</span> <span class="bp">⟨</span><span class="n">hyp_left</span><span class="o">,</span> <span class="n">x_in</span><span class="bp">⟩</span> <span class="o">},</span>
    <span class="o">{</span> <span class="n">simpa</span> <span class="o">[</span><span class="n">union_comm</span><span class="o">]</span> <span class="kn">using</span> <span class="n">this</span> <span class="o">}</span> <span class="o">},</span>
  <span class="o">{</span> <span class="n">intro</span> <span class="n">hyp</span><span class="o">,</span>
    <span class="n">wlog</span> <span class="n">x_in</span> <span class="o">:</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">A</span> <span class="err">∩</span> <span class="n">B</span> <span class="kn">using</span> <span class="n">B</span> <span class="n">C</span><span class="o">,</span>
    <span class="o">{</span> <span class="n">assumption</span> <span class="o">},</span>
    <span class="o">{</span> <span class="n">exact</span> <span class="bp">⟨</span><span class="n">x_in</span><span class="bp">.</span><span class="n">left</span><span class="o">,</span> <span class="n">or</span><span class="bp">.</span><span class="n">inl</span> <span class="n">x_in</span><span class="bp">.</span><span class="n">right</span><span class="bp">⟩</span> <span class="o">},</span>
    <span class="o">{</span> <span class="n">simpa</span> <span class="o">[</span><span class="n">union_comm</span><span class="o">]</span> <span class="kn">using</span> <span class="n">this</span> <span class="o">}</span> <span class="o">}</span>
<span class="kn">end</span>
</pre></div>

#### [ Johannes Hölzl (May 28 2018 at 11:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/new%20wlog/near/127197530):
<p>Instead of using <code>assumption</code> to solve it you can use the new <code>:=</code> syntax:</p>
<div class="codehilite"><pre><span></span><span class="n">wlog</span> <span class="n">x_in</span> <span class="o">:=</span> <span class="n">hyp</span> <span class="kn">using</span> <span class="n">B</span> <span class="n">C</span>
</pre></div>


<p>did you try this?</p>

#### [ Patrick Massot (May 28 2018 at 11:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/new%20wlog/near/127197635):
<p>It doesn't seem to do anything</p>

#### [ Johannes Hölzl (May 28 2018 at 12:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/new%20wlog/near/127198551):
<p>My current assumption is that the hypothesis has syntactically the shape <code>p x ∨ q x</code>. I guess I need to unfold the type of the hypothesis.</p>

#### [ Patrick Massot (May 28 2018 at 13:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/new%20wlog/near/127200877):
<p>I don't know if unfolding is always a good move here, but it could attempted if discharging fails without unfolding (backtracking if unfolding also fails)</p>

#### [ Johannes Hölzl (May 28 2018 at 14:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/new%20wlog/near/127203639):
<p>The discharger is only used for the permuation cases, i.e. all <code>p x y z -&gt; p y z x</code> etc (in your case this is the 3rd goal).<br>
<code>wlog</code> now assumes that you eithr explicitly state the disjunction, or your proof it afterwards.</p>

#### [ Patrick Massot (May 28 2018 at 14:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/new%20wlog/near/127203890):
<p>I still don't understand how to use the <code>:=</code> syntax of <code>wlog</code></p>

#### [ Patrick Massot (May 28 2018 at 14:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/new%20wlog/near/127203996):
<p>And I still haven't met a case where I'm not using the <code>wlog</code> as <code>wlog ... with ..., { finish }, { actual work }, { finish }</code></p>

#### [ Johannes Hölzl (May 28 2018 at 15:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/new%20wlog/near/127204823):
<p>The <code>wlog n := H</code> syntax tells <code>wlog</code> that <code>H</code> is a proof of <code>p x y \or p y x</code> (the disjunction which tells us that we only need to look at these two cases). What are your cases you do <code>wlog</code> on?</p>

#### [ Patrick Massot (May 28 2018 at 15:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/new%20wlog/near/127204999):
<p>Can you do the set theoretic example above for instance?</p>

#### [ Johannes Hölzl (May 28 2018 at 15:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/new%20wlog/near/127205163):
<p>I added them to the test cases in mathlib:</p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">(</span><span class="n">X</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">(</span><span class="n">A</span> <span class="n">B</span> <span class="n">C</span> <span class="o">:</span> <span class="n">set</span> <span class="n">X</span><span class="o">)</span> <span class="o">:</span> <span class="n">A</span> <span class="err">∩</span> <span class="o">(</span><span class="n">B</span> <span class="err">∪</span> <span class="n">C</span><span class="o">)</span> <span class="bp">=</span> <span class="o">(</span><span class="n">A</span> <span class="err">∩</span> <span class="n">B</span><span class="o">)</span> <span class="err">∪</span> <span class="o">(</span><span class="n">A</span> <span class="err">∩</span> <span class="n">C</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">ext</span> <span class="n">x</span><span class="o">,</span>
  <span class="n">split</span><span class="o">,</span>
  <span class="o">{</span> <span class="n">intro</span> <span class="n">hyp</span><span class="o">,</span>
    <span class="n">cases</span> <span class="n">hyp</span><span class="o">,</span>
    <span class="n">wlog</span> <span class="n">x_in</span> <span class="o">:</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">B</span> <span class="o">:=</span> <span class="n">hyp_right</span> <span class="kn">using</span> <span class="n">B</span> <span class="n">C</span><span class="o">,</span>
    <span class="o">{</span> <span class="n">exact</span> <span class="n">or</span><span class="bp">.</span><span class="n">inl</span> <span class="bp">⟨</span><span class="n">hyp_left</span><span class="o">,</span> <span class="n">x_in</span><span class="bp">⟩</span> <span class="o">},</span> <span class="o">},</span>
  <span class="o">{</span> <span class="n">intro</span> <span class="n">hyp</span><span class="o">,</span>
    <span class="n">wlog</span> <span class="n">x_in</span> <span class="o">:</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">A</span> <span class="err">∩</span> <span class="n">B</span> <span class="o">:=</span> <span class="n">hyp</span> <span class="kn">using</span> <span class="n">B</span> <span class="n">C</span><span class="o">,</span>
    <span class="o">{</span> <span class="n">exact</span> <span class="bp">⟨</span><span class="n">x_in</span><span class="bp">.</span><span class="n">left</span><span class="o">,</span> <span class="n">or</span><span class="bp">.</span><span class="n">inl</span> <span class="n">x_in</span><span class="bp">.</span><span class="n">right</span><span class="bp">⟩</span> <span class="o">}</span> <span class="o">}</span>
<span class="kn">end</span>
</pre></div>


<p>The permutation proof is now done using the SMT framework, which seams to work better on these examples.  But sometimes they don't work and I'm not sure yet why not.</p>

#### [ Johannes Hölzl (May 28 2018 at 15:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/new%20wlog/near/127205187):
<p>You can also write</p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">(</span><span class="n">X</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">(</span><span class="n">A</span> <span class="n">B</span> <span class="n">C</span> <span class="o">:</span> <span class="n">set</span> <span class="n">X</span><span class="o">)</span> <span class="o">:</span> <span class="n">A</span> <span class="err">∩</span> <span class="o">(</span><span class="n">B</span> <span class="err">∪</span> <span class="n">C</span><span class="o">)</span> <span class="bp">=</span> <span class="o">(</span><span class="n">A</span> <span class="err">∩</span> <span class="n">B</span><span class="o">)</span> <span class="err">∪</span> <span class="o">(</span><span class="n">A</span> <span class="err">∩</span> <span class="n">C</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">ext</span> <span class="n">x</span><span class="o">,</span>
  <span class="n">split</span><span class="o">,</span>
  <span class="o">{</span> <span class="n">intro</span> <span class="n">hyp</span><span class="o">,</span>
    <span class="n">wlog</span> <span class="n">x_in</span> <span class="o">:</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">B</span> <span class="o">:=</span> <span class="n">hyp</span><span class="bp">.</span><span class="mi">2</span> <span class="kn">using</span> <span class="n">B</span> <span class="n">C</span><span class="o">,</span>
    <span class="o">{</span> <span class="n">exact</span> <span class="n">or</span><span class="bp">.</span><span class="n">inl</span> <span class="bp">⟨</span><span class="n">hyp</span><span class="bp">.</span><span class="mi">1</span><span class="o">,</span> <span class="n">x_in</span><span class="bp">⟩</span> <span class="o">},</span> <span class="o">},</span>
  <span class="o">{</span> <span class="n">intro</span> <span class="n">hyp</span><span class="o">,</span>
    <span class="n">wlog</span> <span class="n">x_in</span> <span class="o">:</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">A</span> <span class="err">∩</span> <span class="n">B</span> <span class="o">:=</span> <span class="n">hyp</span> <span class="kn">using</span> <span class="n">B</span> <span class="n">C</span><span class="o">,</span>
    <span class="o">{</span> <span class="n">exact</span> <span class="bp">⟨</span><span class="n">x_in</span><span class="bp">.</span><span class="n">left</span><span class="o">,</span> <span class="n">or</span><span class="bp">.</span><span class="n">inl</span> <span class="n">x_in</span><span class="bp">.</span><span class="n">right</span><span class="bp">⟩</span> <span class="o">}</span> <span class="o">}</span>
<span class="kn">end</span>
</pre></div>


<p>It's not necessary that you perform the <code>cases hyp</code> in the first case.</p>

#### [ Patrick Massot (May 28 2018 at 15:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/new%20wlog/near/127205270):
<p>Thanks! Is this meant to work with current mathlib?</p>

#### [ Patrick Massot (May 28 2018 at 15:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/new%20wlog/near/127205298):
<p>Lean complains <code>Cases contains variables not declared in </code>using x y z<code> </code></p>

#### [ Johannes Hölzl (May 28 2018 at 15:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/new%20wlog/near/127205315):
<p>Just a second I fixed some problems with supporting <code>_ ∪ _ </code></p>

#### [ Patrick Massot (May 28 2018 at 15:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/new%20wlog/near/127205324):
<p>There is no hurry</p>

#### [ Johannes Hölzl (May 28 2018 at 15:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/new%20wlog/near/127205382):
<p>There is still a strange bug: sometimes the SMT framework solves the permutation problem, in other, nearly equivalent cases it doesn't...</p>

#### [ Patrick Massot (May 28 2018 at 15:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/new%20wlog/near/127205452):
<p>Isn't part of the reason why this SMT stuff is dying?</p>

#### [ Johannes Hölzl (May 28 2018 at 15:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/new%20wlog/near/127205637):
<p>In Lean 3 SMT is still alive :-) We will see what happens in Lean 4. At some point we might want to have a specialized permutation prover which applies symmetry and AC laws.</p>

#### [ Patrick Massot (May 28 2018 at 15:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/new%20wlog/near/127205777):
<p>Maybe we should use Assia's return here. <span class="user-mention" data-user-id="110172">@Assia Mahboubi</span> did you notice <a href="#narrow/stream/113488-general/subject/without.20loss.20of.20advertisement/near/125491146" title="#narrow/stream/113488-general/subject/without.20loss.20of.20advertisement/near/125491146">https://leanprover.zulipchat.com/#narrow/stream/113488-general/subject/without.20loss.20of.20advertisement/near/125491146</a>, <a href="https://github.com/leanprover/mathlib/pull/135" target="_blank" title="https://github.com/leanprover/mathlib/pull/135">https://github.com/leanprover/mathlib/pull/135</a> and the curren thread?</p>

#### [ Patrick Massot (May 28 2018 at 15:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/new%20wlog/near/127205786):
<p>Does it look like what you use in Coq?</p>

#### [ Johannes Hölzl (May 28 2018 at 15:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/new%20wlog/near/127206160):
<p>I just pushed a couple of fixes w.r.t. to the discharger and the handling of <code>_ ∪ _</code>.</p>

#### [ Johannes Hölzl (May 28 2018 at 15:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/new%20wlog/near/127206255):
<p>the <code>wlog</code> tactic in ssreflect is quiet different from Lean's. In ssreflect the <code>wlog</code> tactic introduces  cut, and can be used to generalize some terms. While in Lean it is used to handle do permutations of variables.</p>

#### [ Assia Mahboubi (May 28 2018 at 16:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/new%20wlog/near/127207476):
<p>Hi <span class="user-mention" data-user-id="110031">@Patrick Massot</span> , I was not able to find a precise documentation of the wlog tactic following the links you gave, did I miss something? I must confess that I am starting to have trouble reading Lean code without executing it so it's harder to answer... But from what I could see, <span class="user-mention" data-user-id="110294">@Johannes Hölzl</span> is right, Lean's <code>wlog</code> seems a bit different from Coq's <code>wlog</code>.  Can you describe the behaviour of it? Doesn't it generate a cut in the proof (even if not exposed to the user)? Apologize  in advance if I missed the doc.<br>
Incidentally, there is an even older (2009 I think) paper by John Harrison on <code>wlog</code> reasoning in proof assistants: <a href="https://www.cl.cam.ac.uk/~jrh13/papers/wlog.pdf" target="_blank" title="https://www.cl.cam.ac.uk/~jrh13/papers/wlog.pdf">https://www.cl.cam.ac.uk/~jrh13/papers/wlog.pdf</a></p>

#### [ Patrick Massot (May 28 2018 at 16:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/new%20wlog/near/127207495):
<p>Johannes's version is documented at <a href="https://github.com/leanprover/mathlib/blob/fe7d5738417aeaf835790af2101b98d1758ad8fe/tactic/wlog.lean#L107" target="_blank" title="https://github.com/leanprover/mathlib/blob/fe7d5738417aeaf835790af2101b98d1758ad8fe/tactic/wlog.lean#L107">https://github.com/leanprover/mathlib/blob/fe7d5738417aeaf835790af2101b98d1758ad8fe/tactic/wlog.lean#L107</a></p>

#### [ Assia Mahboubi (May 28 2018 at 16:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/new%20wlog/near/127207504):
<p>But I liked the layout of the script of <code>fundamental</code>,  I agree that it should not be longer than that.</p>

#### [ Patrick Massot (May 28 2018 at 16:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/new%20wlog/near/127207508):
<p>I think the first messages of <a href="#narrow/stream/113488-general/topic/without.20loss.20of.20advertisement" title="#narrow/stream/113488-general/topic/without.20loss.20of.20advertisement">https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/without.20loss.20of.20advertisement</a> should also be a rather good documentation</p>

#### [ Assia Mahboubi (May 28 2018 at 16:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/new%20wlog/near/127207594):
<p>Hmm, this is what I read first and it wasn't enough in my case.</p>

#### [ Patrick Massot (May 28 2018 at 16:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/new%20wlog/near/127207654):
<p>I have no idea how it works. It's like in the mathematician dream: we think in our way and the computer understands without us needing to understand how the computer understands</p>

#### [ Patrick Massot (May 28 2018 at 16:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/new%20wlog/near/127207663):
<p>Of course when it fails you get frustration crises like with Kevin has today</p>

#### [ Assia Mahboubi (May 28 2018 at 16:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/new%20wlog/near/127208541):
<p>Ok so now I have read <span class="user-mention" data-user-id="110294">@Johannes Hölzl</span> , very clear description. So my understanding is that Coq's version is a more general, lower-level building block, and what Johannes describes is a special case, well suited to symmetry arguments and with a nicer syntax. Then Simon seems to bring a very useful layer of automation on top of it. To use the same example as Johannes', in Coq writing<br>
<code>wlog hnm : n m / n &lt;= m =&gt; [h | ]</code><br>
when the current state of the proof is (n m : N)  |- p n m<br>
makes the situation become:<br>
(n m : N) (hnm : n &lt;= m) |- p n m  (i)<br>
and <br>
(n m : N) (h : forall k l, k &lt;= l -&gt; p k l) |- p n m (ii)</p>
<p>(i) is probably the main part of your proof and (ii) should be quite straightforward. But Johannes' version hard-codes the assumption that (ii) will be proved from the fact that (n &lt;= m) \/ (m &lt;= n), when Coq does not.</p>

#### [ Johannes Hölzl (May 28 2018 at 16:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/new%20wlog/near/127208979):
<p>My idea of <code>wlog</code> was to have a generalized version  of John Harrisons <code>wlog</code> to an arbitrary list of variables and cases. But ssreflect's version is a nice building block! <span class="user-mention" data-user-id="110172">@Assia Mahboubi</span> how do you handle the case when your permutation has more than two cases? For example <code>a &lt; b &lt; c \/ a &lt; c &lt; b \/ b &lt; a &lt; c \/ b &lt; c &lt; a \/ c &lt; a &lt; b \/ c &lt; b &lt; a</code> do you need to iterate <code>wlog</code>?</p>

#### [ Assia Mahboubi (May 28 2018 at 17:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/new%20wlog/near/127209436):
<p>Hi <span class="user-mention" data-user-id="110294">@Johannes Hölzl</span>. Correct me if I misunderstand your question. But if I am correct, then no, there is a single <code>wlog</code>, and the main branch of the proof is (1). Then in order to proof (ii), you will need to prove first that your big disjunction holds, and then proceed by case analysis on this big disjunction and used hypothesis <code>h</code> in each case. The only difference I see here is that you have a nice syntax to generate the big disjunction, which is a cut in the proof (ii). This is why I described your implementation as a specialization of Coq's <code>wlog</code>, which on the other hand deals with <code>wlog</code> arguments that may not rely on this kind of properties of the relation.</p>

#### [ Johannes Hölzl (May 28 2018 at 17:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/new%20wlog/near/127209700):
<p>Ah, thanks for the clarification! And I agree that Coq's <code>wlog</code> is more general.</p>


{% endraw %}
