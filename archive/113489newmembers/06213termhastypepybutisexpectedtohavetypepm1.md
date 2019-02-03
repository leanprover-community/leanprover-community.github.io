---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/06213termhastypepybutisexpectedtohavetypepm1.html
---

## Stream: [new members](index.html)
### Topic: [term has type p y but is expected to have type p ?m_1[_]](06213termhastypepybutisexpectedtohavetypepm1.html)

---


{% raw %}
#### [ Alistair Tucker (Dec 02 2018 at 17:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/term%20has%20type%20p%20y%20but%20is%20expected%20to%20have%20type%20p%20%3Fm_1%5B_%5D/near/150728969):
<p>Am I trying to do something impossible?</p>
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">mwe</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">{</span><span class="n">p</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">}</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="bp">∃</span> <span class="o">(</span><span class="n">y</span> <span class="o">:</span> <span class="n">α</span><span class="o">),</span> <span class="n">p</span> <span class="n">y</span><span class="o">)</span> <span class="o">:</span> <span class="bp">∃</span> <span class="o">(</span><span class="n">y</span> <span class="o">:</span> <span class="n">α</span><span class="o">),</span> <span class="n">p</span> <span class="n">y</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">apply</span> <span class="n">exists</span><span class="bp">.</span><span class="n">intro</span><span class="o">,</span>
  <span class="n">cases</span> <span class="n">h</span> <span class="k">with</span> <span class="n">y</span> <span class="n">hy</span><span class="o">,</span>
  <span class="n">exact</span> <span class="n">hy</span><span class="o">,</span>
<span class="kn">end</span>
</pre></div>

#### [ Kevin Buzzard (Dec 02 2018 at 17:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/term%20has%20type%20p%20y%20but%20is%20expected%20to%20have%20type%20p%20%3Fm_1%5B_%5D/near/150729021):
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">mwe</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">{</span><span class="n">p</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">}</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="bp">∃</span> <span class="o">(</span><span class="n">y</span> <span class="o">:</span> <span class="n">α</span><span class="o">),</span> <span class="n">p</span> <span class="n">y</span><span class="o">)</span> <span class="o">:</span> <span class="bp">∃</span> <span class="o">(</span><span class="n">y</span> <span class="o">:</span> <span class="n">α</span><span class="o">),</span> <span class="n">p</span> <span class="n">y</span> <span class="o">:=</span> <span class="n">h</span>
</pre></div>


<p>So the theorem is true, at least :-)</p>

#### [ Kevin Buzzard (Dec 02 2018 at 17:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/term%20has%20type%20p%20y%20but%20is%20expected%20to%20have%20type%20p%20%3Fm_1%5B_%5D/near/150729038):
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">mwe</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">{</span><span class="n">p</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">}</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="bp">∃</span> <span class="o">(</span><span class="n">y</span> <span class="o">:</span> <span class="n">α</span><span class="o">),</span> <span class="n">p</span> <span class="n">y</span><span class="o">)</span> <span class="o">:</span> <span class="bp">∃</span> <span class="o">(</span><span class="n">y</span> <span class="o">:</span> <span class="n">α</span><span class="o">),</span> <span class="n">p</span> <span class="n">y</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">cases</span> <span class="n">h</span> <span class="k">with</span> <span class="n">y</span> <span class="n">hy</span><span class="o">,</span>
  <span class="n">apply</span> <span class="n">exists</span><span class="bp">.</span><span class="n">intro</span><span class="o">,</span>
  <span class="n">exact</span> <span class="n">hy</span><span class="o">,</span>
<span class="kn">end</span>
</pre></div>

#### [ Kenny Lau (Dec 02 2018 at 17:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/term%20has%20type%20p%20y%20but%20is%20expected%20to%20have%20type%20p%20%3Fm_1%5B_%5D/near/150729091):
<div class="codehilite"><pre><span></span><span class="n">meta</span> <span class="n">def</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">interactive</span><span class="bp">.</span><span class="n">result</span> <span class="o">:</span> <span class="n">tactic</span> <span class="n">unit</span> <span class="o">:=</span>
<span class="n">tactic</span><span class="bp">.</span><span class="n">result</span> <span class="bp">&gt;&gt;=</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">trace</span>

<span class="kn">theorem</span> <span class="n">mwe</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">{</span><span class="n">p</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">}</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="bp">∃</span> <span class="o">(</span><span class="n">y</span> <span class="o">:</span> <span class="n">α</span><span class="o">),</span> <span class="n">p</span> <span class="n">y</span><span class="o">)</span> <span class="o">:</span> <span class="bp">∃</span> <span class="o">(</span><span class="n">y</span> <span class="o">:</span> <span class="n">α</span><span class="o">),</span> <span class="n">p</span> <span class="n">y</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">apply</span> <span class="n">exists</span><span class="bp">.</span><span class="n">intro</span><span class="o">,</span>
  <span class="n">cases</span> <span class="n">h</span> <span class="k">with</span> <span class="n">y</span> <span class="n">hy</span><span class="o">,</span>
  <span class="n">result</span><span class="o">,</span>
