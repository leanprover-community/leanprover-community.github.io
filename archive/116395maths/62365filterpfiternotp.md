---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/62365filterpfiternotp.html
---

## Stream: [maths](https://leanprover-community.github.io/archive/116395maths/index.html)
### Topic: [filter p + fiter not p](https://leanprover-community.github.io/archive/116395maths/62365filterpfiternotp.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kevin Buzzard (Aug 15 2018 at 20:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filter%20p%20%2B%20fiter%20not%20p/near/132190025):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">multiset</span>

<span class="kn">open</span> <span class="n">multiset</span>

<span class="kn">example</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">)</span> <span class="o">(</span><span class="n">M</span> <span class="o">:</span> <span class="n">multiset</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">p</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">)</span> <span class="o">[</span><span class="n">decidable_pred</span> <span class="n">p</span><span class="o">]:</span>
<span class="n">filter</span> <span class="n">p</span> <span class="n">M</span> <span class="bp">+</span> <span class="n">filter</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">a</span><span class="o">,</span> <span class="bp">¬</span> <span class="n">p</span> <span class="n">a</span><span class="o">)</span> <span class="n">M</span> <span class="bp">=</span> <span class="n">M</span> <span class="o">:=</span> <span class="n">sorry</span>
</pre></div>


<p>I want this to be much easier than it's turning out to be! Should I be using <code>add_sub_of_le</code>?</p>

#### [ Kevin Buzzard (Aug 15 2018 at 20:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filter%20p%20%2B%20fiter%20not%20p/near/132190288):
<p>Aah Chris has given me a hint :-)</p>

#### [ Kevin Buzzard (Aug 15 2018 at 21:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filter%20p%20%2B%20fiter%20not%20p/near/132195469):
<p>I'm actually trying to prove this:</p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">(</span><span class="n">L</span> <span class="o">:</span> <span class="n">multiset</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">l</span> <span class="err">∈</span> <span class="n">L</span><span class="o">,</span> <span class="n">l</span> <span class="bp">=</span> <span class="mi">4</span> <span class="bp">∨</span> <span class="n">l</span> <span class="bp">=</span> <span class="mi">6</span> <span class="bp">∨</span> <span class="n">l</span> <span class="bp">≥</span> <span class="mi">8</span><span class="o">)</span> <span class="o">:</span>
<span class="n">L</span> <span class="bp">=</span> <span class="n">filter</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">l</span><span class="o">,</span> <span class="n">l</span> <span class="bp">=</span> <span class="mi">4</span><span class="o">)</span> <span class="n">L</span> <span class="bp">+</span> <span class="n">filter</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">l</span><span class="o">,</span> <span class="n">l</span> <span class="bp">=</span> <span class="mi">6</span><span class="o">)</span> <span class="n">L</span> <span class="bp">+</span> <span class="n">filter</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">l</span><span class="o">,</span> <span class="n">l</span> <span class="bp">≥</span> <span class="mi">8</span><span class="o">)</span> <span class="n">L</span> <span class="o">:=</span> <span class="n">sorry</span>
</pre></div>


<p>and I had suspected I'd be done if I had the example above but now I realise I also need </p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">(</span><span class="n">L</span> <span class="o">:</span> <span class="n">multiset</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">p</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">)</span> <span class="o">(</span><span class="n">q</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">)</span>
<span class="o">[</span><span class="n">decidable_pred</span> <span class="n">p</span><span class="o">]</span> <span class="o">[</span><span class="n">decidable_pred</span> <span class="n">q</span><span class="o">]</span> <span class="o">:</span>
<span class="n">filter</span> <span class="n">p</span> <span class="o">(</span><span class="n">filter</span> <span class="n">q</span> <span class="n">L</span><span class="o">)</span> <span class="bp">=</span> <span class="n">filter</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">a</span><span class="o">,</span> <span class="n">p</span> <span class="n">a</span> <span class="bp">∧</span> <span class="n">q</span> <span class="n">a</span><span class="o">)</span> <span class="n">L</span>
</pre></div>


