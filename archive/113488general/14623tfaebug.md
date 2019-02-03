---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/14623tfaebug.html
---

## Stream: [general](index.html)
### Topic: [tfae bug](14623tfaebug.html)

---


{% raw %}
#### [ Patrick Massot (Oct 05 2018 at 08:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tfae%20bug/near/135238104):
<p>Minimized from the open maps thread:</p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">(</span><span class="n">P</span> <span class="n">Q</span> <span class="n">R</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">)</span> <span class="o">:</span> <span class="n">tfae</span> <span class="o">[</span><span class="bp">∀</span> <span class="n">x</span><span class="o">,</span> <span class="n">P</span> <span class="n">x</span><span class="o">,</span> <span class="bp">∀</span> <span class="n">x</span><span class="o">,</span> <span class="n">Q</span> <span class="n">x</span><span class="o">,</span> <span class="bp">∀</span> <span class="n">x</span><span class="o">,</span> <span class="n">R</span> <span class="n">x</span><span class="o">]</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">tfae_have</span> <span class="o">:</span> <span class="mi">1</span> <span class="bp">→</span> <span class="mi">3</span><span class="o">,</span> <span class="k">by</span> <span class="n">sorry</span><span class="o">,</span>
  <span class="n">tfae_have</span> <span class="o">:</span> <span class="mi">3</span> <span class="bp">→</span> <span class="mi">1</span><span class="o">,</span> <span class="k">by</span> <span class="n">sorry</span><span class="o">,</span>
  <span class="n">tfae_have</span> <span class="o">:</span> <span class="mi">3</span> <span class="bp">↔</span> <span class="mi">2</span><span class="o">,</span> <span class="k">by</span> <span class="n">sorry</span><span class="o">,</span>
  <span class="n">tfae_finish</span><span class="o">,</span>
<span class="kn">end</span>
</pre></div>


<p>fails with: <code>exact tactic failed, type mismatch, given expression has type
  (∀ (x : α), Q x) ↔ ∀ (x : α), R x
but is expected to have type
  (∀ (x : α), Q x) ↔ ∀ (x : α), P x</code></p>

#### [ Simon Hudon (Oct 05 2018 at 09:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tfae%20bug/near/135238243):
<p>I'm on it</p>

#### [ Patrick Massot (Oct 05 2018 at 09:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tfae%20bug/near/135238244):
<p>Note that removing the forall hides the issue</p>

#### [ Simon Hudon (Oct 05 2018 at 09:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tfae%20bug/near/135238255):
<p>Does it? That's odd</p>

#### [ Patrick Massot (Oct 05 2018 at 09:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tfae%20bug/near/135238366):
<p>maybe not</p>

#### [ Patrick Massot (Oct 05 2018 at 09:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tfae%20bug/near/135238370):
<p>I changed many times what I tried</p>

#### [ Patrick Massot (Oct 05 2018 at 09:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tfae%20bug/near/135238381):
<p>And also, undo in VScode vim extension is completely crazy, you never know how many steps you will go back</p>

#### [ Patrick Massot (Oct 05 2018 at 09:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tfae%20bug/near/135238463):
<p>Wow, I see completely random behavior</p>

#### [ Patrick Massot (Oct 05 2018 at 09:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tfae%20bug/near/135238466):
<p>I have a series of test cases, restarting Lean server changes the set of failing tests randomly</p>

#### [ Johan Commelin (Oct 05 2018 at 09:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tfae%20bug/near/135238471):
<p>Heisenbugs!</p>

#### [ Johan Commelin (Oct 05 2018 at 09:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tfae%20bug/near/135238534):
<p>A Heisenbug in a theorem prover — the irony</p>

#### [ Patrick Massot (Oct 05 2018 at 09:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tfae%20bug/near/135238543):
<p>My test file is </p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">tfae</span>

<span class="kn">example</span> <span class="o">(</span><span class="n">P</span> <span class="n">Q</span> <span class="n">R</span> <span class="o">:</span> <span class="kt">Prop</span><span class="o">)</span> <span class="o">:</span> <span class="n">tfae</span> <span class="o">[</span><span class="n">P</span><span class="o">,</span> <span class="n">Q</span><span class="o">,</span> <span class="n">R</span><span class="o">]</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">tfae_have</span> <span class="o">:</span> <span class="mi">1</span> <span class="bp">→</span> <span class="mi">2</span><span class="o">,</span> <span class="k">by</span> <span class="n">sorry</span><span class="o">,</span>
  <span class="n">tfae_have</span> <span class="o">:</span> <span class="mi">2</span> <span class="bp">→</span> <span class="mi">1</span><span class="o">,</span> <span class="k">by</span> <span class="n">sorry</span><span class="o">,</span>
  <span class="n">tfae_have</span> <span class="o">:</span> <span class="mi">3</span> <span class="bp">↔</span> <span class="mi">1</span><span class="o">,</span> <span class="k">by</span> <span class="n">sorry</span><span class="o">,</span>
  <span class="n">tfae_finish</span><span class="o">,</span>