<span class="c">/-</span><span class="cm"></span>
<span class="cm">exists.intro ?m_1 (Exists.dcases_on h (λ (y : α) (hy : p y), ?m_2[h, y, hy]))</span>
<span class="cm">-/</span>
  <span class="n">exact</span> <span class="n">hy</span><span class="o">,</span>
<span class="kn">end</span>
</pre></div>

#### [ Alistair Tucker (Dec 02 2018 at 17:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/term%20has%20type%20p%20y%20but%20is%20expected%20to%20have%20type%20p%20%3Fm_1%5B_%5D/near/150729095):
<p>Yes :)  But there is some reason it's in that order. I think...</p>

#### [ Kenny Lau (Dec 02 2018 at 17:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/term%20has%20type%20p%20y%20but%20is%20expected%20to%20have%20type%20p%20%3Fm_1%5B_%5D/near/150729096):
<p>(<code>result</code> is the proof term constructed at that particular moment)</p>

#### [ Kenny Lau (Dec 02 2018 at 17:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/term%20has%20type%20p%20y%20but%20is%20expected%20to%20have%20type%20p%20%3Fm_1%5B_%5D/near/150729099):
<p>and you can see why this is impossible</p>

#### [ Kevin Buzzard (Dec 02 2018 at 17:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/term%20has%20type%20p%20y%20but%20is%20expected%20to%20have%20type%20p%20%3Fm_1%5B_%5D/near/150729154):
<p>After your application of <code>exists.intro</code> one of your goals has a metavariable, which is not at all ideal. I would recommend not using <code>apply exists.intro</code> for this sort of reason.</p>

#### [ Kevin Buzzard (Dec 02 2018 at 17:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/term%20has%20type%20p%20y%20but%20is%20expected%20to%20have%20type%20p%20%3Fm_1%5B_%5D/near/150729224):
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">mwe</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">{</span><span class="n">p</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">}</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="bp">∃</span> <span class="o">(</span><span class="n">y</span> <span class="o">:</span> <span class="n">α</span><span class="o">),</span> <span class="n">p</span> <span class="n">y</span><span class="o">)</span> <span class="o">:</span> <span class="bp">∃</span> <span class="o">(</span><span class="n">y</span> <span class="o">:</span> <span class="n">α</span><span class="o">),</span> <span class="n">p</span> <span class="n">y</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">apply</span> <span class="n">exists</span><span class="bp">.</span><span class="n">intro</span><span class="o">,</span>
  <span class="c1">-- you now have two goals, and one contains a metavariable.</span>
  <span class="c1">-- this is not recommended.</span>
  <span class="c1">-- Your next line only applies to the first goal.</span>
    <span class="n">cases</span> <span class="n">h</span> <span class="k">with</span> <span class="n">y</span> <span class="n">hy</span><span class="o">,</span>
    <span class="c1">-- your metavariable just got uglier.</span>
    <span class="c1">-- This is even less recommended.</span>
    <span class="n">tactic</span><span class="bp">.</span><span class="n">swap</span><span class="o">,</span>
    <span class="c1">-- we are now working with a sensible goal</span>
    <span class="c1">-- but now we need to get data from a proposition.</span>
    <span class="n">exact</span> <span class="n">classical</span><span class="bp">.</span><span class="n">some</span> <span class="n">h</span><span class="o">,</span> <span class="c1">-- I just used a noncomputable axiom</span>
  <span class="c1">-- one goal now</span>
  <span class="n">exact</span> <span class="n">classical</span><span class="bp">.</span><span class="n">some_spec</span> <span class="bp">⟨</span><span class="n">y</span><span class="o">,</span><span class="n">hy</span><span class="bp">⟩</span><span class="o">,</span> <span class="c1">-- I just undid your &quot;cases h&quot; line.</span>
<span class="kn">end</span>
</pre></div>


<p>That's a way to dig yourself out of the hole.</p>

#### [ Kevin Buzzard (Dec 02 2018 at 17:57)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/term%20has%20type%20p%20y%20but%20is%20expected%20to%20have%20type%20p%20%3Fm_1%5B_%5D/near/150729230):
<p><code>#print axioms mwe -- classical.choice</code></p>

#### [ Kenny Lau (Dec 02 2018 at 17:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/term%20has%20type%20p%20y%20but%20is%20expected%20to%20have%20type%20p%20%3Fm_1%5B_%5D/near/150729285):
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">mwe</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">{</span><span class="n">p</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">}</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="bp">∃</span> <span class="o">(</span><span class="n">y</span> <span class="o">:</span> <span class="n">α</span><span class="o">),</span> <span class="n">p</span> <span class="n">y</span><span class="o">)</span> <span class="o">:</span> <span class="bp">∃</span> <span class="o">(</span><span class="n">y</span> <span class="o">:</span> <span class="n">α</span><span class="o">),</span> <span class="n">p</span> <span class="n">y</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">apply</span> <span class="n">exists</span><span class="bp">.</span><span class="n">intro</span><span class="o">,</span>
  <span class="n">cases</span> <span class="n">h</span> <span class="k">with</span> <span class="n">y</span> <span class="n">hy</span><span class="o">,</span>
  <span class="n">exact</span> <span class="n">classical</span><span class="bp">.</span><span class="n">some_spec</span> <span class="bp">_</span>
<span class="kn">end</span>

<span class="bp">#</span><span class="kn">print</span> <span class="n">mwe</span>
<span class="c">/-</span><span class="cm"></span>
<span class="cm">exists.intro (classical.some h) (Exists.dcases_on h (λ (y : α) (hy : p y), classical.some_spec (Exists.intro y hy)))</span>
<span class="cm">-/</span>
</pre></div>

#### [ Alistair Tucker (Dec 02 2018 at 17:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/term%20has%20type%20p%20y%20but%20is%20expected%20to%20have%20type%20p%20%3Fm_1%5B_%5D/near/150729286):
<p>Ha!  it turns out there was no good reason for putting it in that order :)<br>
What do you recommend instead of apply exists.intro?</p>

#### [ Kevin Buzzard (Dec 02 2018 at 17:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/term%20has%20type%20p%20y%20but%20is%20expected%20to%20have%20type%20p%20%3Fm_1%5B_%5D/near/150729289):
<p><code>use</code></p>

#### [ Reid Barton (Dec 02 2018 at 17:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/term%20has%20type%20p%20y%20but%20is%20expected%20to%20have%20type%20p%20%3Fm_1%5B_%5D/near/150729290):
<p>It would probably be better to do the <code>cases</code> first</p>

#### [ Rob Lewis (Dec 02 2018 at 18:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/term%20has%20type%20p%20y%20but%20is%20expected%20to%20have%20type%20p%20%3Fm_1%5B_%5D/near/150729347):
<p>It's not always bad to <code>apply exists.intro</code> and have a metavar for one goal. Sometimes you want to just show the body of the exists, and let Lean figure out what the witness was by unification. (Like in Kenny's example.)</p>