<p>which I'd assumed would be there. </p>
<p>Am I not thinking about this in the right way?</p>

#### [ Mario Carneiro (Aug 15 2018 at 21:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filter%20p%20%2B%20fiter%20not%20p/near/132195624):
<p>I recently discovered that omission as well</p>

#### [ Mario Carneiro (Aug 15 2018 at 21:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filter%20p%20%2B%20fiter%20not%20p/near/132195642):
<p>I could have sworn there was a theorem like that already</p>

#### [ Kevin Buzzard (Aug 15 2018 at 21:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filter%20p%20%2B%20fiter%20not%20p/near/132196310):
<p>For the filter filter thing I've just discovered <code>filter_map</code></p>

#### [ Kevin Buzzard (Aug 15 2018 at 21:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filter%20p%20%2B%20fiter%20not%20p/near/132196408):
<p>There's <code>filter_map_filter_map</code>, <code>filter_filter_map</code> and <code>filter_map_eq_filter</code> and it might be a case of putting these things together.</p>

#### [ Kevin Buzzard (Aug 15 2018 at 22:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filter%20p%20%2B%20fiter%20not%20p/near/132196580):
<p>Another thing I need is </p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">)</span> <span class="o">(</span><span class="n">p</span> <span class="n">q</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">)</span> <span class="o">(</span><span class="n">L</span> <span class="o">:</span> <span class="n">multiset</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">l</span> <span class="err">∈</span> <span class="n">L</span><span class="o">,</span> <span class="n">p</span> <span class="n">l</span> <span class="bp">↔</span> <span class="n">q</span> <span class="n">l</span><span class="o">)</span>
<span class="o">[</span><span class="n">decidable_pred</span> <span class="n">p</span><span class="o">]</span> <span class="o">[</span><span class="n">decidable_pred</span> <span class="n">q</span><span class="o">]</span> <span class="o">:</span>
<span class="n">filter</span> <span class="n">p</span> <span class="n">L</span> <span class="bp">=</span> <span class="n">filter</span> <span class="n">q</span> <span class="n">L</span> <span class="o">:=</span> <span class="n">sorry</span>
</pre></div>


<p>which I suspect I can get with judicious application of <code>filter_le</code></p>

#### [ Mario Carneiro (Aug 15 2018 at 22:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filter%20p%20%2B%20fiter%20not%20p/near/132197033):
<p>that should definitely be there, it should be called <code>filter_congr</code></p>

#### [ Kevin Buzzard (Aug 15 2018 at 22:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filter%20p%20%2B%20fiter%20not%20p/near/132197419):
<p>It seems that it's there for lists but not multisets. Would you try and deduce it for multisets from the list result or use <code>le_filter</code>?</p>

#### [ Kevin Buzzard (Aug 15 2018 at 22:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filter%20p%20%2B%20fiter%20not%20p/near/132198058):
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">filter_congr</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">)</span> <span class="o">(</span><span class="n">p</span> <span class="n">q</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">)</span> <span class="o">(</span><span class="n">L</span> <span class="o">:</span> <span class="n">multiset</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">l</span> <span class="err">∈</span> <span class="n">L</span><span class="o">,</span> <span class="n">p</span> <span class="n">l</span> <span class="bp">↔</span> <span class="n">q</span> <span class="n">l</span><span class="o">)</span>
<span class="o">[</span><span class="n">decidable_pred</span> <span class="n">p</span><span class="o">]</span> <span class="o">[</span><span class="n">decidable_pred</span> <span class="n">q</span><span class="o">]</span> <span class="o">:</span>
<span class="n">filter</span> <span class="n">p</span> <span class="n">L</span> <span class="bp">=</span> <span class="n">filter</span> <span class="n">q</span> <span class="n">L</span> <span class="o">:=</span>
<span class="n">le_antisymm</span>
  <span class="o">(</span><span class="n">le_filter</span><span class="bp">.</span><span class="mi">2</span> <span class="bp">⟨</span><span class="n">filter_le</span> <span class="bp">_</span><span class="o">,</span><span class="bp">λ</span> <span class="n">a</span> <span class="n">Ha</span><span class="o">,</span> <span class="k">by</span> <span class="n">rw</span> <span class="n">mem_filter</span> <span class="n">at</span> <span class="n">Ha</span><span class="bp">;</span><span class="n">exact</span> <span class="o">(</span><span class="n">H</span> <span class="n">a</span> <span class="n">Ha</span><span class="bp">.</span><span class="mi">1</span><span class="o">)</span><span class="bp">.</span><span class="mi">1</span> <span class="n">Ha</span><span class="bp">.</span><span class="mi">2</span><span class="bp">⟩</span><span class="o">)</span>
  <span class="o">(</span><span class="n">le_filter</span><span class="bp">.</span><span class="mi">2</span> <span class="bp">⟨</span><span class="n">filter_le</span> <span class="bp">_</span><span class="o">,</span><span class="bp">λ</span> <span class="n">a</span> <span class="n">Ha</span><span class="o">,</span> <span class="k">by</span> <span class="n">rw</span> <span class="n">mem_filter</span> <span class="n">at</span> <span class="n">Ha</span><span class="bp">;</span><span class="n">exact</span> <span class="o">(</span><span class="n">H</span> <span class="n">a</span> <span class="n">Ha</span><span class="bp">.</span><span class="mi">1</span><span class="o">)</span><span class="bp">.</span><span class="mi">2</span> <span class="n">Ha</span><span class="bp">.</span><span class="mi">2</span><span class="bp">⟩</span><span class="o">)</span>