<span class="kn">end</span>
<span class="kn">example</span> <span class="o">(</span><span class="n">P</span> <span class="n">Q</span> <span class="n">R</span> <span class="o">:</span> <span class="kt">Prop</span><span class="o">)</span> <span class="o">:</span> <span class="n">tfae</span> <span class="o">[</span><span class="n">P</span><span class="o">,</span> <span class="n">Q</span><span class="o">,</span> <span class="n">R</span><span class="o">]</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">tfae_have</span> <span class="o">:</span> <span class="mi">1</span> <span class="bp">→</span> <span class="mi">2</span><span class="o">,</span> <span class="k">by</span> <span class="n">sorry</span><span class="o">,</span>
  <span class="n">tfae_have</span> <span class="o">:</span> <span class="mi">2</span> <span class="bp">→</span> <span class="mi">1</span><span class="o">,</span> <span class="k">by</span> <span class="n">sorry</span><span class="o">,</span>
  <span class="n">tfae_have</span> <span class="o">:</span> <span class="mi">1</span> <span class="bp">↔</span> <span class="mi">3</span><span class="o">,</span> <span class="k">by</span> <span class="n">sorry</span><span class="o">,</span>
  <span class="n">tfae_finish</span><span class="o">,</span>
<span class="kn">end</span>
<span class="kn">example</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">(</span><span class="n">P</span> <span class="n">Q</span> <span class="n">R</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">)</span> <span class="o">:</span> <span class="n">tfae</span> <span class="o">[</span><span class="bp">∀</span> <span class="n">x</span><span class="o">,</span> <span class="n">P</span> <span class="n">x</span><span class="o">,</span> <span class="bp">∀</span> <span class="n">x</span><span class="o">,</span> <span class="n">Q</span> <span class="n">x</span><span class="o">,</span> <span class="bp">∀</span> <span class="n">x</span><span class="o">,</span> <span class="n">R</span> <span class="n">x</span><span class="o">]</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">tfae_have</span> <span class="o">:</span> <span class="mi">1</span> <span class="bp">→</span> <span class="mi">2</span><span class="o">,</span> <span class="k">by</span> <span class="n">sorry</span><span class="o">,</span>
  <span class="n">tfae_have</span> <span class="o">:</span> <span class="mi">2</span> <span class="bp">→</span> <span class="mi">1</span><span class="o">,</span> <span class="k">by</span> <span class="n">sorry</span><span class="o">,</span>
  <span class="n">tfae_have</span> <span class="o">:</span> <span class="mi">1</span> <span class="bp">↔</span> <span class="mi">3</span><span class="o">,</span> <span class="k">by</span> <span class="n">sorry</span><span class="o">,</span>
  <span class="n">tfae_finish</span><span class="o">,</span>
<span class="kn">end</span>
<span class="kn">example</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">(</span><span class="n">P</span> <span class="n">Q</span> <span class="n">R</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">)</span> <span class="o">:</span> <span class="n">tfae</span> <span class="o">[</span><span class="bp">∀</span> <span class="n">x</span><span class="o">,</span> <span class="n">P</span> <span class="n">x</span><span class="o">,</span> <span class="bp">∀</span> <span class="n">x</span><span class="o">,</span> <span class="n">Q</span> <span class="n">x</span><span class="o">,</span> <span class="bp">∀</span> <span class="n">x</span><span class="o">,</span> <span class="n">R</span> <span class="n">x</span><span class="o">]</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">tfae_have</span> <span class="o">:</span> <span class="mi">1</span> <span class="bp">→</span> <span class="mi">2</span><span class="o">,</span> <span class="k">by</span> <span class="n">sorry</span><span class="o">,</span>
  <span class="n">tfae_have</span> <span class="o">:</span> <span class="mi">2</span> <span class="bp">→</span> <span class="mi">1</span><span class="o">,</span> <span class="k">by</span> <span class="n">sorry</span><span class="o">,</span>
  <span class="n">tfae_have</span> <span class="o">:</span> <span class="mi">3</span> <span class="bp">↔</span> <span class="mi">1</span><span class="o">,</span> <span class="k">by</span> <span class="n">sorry</span><span class="o">,</span>
  <span class="n">tfae_finish</span><span class="o">,</span>
