---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/21143newbieprooffromassumptionofinductivelydefinedprop.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [newbie: proof from assumption of inductively defined prop](https://leanprover-community.github.io/archive/113488general/21143newbieprooffromassumptionofinductivelydefinedprop.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kevin Sullivan (Oct 17 2018 at 19:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/newbie%3A%20proof%20from%20assumption%20of%20inductively%20defined%20prop/near/135988274):
<p>Given a typical definition of an evenness property ...</p>
<div class="codehilite"><pre><span></span><span class="kn">inductive</span> <span class="n">ev</span><span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="kt">Prop</span>
<span class="bp">|</span> <span class="n">ev_0</span> <span class="o">:</span> <span class="n">ev</span> <span class="mi">0</span>
<span class="bp">|</span> <span class="n">ev_SS</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">n</span><span class="o">,</span> <span class="n">ev</span> <span class="n">n</span> <span class="bp">→</span> <span class="n">ev</span> <span class="o">(</span><span class="n">n</span> <span class="bp">+</span> <span class="mi">2</span><span class="o">)</span>
</pre></div>


<p>Here's a script that proves that 7 isn't even:</p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">:</span> <span class="bp">¬</span> <span class="n">ev</span> <span class="mi">7</span> <span class="o">:=</span>
<span class="k">begin</span>
<span class="k">assume</span> <span class="n">ev7</span><span class="o">,</span>
<span class="n">cases</span> <span class="n">ev7</span> <span class="k">with</span> <span class="n">ev5</span><span class="o">,</span>
<span class="n">cases</span> <span class="n">ev7_a</span><span class="o">,</span>
<span class="n">cases</span> <span class="n">ev7_a_a</span><span class="o">,</span>
<span class="n">cases</span> <span class="n">ev7_a_a_a</span><span class="o">,</span>
<span class="kn">end</span>
</pre></div>


<p>To prove that 8 is even, I can use repeat { apply ev_SS }.</p>
<p>What is a stylistically nicer way to prove that 7 isn't even.</p>

#### [ Kevin Buzzard (Oct 17 2018 at 20:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/newbie%3A%20proof%20from%20assumption%20of%20inductively%20defined%20prop/near/135989820):
<p>You could move this thread into the <code>new members</code> stream. And if you're posting code you can triple quote it: write <code> ```lean </code> at the beginning and <code> ``` </code> at the end. For your question: you could prove <code>ev n</code> was decidable, and then <code>dec_trivial</code> would decide it.</p>

#### [ Andrew Ashworth (Oct 17 2018 at 20:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/newbie%3A%20proof%20from%20assumption%20of%20inductively%20defined%20prop/near/135990543):
<p>I think this is something that can be improved in Lean 4, when reflection runs a bit faster. <a href="https://people.csail.mit.edu/jgross/personal-website/papers/2018-reification-by-parametricity-itp-camera-ready.pdf" target="_blank" title="https://people.csail.mit.edu/jgross/personal-website/papers/2018-reification-by-parametricity-itp-camera-ready.pdf">https://people.csail.mit.edu/jgross/personal-website/papers/2018-reification-by-parametricity-itp-camera-ready.pdf</a></p>

#### [ Andrew Ashworth (Oct 17 2018 at 20:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/newbie%3A%20proof%20from%20assumption%20of%20inductively%20defined%20prop/near/135990685):
<p>the paper's first few sections go through several ways of implementing an evenness checker</p>

#### [ Kevin Buzzard (Oct 17 2018 at 20:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/newbie%3A%20proof%20from%20assumption%20of%20inductively%20defined%20prop/near/135992402):
<p>got it:</p>
<div class="codehilite"><pre><span></span><span class="kn">instance</span> <span class="n">decidable_ev</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">n</span><span class="o">,</span> <span class="n">decidable</span> <span class="o">(</span><span class="n">ev</span> <span class="n">n</span><span class="o">)</span>
<span class="bp">|</span> <span class="mi">0</span> <span class="o">:=</span> <span class="n">is_true</span> <span class="n">ev_0</span>
<span class="bp">|</span> <span class="mi">1</span> <span class="o">:=</span> <span class="n">is_false</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">ev1</span><span class="o">,</span> <span class="k">by</span> <span class="n">cases</span> <span class="n">ev1</span><span class="o">)</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">n</span> <span class="bp">+</span> <span class="mi">2</span><span class="o">)</span> <span class="o">:=</span> <span class="n">decidable_of_decidable_of_iff</span> <span class="o">(</span><span class="n">decidable_ev</span> <span class="n">n</span><span class="o">)</span> <span class="err">$</span> <span class="o">(</span><span class="n">ev_SS_iff</span> <span class="n">n</span><span class="o">)</span><span class="bp">.</span><span class="n">symm</span>