</pre></div>


<p>I'm now at the stage where I can usually prove these things, but am wondering whether I should be trying to prove them or just asking one of the experts to prove it in half the time. I guess a few months ago I had a Mario factor of 10, but maybe he'd have a job making that proof ten times smaller.</p>

#### [ Kevin Buzzard (Aug 15 2018 at 22:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filter%20p%20%2B%20fiter%20not%20p/near/132198230):
<p><span class="user-mention" data-user-id="110064">@Kenny Lau</span> when you wake up you might like these</p>

#### [ Mario Carneiro (Aug 15 2018 at 22:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filter%20p%20%2B%20fiter%20not%20p/near/132198236):
<div class="codehilite"><pre><span></span>lemma filter_congr {p q : α → Prop} [decidable_pred p] [decidable_pred q]
  {s : multiset α} : (∀ x ∈ s, p x ↔ q x) → filter p s = filter q s :=
quot.induction_on s $ λ l h, congr_arg coe $ filter_congr h
</pre></div>

#### [ Mario Carneiro (Aug 15 2018 at 22:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filter%20p%20%2B%20fiter%20not%20p/near/132198257):
<p>that's like a mario factor of 2.5 or so</p>

#### [ Mario Carneiro (Aug 15 2018 at 22:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filter%20p%20%2B%20fiter%20not%20p/near/132198259):
<p>so definite improvement :)</p>

#### [ Kevin Buzzard (Aug 15 2018 at 22:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filter%20p%20%2B%20fiter%20not%20p/near/132198264):
<p>so you did go for the list approach. Quotients still scare me :-/</p>

#### [ Mario Carneiro (Aug 15 2018 at 22:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filter%20p%20%2B%20fiter%20not%20p/near/132198307):
<p>the theorem was already there...</p>

#### [ Mario Carneiro (Aug 15 2018 at 22:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filter%20p%20%2B%20fiter%20not%20p/near/132198316):
<p>quot.induction_on is great, since everything is suddenly defeq to the equivalent list definition</p>

#### [ Kevin Buzzard (Aug 15 2018 at 22:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filter%20p%20%2B%20fiter%20not%20p/near/132199346):
<p>So I look at it and think "crumbs, I'll end up having to prove that if L1 and L2 are lists which biject with each other then so do filter p L1 and filter p L2, I'm not sure I fancy that..."</p>

#### [ Chris Hughes (Aug 15 2018 at 22:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filter%20p%20%2B%20fiter%20not%20p/near/132199458):
<p>There's only one list.</p>