<span class="kn">end</span>
</pre></div>

#### [ Patrick Massot (Oct 05 2018 at 09:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tfae%20bug/near/135238549):
<p>Creating and deleting a line between two examples also changes what works</p>

#### [ Patrick Massot (Oct 05 2018 at 09:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tfae%20bug/near/135238607):
<p>Can anyone see that, or is it only my computer going crazy?</p>

#### [ Johan Commelin (Oct 05 2018 at 09:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tfae%20bug/near/135238615):
<p>I can reproduce</p>

#### [ Johan Commelin (Oct 05 2018 at 09:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tfae%20bug/near/135238624):
<p>Creating and deleting lines changes what works <em>nondeterministically</em>.</p>

#### [ Patrick Massot (Oct 05 2018 at 09:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tfae%20bug/near/135238683):
<p>I guess meta-land allows non-deterministic algorithms</p>

#### [ Simon Hudon (Oct 05 2018 at 09:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tfae%20bug/near/135238704):
<p>I don't get non-deterministic behavior with that code. I'm in emacs.</p>

#### [ Johan Commelin (Oct 05 2018 at 09:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tfae%20bug/near/135238712):
<p>Right... we need a tactic that will first toss a coin to decide if it will actually help you <span class="emoji emoji-1f643" title="upside down">:upside_down:</span></p>

#### [ Simon Hudon (Oct 05 2018 at 09:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tfae%20bug/near/135238720):
<p>I have such tactics</p>

#### [ Patrick Massot (Oct 05 2018 at 09:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tfae%20bug/near/135238739):
<p>we see that</p>

#### [ Johan Commelin (Oct 05 2018 at 09:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tfae%20bug/near/135238742):
<p><span class="user-mention" data-user-id="110026">@Simon Hudon</span> Do you get any errors at all with that code (apart from the sorries)?</p>

#### [ Simon Hudon (Oct 05 2018 at 09:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tfae%20bug/near/135238744):
<p>Yes, it fails deterministically</p>

#### [ Simon Hudon (Oct 05 2018 at 09:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tfae%20bug/near/135238787):
<p><span class="user-mention" data-user-id="110031">@Patrick Massot</span> I'll remember that</p>

#### [ Bryan Gin-ge Chen (Oct 05 2018 at 09:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tfae%20bug/near/135238799):
<blockquote>
<p>And also, undo in VScode vim extension is completely crazy, you never know how many steps you will go back</p>
</blockquote>
<p>This annoys me to no end as well. However it seems that VS code's built-in undo (cmd+z on mac, ctrl+z on other systems) works independently and seems to function properly.</p>

#### [ Simon Hudon (Oct 05 2018 at 09:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tfae%20bug/near/135239970):
<p>Ok now I see the non deterministic behavior. That looks weird. I think it's because some vertices are being ignored and because they are stored in a hash table and their hash code probably depends on the memory address of the expressions which changes from run to run.</p>

#### [ Mario Carneiro (Oct 05 2018 at 09:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tfae%20bug/near/135240044):
<p>is this because of <code>ref</code>?</p>

#### [ Simon Hudon (Oct 05 2018 at 09:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tfae%20bug/near/135240047):
<p>I don't think so</p>

#### [ Simon Hudon (Oct 05 2018 at 09:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tfae%20bug/near/135240076):
<p>I'm only using <code>expr</code> as a key in hash tables</p>

#### [ Patrick Massot (Oct 05 2018 at 09:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tfae%20bug/near/135240138):
<p>In the mean time, I'd like to sorry this <code>tfae</code> and move on. How to you actually use a <code>tfae</code> statement? I don't see anything in the docs</p>

#### [ Simon Hudon (Oct 05 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tfae%20bug/near/135240208):
<p>That's a correct use of tfae.</p>

#### [ Bryan Gin-ge Chen (Oct 05 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tfae%20bug/near/135240212):
<p><code>tfae.out</code> is probably what you want. It's mentioned obliquely in the docs: "In <code>data/list/basic.lean</code>there are propositions of the form..."</p>

