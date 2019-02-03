---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/33733arationalnumberispositiveiffitsnumeratorispositive.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [a rational number is positive iff its numerator is positive](https://leanprover-community.github.io/archive/113488general/33733arationalnumberispositiveiffitsnumeratorispositive.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kenny Lau (Apr 30 2018 at 20:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125905999):
<p>do we have that?</p>

#### [ Johan Commelin (Apr 30 2018 at 20:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125906320):
<p>So <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mfrac><mrow><mo>−</mo><mn>1</mn></mrow><mrow><mo>−</mo><mn>1</mn></mrow></mfrac></mrow><annotation encoding="application/x-tex">\frac{-1}{-1}</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.845108em;"></span><span class="strut bottom" style="height:1.2484389999999999em;vertical-align:-0.403331em;"></span><span class="base"><span class="mord"><span class="mopen nulldelimiter"></span><span class="mfrac"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.845108em;"><span style="top:-2.655em;"><span class="pstrut" style="height:3em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">−</span><span class="mord mathrm mtight">1</span></span></span></span><span style="top:-3.23em;"><span class="pstrut" style="height:3em;"></span><span class="frac-line" style="border-bottom-width:0.04em;"></span></span><span style="top:-3.394em;"><span class="pstrut" style="height:3em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">−</span><span class="mord mathrm mtight">1</span></span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.403331em;"></span></span></span></span><span class="mclose nulldelimiter"></span></span></span></span></span> is not a positive rational number?</p>

#### [ Kenny Lau (Apr 30 2018 at 20:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125906332):
<p>in <code>rat</code> the denominator is always positive</p>

#### [ Johan Commelin (Apr 30 2018 at 20:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125906393):
<p>So <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mfrac><mrow><mn>1</mn></mrow><mrow><mo>−</mo><mn>2</mn></mrow></mfrac></mrow><annotation encoding="application/x-tex">\frac{1}{-2}</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.845108em;"></span><span class="strut bottom" style="height:1.2484389999999999em;vertical-align:-0.403331em;"></span><span class="base"><span class="mord"><span class="mopen nulldelimiter"></span><span class="mfrac"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.845108em;"><span style="top:-2.655em;"><span class="pstrut" style="height:3em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mtight">−</span><span class="mord mathrm mtight">2</span></span></span></span><span style="top:-3.23em;"><span class="pstrut" style="height:3em;"></span><span class="frac-line" style="border-bottom-width:0.04em;"></span></span><span style="top:-3.394em;"><span class="pstrut" style="height:3em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathrm mtight">1</span></span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.403331em;"></span></span></span></span><span class="mclose nulldelimiter"></span></span></span></span></span> is not a rational number...</p>

#### [ Kenny Lau (Apr 30 2018 at 20:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125906398):
<p>denominator</p>

#### [ Johan Commelin (Apr 30 2018 at 20:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125906409):
<p>I find this disturbing...</p>

#### [ Kenny Lau (Apr 30 2018 at 20:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125906582):
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">rat</span><span class="bp">.</span><span class="n">num_pos_of_pos</span> <span class="o">(</span><span class="n">r</span> <span class="o">:</span> <span class="n">rat</span><span class="o">)</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="n">r</span> <span class="bp">&gt;</span> <span class="mi">0</span><span class="o">)</span> <span class="o">:</span> <span class="o">(</span><span class="n">r</span><span class="bp">.</span><span class="n">num</span> <span class="o">:</span> <span class="n">ℚ</span><span class="o">)</span> <span class="bp">&gt;</span> <span class="mi">0</span> <span class="o">:=</span>
<span class="k">calc</span>  <span class="o">(</span><span class="n">r</span><span class="bp">.</span><span class="n">num</span> <span class="o">:</span> <span class="n">ℚ</span><span class="o">)</span>
    <span class="bp">=</span> <span class="n">r</span><span class="bp">.</span><span class="n">num</span> <span class="bp">/</span> <span class="o">(</span><span class="n">r</span><span class="bp">.</span><span class="n">denom</span><span class="o">:</span><span class="bp">ℤ</span><span class="o">)</span> <span class="bp">*</span> <span class="n">r</span><span class="bp">.</span><span class="n">denom</span> <span class="o">:</span> <span class="n">eq</span><span class="bp">.</span><span class="n">symm</span> <span class="err">$</span> <span class="n">div_mul_cancel</span> <span class="bp">_</span> <span class="err">$</span> <span class="n">ne_of_gt</span> <span class="err">$</span> <span class="n">nat</span><span class="bp">.</span><span class="n">cast_pos</span><span class="bp">.</span><span class="mi">2</span> <span class="n">r</span><span class="bp">.</span><span class="n">pos</span>
<span class="bp">...</span> <span class="bp">=</span> <span class="n">r</span> <span class="bp">*</span> <span class="n">r</span><span class="bp">.</span><span class="n">denom</span> <span class="o">:</span> <span class="k">by</span> <span class="n">rw</span> <span class="o">[</span><span class="err">←</span> <span class="n">rat</span><span class="bp">.</span><span class="n">mk_eq_div</span><span class="o">,</span> <span class="err">←</span> <span class="n">rat</span><span class="bp">.</span><span class="n">num_denom</span> <span class="n">r</span><span class="o">]</span>
<span class="bp">...</span> <span class="bp">&gt;</span> <span class="mi">0</span> <span class="o">:</span> <span class="n">mul_pos</span> <span class="n">H</span> <span class="err">$</span> <span class="n">nat</span><span class="bp">.</span><span class="n">cast_pos</span><span class="bp">.</span><span class="mi">2</span> <span class="n">r</span><span class="bp">.</span><span class="n">pos</span>
</pre></div>

#### [ Kenny Lau (Apr 30 2018 at 20:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125906590):
<p>it's hard to prove anything about the rational numbers when I don't have enough lemmas...</p>

#### [ Johan Commelin (Apr 30 2018 at 20:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125906724):
<p>Are you building an interface for \Q ?</p>

#### [ Kenny Lau (Apr 30 2018 at 20:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125906727):
<p>I'm using Q</p>

#### [ Kenny Lau (Apr 30 2018 at 20:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125906734):
<p>and I'm finding everything hard to prove</p>

#### [ Johan Commelin (Apr 30 2018 at 20:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125906760):
<p>Ok, then we need an interface... because end-users shouldn't use r.num and r.denom, in my opinion.</p>

#### [ Kenny Lau (Apr 30 2018 at 20:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125906768):
<p>well don't rationals have denominators...</p>

#### [ Johan Commelin (Apr 30 2018 at 20:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125906824):
<p>Not really well-defined... I think</p>

#### [ Kenny Lau (Apr 30 2018 at 20:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125906831):
<p>they are</p>

#### [ Johan Commelin (Apr 30 2018 at 20:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125906833):
<p>Of course you can make choices</p>

#### [ Kenny Lau (Apr 30 2018 at 20:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125906836):
<p>no choices required</p>

#### [ Johan Commelin (Apr 30 2018 at 20:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125906842):
<p>Well, not <em>morally</em> well-defined</p>

#### [ Kenny Lau (Apr 30 2018 at 20:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125906854):
<p>in Lean a rational number consists of a numerator in Z, denominator in N, proof that the denominator is positive, and proof that they are coprime</p>

#### [ Kenny Lau (Apr 30 2018 at 20:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125906861):
<p>and I find that to be morally well-defined also</p>

#### [ Kenny Lau (Apr 30 2018 at 20:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125906869):
<p>every rational number has a simplified form</p>

#### [ Johan Commelin (Apr 30 2018 at 20:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125906931):
<p>Yes, but that should be hidden away as much as possible</p>

#### [ Johan Commelin (Apr 30 2018 at 20:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125906940):
<p>I think</p>

#### [ Kenny Lau (Apr 30 2018 at 20:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125906952):
<p>I need its denominator to prove that every rational number is smaller than some power of 2</p>

#### [ Kenny Lau (Apr 30 2018 at 20:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125906956):
<p>in particular, 1/2^r.denom &lt; r</p>

#### [ Johan Commelin (Apr 30 2018 at 20:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125906988):
<p>Well, part of the interface could say that for every rational number <code>r</code> there exists an integer <code>n</code> with <code>r &lt; n</code></p>

#### [ Johan Commelin (Apr 30 2018 at 20:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125906995):
<p>Or something like that.</p>

#### [ Kenny Lau (Apr 30 2018 at 20:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125907033):
<p>aha that's existing</p>

#### [ Kenny Lau (Apr 30 2018 at 20:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125907041):
<p>but I don't like it :P</p>

#### [ Reid Barton (Apr 30 2018 at 20:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125907056):
<p>there's even a class for that</p>

#### [ Kenny Lau (Apr 30 2018 at 20:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125907215):
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">lt_two_pow</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="n">nat</span><span class="o">)</span> <span class="o">:</span> <span class="n">n</span> <span class="bp">&lt;</span> <span class="mi">2</span> <span class="err">^</span> <span class="n">n</span> <span class="o">:=</span>
<span class="n">nat</span><span class="bp">.</span><span class="n">rec_on</span> <span class="n">n</span> <span class="n">dec_trivial</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">n</span> <span class="n">ih</span><span class="o">,</span>
<span class="k">calc</span>  <span class="n">n</span> <span class="bp">+</span> <span class="mi">1</span>
    <span class="bp">&lt;</span> <span class="mi">2</span><span class="err">^</span><span class="n">n</span> <span class="bp">+</span> <span class="mi">1</span>   <span class="o">:</span> <span class="n">nat</span><span class="bp">.</span><span class="n">add_lt_add_right</span> <span class="n">ih</span> <span class="mi">1</span>
<span class="bp">...</span> <span class="bp">≤</span> <span class="mi">2</span><span class="err">^</span><span class="n">n</span> <span class="bp">+</span> <span class="mi">2</span><span class="err">^</span><span class="n">n</span> <span class="o">:</span> <span class="n">nat</span><span class="bp">.</span><span class="n">add_le_add_left</span> <span class="o">(</span><span class="n">nat</span><span class="bp">.</span><span class="n">pow_le_pow_of_le_right</span> <span class="n">dec_trivial</span> <span class="err">$</span> <span class="n">nat</span><span class="bp">.</span><span class="n">zero_le</span> <span class="n">n</span><span class="o">)</span> <span class="o">(</span><span class="mi">2</span><span class="err">^</span><span class="n">n</span><span class="o">)</span>
<span class="bp">...</span> <span class="bp">=</span> <span class="mi">2</span><span class="err">^</span><span class="n">n</span> <span class="bp">*</span> <span class="mi">2</span>   <span class="o">:</span> <span class="n">eq</span><span class="bp">.</span><span class="n">symm</span> <span class="err">$</span> <span class="n">mul_two</span> <span class="o">(</span><span class="mi">2</span><span class="err">^</span><span class="n">n</span><span class="o">)</span>
<span class="bp">...</span> <span class="bp">=</span> <span class="mi">2</span><span class="err">^</span><span class="o">(</span><span class="n">n</span><span class="bp">+</span><span class="mi">1</span><span class="o">)</span>   <span class="o">:</span> <span class="n">eq</span><span class="bp">.</span><span class="n">symm</span> <span class="err">$</span> <span class="n">nat</span><span class="bp">.</span><span class="n">pow_succ</span> <span class="mi">2</span> <span class="n">n</span>

<span class="kn">theorem</span> <span class="n">rat</span><span class="bp">.</span><span class="n">coe_pow</span> <span class="o">(</span><span class="n">m</span> <span class="n">n</span> <span class="o">:</span> <span class="n">nat</span><span class="o">)</span> <span class="o">:</span> <span class="o">(</span><span class="n">m</span> <span class="o">:</span> <span class="n">ℚ</span><span class="o">)</span> <span class="err">^</span> <span class="n">n</span> <span class="bp">=</span> <span class="o">(</span><span class="n">m</span><span class="err">^</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:=</span>
<span class="n">nat</span><span class="bp">.</span><span class="n">rec_on</span> <span class="n">n</span> <span class="n">rfl</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">n</span> <span class="n">ih</span><span class="o">,</span> <span class="k">by</span> <span class="n">simp</span> <span class="o">[</span><span class="n">pow_succ&#39;</span><span class="o">,</span> <span class="n">ih</span><span class="o">,</span> <span class="n">nat</span><span class="bp">.</span><span class="n">pow_succ</span><span class="o">]</span>

<span class="kn">theorem</span> <span class="n">rat</span><span class="bp">.</span><span class="n">num_pos_of_pos</span> <span class="o">(</span><span class="n">r</span> <span class="o">:</span> <span class="n">rat</span><span class="o">)</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="n">r</span> <span class="bp">&gt;</span> <span class="mi">0</span><span class="o">)</span> <span class="o">:</span> <span class="n">r</span><span class="bp">.</span><span class="n">num</span> <span class="bp">&gt;</span> <span class="mi">0</span> <span class="o">:=</span>
<span class="n">int</span><span class="bp">.</span><span class="n">cast_lt</span><span class="bp">.</span><span class="mi">1</span> <span class="err">$</span>
<span class="k">calc</span>  <span class="o">(</span><span class="n">r</span><span class="bp">.</span><span class="n">num</span> <span class="o">:</span> <span class="n">ℚ</span><span class="o">)</span>
    <span class="bp">=</span> <span class="n">r</span><span class="bp">.</span><span class="n">num</span> <span class="bp">/</span> <span class="o">(</span><span class="n">r</span><span class="bp">.</span><span class="n">denom</span><span class="o">:</span><span class="bp">ℤ</span><span class="o">)</span> <span class="bp">*</span> <span class="n">r</span><span class="bp">.</span><span class="n">denom</span> <span class="o">:</span> <span class="n">eq</span><span class="bp">.</span><span class="n">symm</span> <span class="err">$</span> <span class="n">div_mul_cancel</span> <span class="bp">_</span> <span class="err">$</span> <span class="n">ne_of_gt</span> <span class="err">$</span> <span class="n">nat</span><span class="bp">.</span><span class="n">cast_pos</span><span class="bp">.</span><span class="mi">2</span> <span class="n">r</span><span class="bp">.</span><span class="n">pos</span>
<span class="bp">...</span> <span class="bp">=</span> <span class="n">r</span> <span class="bp">*</span> <span class="n">r</span><span class="bp">.</span><span class="n">denom</span> <span class="o">:</span> <span class="k">by</span> <span class="n">rw</span> <span class="o">[</span><span class="err">←</span> <span class="n">rat</span><span class="bp">.</span><span class="n">mk_eq_div</span><span class="o">,</span> <span class="err">←</span> <span class="n">rat</span><span class="bp">.</span><span class="n">num_denom</span> <span class="n">r</span><span class="o">]</span>
<span class="bp">...</span> <span class="bp">&gt;</span> <span class="mi">0</span> <span class="o">:</span> <span class="n">mul_pos</span> <span class="n">H</span> <span class="err">$</span> <span class="n">nat</span><span class="bp">.</span><span class="n">cast_pos</span><span class="bp">.</span><span class="mi">2</span> <span class="n">r</span><span class="bp">.</span><span class="n">pos</span>

<span class="kn">theorem</span> <span class="n">rat</span><span class="bp">.</span><span class="n">one_le_num_of_pos</span> <span class="o">(</span><span class="n">r</span> <span class="o">:</span> <span class="n">rat</span><span class="o">)</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="n">r</span> <span class="bp">&gt;</span> <span class="mi">0</span><span class="o">)</span> <span class="o">:</span> <span class="mi">1</span> <span class="bp">≤</span> <span class="o">(</span><span class="n">r</span><span class="bp">.</span><span class="n">num</span> <span class="o">:</span> <span class="n">ℚ</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">have</span> <span class="n">H1</span> <span class="o">:</span> <span class="o">((</span><span class="mi">0</span><span class="bp">+</span><span class="mi">1</span><span class="o">:</span><span class="bp">ℤ</span><span class="o">):</span><span class="n">ℚ</span><span class="o">)</span> <span class="bp">=</span> <span class="o">(</span><span class="mi">1</span><span class="o">:</span><span class="n">ℚ</span><span class="o">),</span> <span class="k">from</span> <span class="n">rfl</span><span class="o">,</span>
<span class="n">H1</span> <span class="bp">▸</span> <span class="n">int</span><span class="bp">.</span><span class="n">cast_le</span><span class="bp">.</span><span class="mi">2</span> <span class="err">$</span> <span class="n">int</span><span class="bp">.</span><span class="n">add_one_le_of_lt</span> <span class="err">$</span> <span class="n">rat</span><span class="bp">.</span><span class="n">num_pos_of_pos</span> <span class="n">r</span> <span class="n">H</span>

<span class="kn">theorem</span> <span class="n">rat</span><span class="bp">.</span><span class="n">lt</span> <span class="o">(</span><span class="n">r</span> <span class="o">:</span> <span class="n">ℚ</span><span class="o">)</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="n">r</span> <span class="bp">&gt;</span> <span class="mi">0</span><span class="o">)</span> <span class="o">:</span> <span class="o">(</span><span class="mi">1</span> <span class="bp">/</span> <span class="mi">2</span><span class="err">^</span><span class="n">r</span><span class="bp">.</span><span class="n">denom</span> <span class="o">:</span> <span class="n">ℚ</span><span class="o">)</span> <span class="bp">&lt;</span> <span class="n">r</span> <span class="o">:=</span>
<span class="k">calc</span>  <span class="o">(</span><span class="mi">1</span> <span class="bp">/</span> <span class="mi">2</span><span class="err">^</span><span class="n">r</span><span class="bp">.</span><span class="n">denom</span> <span class="o">:</span> <span class="n">ℚ</span><span class="o">)</span>
    <span class="bp">&lt;</span> <span class="mi">1</span> <span class="bp">/</span> <span class="n">r</span><span class="bp">.</span><span class="n">denom</span> <span class="o">:</span> <span class="n">one_div_lt_one_div_of_lt</span> <span class="o">(</span><span class="n">nat</span><span class="bp">.</span><span class="n">cast_pos</span><span class="bp">.</span><span class="mi">2</span> <span class="n">r</span><span class="bp">.</span><span class="n">pos</span><span class="o">)</span>
  <span class="o">(</span><span class="n">trans_rel_left</span> <span class="bp">_</span> <span class="o">(</span><span class="n">nat</span><span class="bp">.</span><span class="n">cast_lt</span><span class="bp">.</span><span class="mi">2</span> <span class="err">$</span> <span class="n">lt_two_pow</span> <span class="bp">_</span><span class="o">)</span> <span class="o">(</span><span class="n">rat</span><span class="bp">.</span><span class="n">coe_pow</span> <span class="mi">2</span> <span class="bp">_</span><span class="o">)</span><span class="bp">.</span><span class="n">symm</span><span class="o">)</span>
