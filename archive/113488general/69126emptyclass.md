---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/69126emptyclass.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [empty class](https://leanprover-community.github.io/archive/113488general/69126emptyclass.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Reid Barton (Apr 24 2018 at 03:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/empty%20class/near/125597374):
<p>What's the right way to declare an empty class (i.e., one with no fields) and an instance of it? I found that this works:</p>
<div class="codehilite"><pre><span></span><span class="n">class</span> <span class="n">C</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span>
<span class="kn">instance</span> <span class="o">:</span> <span class="n">C</span> <span class="n">unit</span> <span class="o">:=</span> <span class="n">C</span><span class="bp">.</span><span class="n">mk</span> <span class="n">unit</span>
</pre></div>


<p>but it seems oddly non-uniform that <code>C.mk</code> takes an explicit argument, and I'd prefer not to repeat it. I guess I could define</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">mkC</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">}</span> <span class="o">:=</span> <span class="n">C</span><span class="bp">.</span><span class="n">mk</span> <span class="n">α</span>
</pre></div>


<p>but I figured I'd ask here</p>

#### [ Simon Hudon (Apr 24 2018 at 03:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/empty%20class/near/125597567):
<p>Try</p>
<div class="codehilite"><pre><span></span>class C (α : Type) :=
 mk {} ::
instance : C unit := C.mk
</pre></div>

#### [ Reid Barton (Apr 24 2018 at 03:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/empty%20class/near/125597691):
<p>That worked, thanks. Also the <code>::</code> isn't needed.</p>

#### [ Reid Barton (Apr 24 2018 at 03:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/empty%20class/near/125597697):
<p>(But I also don't know what it does, so maybe I am missing something?)</p>

#### [ Simon Hudon (Apr 24 2018 at 03:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/empty%20class/near/125597725):
<p>Thanks for the tip!</p>

#### [ Simon Hudon (Apr 24 2018 at 03:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/empty%20class/near/125597771):
<p>It's just a degenerate case of a notation for structure definition that allows you to pick a different name than <code>mk</code> for the constructor:</p>
<div class="codehilite"><pre><span></span><span class="kn">structure</span> <span class="n">foo</span> <span class="o">:=</span>
  <span class="n">my_cons</span> <span class="bp">::</span>
    <span class="o">(</span><span class="n">field1</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span>
    <span class="o">(</span><span class="n">field2</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span>
</pre></div>


{% endraw %}
