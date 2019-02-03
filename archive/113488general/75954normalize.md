---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/75954normalize.html
---

## Stream: [general](index.html)
### Topic: [normalize](75954normalize.html)

---


{% raw %}
#### [ Kenny Lau (Feb 01 2019 at 13:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/normalize/near/157348940):
<p>Ok this situation is quite complicated here and I'm not sure I understand the whole situation (an import graph would be quite beneficial).</p>
<p>So I look at <a href="https://github.com/leanprover-community/mathlib/blob/master/src/algebra/gcd_domain.lean" target="_blank" title="https://github.com/leanprover-community/mathlib/blob/master/src/algebra/gcd_domain.lean">algebra/gcd_domain.lean</a> and think to myself: I should define <code>normalize x</code> to replace <code>x * norm_unit x</code> since that expression is used a lot and should have a name and is actually the whole point of <code>normalization_domain</code> (we don't really care about the unit it multiplies by, right?).</p>
<p>But this would require lemmas from <a href="https://github.com/leanprover-community/mathlib/blob/master/src/ring_theory/associated.lean" target="_blank" title="https://github.com/leanprover-community/mathlib/blob/master/src/ring_theory/associated.lean">ring_theory/associated.lean</a> about units and dvd.</p>
<p>Unfortunately, it imports <a href="https://github.com/leanprover-community/mathlib/blob/master/src/data/int/gcd.lean" target="_blank" title="https://github.com/leanprover-community/mathlib/blob/master/src/data/int/gcd.lean">data/int/gcd.lean</a> which imports algebra.gcd_domain, and this is an essential import in the sense that a majority of the file is based on this import.</p>
<p>However, <code>data/int/gcd.lean</code> is not an essential import of <code>ring_theory/associated.lean</code>, in the sense that &lt; 10% of the file breaks when I remove that import. Things that break include three theorems which is essentially examples about int and nat, and also a section below about normalization domain.</p>

#### [ Kenny Lau (Feb 01 2019 at 13:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/normalize/near/157348941):
<p>So my proposal is:</p>
<p>1. remove the import <code>data/int/gcd.lean</code> from <code>ring_theory/associated.lean</code><br>
2. move <code>ring_theory/associated.lean</code> to <code>algebra/associated.lean</code><br>
3. add the import <code>algebra/associated.lean</code> to <code>algebra/gcd_domain.lean</code><br>
4. add <code>normalize</code> in <code>algebra/gcd_domain.lean</code><br>
5. move the three theorems that break to <code>data/int/gcd.lean</code><br>
6. move the section that breaks to <code>algebra/gcd_domain.lean</code></p>

#### [ Kenny Lau (Feb 01 2019 at 13:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/normalize/near/157348944):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span>  do you think this is a good idea? did I miss anything?</p>

#### [ Mario Carneiro (Feb 01 2019 at 13:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/normalize/near/157349041):
<p>why does <code>int.gcd</code> use <code>algebra.normalization_domain</code>?</p>

#### [ Kenny Lau (Feb 01 2019 at 13:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/normalize/near/157349099):
<p>There is no <code>algebra.normalization_domain</code>: it is just <code>algebra.gcd_domain</code>.</p>

#### [ Kenny Lau (Feb 01 2019 at 13:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/normalize/near/157349103):
<p>And that uses that because the whole file is about gcd</p>

#### [ Mario Carneiro (Feb 01 2019 at 13:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/normalize/near/157349107):
<p><code>nat.gcd</code> doesn't</p>

#### [ Kenny Lau (Feb 01 2019 at 13:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/normalize/near/157349109):
<p>because <code>nat</code> isn't a <code>gcd_domain</code></p>

#### [ Kenny Lau (Feb 01 2019 at 13:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/normalize/near/157349239):
<p>I suppose we can remove the <code>normalization_domain</code> and <code>gcd_domain</code> sections of <code>data/int/gcd.lean</code> and move them to <code>algebra/gcd_domain.lean</code>?</p>

#### [ Kenny Lau (Feb 01 2019 at 13:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/normalize/near/157349245):
<p>What do you think?</p>

#### [ Kenny Lau (Feb 01 2019 at 13:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/normalize/near/157349263):
<p>afterall there's a proof that <code>int</code> is <code>euclidean_domain</code> in <code>algebra/euclidean_domain.lean</code> anyway, so this wouldn't be unprecedented</p>

#### [ Mario Carneiro (Feb 01 2019 at 13:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/normalize/near/157349345):
<p>my guess is that you can do integer gcd by reference to nat gcd, without bringing in the abstract algebra. But setting that aside, I think that moving  <code>ring_theory.associated</code> to <code>algebra</code> is okay for much of it, but not all; you will probably need to split the file</p>

#### [ Kenny Lau (Feb 01 2019 at 13:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/normalize/near/157349369):
<p>Ok I'll experiment on a branch</p>

#### [ Mario Carneiro (Feb 01 2019 at 13:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/normalize/near/157349426):
<p>I think that <code>data.int.gcd</code> shouldn't bring in anything from <code>ring_theory</code></p>

#### [ Kenny Lau (Feb 01 2019 at 13:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/normalize/near/157349455):
<p>I agree</p>

#### [ Kenny Lau (Feb 01 2019 at 14:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/normalize/near/157351447):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> so where should these theorems go?</p>
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">irreducible_iff_nat_prime</span> <span class="o">:</span> <span class="bp">∀</span><span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">),</span> <span class="kn">irreducible</span> <span class="n">a</span> <span class="bp">↔</span> <span class="n">nat</span><span class="bp">.</span><span class="n">prime</span> <span class="n">a</span>
<span class="kn">lemma</span> <span class="n">nat</span><span class="bp">.</span><span class="n">prime_iff_prime</span> <span class="o">{</span><span class="n">p</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">}</span> <span class="o">:</span> <span class="n">p</span><span class="bp">.</span><span class="n">prime</span> <span class="bp">↔</span> <span class="bp">_</span><span class="n">root_</span><span class="bp">.</span><span class="n">prime</span> <span class="o">(</span><span class="n">p</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:=</span>
<span class="kn">lemma</span> <span class="n">nat</span><span class="bp">.</span><span class="n">prime_iff_prime_int</span> <span class="o">{</span><span class="n">p</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">}</span> <span class="o">:</span> <span class="n">p</span><span class="bp">.</span><span class="n">prime</span> <span class="bp">↔</span> <span class="bp">_</span><span class="n">root_</span><span class="bp">.</span><span class="n">prime</span> <span class="o">(</span><span class="n">p</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">)</span> <span class="o">:=</span>
<span class="n">def</span> <span class="n">associates_int_equiv_nat</span> <span class="o">:</span> <span class="o">(</span><span class="n">associates</span> <span class="bp">ℤ</span><span class="o">)</span> <span class="err">≃</span> <span class="bp">ℕ</span> <span class="o">:=</span>
</pre></div>

#### [ Kenny Lau (Feb 01 2019 at 14:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/normalize/near/157351639):
<p><a href="https://github.com/leanprover-community/mathlib/blob/normalize/src/pending/default.lean" target="_blank" title="https://github.com/leanprover-community/mathlib/blob/normalize/src/pending/default.lean">https://github.com/leanprover-community/mathlib/blob/normalize/src/pending/default.lean</a></p>

#### [ Kevin Buzzard (Feb 01 2019 at 15:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/normalize/near/157358389):
<p>Can one break up file <code>X.lean</code> into <code>X_part_1.lean</code> and <code>X_part_2.lean</code> and then just change <code>X.lean</code> into <code>import X_part_1.lean import X_part_2.lean</code>, and then you have more breathing space to fiddle with imports?</p>


{% endraw %}
