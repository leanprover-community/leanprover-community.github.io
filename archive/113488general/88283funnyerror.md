---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/88283funnyerror.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [funny error](https://leanprover-community.github.io/archive/113488general/88283funnyerror.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kenny Lau (May 31 2018 at 05:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/funny%20error/near/127342120):
<p>I could not minimize this error.</p>

#### [ Kenny Lau (May 31 2018 at 05:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/funny%20error/near/127342121):
<p><a href="https://gist.github.com/kckennylau/a62295136d2daf48146f6fcdb8e37a49" target="_blank" title="https://gist.github.com/kckennylau/a62295136d2daf48146f6fcdb8e37a49">https://gist.github.com/kckennylau/a62295136d2daf48146f6fcdb8e37a49</a></p>

#### [ Kenny Lau (May 31 2018 at 05:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/funny%20error/near/127342122):
<p>error:</p>

#### [ Kenny Lau (May 31 2018 at 05:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/funny%20error/near/127342123):
<div class="codehilite"><pre><span></span><span class="n">type</span> <span class="n">mismatch</span> <span class="n">at</span> <span class="n">field</span> <span class="err">&#39;</span><span class="n">right_inv&#39;</span>
  <span class="err">?</span><span class="n">m_1</span>
<span class="n">has</span> <span class="n">type</span>
  <span class="n">function</span><span class="bp">.</span><span class="n">right_inverse</span> <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">φ</span> <span class="o">:</span> <span class="n">alg_hom</span> <span class="o">(</span><span class="n">polynomial</span> <span class="n">R</span><span class="o">)</span> <span class="n">A</span><span class="o">),</span> <span class="n">φ</span><span class="bp">.</span><span class="n">val</span> <span class="o">(</span><span class="n">finsupp</span><span class="bp">.</span><span class="n">single</span> <span class="mi">1</span> <span class="mi">1</span><span class="o">))</span>
    <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">r</span> <span class="o">:</span> <span class="n">A</span><span class="o">),</span>
       <span class="bp">⟨λ</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">polynomial</span> <span class="n">R</span><span class="o">),</span>
          <span class="n">finsupp</span><span class="bp">.</span><span class="n">sum</span> <span class="n">f</span> <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">c</span> <span class="o">:</span> <span class="n">R</span><span class="o">),</span> <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">r</span> <span class="o">:</span> <span class="n">R</span><span class="o">)</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">A</span><span class="o">),</span> <span class="n">algebra</span><span class="bp">.</span><span class="n">f</span> <span class="n">A</span> <span class="n">r</span> <span class="bp">*</span> <span class="n">x</span><span class="o">)</span> <span class="n">c</span> <span class="o">(</span><span class="n">monoid</span><span class="bp">.</span><span class="n">pow</span> <span class="n">r</span> <span class="n">n</span><span class="o">)),</span>
        <span class="bp">_⟩</span><span class="o">)</span>
<span class="n">but</span> <span class="n">is</span> <span class="n">expected</span> <span class="n">to</span> <span class="k">have</span> <span class="n">type</span>
  <span class="n">function</span><span class="bp">.</span><span class="n">right_inverse</span> <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">φ</span> <span class="o">:</span> <span class="n">alg_hom</span> <span class="o">(</span><span class="n">polynomial</span> <span class="n">R</span><span class="o">)</span> <span class="n">A</span><span class="o">),</span> <span class="n">φ</span><span class="bp">.</span><span class="n">val</span> <span class="o">(</span><span class="n">finsupp</span><span class="bp">.</span><span class="n">single</span> <span class="mi">1</span> <span class="mi">1</span><span class="o">))</span>
    <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">r</span> <span class="o">:</span> <span class="n">A</span><span class="o">),</span> <span class="bp">⟨λ</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">polynomial</span> <span class="n">R</span><span class="o">),</span> <span class="n">finsupp</span><span class="bp">.</span><span class="n">sum</span> <span class="n">f</span> <span class="o">(</span><span class="bp">λ</span> <span class="o">(</span><span class="n">n</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">c</span> <span class="o">:</span> <span class="n">R</span><span class="o">),</span> <span class="n">c</span> <span class="err">•</span> <span class="n">r</span> <span class="err">^</span> <span class="n">n</span><span class="o">),</span> <span class="bp">_⟩</span><span class="o">)</span>
</pre></div>

#### [ Kenny Lau (May 31 2018 at 05:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/funny%20error/near/127342164):
<p>where <code>?m_1</code> was a literal underscore</p>

#### [ Kenny Lau (May 31 2018 at 05:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/funny%20error/near/127342165):
<p>that's it folks, an underscore has a type error</p>

#### [ Kenny Lau (May 31 2018 at 05:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/funny%20error/near/127342171):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span></p>

#### [ Kevin Buzzard (May 31 2018 at 06:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/funny%20error/near/127344095):
<p>I think we've seen this happen before</p>

#### [ Kevin Buzzard (May 31 2018 at 06:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/funny%20error/near/127344099):
<p>were you making a big structure and doing crazy stuff like sorrying out constants?</p>

#### [ Kevin Buzzard (May 31 2018 at 06:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/funny%20error/near/127344193):
<p>I find these sorts of things a bit annoying to do for reasons like this</p>


{% endraw %}