#### [ Kevin Buzzard (Aug 15 2018 at 23:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filter%20p%20%2B%20fiter%20not%20p/near/132200798):
<p>I just spent some time actually looking at Mario's proof, and somehow he doesn't have to do at all what I expected him to have to do. The work I imagined having to do is already done in the definition of <code>multiset.filter</code>. Hence the proof is much easier than I'd imagined.</p>

#### [ Kevin Buzzard (Aug 15 2018 at 23:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filter%20p%20%2B%20fiter%20not%20p/near/132201117):
<p>There are 45 instances of this <code>congr_arg coe</code> trick in <code>multiset.lean</code></p>

#### [ Mario Carneiro (Aug 15 2018 at 23:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filter%20p%20%2B%20fiter%20not%20p/near/132201380):
<p>it's basically just saying that when two lists are equal then the multisets they generate are also equal</p>

#### [ Mario Carneiro (Aug 15 2018 at 23:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filter%20p%20%2B%20fiter%20not%20p/near/132201440):
<p>it's very common for multiset equalities after applying <code>quot.induction_on</code> since you might know that the lists are equal</p>

#### [ Mario Carneiro (Aug 15 2018 at 23:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filter%20p%20%2B%20fiter%20not%20p/near/132201459):
<p>for example, associativity of addition of multisets follows from associativity of append on lists, but since the goal is to show that the multisets are equal rather than the lists, we have to <code>congr_arg coe</code></p>

#### [ Mario Carneiro (Aug 15 2018 at 23:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filter%20p%20%2B%20fiter%20not%20p/near/132201474):
<p>if instead, we knew not that the lists were equal but that they were permutations of each other, we would use <code>quot.sound</code> instead</p>

#### [ Kevin Buzzard (Aug 16 2018 at 00:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filter%20p%20%2B%20fiter%20not%20p/near/132202271):
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">(</span><span class="n">L</span> <span class="o">:</span> <span class="n">multiset</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">p</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">)</span> <span class="o">(</span><span class="n">q</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">)</span>
<span class="o">[</span><span class="n">decidable_pred</span> <span class="n">p</span><span class="o">]</span> <span class="o">[</span><span class="n">decidable_pred</span> <span class="n">q</span><span class="o">]</span> <span class="o">:</span>
<span class="n">filter</span> <span class="n">p</span> <span class="o">(</span><span class="n">filter</span> <span class="n">q</span> <span class="n">L</span><span class="o">)</span> <span class="bp">=</span> <span class="n">filter</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">a</span><span class="o">,</span> <span class="n">p</span> <span class="n">a</span> <span class="bp">∧</span> <span class="n">q</span> <span class="n">a</span><span class="o">)</span> <span class="n">L</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">rw</span> <span class="err">←</span><span class="n">filter_map_eq_filter</span> <span class="n">q</span><span class="o">,</span>
  <span class="n">rw</span> <span class="n">filter_filter_map</span><span class="o">,</span>
  <span class="n">rw</span> <span class="err">←</span><span class="n">filter_map_eq_filter</span><span class="o">,</span>
  <span class="n">congr</span><span class="o">,</span>
  <span class="n">funext</span><span class="o">,</span>
  <span class="n">unfold</span> <span class="n">option</span><span class="bp">.</span><span class="n">filter</span><span class="o">,</span>
  <span class="n">unfold</span> <span class="n">option</span><span class="bp">.</span><span class="n">guard</span><span class="o">,</span>
  <span class="n">split_ifs</span><span class="bp">;</span><span class="n">unfold</span> <span class="n">option</span><span class="bp">.</span><span class="n">bind</span><span class="bp">;</span> <span class="n">try</span> <span class="o">{</span><span class="n">unfold</span> <span class="n">option</span><span class="bp">.</span><span class="n">guard</span><span class="bp">;</span><span class="n">split_ifs</span><span class="o">},</span>
  <span class="n">finish</span><span class="o">,</span><span class="n">cc</span><span class="o">,</span><span class="n">finish</span><span class="o">,</span><span class="n">refl</span><span class="o">,</span><span class="n">finish</span><span class="o">,</span>