<span class="kn">example</span> <span class="o">:</span> <span class="bp">¬</span> <span class="n">ev</span> <span class="mi">7</span> <span class="o">:=</span> <span class="n">dec_trivial</span>
</pre></div>

#### [ Kevin Buzzard (Oct 17 2018 at 20:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/newbie%3A%20proof%20from%20assumption%20of%20inductively%20defined%20prop/near/135992403):
<p>dammit I failed:</p>
<div class="codehilite"><pre><span></span><span class="kn">inductive</span> <span class="n">ev</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="kt">Prop</span>
<span class="bp">|</span> <span class="n">ev_0</span> <span class="o">:</span> <span class="n">ev</span> <span class="mi">0</span>
<span class="bp">|</span> <span class="n">ev_SS</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">n</span><span class="o">,</span> <span class="n">ev</span> <span class="n">n</span> <span class="bp">→</span> <span class="n">ev</span> <span class="o">(</span><span class="n">n</span> <span class="bp">+</span> <span class="mi">2</span><span class="o">)</span>

<span class="kn">open</span> <span class="n">ev</span>

<span class="kn">lemma</span> <span class="n">ev_SS_iff</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="n">ev</span> <span class="o">(</span><span class="n">n</span> <span class="bp">+</span> <span class="mi">2</span><span class="o">)</span> <span class="bp">↔</span> <span class="n">ev</span> <span class="n">n</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">split</span><span class="o">,</span>
  <span class="o">{</span> <span class="c1">-- cases way</span>
    <span class="n">intro</span> <span class="n">evSS</span><span class="o">,</span>
    <span class="n">cases</span> <span class="n">evSS</span><span class="o">,</span>
    <span class="n">assumption</span>
  <span class="o">},</span>
  <span class="o">{</span> <span class="c1">-- easy way</span>
    <span class="n">exact</span> <span class="n">ev_SS</span> <span class="n">n</span>
  <span class="o">}</span>
<span class="kn">end</span>

<span class="kn">open</span> <span class="n">ev</span>

<span class="kn">instance</span> <span class="n">decidable_ev</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">n</span><span class="o">,</span> <span class="n">decidable</span> <span class="o">(</span><span class="n">ev</span> <span class="n">n</span><span class="o">)</span>
<span class="bp">|</span> <span class="mi">0</span> <span class="o">:=</span> <span class="n">is_true</span> <span class="n">ev_0</span>
<span class="bp">|</span> <span class="mi">1</span> <span class="o">:=</span> <span class="n">is_false</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">ev1</span><span class="o">,</span> <span class="k">by</span> <span class="n">cases</span> <span class="n">ev1</span><span class="o">)</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">n</span> <span class="bp">+</span> <span class="mi">2</span><span class="o">)</span> <span class="o">:=</span> <span class="k">begin</span> <span class="n">rw</span> <span class="n">ev_SS_iff</span> <span class="n">n</span><span class="o">,</span> <span class="n">exact</span> <span class="n">decidable_ev</span> <span class="n">n</span> <span class="kn">end</span>

<span class="kn">example</span> <span class="o">:</span> <span class="n">decidable</span> <span class="o">(</span><span class="n">ev</span> <span class="mi">2</span><span class="o">)</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">apply_instance</span>

<span class="kn">example</span> <span class="o">:</span> <span class="n">ev</span> <span class="mi">2</span> <span class="o">:=</span> <span class="n">dec_trivial</span> <span class="c1">-- fails</span>
<span class="c">/-</span><span class="cm"></span>
<span class="cm">exact tactic failed, type mismatch, given expression has type</span>
<span class="cm">  true</span>
<span class="cm">but is expected to have type</span>
<span class="cm">  as_true (ev 2)</span>
<span class="cm">state:</span>
<span class="cm">⊢ as_true (ev 2)</span>
<span class="cm">-/</span>
</pre></div>

