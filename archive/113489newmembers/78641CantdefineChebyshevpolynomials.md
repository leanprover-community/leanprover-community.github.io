---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/78641CantdefineChebyshevpolynomials.html
---

## Stream: [new members](index.html)
### Topic: [Can't define Chebyshev polynomials](78641CantdefineChebyshevpolynomials.html)

---


{% raw %}
#### [ Abhimanyu Pallavi Sudhir (Jan 12 2019 at 18:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Can%27t%20define%20Chebyshev%20polynomials/near/154992565):
<p>Why doesn't this work?</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">chebyshev</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="n">polynomial</span> <span class="n">ℝ</span>
<span class="bp">|</span> <span class="mi">0</span> <span class="o">:=</span> <span class="n">polynomial</span><span class="bp">.</span><span class="n">C</span> <span class="mi">1</span>
<span class="bp">|</span> <span class="mi">1</span> <span class="o">:=</span> <span class="n">polynomial</span><span class="bp">.</span><span class="n">X</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">n</span> <span class="bp">+</span> <span class="mi">2</span><span class="o">)</span> <span class="o">:=</span> <span class="mi">2</span> <span class="bp">*</span> <span class="n">polynomial</span><span class="bp">.</span><span class="n">X</span> <span class="bp">*</span> <span class="n">chebyshev</span> <span class="o">(</span><span class="n">n</span> <span class="bp">+</span> <span class="mi">1</span><span class="o">)</span> <span class="bp">-</span> <span class="n">chebyshev</span> <span class="n">n</span>
</pre></div>


<p>Lean tells me the definition relies on <code>classical.choice</code>. Indeed putting <code>noncomputable</code> at the front fixes things, but why is it noncomputable?</p>

#### [ Kevin Buzzard (Jan 12 2019 at 18:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Can%27t%20define%20Chebyshev%20polynomials/near/154993140):
<p>The definition of <code>polynomial X</code> is "functions from nat to X which vanish outside a finite set"; "vanish" means "equals zero", and equality is undecidable in the reals. This might be something to do with it. Try <code>polynomial int</code> and see if it fixes things!</p>

#### [ Kevin Buzzard (Jan 12 2019 at 18:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Can%27t%20define%20Chebyshev%20polynomials/near/154993205):
<p>NB <code>import analysis.polynomial</code> to make it work, but indeed int fixes things, and is probably the "correct" thing to do.</p>

#### [ Kevin Buzzard (Jan 12 2019 at 19:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Can%27t%20define%20Chebyshev%20polynomials/near/154993404):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">analysis</span><span class="bp">.</span><span class="n">polynomial</span>

<span class="n">def</span> <span class="n">chebyshev</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="n">polynomial</span> <span class="bp">ℤ</span>
<span class="bp">|</span> <span class="mi">0</span> <span class="o">:=</span> <span class="n">polynomial</span><span class="bp">.</span><span class="n">C</span> <span class="mi">1</span>
<span class="bp">|</span> <span class="mi">1</span> <span class="o">:=</span> <span class="n">polynomial</span><span class="bp">.</span><span class="n">X</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">n</span> <span class="bp">+</span> <span class="mi">2</span><span class="o">)</span> <span class="o">:=</span> <span class="mi">2</span> <span class="bp">*</span> <span class="n">polynomial</span><span class="bp">.</span><span class="n">X</span> <span class="bp">*</span> <span class="n">chebyshev</span> <span class="o">(</span><span class="n">n</span> <span class="bp">+</span> <span class="mi">1</span><span class="o">)</span> <span class="bp">-</span> <span class="n">chebyshev</span> <span class="n">n</span>

<span class="bp">#</span><span class="kn">eval</span> <span class="n">chebyshev</span> <span class="mi">17</span> <span class="c1">-- just about works on my desktop</span>
<span class="c">/-</span><span class="cm"></span>
<span class="cm">C (65536) * X ^ 17 + C (-278528) * X ^ 15 + C (487424) * X ^ 13 + C (-452608) * X ^ 11 + C (239360) * X ^ 9 + C (-71808) * X ^ 7 + C (11424) * X ^ 5 + C (-816) * X ^ 3 + C (17) * X</span>
<span class="cm">-/</span>

