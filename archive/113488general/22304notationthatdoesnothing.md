---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/22304notationthatdoesnothing.html
---

## Stream: [general](index.html)
### Topic: [notation that does nothing](22304notationthatdoesnothing.html)

---


{% raw %}
#### [ Johan Commelin (Nov 21 2018 at 13:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20that%20does%20nothing/near/148107367):
<p>I want something like this:</p>
<div class="codehilite"><pre><span></span><span class="n">local</span> <span class="kn">notation</span> <span class="bp">`</span> <span class="o">[</span><span class="bp">`</span><span class="n">n</span><span class="bp">`</span><span class="o">]</span> <span class="bp">`</span> <span class="o">:=</span> <span class="o">(((</span><span class="n">id</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="n">simplex_category</span><span class="o">)</span> <span class="o">(</span><span class="n">n</span><span class="o">))</span> <span class="o">:</span> <span class="n">simplex_category</span><span class="o">)</span>
<span class="kn">instance</span> <span class="o">:</span> <span class="n">has_coe_to_sort</span> <span class="n">simplex_category</span> <span class="o">:=</span> <span class="o">{</span> <span class="n">S</span> <span class="o">:=</span> <span class="kt">Type</span><span class="o">,</span> <span class="n">coe</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">n</span><span class="o">,</span> <span class="n">fin</span> <span class="err">$</span> <span class="n">n</span><span class="bp">+</span><span class="mi">1</span> <span class="o">}</span>
</pre></div>


<p>In other words, it should take whatever is between <code>[</code> and <code>]</code>, interpret that as a <code>ℕ</code>, but interpret <code>[_]</code> as an element of <code>simplex_category</code>.<br>
In this way, I can talk about <code>[n+1]</code> without defining addition or one for <code>simplex_category</code>. In this way I can also coerce <code>[n]</code> to <code>fin (n+1)</code> without defining that coercion for all naturals.<br>
In other words, I would like to make sure that <code>i : [n+1]</code> typechecks.</p>

#### [ Simon Hudon (Nov 21 2018 at 21:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20that%20does%20nothing/near/148135059):
<p>Your snippet doesn't work?</p>

#### [ Chris Hughes (Nov 21 2018 at 21:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20that%20does%20nothing/near/148135146):
<p>Isn't this overloaded from <code>list</code></p>

#### [ Chris Hughes (Nov 21 2018 at 21:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20that%20does%20nothing/near/148135157):
<p>Use a different type of brackets?</p>

#### [ Simon Hudon (Nov 21 2018 at 21:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20that%20does%20nothing/near/148135163):
<p>Instead of using <code>id</code>, try using:</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">my_brackets</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="n">nat</span><span class="o">)</span> <span class="o">:</span> <span class="n">simplex_category</span> <span class="o">:=</span> <span class="n">n</span>
<span class="n">local</span> <span class="kn">notation</span> <span class="bp">`</span> <span class="o">[</span><span class="bp">`</span><span class="n">n</span><span class="bp">`</span><span class="o">]</span> <span class="bp">`</span> <span class="o">:=</span> <span class="n">my_brackets</span> <span class="n">n</span>
</pre></div>

#### [ Simon Hudon (Nov 21 2018 at 21:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20that%20does%20nothing/near/148135203):
<p>Yes, that's also true</p>

#### [ Simon Hudon (Nov 21 2018 at 21:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20that%20does%20nothing/near/148135220):
<p>A lot of brackets are already taken</p>

#### [ Johan Commelin (Nov 21 2018 at 21:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20that%20does%20nothing/near/148135866):
<p>I now have</p>
<div class="codehilite"><pre><span></span><span class="kn">inductive</span> <span class="n">simplex_category</span>
<span class="bp">|</span> <span class="n">from_nat</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="bp">→</span> <span class="n">simplex_category</span>

<span class="kn">namespace</span> <span class="n">simplex_category</span>

<span class="n">local</span> <span class="kn">notation</span> <span class="bp">`</span> <span class="o">[</span><span class="bp">`</span><span class="n">n</span><span class="bp">`</span><span class="o">]</span> <span class="bp">`</span> <span class="o">:=</span> <span class="n">from_nat</span> <span class="n">n</span>

<span class="kn">instance</span> <span class="o">:</span> <span class="n">has_coe_to_sort</span> <span class="n">simplex_category</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">S</span> <span class="o">:=</span> <span class="kt">Type</span><span class="o">,</span>
  <span class="n">coe</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">n</span><span class="o">,</span> <span class="n">simplex_category</span><span class="bp">.</span><span class="n">cases_on</span> <span class="n">n</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">n</span><span class="o">,</span> <span class="n">fin</span> <span class="err">$</span> <span class="n">n</span><span class="bp">+</span><span class="mi">1</span><span class="o">)</span> <span class="o">}</span>

<span class="kn">instance</span> <span class="o">{</span><span class="err">Δ</span> <span class="o">:</span> <span class="n">simplex_category</span><span class="o">}</span> <span class="o">:</span> <span class="n">linear_order</span> <span class="err">Δ</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">cases</span> <span class="err">Δ</span><span class="bp">;</span> <span class="n">unfold_coes</span><span class="bp">;</span> <span class="n">apply_instance</span>

<span class="kn">instance</span> <span class="o">:</span> <span class="n">category_theory</span><span class="bp">.</span><span class="n">category</span> <span class="n">simplex_category</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">hom</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="err">Δ</span> <span class="err">Δ&#39;</span><span class="o">,</span> <span class="o">{</span><span class="n">f</span> <span class="o">:</span> <span class="err">Δ</span> <span class="bp">→</span> <span class="err">Δ&#39;</span> <span class="bp">//</span> <span class="n">monotone</span> <span class="n">f</span><span class="o">},</span>
  <span class="n">id</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="bp">_</span><span class="o">,</span> <span class="bp">⟨_</span><span class="o">,</span> <span class="n">monotone_id</span><span class="bp">⟩</span><span class="o">,</span>
  <span class="n">comp</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span> <span class="n">f</span> <span class="n">g</span><span class="o">,</span> <span class="bp">⟨_</span><span class="o">,</span> <span class="n">monotone_comp</span> <span class="n">f</span><span class="bp">.</span><span class="mi">2</span> <span class="n">g</span><span class="bp">.</span><span class="mi">2</span><span class="bp">⟩</span> <span class="o">}</span>
</pre></div>


<p>It seems to work as intended. It seems like a bit of a trick to define and inductive type that is equivalent to <code>nat</code>, but whatever.</p>

#### [ Johan Commelin (Nov 21 2018 at 21:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20that%20does%20nothing/near/148135918):
<p>And I definitely want <code>[n]</code> notation. It's just silly that the notation for lists isn't local.</p>

#### [ Kevin Buzzard (Nov 21 2018 at 21:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/notation%20that%20does%20nothing/near/148136538):
<p>Making copies of inductive types is not uncommon. If you want to do congruence mod n on the integers, you run into problems because equivalence relations are a class but you want more than one equivalence relation on the integers. You can fix it by making these fake copies.</p>


{% endraw %}
