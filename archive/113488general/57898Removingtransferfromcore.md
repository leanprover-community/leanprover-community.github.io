---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/57898Removingtransferfromcore.html
---

## Stream: [general](index.html)
### Topic: [Removing transfer from core](57898Removingtransferfromcore.html)

---


{% raw %}
#### [ Gabriel Ebner (Jan 10 2019 at 12:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Removing%20transfer%20from%20core/near/154832021):
<p><span class="user-mention" data-user-id="110294">@Johannes Hölzl</span> suggested removing transfer from core and move it into mathlib.  Maybe the biggest positive effect is that we could then use the ⇒ symbol in mathlib.<br>
I tried just removing the file, but some theorems about integers and dlist are proving using transfer.  Any ideas?  Does anyone want to rewrite the proofs by hand?  Should we just remove the ⇒ notation for 3.4.2?</p>

#### [ Kevin Buzzard (Jan 10 2019 at 12:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Removing%20transfer%20from%20core/near/154832868):
<p>Can one move those theorems about integers out of core as well?</p>

#### [ Gabriel Ebner (Jan 10 2019 at 13:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Removing%20transfer%20from%20core/near/154835519):
<p>Probably not:</p>
<div class="codehilite"><pre><span></span><span class="kn">instance</span> <span class="o">:</span> <span class="n">comm_ring</span> <span class="n">int</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">add</span>            <span class="o">:=</span> <span class="n">int</span><span class="bp">.</span><span class="n">add</span><span class="o">,</span>
  <span class="n">add_assoc</span>      <span class="o">:=</span> <span class="k">by</span> <span class="n">int</span><span class="bp">.</span><span class="n">transfer</span><span class="o">,</span>
  <span class="n">zero</span>           <span class="o">:=</span> <span class="n">int</span><span class="bp">.</span><span class="n">zero</span><span class="o">,</span>
  <span class="n">zero_add</span>       <span class="o">:=</span> <span class="k">by</span> <span class="n">int</span><span class="bp">.</span><span class="n">transfer</span><span class="o">,</span>
  <span class="n">add_zero</span>       <span class="o">:=</span> <span class="k">by</span> <span class="n">int</span><span class="bp">.</span><span class="n">transfer</span><span class="o">,</span>
  <span class="n">neg</span>            <span class="o">:=</span> <span class="n">int</span><span class="bp">.</span><span class="n">neg</span><span class="o">,</span>
  <span class="n">add_left_neg</span>   <span class="o">:=</span> <span class="k">by</span> <span class="n">int</span><span class="bp">.</span><span class="n">transfer</span><span class="o">,</span>
  <span class="n">add_comm</span>       <span class="o">:=</span> <span class="k">by</span> <span class="n">int</span><span class="bp">.</span><span class="n">transfer</span><span class="o">,</span>
  <span class="n">mul</span>            <span class="o">:=</span> <span class="n">int</span><span class="bp">.</span><span class="n">mul</span><span class="o">,</span>
  <span class="n">mul_assoc</span>      <span class="o">:=</span> <span class="k">by</span> <span class="n">int</span><span class="bp">.</span><span class="n">transfer</span> <span class="n">tt</span><span class="o">,</span>
  <span class="n">one</span>            <span class="o">:=</span> <span class="n">int</span><span class="bp">.</span><span class="n">one</span><span class="o">,</span>
  <span class="n">one_mul</span>        <span class="o">:=</span> <span class="k">by</span> <span class="n">int</span><span class="bp">.</span><span class="n">transfer</span><span class="o">,</span>
  <span class="n">mul_one</span>        <span class="o">:=</span> <span class="k">by</span> <span class="n">int</span><span class="bp">.</span><span class="n">transfer</span><span class="o">,</span>
  <span class="n">left_distrib</span>   <span class="o">:=</span> <span class="k">by</span> <span class="n">int</span><span class="bp">.</span><span class="n">transfer</span> <span class="n">tt</span><span class="o">,</span>
  <span class="n">right_distrib</span>  <span class="o">:=</span> <span class="k">by</span> <span class="n">int</span><span class="bp">.</span><span class="n">transfer</span> <span class="n">tt</span><span class="o">,</span>
  <span class="n">mul_comm</span>       <span class="o">:=</span> <span class="k">by</span> <span class="n">int</span><span class="bp">.</span><span class="n">transfer</span><span class="o">}</span>
</pre></div>

#### [ Simon Hudon (Jan 10 2019 at 17:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Removing%20transfer%20from%20core/near/154853060):
<p>Can a more specific script handle them? E.g. search and replace mul with add and other lemmas similarly? Also Can we take dlist out of core?</p>

#### [ Gabriel Ebner (Jan 10 2019 at 17:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Removing%20transfer%20from%20core/near/154853245):
<p><code>dlist</code> is not the problem.  Only three examples for <code>dlist</code> use <code>transfer</code>.</p>

#### [ Gabriel Ebner (Jan 10 2019 at 17:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Removing%20transfer%20from%20core/near/154853346):
<p>It's the integers that are problematic.  We prove that the integers form a commutative ring using transfer, I'm not sure we should remove that instance from core.</p>

#### [ Gabriel Ebner (Jan 10 2019 at 17:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Removing%20transfer%20from%20core/near/154853532):
<p>Maybe I should clarify: <code>transfer</code> here switches between two isomorphic representations of the integers.  The definition of <code>int</code> is an inductive type with two constructors 1) non-negative natural number 2) negative number.  The <code>transfer</code> tactic then switches to the much nicer definition using pairs of natural numbers.</p>