#### [ Kenny Lau (Dec 02 2018 at 18:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/term%20has%20type%20p%20y%20but%20is%20expected%20to%20have%20type%20p%20%3Fm_1%5B_%5D/near/150729348):
<p>I'm surprised the <code>_</code> worked</p>

#### [ Kevin Buzzard (Dec 02 2018 at 18:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/term%20has%20type%20p%20y%20but%20is%20expected%20to%20have%20type%20p%20%3Fm_1%5B_%5D/near/150729351):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">interactive</span>

<span class="kn">theorem</span> <span class="n">mwe</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">{</span><span class="n">p</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">}</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="bp">∃</span> <span class="o">(</span><span class="n">y</span> <span class="o">:</span> <span class="n">α</span><span class="o">),</span> <span class="n">p</span> <span class="n">y</span><span class="o">)</span> <span class="o">:</span> <span class="bp">∃</span> <span class="o">(</span><span class="n">y</span> <span class="o">:</span> <span class="n">α</span><span class="o">),</span> <span class="n">p</span> <span class="n">y</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">cases</span> <span class="n">h</span> <span class="k">with</span> <span class="n">y</span> <span class="n">hy</span><span class="o">,</span>
  <span class="n">use</span> <span class="n">y</span><span class="o">,</span>
  <span class="n">assumption</span>
<span class="kn">end</span>

<span class="bp">#</span><span class="kn">print</span> <span class="n">axioms</span> <span class="n">mwe</span> <span class="c1">-- no axioms</span>
</pre></div>

#### [ Alistair Tucker (Dec 02 2018 at 18:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/term%20has%20type%20p%20y%20but%20is%20expected%20to%20have%20type%20p%20%3Fm_1%5B_%5D/near/150729362):
<p>"use" is a tactic?</p>

#### [ Kevin Buzzard (Dec 02 2018 at 18:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/term%20has%20type%20p%20y%20but%20is%20expected%20to%20have%20type%20p%20%3Fm_1%5B_%5D/near/150729365):
<p>As of about a week ago</p>

#### [ Kevin Buzzard (Dec 02 2018 at 18:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/term%20has%20type%20p%20y%20but%20is%20expected%20to%20have%20type%20p%20%3Fm_1%5B_%5D/near/150729375):
<p><code>existsi</code> is an older one, it's a bit less robust but it would work here</p>

