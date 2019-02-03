---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/37885finntoTvsfinsuppfinnT.html
---

## Stream: [maths](index.html)
### Topic: [`fin n \to T` vs `finsupp (fin n) T`](37885finntoTvsfinsuppfinnT.html)

---


{% raw %}
#### [ Johan Commelin (May 28 2018 at 15:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/%60fin%20n%20%5Cto%20T%60%20vs%20%60finsupp%20%28fin%20n%29%20T%60/near/127206339):
<p>General question: (<code>T</code> is a type) is it easy to move back and forth between <code>fin n \to T</code> and the finsupp variant?<br>
Specific question: I am working with <code>nnreal^n</code>, and I model it as <code>fin n \to nnreal</code>. Now I have a map <code>fin n \to fin m</code> and I want to get the induced map <code>nnreal^n \to nnreal^m</code>. This is almost <code>finsupp.map_domain</code>. Except that I finitely supported functions, but general ones. Is it easy to still use <code>map_domain</code>?</p>

#### [ Chris Hughes (May 28 2018 at 16:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/%60fin%20n%20%5Cto%20T%60%20vs%20%60finsupp%20%28fin%20n%29%20T%60/near/127207254):
<p>I guess you could just turn your fin n \to T into a finsupp quite easily. Just by doing <code>support := univ.filter (\la x, fx \ne!= 0)</code> etc.<br>
Might e useful in general to define that function from a <code>fintype → T</code> to <code>fintype →₀ T</code></p>

#### [ Johan Commelin (May 28 2018 at 16:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/%60fin%20n%20%5Cto%20T%60%20vs%20%60finsupp%20%28fin%20n%29%20T%60/near/127207269):
<p>Should that go into mathlib?</p>

#### [ Johannes Hölzl (May 28 2018 at 16:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/%60fin%20n%20%5Cto%20T%60%20vs%20%60finsupp%20%28fin%20n%29%20T%60/near/127207324):
<p>Yes. Just not for <code>fin n</code> specifically but for each <code>fintype</code>.</p>

#### [ Johan Commelin (May 28 2018 at 16:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/%60fin%20n%20%5Cto%20T%60%20vs%20%60finsupp%20%28fin%20n%29%20T%60/near/127207358):
<p>Ok, I'll put it into finsupp.lean</p>

#### [ Johan Commelin (May 28 2018 at 16:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/%60fin%20n%20%5Cto%20T%60%20vs%20%60finsupp%20%28fin%20n%29%20T%60/near/127207407):
<p>What is the canonical name for this beast?</p>

#### [ Johan Commelin (May 28 2018 at 16:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/%60fin%20n%20%5Cto%20T%60%20vs%20%60finsupp%20%28fin%20n%29%20T%60/near/127207409):
<p>Some sort of <code>coe</code>?</p>

#### [ Johan Commelin (May 28 2018 at 16:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/%60fin%20n%20%5Cto%20T%60%20vs%20%60finsupp%20%28fin%20n%29%20T%60/near/127207412):
<p>I've never done anything with <code>coe</code></p>

#### [ Johan Commelin (May 28 2018 at 16:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/%60fin%20n%20%5Cto%20T%60%20vs%20%60finsupp%20%28fin%20n%29%20T%60/near/127207991):
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">foobar</span> <span class="o">{</span><span class="n">T</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">[</span><span class="n">has_zero</span> <span class="n">T</span><span class="o">]</span> <span class="o">[</span><span class="n">decidable_eq</span> <span class="n">T</span><span class="o">]</span> <span class="o">{</span><span class="n">X</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span>  <span class="o">[</span><span class="n">fintype</span> <span class="n">X</span><span class="o">]</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">X</span> <span class="bp">→</span> <span class="n">T</span><span class="o">)</span> <span class="o">:</span> <span class="o">(</span><span class="n">X</span> <span class="bp">→</span><span class="err">₀</span> <span class="n">T</span><span class="o">)</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">support</span> <span class="o">:=</span> <span class="n">univ</span><span class="bp">.</span><span class="n">filter</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">x</span><span class="o">,</span> <span class="n">f</span> <span class="n">x</span> <span class="bp">≠</span> <span class="mi">0</span><span class="o">),</span>
  <span class="n">to_fun</span> <span class="o">:=</span> <span class="n">f</span><span class="o">,</span>
  <span class="n">mem_support_to_fun</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">x</span><span class="o">,</span> <span class="bp">⟨λ</span> <span class="n">h</span><span class="o">,</span> <span class="o">(</span><span class="n">mem_filter</span><span class="bp">.</span><span class="n">mp</span> <span class="n">h</span><span class="o">)</span><span class="bp">.</span><span class="mi">2</span><span class="o">,</span> <span class="bp">λ</span> <span class="n">h</span><span class="o">,</span> <span class="o">(</span><span class="n">mem_filter</span><span class="bp">.</span><span class="n">mpr</span> <span class="bp">⟨</span><span class="n">mem_univ</span> <span class="n">x</span><span class="o">,</span> <span class="n">h</span><span class="bp">⟩</span><span class="o">)</span><span class="bp">⟩</span><span class="o">}</span>
</pre></div>


{% endraw %}