#### [ Mario Carneiro (Oct 05 2018 at 09:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tfae%20bug/near/135240221):
<p>you state follow up equivalences you are interested in and refer to the elements of the list by their index</p>

#### [ Mario Carneiro (Oct 05 2018 at 09:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tfae%20bug/near/135240260):
<p>and use those numbers in <code>tfae.out</code></p>

#### [ Simon Hudon (Oct 05 2018 at 09:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tfae%20bug/near/135240283):
<p>With one added oddity: the indices are <code>1 ≤ i ≤ xs.length</code> rather than <code>0 ≤ i &lt; xs.length</code></p>

#### [ Patrick Massot (Oct 05 2018 at 10:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tfae%20bug/near/135240585):
<p>I can't use it, probably because of parameters. Compare:</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">tfae</span>
<span class="kn">open</span> <span class="n">list</span>
<span class="kn">constants</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">(</span><span class="n">P</span> <span class="n">Q</span> <span class="n">R</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">)</span>

<span class="kn">lemma</span> <span class="n">eqv</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="n">P</span> <span class="n">x</span> <span class="bp">↔</span> <span class="n">Q</span> <span class="n">x</span> <span class="o">:=</span>
<span class="n">sorry</span>

<span class="kn">example</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">P</span> <span class="n">x</span><span class="o">)</span> <span class="o">:</span> <span class="n">P</span> <span class="n">x</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">rw</span> <span class="n">eqv</span> <span class="n">at</span> <span class="bp">*</span><span class="o">,</span>
  <span class="n">assumption</span>
<span class="kn">end</span>

<span class="kn">lemma</span> <span class="n">eqvs</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">α</span><span class="o">):</span> <span class="n">tfae</span> <span class="o">[</span><span class="n">P</span> <span class="n">x</span><span class="o">,</span> <span class="n">Q</span> <span class="n">x</span><span class="o">,</span> <span class="n">R</span> <span class="n">x</span><span class="o">]</span> <span class="o">:=</span>
<span class="n">sorry</span>

<span class="kn">example</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">P</span> <span class="n">x</span><span class="o">)</span> <span class="o">:</span> <span class="n">P</span> <span class="n">x</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">rw</span> <span class="n">tfae</span><span class="bp">.</span><span class="n">out</span> <span class="o">(</span><span class="n">eqvs</span> <span class="o">)</span> <span class="mi">1</span> <span class="mi">2</span><span class="o">,</span>
  <span class="n">assumption</span>
<span class="kn">end</span>
</pre></div>

#### [ Simon Hudon (Oct 05 2018 at 10:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tfae%20bug/near/135240708):
<p>Sorry, my comment was misleading: the indices start at 1 in the proof, not when you use the theorem.</p>
<p>Now that I'm saying, I think we should remove that oddity.</p>

#### [ Patrick Massot (Oct 05 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tfae%20bug/near/135240728):
<p>Can you fix my example above?</p>

#### [ Simon Hudon (Oct 05 2018 at 10:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tfae%20bug/near/135240741):
<p><code> rw tfae.out (eqvs ) 0 1,</code></p>

#### [ Patrick Massot (Oct 05 2018 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tfae%20bug/near/135240789):
<p>doesn't work</p>

#### [ Simon Hudon (Oct 05 2018 at 10:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tfae%20bug/near/135240802):
<p>What error do you get?</p>

#### [ Mario Carneiro (Oct 05 2018 at 10:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tfae%20bug/near/135241134):
<p>Sorry I wasn't clear. You can't use it directly as a rewrite rule, you have to restate the theorem and prove it by <code>tfae.out</code></p>

#### [ Mario Carneiro (Oct 05 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tfae%20bug/near/135241156):
<div class="codehilite"><pre><span></span>theorem eqvs_PQ (x : α) : P x ↔ Q x := (eqvs x).out 0 1
theorem eqvs_PR (x : α) : P x ↔ R x := (eqvs x).out 0 2
</pre></div>

#### [ Patrick Massot (Oct 05 2018 at 10:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tfae%20bug/near/135241387):
<p>Thanks. It's somehow disappointing</p>

#### [ Patrick Massot (Oct 05 2018 at 10:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tfae%20bug/near/135241396):
<p>Arg, I'm super late</p>

#### [ Johan Commelin (Oct 05 2018 at 10:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tfae%20bug/near/135241466):
<p>Oooh, that's disappointing indeed.</p>

#### [ Johan Commelin (Oct 05 2018 at 10:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tfae%20bug/near/135241610):
<p>Would something like <code>erw</code> be able to deal with this?</p>