<span class="bp">...</span> <span class="bp">≤</span> <span class="n">r</span><span class="bp">.</span><span class="n">num</span> <span class="bp">/</span> <span class="n">r</span><span class="bp">.</span><span class="n">denom</span> <span class="o">:</span> <span class="n">div_le_div_of_le_of_pos</span> <span class="o">(</span><span class="n">rat</span><span class="bp">.</span><span class="n">one_le_num_of_pos</span> <span class="n">r</span> <span class="n">H</span><span class="o">)</span> <span class="o">(</span><span class="n">nat</span><span class="bp">.</span><span class="n">cast_pos</span><span class="bp">.</span><span class="mi">2</span> <span class="n">r</span><span class="bp">.</span><span class="n">pos</span><span class="o">)</span>
<span class="bp">...</span> <span class="bp">=</span> <span class="n">r</span><span class="bp">.</span><span class="n">num</span> <span class="bp">/</span> <span class="o">(</span><span class="n">r</span><span class="bp">.</span><span class="n">denom</span><span class="o">:</span><span class="bp">ℤ</span><span class="o">)</span> <span class="o">:</span> <span class="n">rfl</span>
<span class="bp">...</span> <span class="bp">=</span> <span class="n">r</span> <span class="o">:</span> <span class="k">by</span> <span class="n">rw</span> <span class="o">[</span><span class="err">←</span> <span class="n">rat</span><span class="bp">.</span><span class="n">mk_eq_div</span><span class="o">,</span> <span class="err">←</span> <span class="n">rat</span><span class="bp">.</span><span class="n">num_denom</span> <span class="n">r</span><span class="o">]</span>
</pre></div>

