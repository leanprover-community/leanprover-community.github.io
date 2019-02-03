---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/28866Stronginductioninlean.html
---

## Stream: [new members](https://leanprover-community.github.io/archive/113489newmembers/index.html)
### Topic: [Strong induction in lean](https://leanprover-community.github.io/archive/113489newmembers/28866Stronginductioninlean.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Calle Sönne (Nov 19 2018 at 17:14)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Strong%20induction%20in%20lean/near/147975900):
<p>I want to prove strong induction in lean but Im having a hard time writing it out. Is it possible to do and-statements of variable length in lean? Something like this is what I want to do in lean:</p>
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">strong_induction</span> <span class="o">(</span><span class="n">P</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">)</span> <span class="o">(</span><span class="n">H0</span> <span class="o">:</span> <span class="n">P</span> <span class="mi">0</span><span class="o">)</span> <span class="o">(</span><span class="n">Hn</span> <span class="o">:</span> <span class="bp">∀</span>
    <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">),</span> <span class="n">P</span> <span class="mi">1</span> <span class="bp">∧</span> <span class="n">P</span> <span class="mi">2</span> <span class="bp">∧</span> <span class="bp">...</span> <span class="bp">∧</span> <span class="n">P</span> <span class="n">n</span> <span class="bp">→</span> <span class="n">P</span> <span class="o">(</span><span class="n">n</span><span class="bp">+</span><span class="mi">1</span><span class="o">))</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">m</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">,</span> <span class="n">P</span> <span class="n">m</span> <span class="o">:=</span> <span class="n">sorry</span>
</pre></div>


<p>or maybe like this if that's possible:</p>
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">strong_induction&#39;</span> <span class="o">(</span><span class="n">P</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">)</span> <span class="o">(</span><span class="n">H0</span> <span class="o">:</span> <span class="n">P</span> <span class="mi">0</span><span class="o">)</span> <span class="o">(</span><span class="n">Hn</span> <span class="o">:</span> <span class="bp">∀</span>
    <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">),</span> <span class="n">P</span> <span class="n">s</span> <span class="bp">→</span> <span class="n">P</span> <span class="o">(</span><span class="n">n</span><span class="bp">+</span><span class="mi">1</span><span class="o">),</span> <span class="bp">∀</span> <span class="o">(</span><span class="n">s</span><span class="o">:</span><span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">Hs</span> <span class="o">:</span> <span class="n">s</span> <span class="bp">≤</span> <span class="n">n</span><span class="o">)</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">m</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">,</span> <span class="n">P</span> <span class="n">m</span> <span class="o">:=</span> <span class="n">sorry</span>
</pre></div>

#### [ Rob Lewis (Nov 19 2018 at 17:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Strong%20induction%20in%20lean/near/147976238):
<p>You might want to look at <code>nat.strong_induction_on</code> and <code>nat.case_strong_induction_on</code>, which follow the pattern of your second example.</p>

#### [ Kevin Buzzard (Nov 19 2018 at 18:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Strong%20induction%20in%20lean/near/147980492):
<p><code>theorem strong_induction (P : ℕ → Prop) (H : ∀ n : ℕ, (∀ m : ℕ, m &lt; n → P m) → P n) (n : ℕ) : P n := sorry</code> would be the way I'd formalise it.</p>

#### [ Kevin Buzzard (Nov 19 2018 at 18:21)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Strong%20induction%20in%20lean/near/147980545):
<p>Note that the devious case <code>H 0</code> says that if something is true for all elements of the empty set, then <code>P 0</code> follows, which is a trick I mentioned in lectures. There is something called "well-founded induction" which works on any set with a well-founded ordering -- for example the naturals, but also many other ordered sets.</p>

#### [ Calle Sönne (Nov 19 2018 at 19:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Strong%20induction%20in%20lean/near/147984947):
<p>Ah forgot about that trick, thank you!</p>


{% endraw %}