<span class="bp">#</span><span class="kn">eval</span> <span class="n">chebyshev</span> <span class="mi">19</span> <span class="c1">-- (deterministic) timeout</span>
</pre></div>

#### [ Mario Carneiro (Jan 12 2019 at 19:06)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Can%27t%20define%20Chebyshev%20polynomials/near/154993597):
<p>you can probably get farther with a list based representation of the polynomials</p>

#### [ Kevin Buzzard (Jan 12 2019 at 19:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Can%27t%20define%20Chebyshev%20polynomials/near/154993606):
<p>I guess the reason lists aren't used in general is that the leading term might be 0, which causes problems in general; however it will not cause problems here.</p>

#### [ Mario Carneiro (Jan 12 2019 at 19:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Can%27t%20define%20Chebyshev%20polynomials/near/154993616):
<p>well, it would make it harder to print if the leading term was 0</p>

#### [ Mario Carneiro (Jan 12 2019 at 19:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Can%27t%20define%20Chebyshev%20polynomials/near/154993617):
<p>and get the degree and other things</p>

#### [ Kevin Buzzard (Jan 12 2019 at 19:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Can%27t%20define%20Chebyshev%20polynomials/near/154993618):
<p>In general I guess one could define some more computationally efficient but slightly broken "non-zero polynomials" with addition only defined if you can prove that the degrees are unequal, and multiplication OK over an integral semi-domain :-)</p>

#### [ Kevin Buzzard (Jan 12 2019 at 19:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Can%27t%20define%20Chebyshev%20polynomials/near/154993669):
<p>But even lists are inefficient, right, because they're linked lists in reality?</p>

#### [ Mario Carneiro (Jan 12 2019 at 19:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Can%27t%20define%20Chebyshev%20polynomials/near/154993672):
<p>If you want to forgo the equality checks, you can define a polynomial as a quotient of representations with some zeros at the end</p>

#### [ Mario Carneiro (Jan 12 2019 at 19:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Can%27t%20define%20Chebyshev%20polynomials/near/154993681):
<p>then addition and multiplication are easy and degree needs equality</p>

#### [ Mario Carneiro (Jan 12 2019 at 19:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Can%27t%20define%20Chebyshev%20polynomials/near/154993690):
<p>yes lists are linked lists which aren't so great</p>

#### [ Mario Carneiro (Jan 12 2019 at 19:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Can%27t%20define%20Chebyshev%20polynomials/near/154993744):
<p>you could use buffer for really good VM performance</p>

#### [ Mario Carneiro (Jan 12 2019 at 19:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Can%27t%20define%20Chebyshev%20polynomials/near/154993749):
<p>but they are better than functions which is what is currently used</p>

#### [ Mario Carneiro (Jan 12 2019 at 19:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Can%27t%20define%20Chebyshev%20polynomials/near/154993751):
<p>I think the polynomials become big if else chains</p>

#### [ Mario Carneiro (Jan 12 2019 at 19:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Can%27t%20define%20Chebyshev%20polynomials/near/154993815):
<p>in fact, they probably aren't even reduced, you get these big thunks for calculating the coefficients</p>

#### [ Mario Carneiro (Jan 12 2019 at 19:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Can%27t%20define%20Chebyshev%20polynomials/near/154993822):
<p>the advantage of lists is they are a strict data structure, you calculate all the values before recursing</p>

#### [ Mario Carneiro (Jan 12 2019 at 19:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Can%27t%20define%20Chebyshev%20polynomials/near/154993836):
<p>also -- should have mentioned this before -- <code>chebyshev</code> there has an exponential time implementation</p>

#### [ Mario Carneiro (Jan 12 2019 at 19:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Can%27t%20define%20Chebyshev%20polynomials/near/154993839):
<p>just like the naive fib algorithm</p>


{% endraw %}