#### [ Kenny Lau (Apr 30 2018 at 20:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125907217):
<p>yay done</p>

#### [ Johan Commelin (Apr 30 2018 at 20:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125907246):
<p>I just don't like the fact that if some computation spits out two integers, <code>a</code> and <code>b</code>, with <code>b \ne 0</code>, and I want to consider the rational number <code>a/b</code>, then Lean decides it <em>also</em> wants to put them in lowest terms.</p>

#### [ Johan Commelin (Apr 30 2018 at 20:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125907251):
<p>That might be an immense computation</p>

#### [ Johan Commelin (Apr 30 2018 at 20:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125907264):
<p>Or can it formally divide away the gcd, without actually calculating it?</p>

#### [ Kevin Buzzard (Apr 30 2018 at 20:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125907336):
<p>Johan you should take a look at <code>data/rat.lean</code> in mathlib</p>

#### [ Kevin Buzzard (Apr 30 2018 at 20:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125907337):
<p>I found that file not too intimidating</p>

#### [ Johan Commelin (Apr 30 2018 at 20:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125907343):
<p>Will do</p>

#### [ Kevin Buzzard (Apr 30 2018 at 20:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125907393):
<p>I would tell my students "of course a rational number is an equivalence class"</p>

#### [ Kevin Buzzard (Apr 30 2018 at 20:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125907398):
<p>(because it's Z localised away from 0)</p>

#### [ Kevin Buzzard (Apr 30 2018 at 20:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125907401):
<p>but in Lean working with equivalence classes is sometimes hard work</p>

#### [ Kevin Buzzard (Apr 30 2018 at 20:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125907406):
<p>so if they can get away with it, they work with an inductive type</p>

#### [ Kevin Buzzard (Apr 30 2018 at 20:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125907482):
<p>So they go with this structure of a numerator n in Z, a denominator d in N, a proof that d &gt; 0 and a proof that n and d are coprime!</p>

#### [ Reid Barton (Apr 30 2018 at 20:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125907488):
<p>If you don't reduce to lowest terms, then <code>1/2 + 1/2 + 1/2 + ... + 1/2</code> becomes an unwieldy computation</p>

#### [ Kevin Buzzard (Apr 30 2018 at 20:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125907492):
<p>At this point you can't even make 6/8</p>

#### [ Kevin Buzzard (Apr 30 2018 at 20:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125907495):
<p>but it's OK, they're only a few lines in</p>

#### [ Kevin Buzzard (Apr 30 2018 at 20:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125907501):
<p>and then they go on to make other constructors</p>

#### [ Kevin Buzzard (Apr 30 2018 at 20:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125907513):
<p>because they implemented Euclid already</p>

#### [ Kevin Buzzard (Apr 30 2018 at 20:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125907535):
<p>so you finally get a definition of <code>mk</code></p>

#### [ Kevin Buzzard (Apr 30 2018 at 20:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125907576):
<p>on line 61</p>

#### [ Kevin Buzzard (Apr 30 2018 at 20:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125907581):
<p>and they define <code>/</code> to be mk</p>

#### [ Johan Commelin (Apr 30 2018 at 20:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125907592):
<p>Well, Lean can decide to reduce to lowest terms when I force it to actually compute something. But if I want to define <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mfrac><mrow><mi>π</mi><mo>(</mo><mn>1</mn><msup><mn>0</mn><mn>9</mn></msup><mo>)</mo><mo>−</mo><mn>1</mn></mrow><mrow><mi>π</mi><mo>(</mo><mn>1</mn><msup><mn>0</mn><mn>9</mn></msup><mo>+</mo><mn>1</mn><mo>)</mo><mo>−</mo><mn>1</mn></mrow></mfrac></mrow><annotation encoding="application/x-tex">\frac{\pi(10^9)-1}{\pi(10^9+1)-1}</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:1.10892em;"></span><span class="strut bottom" style="height:1.62892em;vertical-align:-0.52em;"></span><span class="base"><span class="mord"><span class="mopen nulldelimiter"></span><span class="mfrac"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:1.10892em;"><span style="top:-2.655em;"><span class="pstrut" style="height:3em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathit mtight" style="margin-right:0.03588em;">π</span><span class="mopen mtight">(</span><span class="mord mathrm mtight">1</span><span class="mord mtight"><span class="mord mathrm mtight">0</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.7463142857142857em;"><span style="top:-2.786em;margin-right:0.07142857142857144em;"><span class="pstrut" style="height:2.5em;"></span><span class="sizing reset-size3 size1 mtight"><span class="mord mathrm mtight">9</span></span></span></span></span></span></span></span><span class="mbin mtight">+</span><span class="mord mathrm mtight">1</span><span class="mclose mtight">)</span><span class="mbin mtight">−</span><span class="mord mathrm mtight">1</span></span></span></span><span style="top:-3.23em;"><span class="pstrut" style="height:3em;"></span><span class="frac-line" style="border-bottom-width:0.04em;"></span></span><span style="top:-3.485em;"><span class="pstrut" style="height:3em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathit mtight" style="margin-right:0.03588em;">π</span><span class="mopen mtight">(</span><span class="mord mathrm mtight">1</span><span class="mord mtight"><span class="mord mathrm mtight">0</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.8913142857142857em;"><span style="top:-2.931em;margin-right:0.07142857142857144em;"><span class="pstrut" style="height:2.5em;"></span><span class="sizing reset-size3 size1 mtight"><span class="mord mathrm mtight">9</span></span></span></span></span></span></span></span><span class="mclose mtight">)</span><span class="mbin mtight">−</span><span class="mord mathrm mtight">1</span></span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.52em;"></span></span></span></span><span class="mclose nulldelimiter"></span></span></span></span></span> where <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>π</mi><mo>(</mo><mi>n</mi><mo>)</mo></mrow><annotation encoding="application/x-tex">\pi(n)</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.03588em;">π</span><span class="mopen">(</span><span class="mord mathit">n</span><span class="mclose">)</span></span></span></span> is the <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>n</mi></mrow><annotation encoding="application/x-tex">n</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.43056em;"></span><span class="strut bottom" style="height:0.43056em;vertical-align:0em;"></span><span class="base"><span class="mord mathit">n</span></span></span></span>-th prime, that should be possible, right?</p>

#### [ Kevin Buzzard (Apr 30 2018 at 20:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125907598):
<p>inductive structures with lots of things which are quite easy to carry around are very popular round here</p>

#### [ Johan Commelin (Apr 30 2018 at 20:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125907606):
<p>It shouldn't actually start computing those primes.</p>

#### [ Kevin Buzzard (Apr 30 2018 at 20:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125907624):
<p>If you want to actually work something complicated out then you should not be using Lean at this point</p>

#### [ Johan Commelin (Apr 30 2018 at 20:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125907626):
<p>Also, I <em>would</em> want to have a proof that <code>d = 0</code>, <em>all the time</em></p>

#### [ Reid Barton (Apr 30 2018 at 20:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125907630):
<p>If you believe it won't start computing the primes, then why would it need to do the conversion to lowest terms?</p>

#### [ Johan Commelin (Apr 30 2018 at 20:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125907634):
<p>But there they choose to just put <code>n/0 = 0</code></p>

#### [ Kevin Buzzard (Apr 30 2018 at 20:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125907681):
<p><code>n/0=0</code>.</p>

#### [ Kevin Buzzard (Apr 30 2018 at 20:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125907684):
<p>Mathematicians can often get upset about that.</p>

#### [ Kevin Buzzard (Apr 30 2018 at 20:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125907696):
<p>but the issue is just notation</p>

#### [ Kevin Buzzard (Apr 30 2018 at 20:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125907714):
<p>Just imagine you went through all the Lean source code replacing the notation <code>/</code> with something that looked more like <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msup><mi mathvariant="normal">/</mi><mo>∗</mo></msup></mrow><annotation encoding="application/x-tex">/^*</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mord"><span class="mord mathrm">/</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.688696em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mbin mtight">∗</span></span></span></span></span></span></span></span></span></span></span></p>

#### [ Kevin Buzzard (Apr 30 2018 at 20:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125907754):
<p>and the asterisk indicates a footnote:</p>

#### [ Kevin Buzzard (Apr 30 2018 at 20:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125907763):
<p>"Note to mathematicians: this is not your divide. This is just notation for a different function which we invented because we find it more useful."</p>

#### [ Johan Commelin (Apr 30 2018 at 20:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125907766):
<blockquote>
<p>If you want to actually work something complicated out then you should not be using Lean at this point</p>
</blockquote>
<p>Says the person who is formalising schemes... <span class="emoji emoji-1f923" title="rolling on the floor laughing">:rolling_on_the_floor_laughing:</span></p>

#### [ Kevin Buzzard (Apr 30 2018 at 20:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125907767):
<p>because whenever a mathematician writes the symbol <code>/</code></p>

#### [ Kevin Buzzard (Apr 30 2018 at 20:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125907780):
<p>they are doing that thing that mathematicians love to do -- they are making a promise.</p>

#### [ Johan Commelin (Apr 30 2018 at 20:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125907785):
<p>Lol</p>

#### [ Kevin Buzzard (Apr 30 2018 at 20:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125907790):
<p>They are saying "I promise that the denominator is not zero."</p>

#### [ Johan Commelin (Apr 30 2018 at 20:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125907794):
<p>Yeah, ok... I'll try to forget some of my home culture.</p>

#### [ Kevin Buzzard (Apr 30 2018 at 20:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125907796):
<p>but if you really make them keep their promises</p>

#### [ Kevin Buzzard (Apr 30 2018 at 20:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125907807):
<p>then that means that they have to supply a proof.</p>

#### [ Kevin Buzzard (Apr 30 2018 at 21:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125907861):
<p>And that is your input which you as a mathematician enter into /</p>

#### [ Kevin Buzzard (Apr 30 2018 at 21:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125907873):
<p>and that's exactly the data needed to work out /*</p>

#### [ Kevin Buzzard (Apr 30 2018 at 21:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125907875):
<p>with a guarantee that it's equal to /</p>

#### [ Johan Commelin (Apr 30 2018 at 21:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125907877):
<p>Fair enough</p>

#### [ Kevin Buzzard (Apr 30 2018 at 21:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125907879):
<p>Mathematicans are full of promises.</p>

#### [ Kevin Buzzard (Apr 30 2018 at 21:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125907883):
<p>A is a hypergeometric schemeoid</p>

#### [ Kevin Buzzard (Apr 30 2018 at 21:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125907896):
<p>and B is a set that bijects with A</p>

#### [ Kevin Buzzard (Apr 30 2018 at 21:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125907902):
<p>therefore B is a hypergeometric schemeoid.</p>

#### [ Kevin Buzzard (Apr 30 2018 at 21:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125907909):
<p>That statement comes with a promise. I had not realised this until very recently.</p>

#### [ Kevin Buzzard (Apr 30 2018 at 21:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125907960):
<p>The promise is: "I promise that the definition of a hypergeometric schemeoid structure on a set A does not involve actually looking at any of A's elements"</p>

#### [ Kevin Buzzard (Apr 30 2018 at 21:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125907965):
<p>"it just involves things like structures of multiplication and addition on A</p>

#### [ Kevin Buzzard (Apr 30 2018 at 21:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125908006):
<p>You don't have to rely on A having an element containing an element containing the empty set in the definition -- but such a condition is a <strong>completely valid thing to say in ZFC</strong>.</p>

#### [ Johan Commelin (Apr 30 2018 at 21:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125908047):
<p>Yup...</p>

#### [ Kevin Buzzard (Apr 30 2018 at 21:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125908052):
<p>So when you make that transport of structure you are making a promise</p>

#### [ Kevin Buzzard (Apr 30 2018 at 21:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125908063):
<p>and mathematicians have kind of forgotten this, because it's just part of the culture.</p>

#### [ Johan Commelin (Apr 30 2018 at 21:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125908072):
<p>And lately we have more or less been working under that promise all the time... to never actually look at the elements of our sets.</p>

#### [ Johan Commelin (Apr 30 2018 at 21:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125908088):
<p>Our objects may have an element "3", but we don't actually care what that element "3" looks like. As long as it behaves like a "3"</p>

#### [ Kevin Buzzard (Apr 30 2018 at 21:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125908089):
<p>There are certain things we _can_ do to sets, but we choose not to do. If G is a group, I don't care about the underlying set, I just care about one special element of G with the _name_ "identity" -- I don't care which set it is -- and the inversion and multiplication.</p>

#### [ Chris Hughes (Apr 30 2018 at 21:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125908159):
<p><code>pow_unbounded_of_gt_one</code> in <code>algebra.archimedean</code> sounds like what you want.</p>

#### [ Kevin Buzzard (Apr 30 2018 at 21:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125908160):
<p>And I would be really interested in formalising the notion of what we as mathematicians consider decent things to do to types. Exactly what can mathematicians do to mathematical objects?</p>

#### [ Johan Commelin (Apr 30 2018 at 21:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125908210):
<p>Agreed. (But we are stealing Kenny's thread...) Chris subtly reminded me of that (-;</p>

#### [ Mario Carneiro (May 01 2018 at 02:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125921367):
<blockquote>
<p>I just don't like the fact that if some computation spits out two integers, a and b, with b \ne 0, and I want to consider the rational number a/b, then Lean decides it also wants to put them in lowest terms. That might be an immense computation</p>
</blockquote>
<p>The runtime for doing this is not much more than multiplication of rationals to begin with, so I think it's a reasonable cost given you are doing a division. As Reid says, the alternative is much worse, unnormalized rationals have exponentially worse runtime in some situations.</p>
<blockquote>
<p>Well, Lean can decide to reduce to lowest terms when I force it to actually compute something. But if I want to define <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mfrac><mrow><mi>π</mi><mo>(</mo><mn>1</mn><msup><mn>0</mn><mn>9</mn></msup><mo>)</mo><mo>−</mo><mn>1</mn></mrow><mrow><mi>π</mi><mo>(</mo><mn>1</mn><msup><mn>0</mn><mn>9</mn></msup><mo>+</mo><mn>1</mn><mo>)</mo><mo>−</mo><mn>1</mn></mrow></mfrac></mrow><annotation encoding="application/x-tex">\frac{\pi(10^9)-1}{\pi(10^9+1)-1}</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:1.10892em;"></span><span class="strut bottom" style="height:1.62892em;vertical-align:-0.52em;"></span><span class="base"><span class="mord"><span class="mopen nulldelimiter"></span><span class="mfrac"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:1.10892em;"><span style="top:-2.655em;"><span class="pstrut" style="height:3em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathit mtight" style="margin-right:0.03588em;">π</span><span class="mopen mtight">(</span><span class="mord mathrm mtight">1</span><span class="mord mtight"><span class="mord mathrm mtight">0</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.7463142857142857em;"><span style="top:-2.786em;margin-right:0.07142857142857144em;"><span class="pstrut" style="height:2.5em;"></span><span class="sizing reset-size3 size1 mtight"><span class="mord mathrm mtight">9</span></span></span></span></span></span></span></span><span class="mbin mtight">+</span><span class="mord mathrm mtight">1</span><span class="mclose mtight">)</span><span class="mbin mtight">−</span><span class="mord mathrm mtight">1</span></span></span></span><span style="top:-3.23em;"><span class="pstrut" style="height:3em;"></span><span class="frac-line" style="border-bottom-width:0.04em;"></span></span><span style="top:-3.485em;"><span class="pstrut" style="height:3em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathit mtight" style="margin-right:0.03588em;">π</span><span class="mopen mtight">(</span><span class="mord mathrm mtight">1</span><span class="mord mtight"><span class="mord mathrm mtight">0</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.8913142857142857em;"><span style="top:-2.931em;margin-right:0.07142857142857144em;"><span class="pstrut" style="height:2.5em;"></span><span class="sizing reset-size3 size1 mtight"><span class="mord mathrm mtight">9</span></span></span></span></span></span></span></span><span class="mclose mtight">)</span><span class="mbin mtight">−</span><span class="mord mathrm mtight">1</span></span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.52em;"></span></span></span></span><span class="mclose nulldelimiter"></span></span></span></span></span> where <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>π</mi><mo>(</mo><mi>n</mi><mo>)</mo></mrow><annotation encoding="application/x-tex">\pi(n)</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.03588em;">π</span><span class="mopen">(</span><span class="mord mathit">n</span><span class="mclose">)</span></span></span></span> is the <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>n</mi></mrow><annotation encoding="application/x-tex">n</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.43056em;"></span><span class="strut bottom" style="height:0.43056em;vertical-align:0em;"></span><span class="base"><span class="mord mathit">n</span></span></span></span>-th prime, that should be possible, right?</p>
</blockquote>
<p>If you say <code>def x : rat := pi bla bla...</code> then nothing is computed up front, but <code>x</code> is computed when you use it in a program which is <code>#eval</code>'d. In particular, Lean uses an eager evaluation semantics, so in fact <code>pi(10^9)</code> will be calculated <em>regardless</em> of whether rationals are defined as a quotient or as reduced fractions. (This isn't Haskell!) The only way to avoid the calculation at this stage is to have <code>/</code> be some sort of thunk-taking operation so as to defer evaluation of its arguments, but it is not at all obvious that these "lazy rats" are the intended usual use of rational numbers.</p>

#### [ Johan Commelin (May 01 2018 at 06:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125929510):
<p>Ok, understood. Somehow laziness feels natural to me. But I don't have that much experience actually. If at some point I need it, then I'll bring it up again (-;</p>

#### [ Reid Barton (May 01 2018 at 07:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/a%20rational%20number%20is%20positive%20iff%20its%20numerator%20is%20positive/near/125929676):
<p>The point I was (too obliquely) trying to make before is that if Lean were lazy, then it would presumably have no reason to do the GCD computation, either</p>


{% endraw %}