#### [ Simon Hudon (Oct 05 2018 at 10:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tfae%20bug/near/135241679):
<p>What if you could do: <code>from_tfae h : eqvs 0 1</code> first to add an assumption <code>h</code> with the right equivalence?</p>

#### [ Johan Commelin (Oct 05 2018 at 10:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tfae%20bug/near/135241704):
<p>We need a <code>rw</code> on steroids. One that will use more power to do the job. Like <code>simp</code> it should dive into binders etc, so that we no longer need to do the <code>conv</code> dance. And it should also unpack this stuff from <code>tfae.out</code> so that it can just use it to <code>rw</code>.</p>

#### [ Johan Commelin (Oct 05 2018 at 10:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tfae%20bug/near/135241728):
<p><span class="user-mention" data-user-id="110026">@Simon Hudon</span> Yes, you could just do <code>have : P → Q := tfae.out 0 1</code> and then <code>rw this</code>.</p>

#### [ Johan Commelin (Oct 05 2018 at 10:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tfae%20bug/near/135241732):
<p>But it is too verbose.</p>

#### [ Johan Commelin (Oct 05 2018 at 10:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tfae%20bug/near/135241794):
<p>Yes. It's confusing... mathematicians keep complaining that proofs are too compact and unreadable in term mode. Otoh we love the brevity of informal maths...</p>

#### [ Patrick Massot (Oct 06 2018 at 18:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tfae%20bug/near/135317699):
<blockquote>
<blockquote>
<p>And also, undo in VScode vim extension is completely crazy, you never know how many steps you will go back</p>
</blockquote>
<p>This annoys me to no end as well. However it seems that VS code's built-in undo (cmd+z on mac, ctrl+z on other systems) works independently and seems to function properly.</p>
</blockquote>
<p><span class="user-mention" data-user-id="123965">@Bryan Gin-ge Chen</span>  Gabriel just told me to use the trick described in <a href="https://github.com/VSCodeVim/Vim/issues/1490#issuecomment-352167221" target="_blank" title="https://github.com/VSCodeVim/Vim/issues/1490#issuecomment-352167221">https://github.com/VSCodeVim/Vim/issues/1490#issuecomment-352167221</a></p>

#### [ Johan Commelin (Nov 18 2018 at 19:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tfae%20bug/near/147925497):
<p><span class="user-mention" data-user-id="110026">@Simon Hudon</span> How are things going with <code>tfae</code>? Is there something blocking progress? I'm currently stating 5 equivalent conditions for a presheaf to be a sheaf. I think <code>tfae</code> could increase the user experience <span class="emoji emoji-1f603" title="smiley">:smiley:</span></p>

#### [ Simon Hudon (Nov 18 2018 at 19:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tfae%20bug/near/147925626):
<p>I haven't fixed the bug yet, I was under the impression that it didn't always manifest and tfae has been merged so you should be able to use it and cross your fingers.</p>

#### [ Patrick Massot (Nov 19 2018 at 22:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/tfae%20bug/near/147998398):
<p>I can still see the bug using the latest mathlib.</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">tfae</span>

<span class="kn">example</span> <span class="o">(</span><span class="n">P</span> <span class="n">Q</span> <span class="n">R</span> <span class="o">:</span> <span class="kt">Prop</span><span class="o">)</span> <span class="o">:</span> <span class="n">tfae</span> <span class="o">[</span><span class="n">P</span><span class="o">,</span> <span class="n">Q</span><span class="o">,</span> <span class="n">R</span><span class="o">]</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">tfae_have</span> <span class="o">:</span> <span class="mi">1</span> <span class="bp">→</span> <span class="mi">2</span><span class="o">,</span> <span class="k">by</span> <span class="n">sorry</span><span class="o">,</span>
  <span class="n">tfae_have</span> <span class="o">:</span> <span class="mi">2</span> <span class="bp">→</span> <span class="mi">1</span><span class="o">,</span> <span class="k">by</span> <span class="n">sorry</span><span class="o">,</span>
  <span class="n">tfae_have</span> <span class="o">:</span> <span class="mi">3</span> <span class="bp">↔</span> <span class="mi">1</span><span class="o">,</span> <span class="k">by</span> <span class="n">sorry</span><span class="o">,</span>
  <span class="n">tfae_finish</span><span class="o">,</span>
<span class="kn">end</span>
</pre></div>


<p>doesn't work here</p>


{% endraw %}