#### [ Kevin Buzzard (Oct 17 2018 at 20:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/newbie%3A%20proof%20from%20assumption%20of%20inductively%20defined%20prop/near/135992404):
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">:</span> <span class="bp">¬</span> <span class="o">(</span><span class="n">ev</span> <span class="mi">7</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">repeat</span> <span class="o">{</span><span class="n">rw</span> <span class="n">ev_SS_iff</span><span class="o">},</span>
  <span class="n">intro</span> <span class="n">ev1</span><span class="o">,</span><span class="n">cases</span> <span class="n">ev1</span>
<span class="kn">end</span>
</pre></div>


<p>is an answer (using the lemma I proved in the previous post).</p>

#### [ Kevin Buzzard (Oct 17 2018 at 20:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/newbie%3A%20proof%20from%20assumption%20of%20inductively%20defined%20prop/near/135992525):
<p>Sorry, had dodgy internet and posts have appeared in random order</p>

#### [ Chris Hughes (Oct 17 2018 at 20:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/newbie%3A%20proof%20from%20assumption%20of%20inductively%20defined%20prop/near/135992534):
<p>I'm guessing <code>dec_trivial</code> failed because you didn't make decidable an instance.</p>

#### [ Kevin Buzzard (Oct 17 2018 at 20:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/newbie%3A%20proof%20from%20assumption%20of%20inductively%20defined%20prop/near/135992607):
<p>My rw proof doesn't work for some reason</p>

#### [ Scott Olson (Oct 17 2018 at 20:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/newbie%3A%20proof%20from%20assumption%20of%20inductively%20defined%20prop/near/135992638):
<p>I think the problem is rewriting with an <code>iff</code> invokes propext which then cannot reduce?</p>

#### [ Scott Olson (Oct 17 2018 at 20:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/newbie%3A%20proof%20from%20assumption%20of%20inductively%20defined%20prop/near/135992659):
<div class="codehilite"><pre><span></span><span class="bp">#</span><span class="kn">eval</span> <span class="o">(</span><span class="n">ev</span> <span class="mi">2</span> <span class="o">:</span> <span class="n">bool</span><span class="o">)</span> <span class="c1">-- tt</span>
<span class="bp">#</span><span class="n">reduce</span> <span class="o">(</span><span class="n">ev</span> <span class="mi">2</span> <span class="o">:</span> <span class="n">bool</span><span class="o">)</span> <span class="c1">-- decidable.rec (λ (h : ev 2 → false), ff) (λ (h : ev 2), tt) (eq.rec (is_true ev_0) _)</span>
</pre></div>

#### [ Scott Olson (Oct 17 2018 at 20:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/newbie%3A%20proof%20from%20assumption%20of%20inductively%20defined%20prop/near/135992755):
<p>If you <code>set_option pp.proofs true</code> the innocent little <code>_</code> there is <code>(propext &lt;large iff structure expression&gt;)</code></p>

#### [ Kevin Buzzard (Oct 17 2018 at 20:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/newbie%3A%20proof%20from%20assumption%20of%20inductively%20defined%20prop/near/135992771):
<p>Nice!</p>

#### [ Kenny Lau (Oct 17 2018 at 20:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/newbie%3A%20proof%20from%20assumption%20of%20inductively%20defined%20prop/near/135992968):
<div class="codehilite"><pre><span></span><span class="kn">inductive</span> <span class="n">ev</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="kt">Prop</span>
<span class="bp">|</span> <span class="n">ev_0</span> <span class="o">:</span> <span class="n">ev</span> <span class="mi">0</span>
<span class="bp">|</span> <span class="n">ev_SS</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">n</span><span class="o">,</span> <span class="n">ev</span> <span class="n">n</span> <span class="bp">→</span> <span class="n">ev</span> <span class="o">(</span><span class="n">n</span> <span class="bp">+</span> <span class="mi">2</span><span class="o">)</span>

