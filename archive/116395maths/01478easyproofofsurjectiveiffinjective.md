---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/01478easyproofofsurjectiveiffinjective.html
---

## Stream: [maths](index.html)
### Topic: [easy proof of surjective_iff_injective](01478easyproofofsurjectiveiffinjective.html)

---


{% raw %}
#### [ Chris Hughes (Apr 06 2018 at 18:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/easy%20proof%20of%20surjective_iff_injective/near/124726537):
<p>Is there an easy proof of </p>
<div class="codehilite"><pre><span></span><span class="kn">lemma</span>  <span class="n">injective_iff_surjective</span> <span class="o">[</span><span class="n">fintype</span> <span class="n">α</span><span class="o">]</span> <span class="o">{</span><span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span><span class="o">}</span> <span class="o">(</span><span class="n">e</span> <span class="o">:</span> <span class="n">α</span> <span class="err">≃</span> <span class="n">β</span><span class="o">)</span> <span class="o">:</span> <span class="n">injective</span> <span class="n">f</span> <span class="bp">↔</span>  <span class="n">surjective</span> <span class="n">f</span>
</pre></div>


<p>It took me 40 lines, but with stuff like this, there's often some one or two line proof.</p>

#### [ Kevin Buzzard (Apr 06 2018 at 18:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/easy%20proof%20of%20surjective_iff_injective/near/124726662):
<p>I have no idea whether this maths idea is easily leanified, but using e you can build a map alpha -&gt; alpha (f then e to get you back to alpha), and if the collection of all such maps alpha -&gt; alpha is known to be a fintype then you know there must exist nats <code>a&lt;b</code> with f^a = f^b (f^n = f composed with itself n times).</p>

#### [ Kevin Buzzard (Apr 06 2018 at 18:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/easy%20proof%20of%20surjective_iff_injective/near/124726668):
<p>Now under either the injectivity or the surjectivity assumption you can deduce f^{b-a} = id</p>

#### [ Kevin Buzzard (Apr 06 2018 at 18:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/easy%20proof%20of%20surjective_iff_injective/near/124726669):
<p>and then f^{b-a-1} is the inverse</p>

#### [ Chris Hughes (Apr 06 2018 at 18:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/easy%20proof%20of%20surjective_iff_injective/near/124727085):
<p>Sounds very doable. I'm not sure there's a power function on functions yet though.</p>

#### [ Chris Hughes (Apr 06 2018 at 21:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/easy%20proof%20of%20surjective_iff_injective/near/124733354):
<p>Longer, but cooler</p>
<div class="codehilite"><pre><span></span><span class="kn">instance</span> <span class="k">fun</span><span class="bp">.</span><span class="n">monoid</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">:</span> <span class="n">monoid</span> <span class="o">(</span><span class="n">α</span> <span class="bp">→</span> <span class="n">α</span><span class="o">)</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">mul</span> <span class="o">:=</span> <span class="o">(</span><span class="err">∘</span><span class="o">),</span>
  <span class="n">mul_assoc</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="bp">_</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">,</span> <span class="n">rfl</span><span class="o">,</span>
  <span class="n">one</span> <span class="o">:=</span> <span class="n">id</span><span class="o">,</span>
  <span class="n">one_mul</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="bp">_</span><span class="o">,</span> <span class="n">rfl</span><span class="o">,</span>
  <span class="n">mul_one</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="bp">_</span><span class="o">,</span> <span class="n">rfl</span> <span class="o">}</span>