<span class="kn">end</span>
</pre></div>


<p>I kept wanting it to die but it wouldn't die. I'm not sure this one is mathlib-ready.</p>

#### [ Mario Carneiro (Aug 16 2018 at 00:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filter%20p%20%2B%20fiter%20not%20p/near/132203124):
<p>no worries, I killed it</p>

#### [ Mario Carneiro (Aug 16 2018 at 00:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filter%20p%20%2B%20fiter%20not%20p/near/132203154):
<blockquote>
<p><code>finish,cc,finish,refl,finish</code></p>
</blockquote>
<p>lol, I'm imagining kevin stabbing the proof "die! die! you're finished!"</p>

#### [ Kevin Buzzard (Aug 16 2018 at 01:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filter%20p%20%2B%20fiter%20not%20p/near/132206369):
<p>I guess I can do the original question using <code>multiset.ext</code> if I had these:</p>
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">count_filter_eq_zero</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">)</span> <span class="o">(</span><span class="n">M</span> <span class="o">:</span> <span class="n">multiset</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">p</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">)</span>
<span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">[</span><span class="n">decidable_eq</span> <span class="n">α</span><span class="o">]</span> <span class="o">[</span><span class="n">decidable_pred</span> <span class="n">p</span><span class="o">]</span>
<span class="o">(</span><span class="n">hnp</span> <span class="o">:</span> <span class="bp">¬</span> <span class="n">p</span> <span class="n">a</span><span class="o">)</span> <span class="o">:</span> <span class="n">count</span> <span class="n">a</span> <span class="o">(</span><span class="n">filter</span> <span class="n">p</span> <span class="n">M</span><span class="o">)</span> <span class="bp">=</span> <span class="mi">0</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">rw</span> <span class="n">count_eq_zero</span><span class="o">,</span>
  <span class="n">intro</span> <span class="n">Hin</span><span class="o">,</span>
  <span class="n">rw</span> <span class="n">mem_filter</span> <span class="n">at</span> <span class="n">Hin</span><span class="o">,</span>
  <span class="n">apply</span> <span class="n">hnp</span><span class="o">,</span>
  <span class="n">exact</span> <span class="n">Hin</span><span class="bp">.</span><span class="n">right</span>
<span class="kn">end</span>

<span class="kn">theorem</span> <span class="n">count_filter</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">)</span> <span class="o">(</span><span class="n">M</span> <span class="o">:</span> <span class="n">multiset</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">p</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">)</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">[</span><span class="n">decidable_eq</span> <span class="n">α</span><span class="o">]</span> <span class="o">[</span><span class="n">decidable_pred</span> <span class="n">p</span><span class="o">]</span>
<span class="o">(</span><span class="n">hp</span> <span class="o">:</span> <span class="n">p</span> <span class="n">a</span><span class="o">)</span> <span class="o">:</span> <span class="n">count</span> <span class="n">a</span> <span class="n">M</span> <span class="bp">=</span> <span class="n">count</span> <span class="n">a</span> <span class="o">(</span><span class="n">filter</span> <span class="n">p</span> <span class="n">M</span><span class="o">)</span> <span class="o">:=</span> <span class="n">sorry</span>
</pre></div>


<p>Straightforward for the first one and could easily be mathlibbed up; one could also define <code>count_filter</code> to mean <code>count a (filter p M) = if (p a) then count a M else 0</code>, perhaps that's the natural lemma?</p>

#### [ Mario Carneiro (Aug 16 2018 at 01:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filter%20p%20%2B%20fiter%20not%20p/near/132206556):
<p>I added the theorems fyi</p>

#### [ Kevin Buzzard (Aug 16 2018 at 01:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filter%20p%20%2B%20fiter%20not%20p/near/132207003):
<p>Oh thanks! I was checking email waiting for a push but I now realise that I only get emails for PR's.</p>