<span class="kn">instance</span> <span class="o">:</span> <span class="n">decidable_pred</span> <span class="n">ev</span>
<span class="bp">|</span> <span class="mi">0</span> <span class="o">:=</span> <span class="n">is_true</span> <span class="n">ev</span><span class="bp">.</span><span class="n">ev_0</span>
<span class="bp">|</span> <span class="mi">1</span> <span class="o">:=</span> <span class="n">is_false</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">H</span><span class="o">,</span> <span class="k">by</span> <span class="n">cases</span> <span class="n">H</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">n</span><span class="bp">+</span><span class="mi">2</span><span class="o">)</span> <span class="o">:=</span> <span class="k">match</span> <span class="n">ev</span><span class="bp">.</span><span class="n">decidable_pred</span> <span class="n">n</span> <span class="k">with</span>
    <span class="bp">|</span> <span class="n">is_true</span> <span class="n">H</span> <span class="o">:=</span> <span class="n">is_true</span> <span class="o">(</span><span class="n">ev</span><span class="bp">.</span><span class="n">ev_SS</span> <span class="n">n</span> <span class="n">H</span><span class="o">)</span>
    <span class="bp">|</span> <span class="n">is_false</span> <span class="n">H</span> <span class="o">:=</span> <span class="n">is_false</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">h</span><span class="o">,</span> <span class="k">by</span> <span class="n">cases</span> <span class="n">h</span> <span class="k">with</span> <span class="n">h</span> <span class="n">h</span><span class="bp">;</span> <span class="n">exact</span> <span class="n">H</span> <span class="n">h</span><span class="o">)</span>
    <span class="kn">end</span>
</pre></div>

#### [ Chris Hughes (Oct 17 2018 at 20:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/newbie%3A%20proof%20from%20assumption%20of%20inductively%20defined%20prop/near/135993101):
<p><span class="user-mention" data-user-id="110064">@Kenny Lau</span> now that we've established that "computable" functions aren't really computable unless you avoid <code>propext</code> and <code>quot.sound</code>, are you going to start avoiding those axioms as well?</p>

#### [ Kenny Lau (Oct 17 2018 at 20:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/newbie%3A%20proof%20from%20assumption%20of%20inductively%20defined%20prop/near/135993158):
<div class="codehilite"><pre><span></span><span class="kn">inductive</span> <span class="n">ev</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="kt">Prop</span>
<span class="bp">|</span> <span class="n">ev_0</span> <span class="o">:</span> <span class="n">ev</span> <span class="mi">0</span>
<span class="bp">|</span> <span class="n">ev_SS</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">n</span><span class="o">,</span> <span class="n">ev</span> <span class="n">n</span> <span class="bp">→</span> <span class="n">ev</span> <span class="o">(</span><span class="n">n</span> <span class="bp">+</span> <span class="mi">2</span><span class="o">)</span>

<span class="kn">theorem</span> <span class="n">ev_iff</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="n">ev</span> <span class="n">n</span> <span class="bp">↔</span> <span class="n">ev</span> <span class="o">(</span><span class="n">n</span> <span class="bp">+</span> <span class="mi">2</span><span class="o">)</span> <span class="o">:=</span>
<span class="bp">⟨</span><span class="n">ev</span><span class="bp">.</span><span class="n">ev_SS</span> <span class="n">n</span><span class="o">,</span> <span class="bp">λ</span> <span class="n">H</span><span class="o">,</span> <span class="k">by</span> <span class="n">cases</span> <span class="n">H</span> <span class="k">with</span> <span class="n">h</span> <span class="n">h</span><span class="bp">;</span> <span class="n">exact</span> <span class="n">h</span><span class="bp">⟩</span>

<span class="kn">instance</span> <span class="n">decidable_ev</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">n</span><span class="o">,</span> <span class="n">decidable</span> <span class="o">(</span><span class="n">ev</span> <span class="n">n</span><span class="o">)</span>
<span class="bp">|</span> <span class="mi">0</span> <span class="o">:=</span> <span class="n">is_true</span> <span class="n">ev</span><span class="bp">.</span><span class="n">ev_0</span>
<span class="bp">|</span> <span class="mi">1</span> <span class="o">:=</span> <span class="n">is_false</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">ev1</span><span class="o">,</span> <span class="k">by</span> <span class="n">cases</span> <span class="n">ev1</span><span class="o">)</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">n</span> <span class="bp">+</span> <span class="mi">2</span><span class="o">)</span> <span class="o">:=</span> <span class="n">decidable_of_decidable_of_iff</span> <span class="o">(</span><span class="n">decidable_ev</span> <span class="n">n</span><span class="o">)</span> <span class="o">(</span><span class="n">ev_iff</span> <span class="n">n</span><span class="o">)</span>
</pre></div>