<span class="kn">lemma</span> <span class="n">eq_of_left_inv_of_right_inv</span> <span class="o">[</span><span class="n">monoid</span> <span class="n">α</span><span class="o">]</span> <span class="o">{</span><span class="n">a</span> <span class="n">b</span> <span class="n">c</span> <span class="o">:</span> <span class="n">α</span><span class="o">}</span>
    <span class="o">(</span><span class="n">h₁</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">*</span> <span class="n">b</span> <span class="bp">=</span> <span class="mi">1</span><span class="o">)</span> <span class="o">(</span><span class="n">h₂</span> <span class="o">:</span> <span class="n">c</span> <span class="bp">*</span> <span class="n">a</span> <span class="bp">=</span> <span class="mi">1</span><span class="o">)</span> <span class="o">:</span> <span class="n">b</span> <span class="bp">=</span> <span class="n">c</span> <span class="o">:=</span>
<span class="k">have</span> <span class="n">h₃</span> <span class="o">:</span> <span class="n">c</span>  <span class="bp">*</span> <span class="n">a</span> <span class="bp">*</span> <span class="n">b</span> <span class="bp">=</span> <span class="n">c</span> <span class="bp">*</span> <span class="mi">1</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">rw</span> <span class="o">[</span><span class="err">←</span> <span class="n">h₁</span><span class="o">,</span> <span class="n">mul_assoc</span><span class="o">],</span>
<span class="k">by</span> <span class="n">rwa</span> <span class="o">[</span><span class="n">h₂</span><span class="o">,</span> <span class="n">one_mul</span><span class="o">,</span> <span class="n">mul_one</span><span class="o">]</span> <span class="n">at</span> <span class="n">h₃</span>

<span class="kn">lemma</span> <span class="n">pow_mul_pow_eq_one</span> <span class="o">[</span><span class="n">monoid</span> <span class="n">α</span><span class="o">]</span> <span class="o">{</span><span class="n">a</span> <span class="n">b</span> <span class="o">:</span> <span class="n">α</span><span class="o">}</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">n</span><span class="o">,</span> <span class="n">a</span> <span class="bp">*</span> <span class="n">b</span> <span class="bp">=</span> <span class="mi">1</span> <span class="bp">→</span> <span class="n">a</span><span class="err">^</span><span class="n">n</span> <span class="bp">*</span> <span class="n">b</span><span class="err">^</span><span class="n">n</span> <span class="bp">=</span> <span class="mi">1</span>
<span class="bp">|</span> <span class="mi">0</span>     <span class="o">:=</span> <span class="bp">λ</span> <span class="n">h</span><span class="o">,</span> <span class="n">one_mul</span> <span class="bp">_</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">n</span><span class="bp">+</span><span class="mi">1</span><span class="o">)</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">h</span><span class="o">,</span>
  <span class="k">by</span> <span class="n">rw</span> <span class="o">[</span><span class="n">pow_succ&#39;</span><span class="o">,</span> <span class="bp">_</span><span class="n">root_</span><span class="bp">.</span><span class="n">pow_succ</span><span class="o">,</span> <span class="n">mul_assoc</span><span class="o">,</span> <span class="err">←</span> <span class="n">mul_assoc</span> <span class="n">a</span><span class="o">,</span> <span class="n">h</span><span class="o">,</span> <span class="n">one_mul</span><span class="o">]</span><span class="bp">;</span>
  <span class="n">exact</span> <span class="n">pow_mul_pow_eq_one</span> <span class="n">n</span> <span class="n">h</span>

<span class="kn">lemma</span> <span class="n">mul_eq_one_of_mul_eq_one</span> <span class="o">[</span><span class="n">fintype</span> <span class="n">α</span><span class="o">]</span> <span class="o">[</span><span class="n">monoid</span> <span class="n">α</span><span class="o">]</span>
    <span class="o">(</span><span class="n">a</span> <span class="n">b</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">*</span> <span class="n">b</span> <span class="bp">=</span> <span class="mi">1</span><span class="o">)</span> <span class="o">:</span> <span class="n">b</span> <span class="bp">*</span> <span class="n">a</span> <span class="bp">=</span> <span class="mi">1</span> <span class="o">:=</span>
<span class="k">have</span> <span class="n">hmn</span> <span class="o">:</span> <span class="bp">∃</span> <span class="n">m</span> <span class="n">n</span><span class="o">,</span> <span class="n">m</span> <span class="bp">≠</span> <span class="n">n</span> <span class="bp">∧</span> <span class="n">a</span><span class="err">^</span><span class="n">n</span> <span class="bp">=</span> <span class="n">a</span><span class="err">^</span><span class="n">m</span> <span class="o">:=</span>
<span class="n">by_contradiction</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">h</span><span class="o">,</span> <span class="n">set</span><span class="bp">.</span><span class="n">not_injective_nat_fintype</span>
<span class="o">(</span><span class="k">show</span> <span class="n">injective</span> <span class="o">(</span><span class="n">monoid</span><span class="bp">.</span><span class="n">pow</span> <span class="n">a</span><span class="o">),</span> <span class="k">from</span>
<span class="bp">λ</span> <span class="n">m</span> <span class="n">n</span> <span class="n">h₁</span><span class="o">,</span> <span class="n">by_contradiction</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">h₂</span><span class="o">,</span> <span class="n">h</span> <span class="bp">⟨</span><span class="n">m</span><span class="o">,</span> <span class="n">n</span><span class="o">,</span> <span class="n">h₂</span><span class="o">,</span> <span class="n">h₁</span><span class="bp">.</span><span class="n">symm</span><span class="bp">⟩</span><span class="o">),</span>
<span class="k">let</span> <span class="bp">⟨</span><span class="n">m</span><span class="o">,</span> <span class="n">n</span><span class="o">,</span> <span class="n">hmn₁</span><span class="o">,</span> <span class="n">hmn₂</span><span class="bp">⟩</span> <span class="o">:=</span> <span class="n">hmn</span> <span class="k">in</span>
<span class="k">begin</span>
  <span class="n">clear</span> <span class="bp">_</span><span class="n">let_match</span><span class="o">,</span>
  <span class="n">wlog</span> <span class="n">hn</span> <span class="o">:</span> <span class="n">n</span> <span class="bp">≤</span> <span class="n">m</span> <span class="kn">using</span> <span class="n">n</span> <span class="n">m</span><span class="o">,</span>
  <span class="k">have</span> <span class="o">:</span> <span class="mi">0</span> <span class="bp">&lt;</span> <span class="n">m</span> <span class="bp">-</span> <span class="n">n</span> <span class="o">:=</span> <span class="n">nat</span><span class="bp">.</span><span class="n">sub_pos_of_lt</span> <span class="o">(</span><span class="n">lt_of_le_of_ne</span> <span class="n">hn</span> <span class="n">hmn₁</span><span class="bp">.</span><span class="n">symm</span><span class="o">),</span>
  <span class="k">have</span> <span class="n">h₁</span> <span class="o">:</span> <span class="n">a</span><span class="err">^</span><span class="n">n</span> <span class="bp">*</span> <span class="n">b</span><span class="err">^</span><span class="n">n</span> <span class="bp">=</span> <span class="n">a</span><span class="err">^</span><span class="o">(</span><span class="n">m</span> <span class="bp">-</span> <span class="n">n</span><span class="o">)</span> <span class="bp">*</span> <span class="n">a</span><span class="err">^</span><span class="n">n</span> <span class="bp">*</span> <span class="n">b</span><span class="err">^</span><span class="n">n</span> <span class="o">:=</span>
    <span class="k">by</span> <span class="n">rw</span> <span class="o">[</span><span class="err">←</span> <span class="bp">_</span><span class="n">root_</span><span class="bp">.</span><span class="n">pow_add</span><span class="o">,</span> <span class="n">nat</span><span class="bp">.</span><span class="n">sub_add_cancel</span> <span class="n">hn</span><span class="o">,</span> <span class="n">hmn₂</span><span class="o">],</span>
  <span class="n">rw</span> <span class="o">[</span><span class="n">mul_assoc</span><span class="o">,</span> <span class="n">pow_mul_pow_eq_one</span> <span class="bp">_</span> <span class="n">h</span><span class="o">,</span> <span class="n">mul_one</span><span class="o">,</span> <span class="err">←</span> <span class="n">succ_pred_eq_of_pos</span>
      <span class="n">this</span><span class="o">,</span> <span class="n">pow_succ&#39;</span><span class="o">]</span> <span class="n">at</span> <span class="n">h₁</span><span class="o">,</span>
  <span class="n">rw</span> <span class="o">[</span><span class="n">eq_of_left_inv_of_right_inv</span> <span class="n">h</span> <span class="n">h₁</span><span class="bp">.</span><span class="n">symm</span><span class="o">,</span> <span class="n">h₁</span><span class="o">],</span>
<span class="kn">end</span>

<span class="kn">lemma</span> <span class="n">surjective_iff_injective</span> <span class="o">[</span><span class="n">fintype</span> <span class="n">α</span><span class="o">]</span> <span class="o">{</span><span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">α</span><span class="o">}</span> <span class="o">:</span> <span class="n">injective</span> <span class="n">f</span> <span class="bp">↔</span> <span class="n">surjective</span> <span class="n">f</span> <span class="o">:=</span>
<span class="n">or</span><span class="bp">.</span><span class="n">cases_on</span> <span class="o">(</span><span class="n">classical</span><span class="bp">.</span><span class="n">em</span> <span class="o">(</span><span class="n">nonempty</span> <span class="n">α</span><span class="o">))</span>
  <span class="o">(</span><span class="bp">λ</span> <span class="bp">⟨</span><span class="n">a</span><span class="bp">⟩</span><span class="o">,</span> <span class="bp">⟨λ</span> <span class="n">hinj</span><span class="o">,</span> <span class="n">surjective_of_has_right_inverse</span> <span class="err">$</span>
    <span class="k">let</span> <span class="bp">⟨</span><span class="n">g</span><span class="o">,</span> <span class="n">hg</span><span class="bp">⟩</span> <span class="o">:=</span> <span class="bp">@</span><span class="n">injective</span><span class="bp">.</span><span class="n">has_left_inverse</span> <span class="bp">_</span> <span class="bp">⟨</span><span class="n">a</span><span class="bp">⟩</span> <span class="bp">_</span> <span class="bp">_</span> <span class="n">hinj</span> <span class="k">in</span>
    <span class="bp">⟨</span><span class="n">g</span><span class="o">,</span> <span class="bp">λ</span> <span class="n">x</span><span class="o">,</span> <span class="k">show</span> <span class="o">(</span><span class="n">f</span> <span class="bp">*</span> <span class="n">g</span><span class="o">)</span> <span class="n">x</span> <span class="bp">=</span> <span class="n">x</span><span class="o">,</span> <span class="k">by</span> <span class="n">rw</span> <span class="n">mul_eq_one_of_mul_eq_one</span>
        <span class="n">g</span> <span class="n">f</span> <span class="o">(</span><span class="n">id_of_left_inverse</span> <span class="n">hg</span><span class="o">)</span><span class="bp">;</span> <span class="n">refl</span><span class="bp">⟩</span><span class="o">,</span>
  <span class="bp">λ</span> <span class="n">hsurj</span><span class="o">,</span> <span class="n">injective_of_has_left_inverse</span> <span class="err">$</span>
    <span class="k">let</span> <span class="bp">⟨</span><span class="n">g</span><span class="o">,</span> <span class="n">hg</span><span class="bp">⟩</span> <span class="o">:=</span> <span class="n">surjective</span><span class="bp">.</span><span class="n">has_right_inverse</span> <span class="n">hsurj</span> <span class="k">in</span>
    <span class="bp">⟨</span><span class="n">g</span><span class="o">,</span> <span class="bp">λ</span> <span class="n">x</span><span class="o">,</span> <span class="k">show</span> <span class="o">(</span><span class="n">g</span> <span class="bp">*</span> <span class="n">f</span><span class="o">)</span> <span class="n">x</span> <span class="bp">=</span> <span class="n">x</span><span class="o">,</span> <span class="k">by</span> <span class="n">rw</span> <span class="n">mul_eq_one_of_mul_eq_one</span>
        <span class="n">f</span> <span class="n">g</span> <span class="o">(</span><span class="n">id_of_right_inverse</span> <span class="n">hg</span><span class="o">)</span><span class="bp">;</span> <span class="n">refl</span><span class="bp">⟩⟩</span><span class="o">)</span>
<span class="o">(</span><span class="bp">λ</span> <span class="n">h</span><span class="o">,</span> <span class="bp">⟨λ</span> <span class="bp">_</span> <span class="n">a</span><span class="o">,</span> <span class="n">false</span><span class="bp">.</span><span class="n">elim</span> <span class="o">(</span><span class="n">h</span> <span class="bp">⟨</span><span class="n">a</span><span class="bp">⟩</span><span class="o">),</span> <span class="bp">λ</span> <span class="bp">_</span> <span class="n">a</span><span class="o">,</span> <span class="n">false</span><span class="bp">.</span><span class="n">elim</span> <span class="o">(</span><span class="n">h</span> <span class="bp">⟨</span><span class="n">a</span><span class="bp">⟩</span><span class="o">)</span><span class="bp">⟩</span><span class="o">)</span>
</pre></div>

#### [ Chris Hughes (Apr 06 2018 at 21:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/easy%20proof%20of%20surjective_iff_injective/near/124733504):
<p>Some of the monoid stuff is there already actually.</p>

#### [ Kevin Buzzard (Apr 06 2018 at 21:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/easy%20proof%20of%20surjective_iff_injective/near/124734102):
<p>I agree it's cooler, in the sense that you seem here to be proving what look like fundamental facts about monoids. Dumb question:  is there some infinite monoid for which an element can have a left inverse which is not a right inverse?</p>

#### [ Kevin Buzzard (Apr 06 2018 at 21:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/easy%20proof%20of%20surjective_iff_injective/near/124734144):
<p>That's the sort of question asked by someone who does not have a good enough collection of monoids in their brain</p>

#### [ Mario Carneiro (Apr 06 2018 at 21:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/easy%20proof%20of%20surjective_iff_injective/near/124734460):
<p>Yes. <code>pred</code> and <code>succ</code> are a perfect example of this: <code>pred (succ n) = n</code> but <code>succ (pred n) != n</code></p>

#### [ Kevin Buzzard (Apr 06 2018 at 22:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/easy%20proof%20of%20surjective_iff_injective/near/124736849):
<p>Aah, endomorphisms of an arbitrary set are a monoid.</p>

#### [ Kevin Buzzard (Apr 06 2018 at 22:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/easy%20proof%20of%20surjective_iff_injective/near/124736923):
<p>I see. In fact a category with one object is the same thing as a monoid, and an example of a category with one object is take your favourite algebraic structure and consider structure-preserving endomorphisms of an object with that structure.</p>

#### [ Kevin Buzzard (Apr 06 2018 at 22:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/easy%20proof%20of%20surjective_iff_injective/near/124736932):
<p>Here we have the simple case of a set, i.e. no algebraic structure at all.</p>

#### [ Kevin Buzzard (Apr 06 2018 at 22:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/easy%20proof%20of%20surjective_iff_injective/near/124736947):
<p>well, maybe "the empty algebraic structure" is a better way of saying it</p>

#### [ Kevin Buzzard (Apr 06 2018 at 22:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/easy%20proof%20of%20surjective_iff_injective/near/124737052):
<p>so this (succ and pred) is a proof that the naturals are not a fintype.</p>

#### [ Kevin Buzzard (Apr 06 2018 at 22:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/easy%20proof%20of%20surjective_iff_injective/near/124737895):
<p>actually, that's circular, because Chris (and me!) uses the fact that they're infinite in the proof.</p>

#### [ Kevin Buzzard (Apr 06 2018 at 22:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/easy%20proof%20of%20surjective_iff_injective/near/124737952):
<p>Oh, +1 for use of wlog ;-)</p>

#### [ Simon Hudon (Apr 06 2018 at 22:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/easy%20proof%20of%20surjective_iff_injective/near/124737978):
<p>Was <code>wlog</code> hard to use?</p>

#### [ Kevin Buzzard (Apr 06 2018 at 22:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/easy%20proof%20of%20surjective_iff_injective/near/124738032):
<p>No, it's just such a natural maths thing to use and it wasn't there a few weeks ago :-)</p>

#### [ Kevin Buzzard (Apr 06 2018 at 22:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/easy%20proof%20of%20surjective_iff_injective/near/124738034):
<p>So just the opposite really.</p>

#### [ Simon Hudon (Apr 06 2018 at 23:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/easy%20proof%20of%20surjective_iff_injective/near/124738150):
<p>Glad to hear it :)</p>


{% endraw %}