#### [ Kevin Buzzard (Dec 02 2018 at 18:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/term%20has%20type%20p%20y%20but%20is%20expected%20to%20have%20type%20p%20%3Fm_1%5B_%5D/near/150729418):
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">mwe</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">{</span><span class="n">p</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">}</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="bp">∃</span> <span class="o">(</span><span class="n">y</span> <span class="o">:</span> <span class="n">α</span><span class="o">),</span> <span class="n">p</span> <span class="n">y</span><span class="o">)</span> <span class="o">:</span> <span class="bp">∃</span> <span class="o">(</span><span class="n">y</span> <span class="o">:</span> <span class="n">α</span><span class="o">),</span> <span class="n">p</span> <span class="n">y</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">cases</span> <span class="n">h</span> <span class="k">with</span> <span class="n">y</span> <span class="n">hy</span><span class="o">,</span>
  <span class="n">existsi</span> <span class="n">y</span><span class="o">,</span>
  <span class="n">assumption</span>
<span class="kn">end</span>
</pre></div>

#### [ Kevin Buzzard (Dec 02 2018 at 18:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/term%20has%20type%20p%20y%20but%20is%20expected%20to%20have%20type%20p%20%3Fm_1%5B_%5D/near/150729420):
<p>no import needed</p>

#### [ Alistair Tucker (Dec 02 2018 at 18:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/term%20has%20type%20p%20y%20but%20is%20expected%20to%20have%20type%20p%20%3Fm_1%5B_%5D/near/150729424):
<p>Thank you all</p>

#### [ Reid Barton (Dec 02 2018 at 18:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/term%20has%20type%20p%20y%20but%20is%20expected%20to%20have%20type%20p%20%3Fm_1%5B_%5D/near/150729433):
<p>Your original one didn't work because you wanted <code>exact hy</code> to also solve the other goal with <code>y</code>, but <code>y</code> was not in scope for the other goal!</p>

#### [ Kevin Buzzard (Dec 02 2018 at 18:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/term%20has%20type%20p%20y%20but%20is%20expected%20to%20have%20type%20p%20%3Fm_1%5B_%5D/near/150729480):
<p>Yes! And it's hard to get access to it too, because <code>\exists</code> only eliminates to <code>Prop</code>.</p>

#### [ Kenny Lau (Dec 02 2018 at 18:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/term%20has%20type%20p%20y%20but%20is%20expected%20to%20have%20type%20p%20%3Fm_1%5B_%5D/near/150729501):
<p>again, you can see it using this:</p>
<div class="codehilite"><pre><span></span><span class="n">meta</span> <span class="n">def</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">interactive</span><span class="bp">.</span><span class="n">result</span> <span class="o">:</span> <span class="n">tactic</span> <span class="n">unit</span> <span class="o">:=</span>
<span class="n">tactic</span><span class="bp">.</span><span class="n">result</span> <span class="bp">&gt;&gt;=</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">trace</span>

<span class="kn">theorem</span> <span class="n">mwe</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">{</span><span class="n">p</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">}</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="bp">∃</span> <span class="o">(</span><span class="n">y</span> <span class="o">:</span> <span class="n">α</span><span class="o">),</span> <span class="n">p</span> <span class="n">y</span><span class="o">)</span> <span class="o">:</span> <span class="bp">∃</span> <span class="o">(</span><span class="n">y</span> <span class="o">:</span> <span class="n">α</span><span class="o">),</span> <span class="n">p</span> <span class="n">y</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">apply</span> <span class="n">exists</span><span class="bp">.</span><span class="n">intro</span><span class="o">,</span>
  <span class="n">cases</span> <span class="n">h</span> <span class="k">with</span> <span class="n">y</span> <span class="n">hy</span><span class="o">,</span>
  <span class="n">result</span><span class="o">,</span>
<span class="c">/-</span><span class="cm"></span>
<span class="cm">exists.intro ?m_1 (Exists.dcases_on h (λ (y : α) (hy : p y), ?m_2[h, y, hy]))</span>
<span class="cm">-/</span>
  <span class="n">exact</span> <span class="n">hy</span><span class="o">,</span>
<span class="kn">end</span>
</pre></div>

#### [ Kenny Lau (Dec 02 2018 at 18:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/term%20has%20type%20p%20y%20but%20is%20expected%20to%20have%20type%20p%20%3Fm_1%5B_%5D/near/150729503):
<p>there's no way to unify <code>?m_1</code> with <code>y</code> because <code>y</code> doesn't even exist in the scope of <code>?m_1</code></p>

#### [ Kevin Buzzard (Dec 02 2018 at 18:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/term%20has%20type%20p%20y%20but%20is%20expected%20to%20have%20type%20p%20%3Fm_1%5B_%5D/near/150729543):
<p>[just to be clear -- Kenny's code doesn't run]</p>


{% endraw %}