#### [ Kenny Lau (Oct 17 2018 at 20:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/newbie%3A%20proof%20from%20assumption%20of%20inductively%20defined%20prop/near/135993447):
<div class="codehilite"><pre><span></span><span class="kn">inductive</span> <span class="n">ev</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="kt">Prop</span>
<span class="bp">|</span> <span class="n">ev_0</span> <span class="o">:</span> <span class="n">ev</span> <span class="mi">0</span>
<span class="bp">|</span> <span class="n">ev_SS</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">n</span><span class="o">,</span> <span class="n">ev</span> <span class="n">n</span> <span class="bp">→</span> <span class="n">ev</span> <span class="o">(</span><span class="n">n</span> <span class="bp">+</span> <span class="mi">2</span><span class="o">)</span>

<span class="n">def</span> <span class="n">ev_b</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="n">bool</span>
<span class="bp">|</span> <span class="mi">0</span> <span class="o">:=</span> <span class="n">tt</span>
<span class="bp">|</span> <span class="mi">1</span> <span class="o">:=</span> <span class="n">ff</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">n</span><span class="bp">+</span><span class="mi">2</span><span class="o">)</span> <span class="o">:=</span> <span class="n">ev_b</span> <span class="n">n</span>

<span class="kn">theorem</span> <span class="n">ev_iff</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">n</span><span class="o">,</span> <span class="n">ev_b</span> <span class="n">n</span> <span class="bp">↔</span> <span class="n">ev</span> <span class="n">n</span>
<span class="bp">|</span> <span class="mi">0</span> <span class="o">:=</span> <span class="bp">⟨λ</span> <span class="bp">_</span><span class="o">,</span> <span class="n">ev</span><span class="bp">.</span><span class="n">ev_0</span><span class="o">,</span> <span class="bp">λ</span> <span class="bp">_</span><span class="o">,</span> <span class="n">rfl</span><span class="bp">⟩</span>
<span class="bp">|</span> <span class="mi">1</span> <span class="o">:=</span> <span class="bp">⟨λ</span> <span class="n">ev1</span><span class="o">,</span> <span class="k">by</span> <span class="n">cases</span> <span class="n">ev1</span><span class="o">,</span> <span class="bp">λ</span> <span class="n">ev1</span><span class="o">,</span> <span class="k">by</span> <span class="n">cases</span> <span class="n">ev1</span><span class="bp">⟩</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">n</span><span class="bp">+</span><span class="mi">2</span><span class="o">)</span> <span class="o">:=</span> <span class="bp">⟨λ</span> <span class="n">evss</span><span class="o">,</span> <span class="n">ev</span><span class="bp">.</span><span class="n">ev_SS</span> <span class="n">n</span> <span class="o">((</span><span class="n">ev_iff</span> <span class="n">n</span><span class="o">)</span><span class="bp">.</span><span class="mi">1</span> <span class="n">evss</span><span class="o">),</span>
    <span class="bp">λ</span> <span class="n">evss</span><span class="o">,</span> <span class="k">by</span> <span class="n">cases</span> <span class="n">evss</span> <span class="k">with</span> <span class="bp">_</span> <span class="n">evss</span><span class="bp">;</span> <span class="n">exact</span> <span class="o">(</span><span class="n">ev_iff</span> <span class="n">n</span><span class="o">)</span><span class="bp">.</span><span class="mi">2</span> <span class="n">evss</span><span class="bp">⟩</span>

<span class="kn">instance</span> <span class="o">:</span> <span class="n">decidable_pred</span> <span class="n">ev</span> <span class="o">:=</span>
<span class="bp">λ</span> <span class="n">n</span><span class="o">,</span> <span class="n">decidable_of_decidable_of_iff</span> <span class="n">infer_instance</span> <span class="o">(</span><span class="n">ev_iff</span> <span class="n">n</span><span class="o">)</span>
</pre></div>

#### [ Mario Carneiro (Oct 17 2018 at 22:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/newbie%3A%20proof%20from%20assumption%20of%20inductively%20defined%20prop/near/135998146):
<p>You should use <code>bodd</code> instead, it has an efficient implementation in VM and a not stupid implementation in kernel</p>


{% endraw %}
