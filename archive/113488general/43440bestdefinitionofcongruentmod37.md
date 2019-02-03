---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/43440bestdefinitionofcongruentmod37.html
---

## Stream: [general](index.html)
### Topic: [best definition of "congruent mod 37"](43440bestdefinitionofcongruentmod37.html)

---


{% raw %}
#### [ Kevin Buzzard (Aug 25 2018 at 11:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/best%20definition%20of%20%22congruent%20mod%2037%22/near/132741889):
<div class="codehilite"><pre><span></span><span class="kn">definition</span> <span class="n">r1</span> <span class="o">(</span><span class="n">a</span> <span class="n">b</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">)</span> <span class="o">:=</span> <span class="bp">∃</span> <span class="n">k</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">,</span> <span class="n">a</span> <span class="bp">-</span> <span class="n">b</span> <span class="bp">=</span> <span class="mi">37</span> <span class="bp">*</span> <span class="n">k</span>
<span class="kn">definition</span> <span class="n">r2</span> <span class="o">(</span><span class="n">a</span> <span class="n">b</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">)</span> <span class="o">:=</span> <span class="bp">∃</span> <span class="n">k</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">,</span> <span class="n">a</span> <span class="bp">-</span> <span class="n">b</span> <span class="bp">=</span> <span class="n">k</span> <span class="bp">*</span> <span class="mi">37</span>
<span class="kn">definition</span> <span class="n">r3</span> <span class="o">(</span><span class="n">a</span> <span class="n">b</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">)</span> <span class="o">:=</span> <span class="bp">∃</span> <span class="n">k</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">,</span> <span class="mi">37</span> <span class="bp">*</span> <span class="n">k</span> <span class="bp">=</span> <span class="n">a</span> <span class="bp">-</span> <span class="n">b</span>
<span class="kn">definition</span> <span class="n">r4</span> <span class="o">(</span><span class="n">a</span> <span class="n">b</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">)</span> <span class="o">:=</span> <span class="bp">∃</span> <span class="n">k</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">,</span> <span class="n">k</span> <span class="bp">*</span> <span class="mi">37</span> <span class="bp">=</span> <span class="n">b</span> <span class="bp">-</span> <span class="n">a</span>
<span class="c1">-- I&#39;m open to more suggestions</span>

<span class="kn">definition</span> <span class="n">r1</span><span class="bp">.</span><span class="n">symm</span> <span class="o">(</span><span class="n">a</span> <span class="n">b</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">)</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="n">r1</span> <span class="n">a</span> <span class="n">b</span><span class="o">)</span> <span class="o">:</span> <span class="n">r1</span> <span class="n">b</span> <span class="n">a</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">cases</span> <span class="n">H</span> <span class="k">with</span> <span class="n">k</span> <span class="n">Hk</span><span class="o">,</span>
  <span class="n">existsi</span> <span class="bp">-</span><span class="n">k</span><span class="o">,</span>
  <span class="n">simp</span> <span class="o">[</span><span class="n">Hk</span><span class="o">],</span> <span class="c1">-- b + -a = -(37 * k)</span>
  <span class="n">sorry</span>
<span class="kn">end</span>

<span class="kn">definition</span> <span class="n">r2</span><span class="bp">.</span><span class="n">symm</span> <span class="o">(</span><span class="n">a</span> <span class="n">b</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">)</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="n">r2</span> <span class="n">a</span> <span class="n">b</span><span class="o">)</span> <span class="o">:</span> <span class="n">r2</span> <span class="n">b</span> <span class="n">a</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">cases</span> <span class="n">H</span> <span class="k">with</span> <span class="n">k</span> <span class="n">Hk</span><span class="o">,</span>
  <span class="n">existsi</span> <span class="bp">-</span><span class="n">k</span><span class="o">,</span>
  <span class="n">simp</span> <span class="o">[</span><span class="n">Hk</span><span class="o">],</span> <span class="c1">-- b + -a = -(k * 37)</span>
  <span class="n">sorry</span>
<span class="kn">end</span>

<span class="kn">definition</span> <span class="n">r3</span><span class="bp">.</span><span class="n">symm</span> <span class="o">(</span><span class="n">a</span> <span class="n">b</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">)</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="n">r3</span> <span class="n">a</span> <span class="n">b</span><span class="o">)</span> <span class="o">:</span> <span class="n">r3</span> <span class="n">b</span> <span class="n">a</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">cases</span> <span class="n">H</span> <span class="k">with</span> <span class="n">k</span> <span class="n">Hk</span><span class="o">,</span>
  <span class="n">existsi</span> <span class="bp">-</span><span class="n">k</span><span class="o">,</span>
  <span class="n">simp</span> <span class="o">[</span><span class="n">Hk</span><span class="o">]</span> <span class="c1">-- success!</span>
<span class="kn">end</span>

<span class="kn">definition</span> <span class="n">r4</span><span class="bp">.</span><span class="n">symm</span> <span class="o">(</span><span class="n">a</span> <span class="n">b</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">)</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="n">r4</span> <span class="n">a</span> <span class="n">b</span><span class="o">)</span> <span class="o">:</span> <span class="n">r4</span> <span class="n">b</span> <span class="n">a</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">cases</span> <span class="n">H</span> <span class="k">with</span> <span class="n">k</span> <span class="n">Hk</span><span class="o">,</span>
  <span class="n">existsi</span> <span class="bp">-</span><span class="n">k</span><span class="o">,</span>
  <span class="n">simp</span> <span class="o">[</span><span class="n">Hk</span><span class="o">]</span> <span class="c1">-- success!</span>
<span class="kn">end</span>
</pre></div>


<p>If you'd asked me in advance which relations would be easiest to work with I realise I would have no idea. But it seems <code>r3</code> and <code>r4</code> are better than <code>r1</code> and <code>r2</code>. Why is this?</p>

#### [ Kenny Lau (Aug 25 2018 at 11:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/best%20definition%20of%20%22congruent%20mod%2037%22/near/132741991):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">int</span><span class="bp">.</span><span class="n">modeq</span>

<span class="n">def</span> <span class="n">r5</span> <span class="o">(</span><span class="n">a</span> <span class="n">b</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">)</span> <span class="o">:=</span> <span class="n">a</span> <span class="bp">≡</span> <span class="n">b</span> <span class="o">[</span><span class="n">ZMOD</span> <span class="mi">37</span><span class="o">]</span>

<span class="kn">theorem</span> <span class="n">r5</span><span class="bp">.</span><span class="n">symm</span> <span class="o">(</span><span class="n">a</span> <span class="n">b</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">)</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="n">r5</span> <span class="n">a</span> <span class="n">b</span><span class="o">)</span> <span class="o">:</span> <span class="n">r5</span> <span class="n">b</span> <span class="n">a</span> <span class="o">:=</span>
<span class="n">int</span><span class="bp">.</span><span class="n">modeq</span><span class="bp">.</span><span class="n">symm</span> <span class="n">H</span>
</pre></div>

#### [ Johan Commelin (Aug 25 2018 at 11:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/best%20definition%20of%20%22congruent%20mod%2037%22/near/132741992):
<p>Of course you could also try<br>
<code>definition r6 (a b : ℤ) := ∃ k : ℤ, a = b + 37 * k</code><br>
I have no idea if it is easy to work with...</p>

#### [ Patrick Massot (Aug 25 2018 at 11:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/best%20definition%20of%20%22congruent%20mod%2037%22/near/132742000):
<p>You could insert <code>eq.symm</code> in your simp</p>

#### [ Kevin Buzzard (Aug 25 2018 at 11:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/best%20definition%20of%20%22congruent%20mod%2037%22/near/132742152):
<p>My "objection" to Kenny's approach is that my question is really about how one writes the interface, not the fact that it's there already.</p>

#### [ Kevin Buzzard (Aug 25 2018 at 11:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/best%20definition%20of%20%22congruent%20mod%2037%22/near/132742206):
<p>My objection to Patrick's is that sure I could work a bit harder and get stuff to work, but why do I have to do this for some and not others? Is it the case that <code>r3</code> and <code>r4</code> are actually <em>better</em> in some way?</p>

#### [ Patrick Massot (Aug 25 2018 at 11:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/best%20definition%20of%20%22congruent%20mod%2037%22/near/132742216):
<p>I think r6 is better</p>

#### [ Patrick Massot (Aug 25 2018 at 11:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/best%20definition%20of%20%22congruent%20mod%2037%22/near/132742255):
<p>because you can use <code>rw Hk, ring</code></p>

#### [ Kevin Buzzard (Aug 25 2018 at 11:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/best%20definition%20of%20%22congruent%20mod%2037%22/near/132742258):
<p><code>simp</code> works for <code>r6</code> too</p>

#### [ Kevin Buzzard (Aug 25 2018 at 11:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/best%20definition%20of%20%22congruent%20mod%2037%22/near/132742264):
<p>One problem with r1 -- r4 is that you can't use rw with any of them</p>

#### [ Chris Hughes (Aug 25 2018 at 11:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/best%20definition%20of%20%22congruent%20mod%2037%22/near/132742265):
<p>Johan's definition generalizes to a semiring :-)</p>

#### [ Kevin Buzzard (Aug 25 2018 at 11:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/best%20definition%20of%20%22congruent%20mod%2037%22/near/132742268):
<p>I don't think symmetry is true for a semiring :-)</p>

#### [ Patrick Massot (Aug 25 2018 at 11:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/best%20definition%20of%20%22congruent%20mod%2037%22/near/132742275):
<p>Kevin, do you see what you've done to your students?</p>

#### [ Kevin Buzzard (Aug 25 2018 at 11:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/best%20definition%20of%20%22congruent%20mod%2037%22/near/132742311):
<p>only one of them!</p>

#### [ Patrick Massot (Aug 25 2018 at 11:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/best%20definition%20of%20%22congruent%20mod%2037%22/near/132742324):
<p>Oh yeah, the other one became a constructivist...</p>

#### [ Kevin Buzzard (Aug 25 2018 at 11:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/best%20definition%20of%20%22congruent%20mod%2037%22/near/132742327):
<p>:-)</p>

#### [ Kevin Buzzard (Aug 25 2018 at 11:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/best%20definition%20of%20%22congruent%20mod%2037%22/near/132742334):
<p>maybe I need to rethink this entire thing</p>

#### [ Patrick Massot (Aug 25 2018 at 11:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/best%20definition%20of%20%22congruent%20mod%2037%22/near/132742387):
<p>I think r3-r6 are better than r1 and r2 because it allows to write the same thing as in real world: <code>cases H with k Hk,  existsi -k,  finish</code></p>

#### [ Kevin Buzzard (Aug 25 2018 at 11:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/best%20definition%20of%20%22congruent%20mod%2037%22/near/132742450):
<p>But isn't this answer just like mine -- "try all ways, see which ones work, decide those must be the best ways"</p>

#### [ Kevin Buzzard (Aug 25 2018 at 11:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/best%20definition%20of%20%22congruent%20mod%2037%22/near/132742451):
<p>I was interested in knowing which was the best way before I started</p>

#### [ Kevin Buzzard (Aug 25 2018 at 11:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/best%20definition%20of%20%22congruent%20mod%2037%22/near/132742453):
<p>I don't see how to figure it out a priori</p>

#### [ Patrick Massot (Aug 25 2018 at 11:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/best%20definition%20of%20%22congruent%20mod%2037%22/near/132742492):
<p>I think that we could have anticipated that Johan's version would be easier to rewrite</p>

#### [ Kevin Buzzard (Aug 25 2018 at 11:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/best%20definition%20of%20%22congruent%20mod%2037%22/near/132742625):
<p>yes; I didn't instinctively mention that possibility because it looked so asymmetric</p>

#### [ Kevin Buzzard (Aug 25 2018 at 11:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/best%20definition%20of%20%22congruent%20mod%2037%22/near/132742627):
<p>which is counter to my intuition, but which seems to play a big role here</p>

#### [ Kevin Buzzard (Aug 25 2018 at 11:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/best%20definition%20of%20%22congruent%20mod%2037%22/near/132742632):
<p>Mathematicians even _say_ "a and b are congruent mod 37" and there's an implicit symmetry implied when we say "and", but when you have to prove symmetry the first thing you have to do is to break it I guess</p>

#### [ Kevin Buzzard (Aug 25 2018 at 11:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/best%20definition%20of%20%22congruent%20mod%2037%22/near/132742634):
<p>and Johan's breaks it the most</p>

#### [ Patrick Massot (Aug 25 2018 at 11:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/best%20definition%20of%20%22congruent%20mod%2037%22/near/132742637):
<p>The point is that <code>x = ...</code> can't fail to rewrite <code>x</code></p>

#### [ Patrick Massot (Aug 25 2018 at 11:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/best%20definition%20of%20%22congruent%20mod%2037%22/near/132742670):
<p>whatever you do to <code>x</code> in your expression</p>

#### [ Kenny Lau (Aug 25 2018 at 13:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/best%20definition%20of%20%22congruent%20mod%2037%22/near/132746777):
<blockquote>
<p>My "objection" to Kenny's approach is that my question is really about how one writes the interface, not the fact that it's there already.</p>
</blockquote>
<p>my objection to your objection is that my answer prompts one to look at the definition in mathlib:</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">modeq</span> <span class="o">(</span><span class="n">n</span> <span class="n">a</span> <span class="n">b</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">)</span> <span class="o">:=</span> <span class="n">a</span> <span class="err">%</span> <span class="n">n</span> <span class="bp">=</span> <span class="n">b</span> <span class="err">%</span> <span class="n">n</span>

<span class="kn">notation</span> <span class="n">a</span> <span class="bp">`</span> <span class="bp">≡</span> <span class="bp">`</span><span class="o">:</span><span class="mi">50</span> <span class="n">b</span> <span class="bp">`</span> <span class="o">[</span><span class="n">ZMOD</span> <span class="bp">`</span><span class="o">:</span><span class="mi">50</span> <span class="n">n</span> <span class="bp">`</span><span class="o">]</span><span class="bp">`</span><span class="o">:</span><span class="mi">0</span> <span class="o">:=</span> <span class="n">modeq</span> <span class="n">n</span> <span class="n">a</span> <span class="n">b</span>

<span class="kn">namespace</span> <span class="n">modeq</span>
<span class="kn">variables</span> <span class="o">{</span><span class="n">n</span> <span class="n">m</span> <span class="n">a</span> <span class="n">b</span> <span class="n">c</span> <span class="n">d</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">}</span>

<span class="bp">@</span><span class="o">[</span><span class="n">refl</span><span class="o">]</span> <span class="kn">protected</span> <span class="kn">theorem</span> <span class="n">refl</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">)</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">≡</span> <span class="n">a</span> <span class="o">[</span><span class="n">ZMOD</span> <span class="n">n</span><span class="o">]</span> <span class="o">:=</span> <span class="bp">@</span><span class="n">rfl</span> <span class="bp">_</span> <span class="bp">_</span>

<span class="bp">@</span><span class="o">[</span><span class="n">symm</span><span class="o">]</span> <span class="kn">protected</span> <span class="kn">theorem</span> <span class="n">symm</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">≡</span> <span class="n">b</span> <span class="o">[</span><span class="n">ZMOD</span> <span class="n">n</span><span class="o">]</span> <span class="bp">→</span> <span class="n">b</span> <span class="bp">≡</span> <span class="n">a</span> <span class="o">[</span><span class="n">ZMOD</span> <span class="n">n</span><span class="o">]</span> <span class="o">:=</span> <span class="n">eq</span><span class="bp">.</span><span class="n">symm</span>

<span class="bp">@</span><span class="o">[</span><span class="n">trans</span><span class="o">]</span> <span class="kn">protected</span> <span class="kn">theorem</span> <span class="n">trans</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">≡</span> <span class="n">b</span> <span class="o">[</span><span class="n">ZMOD</span> <span class="n">n</span><span class="o">]</span> <span class="bp">→</span> <span class="n">b</span> <span class="bp">≡</span> <span class="n">c</span> <span class="o">[</span><span class="n">ZMOD</span> <span class="n">n</span><span class="o">]</span> <span class="bp">→</span> <span class="n">a</span> <span class="bp">≡</span> <span class="n">c</span> <span class="o">[</span><span class="n">ZMOD</span> <span class="n">n</span><span class="o">]</span> <span class="o">:=</span> <span class="n">eq</span><span class="bp">.</span><span class="n">trans</span>
</pre></div>

#### [ Kevin Buzzard (Aug 25 2018 at 14:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/best%20definition%20of%20%22congruent%20mod%2037%22/near/132746937):
<p>Yes but my actual question is: "I am defining some new relation on some new type completely unrelated to the integers, and I want to prove it's an equivalence relation. I've just realised that mathematically equivalent definitions of the relation will behave differently in Lean, so I need some pointers about how to formulate my relation so that I can use it efficiently".</p>

#### [ Kenny Lau (Aug 25 2018 at 14:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/best%20definition%20of%20%22congruent%20mod%2037%22/near/132746951):
<p>my objection is that you don't just have some random types</p>

#### [ Kenny Lau (Aug 25 2018 at 14:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/best%20definition%20of%20%22congruent%20mod%2037%22/near/132746954):
<p>if it's a group like the integers are, then you should just use quotient groups</p>


{% endraw %}