#### [ Kenny Lau (Aug 17 2018 at 08:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filter%20p%20%2B%20fiter%20not%20p/near/132285416):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">multiset</span>

<span class="kn">open</span> <span class="n">multiset</span>

<span class="kn">theorem</span> <span class="n">filter_inclusion_exclusion</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">)</span> <span class="o">(</span><span class="n">p</span> <span class="n">q</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">)</span>
  <span class="o">[</span><span class="n">decidable_pred</span> <span class="n">p</span><span class="o">]</span> <span class="o">[</span><span class="n">decidable_pred</span> <span class="n">q</span><span class="o">]</span> <span class="o">(</span><span class="n">L</span> <span class="o">:</span> <span class="n">multiset</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span>
  <span class="n">filter</span> <span class="n">p</span> <span class="n">L</span> <span class="bp">+</span> <span class="n">filter</span> <span class="n">q</span> <span class="n">L</span> <span class="bp">=</span> <span class="n">filter</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">x</span><span class="o">,</span> <span class="n">p</span> <span class="n">x</span> <span class="bp">∨</span> <span class="n">q</span> <span class="n">x</span><span class="o">)</span> <span class="n">L</span> <span class="bp">+</span> <span class="n">filter</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">x</span><span class="o">,</span> <span class="n">p</span> <span class="n">x</span> <span class="bp">∧</span> <span class="n">q</span> <span class="n">x</span><span class="o">)</span> <span class="n">L</span> <span class="o">:=</span>
<span class="n">multiset</span><span class="bp">.</span><span class="n">induction_on</span> <span class="n">L</span> <span class="o">(</span><span class="k">by</span> <span class="n">simp</span><span class="o">)</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">hd</span> <span class="n">tl</span> <span class="n">ih</span><span class="o">,</span>
<span class="k">by</span> <span class="n">by_cases</span> <span class="n">H1</span> <span class="o">:</span> <span class="n">p</span> <span class="n">hd</span><span class="bp">;</span> <span class="n">by_cases</span> <span class="n">H2</span> <span class="o">:</span> <span class="n">q</span> <span class="n">hd</span><span class="bp">;</span> <span class="n">simpa</span> <span class="o">[</span><span class="n">H1</span><span class="o">,</span> <span class="n">H2</span><span class="o">]</span> <span class="kn">using</span> <span class="n">ih</span>

<span class="kn">example</span> <span class="o">(</span><span class="n">L</span> <span class="o">:</span> <span class="n">multiset</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">l</span> <span class="err">∈</span> <span class="n">L</span><span class="o">,</span> <span class="n">l</span> <span class="bp">=</span> <span class="mi">4</span> <span class="bp">∨</span> <span class="n">l</span> <span class="bp">=</span> <span class="mi">6</span> <span class="bp">∨</span> <span class="n">l</span> <span class="bp">≥</span> <span class="mi">8</span><span class="o">)</span> <span class="o">:</span>
<span class="n">L</span> <span class="bp">=</span> <span class="n">filter</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">l</span><span class="o">,</span> <span class="n">l</span> <span class="bp">=</span> <span class="mi">4</span><span class="o">)</span> <span class="n">L</span> <span class="bp">+</span> <span class="n">filter</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">l</span><span class="o">,</span> <span class="n">l</span> <span class="bp">=</span> <span class="mi">6</span><span class="o">)</span> <span class="n">L</span> <span class="bp">+</span> <span class="n">filter</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">l</span><span class="o">,</span> <span class="n">l</span> <span class="bp">≥</span> <span class="mi">8</span><span class="o">)</span> <span class="n">L</span> <span class="o">:=</span>
<span class="k">have</span> <span class="n">H1</span> <span class="o">:</span> <span class="n">filter</span> <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">),</span> <span class="n">x</span> <span class="bp">=</span> <span class="mi">4</span> <span class="bp">∧</span> <span class="n">x</span> <span class="bp">=</span> <span class="mi">6</span><span class="o">)</span> <span class="n">L</span> <span class="bp">=</span> <span class="mi">0</span><span class="o">,</span>
  <span class="k">from</span> <span class="n">filter_eq_nil</span><span class="bp">.</span><span class="mi">2</span> <span class="err">$</span> <span class="bp">λ</span> <span class="bp">_</span> <span class="bp">_</span> <span class="n">H</span><span class="o">,</span> <span class="k">by</span> <span class="n">cc</span><span class="o">,</span>