#### [ Andrew Ashworth (Jan 10 2019 at 17:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Removing%20transfer%20from%20core/near/154853971):
<p>The proofs for <code>int</code> should be in the git history, iirc. They were not always proved via transfer, but maybe I am thinking of Lean 2.</p>

#### [ Gabriel Ebner (Jan 10 2019 at 18:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Removing%20transfer%20from%20core/near/154854522):
<p>Doesn't even look so bad.  I thought it was more horrible:</p>
<div class="codehilite"><pre><span></span> <span class="kn">protected</span> <span class="kn">lemma</span> <span class="n">distrib_left</span> <span class="o">(</span><span class="n">a</span> <span class="n">b</span> <span class="n">c</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">)</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">*</span> <span class="o">(</span><span class="n">b</span> <span class="bp">+</span> <span class="n">c</span><span class="o">)</span> <span class="bp">=</span> <span class="n">a</span> <span class="bp">*</span> <span class="n">b</span> <span class="bp">+</span> <span class="n">a</span> <span class="bp">*</span> <span class="n">c</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">cases</span> <span class="o">(</span><span class="n">int</span><span class="bp">.</span><span class="n">left_total_rel_int_nat_nat</span> <span class="n">a</span><span class="o">)</span> <span class="k">with</span> <span class="n">a&#39;</span> <span class="n">ha</span><span class="o">,</span>
  <span class="n">cases</span> <span class="o">(</span><span class="n">int</span><span class="bp">.</span><span class="n">left_total_rel_int_nat_nat</span> <span class="n">b</span><span class="o">)</span> <span class="k">with</span> <span class="n">b&#39;</span> <span class="n">hb</span><span class="o">,</span>
  <span class="n">cases</span> <span class="o">(</span><span class="n">int</span><span class="bp">.</span><span class="n">left_total_rel_int_nat_nat</span> <span class="n">c</span><span class="o">)</span> <span class="k">with</span> <span class="n">c&#39;</span> <span class="n">hc</span><span class="o">,</span>
  <span class="n">apply</span> <span class="o">(</span><span class="n">int</span><span class="bp">.</span><span class="n">rel_eq</span> <span class="o">(</span><span class="n">int</span><span class="bp">.</span><span class="n">rel_mul</span> <span class="n">ha</span> <span class="o">(</span><span class="n">int</span><span class="bp">.</span><span class="n">rel_add</span> <span class="n">hb</span> <span class="n">hc</span><span class="o">))</span>
    <span class="o">(</span><span class="n">int</span><span class="bp">.</span><span class="n">rel_add</span> <span class="o">(</span><span class="n">int</span><span class="bp">.</span><span class="n">rel_mul</span> <span class="n">ha</span> <span class="n">hb</span><span class="o">)</span> <span class="o">(</span><span class="n">int</span><span class="bp">.</span><span class="n">rel_mul</span> <span class="n">ha</span> <span class="n">hc</span><span class="o">)))</span><span class="err">^</span><span class="bp">.</span><span class="n">mpr</span><span class="o">,</span>
  <span class="n">simp</span> <span class="o">[</span><span class="n">mul_add</span><span class="o">,</span> <span class="n">add_mul</span><span class="o">]</span>
<span class="kn">end</span>
</pre></div>


<p><a href="https://github.com/leanprover/lean/commit/1f45995c169fb518177dfad5060b5a748e8a3b1f#diff-3e35acfba743354acb6f107e860bdb79" target="_blank" title="https://github.com/leanprover/lean/commit/1f45995c169fb518177dfad5060b5a748e8a3b1f#diff-3e35acfba743354acb6f107e860bdb79">https://github.com/leanprover/lean/commit/1f45995c169fb518177dfad5060b5a748e8a3b1f#diff-3e35acfba743354acb6f107e860bdb79</a></p>

#### [ Simon Hudon (Jan 10 2019 at 18:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Removing%20transfer%20from%20core/near/154855637):
<p>How are integers used in core? I thought only natural numbers were really needed there</p>

#### [ Reid Barton (Jan 10 2019 at 18:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Removing%20transfer%20from%20core/near/154855944):
<p>What about, in 3.4.2, simply freeing up the character ⇒ somehow, while leaving transfer and the instances in place?</p>

#### [ Simon Hudon (Jan 10 2019 at 18:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Removing%20transfer%20from%20core/near/154856174):
<p>Actually <span class="user-mention" data-user-id="110294">@Johannes Hölzl</span> and I would really like to move <code>transfer</code> to mathlib so that we can keep developing it</p>

#### [ Johannes Hölzl (Jan 10 2019 at 19:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Removing%20transfer%20from%20core/near/154860802):
<p>well, <code>transfer</code> is not so important (we can copy it under another name). I guess <code>⇒</code> is more important for some people</p>

#### [ Mario Carneiro (Jan 10 2019 at 21:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Removing%20transfer%20from%20core/near/154869086):
<p>I can rewrite the proofs for <code>int</code> if required; do the previous proofs work?</p>

#### [ Gabriel Ebner (Jan 10 2019 at 21:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Removing%20transfer%20from%20core/near/154869179):
<p>Probably.</p>

#### [ Gabriel Ebner (Jan 11 2019 at 18:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/Removing%20transfer%20from%20core/near/154931531):
<p>See <a href="https://github.com/leanprover/lean/pull/1989" target="_blank" title="https://github.com/leanprover/lean/pull/1989">https://github.com/leanprover/lean/pull/1989</a></p>


{% endraw %}
