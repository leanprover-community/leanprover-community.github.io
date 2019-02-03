---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/18763suprandrange.html
---

## Stream: [maths](https://leanprover-community.github.io/archive/116395maths/index.html)
### Topic: [supr and range](https://leanprover-community.github.io/archive/116395maths/18763suprandrange.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Sebastien Gouezel (Nov 13 2018 at 18:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/supr%20and%20range/near/147609120):
<p>There are the following definitions in mathlib:</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">supr</span> <span class="o">(</span><span class="n">s</span> <span class="o">:</span> <span class="n">ι</span> <span class="bp">→</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="n">α</span> <span class="o">:=</span> <span class="n">Sup</span> <span class="o">{</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">|</span> <span class="bp">∃</span><span class="n">i</span> <span class="o">:</span> <span class="n">ι</span><span class="o">,</span> <span class="n">a</span> <span class="bp">=</span> <span class="n">s</span> <span class="n">i</span><span class="o">}</span>

<span class="n">def</span> <span class="n">range</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">ι</span> <span class="bp">→</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span> <span class="o">:=</span> <span class="o">{</span><span class="n">x</span> <span class="bp">|</span> <span class="bp">∃</span><span class="n">y</span><span class="o">,</span> <span class="n">f</span> <span class="n">y</span> <span class="bp">=</span> <span class="n">x</span><span class="o">}</span>
</pre></div>


<p>You can see that the order after the existential quantifiers is swapped. Therefore, <code>supr f</code>and <code>Sup (range f)</code> are not defeq. Is this on purpose or by accident? More importantly, if I want to unify the two, which one should I choose? I would rather use the first one <code>∃i, a = s i</code>, which could help the simplifier to rewrite <code>a</code> if at some point we end up with an assumption of the form <code>a = s i</code>, but there might be some reason I am missing for the current definition of <code>range</code>.</p>

#### [ Sebastien Gouezel (Nov 13 2018 at 18:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/supr%20and%20range/near/147609524):
<p>Additional data point:</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">image</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span><span class="o">)</span> <span class="o">(</span><span class="n">s</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="n">set</span> <span class="n">β</span> <span class="o">:=</span> <span class="o">{</span><span class="n">b</span> <span class="bp">|</span> <span class="bp">∃</span> <span class="n">a</span><span class="o">,</span> <span class="n">a</span> <span class="err">∈</span> <span class="n">s</span> <span class="bp">∧</span> <span class="n">f</span> <span class="n">a</span> <span class="bp">=</span> <span class="n">b</span><span class="o">}</span>
</pre></div>

#### [ Johannes Hölzl (Nov 13 2018 at 18:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/supr%20and%20range/near/147609790):
<p>oops, I never realized this. I would keep <code>range</code> (as it is similar to <code>image</code>), and change <code>supr</code>.</p>

#### [ Mario Carneiro (Nov 13 2018 at 18:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/supr%20and%20range/near/147610281):
<p>the variable on the right thing is also consistent with the definition of <code>eq</code></p>

#### [ Sebastien Gouezel (Nov 13 2018 at 18:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/supr%20and%20range/near/147611469):
<blockquote>
<p>the variable on the right thing is also consistent with the definition of <code>eq</code></p>
</blockquote>
<p>Not sure I get it (too many variables around :). Do you mean that you also think that the definition of <code>supr</code> and <code>image</code> is right, and that I should fix <code>range</code>?</p>

#### [ Johannes Hölzl (Nov 13 2018 at 18:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/supr%20and%20range/near/147612064):
<p><code>range</code> and <code>image</code> are the same (the function application is left, and the set-comprehension variable is right). For <code>supr</code> it is the other way round</p>

#### [ Johan Commelin (Nov 13 2018 at 18:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/supr%20and%20range/near/147612160):
<p>Shouldn't <code>supr</code> be redefined to use <code>range</code> explicitly?</p>

#### [ Johannes Hölzl (Nov 13 2018 at 18:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/supr%20and%20range/near/147612244):
<p>Yes, <code>def supr (s : ι → α) : α := Sup (range s)</code></p>

#### [ Johan Commelin (Nov 13 2018 at 18:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/supr%20and%20range/near/147612351):
<p>Maybe then we should rename <code>infi</code> to <code>infr</code>, and then the <code>r</code> stands for <code>range</code> <span class="emoji emoji-1f643" title="upside down">:upside_down:</span> <span class="emoji emoji-1f648" title="see no evil">:see_no_evil:</span></p>

#### [ Sebastien Gouezel (Nov 14 2018 at 09:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/supr%20and%20range/near/147655093):
<blockquote>
<p>Yes, <code>def supr (s : ι → α) : α := Sup (range s)</code></p>
</blockquote>
<p>Done in #PR474. It was slightly more painful than I expected, as I had to fix the library all over the place...</p>


{% endraw %}