<span class="k">have</span> <span class="n">H2</span> <span class="o">:</span> <span class="n">filter</span> <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">),</span> <span class="o">(</span><span class="n">x</span> <span class="bp">=</span> <span class="mi">4</span> <span class="bp">∨</span> <span class="n">x</span> <span class="bp">=</span> <span class="mi">6</span><span class="o">)</span> <span class="bp">∧</span> <span class="n">x</span> <span class="bp">≥</span> <span class="mi">8</span><span class="o">)</span> <span class="n">L</span> <span class="bp">=</span> <span class="mi">0</span><span class="o">,</span>
  <span class="k">from</span> <span class="n">filter_eq_nil</span><span class="bp">.</span><span class="mi">2</span> <span class="err">$</span> <span class="bp">λ</span> <span class="bp">_</span> <span class="bp">_</span> <span class="n">H</span><span class="o">,</span> <span class="k">by</span> <span class="n">cases</span> <span class="n">H</span><span class="bp">.</span><span class="mi">1</span><span class="bp">;</span> <span class="n">subst</span> <span class="n">h</span><span class="bp">;</span>
  <span class="k">from</span> <span class="n">absurd</span> <span class="n">H</span><span class="bp">.</span><span class="mi">2</span> <span class="n">dec_trivial</span><span class="o">,</span>
<span class="k">by</span> <span class="n">rw</span> <span class="o">[</span><span class="n">filter_inclusion_exclusion</span><span class="o">,</span> <span class="n">H1</span><span class="o">,</span> <span class="n">add_zero</span><span class="o">]</span><span class="bp">;</span>
<span class="n">rw</span> <span class="o">[</span><span class="n">filter_inclusion_exclusion</span><span class="o">,</span> <span class="n">H2</span><span class="o">,</span> <span class="n">add_zero</span><span class="o">]</span><span class="bp">;</span>
<span class="n">symmetry</span><span class="bp">;</span> <span class="n">rw</span> <span class="o">[</span><span class="n">filter_eq_self</span><span class="o">]</span><span class="bp">;</span> <span class="n">intros</span><span class="bp">;</span>
<span class="n">rw</span> <span class="o">[</span><span class="n">or_assoc</span><span class="o">]</span><span class="bp">;</span> <span class="n">solve_by_elim</span>
</pre></div>

#### [ Mario Carneiro (Aug 17 2018 at 08:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filter%20p%20%2B%20fiter%20not%20p/near/132286367):
<p><code>filter_inclusion_exclusion</code> is already in mathlib, I think I called it <code>filter_add_filter</code></p>

#### [ Kevin Buzzard (Aug 17 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filter%20p%20%2B%20fiter%20not%20p/near/132288987):
<p><span class="user-mention" data-user-id="120469">@Ellen Arlt</span> with this and the 468 lemma you can break up your multiset into those three multisets, and evaluate the sum for the fully controlled value on each one. This is how I would prove the second lemma you emailed me. I'm in a field right now with no laptop so can't do it, but everything you need is now there thanks to Mario and Kenny. If you've not done it by Tuesday I can help then.</p>

#### [ Kevin Buzzard (Aug 17 2018 at 10:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filter%20p%20%2B%20fiter%20not%20p/near/132289276):
<p>Are these holes in mathlib by the way? Here's a stupid question. Is there not yet some completely standard list of "all the things that should be proved about multisets" somewhere, and when people make new proof verifiers they just copy the list? I know <code>multiset.lean</code> is long but in some sense are we still "making it up as we go along" and adding things people need, or will this stop at some point, or is there a known list (eg whatever the analogous file is in coq or whatever) of facts which people will need and which haven't all been written up yet? I'm assuming not. I'm asking what multiset.lean will look like in 5 years' time basically</p>

#### [ Mario Carneiro (Aug 17 2018 at 10:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filter%20p%20%2B%20fiter%20not%20p/near/132289497):
<p>I think it is a process of continuous addition with a finite limit</p>

#### [ Sean Leather (Aug 17 2018 at 10:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filter%20p%20%2B%20fiter%20not%20p/near/132289507):
<p>I think there are a couple of things here:</p>
<p>1. It's hard to imagine all the theorems needed to make a theory (e.g. of multisets) complete.<br>
2. Even if you can imagine them all, it will take time to implement them.<br>
3. If you don't release before you implement them all, nobody else can use what you have in the meantime.</p>

#### [ Mario Carneiro (Aug 17 2018 at 10:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filter%20p%20%2B%20fiter%20not%20p/near/132289524):
<p>for example, <code>filter_inclusion_exclusion</code> is on that list, this 468 lemma is not</p>

#### [ Mario Carneiro (Aug 17 2018 at 10:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filter%20p%20%2B%20fiter%20not%20p/near/132289586):
<p>the criterion is basically to have maximally general theorems which combine at most two or three concepts together</p>

#### [ Mario Carneiro (Aug 17 2018 at 10:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filter%20p%20%2B%20fiter%20not%20p/near/132289624):
<p>i.e. <code>a + b + c = a + (b + c)</code> is a good lemma, <code>a + (a + b) + c + (d + e) = e + a + (a + c) + (d + b)</code> is not</p>

#### [ Mario Carneiro (Aug 17 2018 at 10:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filter%20p%20%2B%20fiter%20not%20p/near/132289841):
<p>Coq probably has a similar file, and they are going through a similar process, but since their file is older I'm sure they will be closer to convergence and we might find a few lemmas there that aren't in mathlib. But no one has the complete list, and like any convergent sequence of integers I'm not sure we would know that we have converged when we do</p>

#### [ Sean Leather (Aug 17 2018 at 10:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filter%20p%20%2B%20fiter%20not%20p/near/132289918):
<p>So we need a (meta) proof that the theory is complete...</p>

#### [ Mario Carneiro (Aug 17 2018 at 10:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filter%20p%20%2B%20fiter%20not%20p/near/132290080):
<p>I think that in principle you could write a program to generate these facts. The hart part would be picking only the true ones</p>

#### [ Mario Carneiro (Aug 17 2018 at 10:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filter%20p%20%2B%20fiter%20not%20p/near/132290108):
<p>But keep in mind that this generation process is also highly dependent on what definitions exist. The more definitions you have, the more ways there are to combine them</p>

#### [ Mario Carneiro (Aug 17 2018 at 10:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filter%20p%20%2B%20fiter%20not%20p/near/132290159):
<p>so a definition can make a previously arbitrary looking statement become a natural question</p>

#### [ Mario Carneiro (Aug 17 2018 at 10:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filter%20p%20%2B%20fiter%20not%20p/near/132290182):
<p>and this is why I take seriously the introduction of new definitions, since every definition comes with a cloud of associated theorems to prove</p>

#### [ Gabriel Ebner (Aug 17 2018 at 10:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filter%20p%20%2B%20fiter%20not%20p/near/132290240):
<blockquote>
<p>I think that in principle you could write a program to generate these facts. The hart part would be picking only the true ones</p>
</blockquote>
<p>Moa Johannson has done some work on theory exploration; <a href="https://github.com/moajohansson/IsaHipster" target="_blank" title="https://github.com/moajohansson/IsaHipster">IsaHipster</a> is pretty much such a tool for Isabelle.  Essentially, they enumerate statements up to a certain size and use random testing to filter out obviously wrong ones.  The rest are handed to sledgehammer.</p>

#### [ Scott Morrison (Aug 22 2018 at 07:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/filter%20p%20%2B%20fiter%20not%20p/near/132559474):
<p>Ugh... I'm not sure I want to be part of a tradition of mathematics that works that way. :-)</p>


{% endraw %}
