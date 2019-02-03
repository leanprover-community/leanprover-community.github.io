---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/16752Howtoparsethisexample.html
---

## Stream: [maths](https://leanprover-community.github.io/archive/116395maths/index.html)
### Topic: [How to parse this example?](https://leanprover-community.github.io/archive/116395maths/16752Howtoparsethisexample.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ None proffered (Aug 07 2018 at 20:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/How%20to%20parse%20this%20example%3F/near/131060242):
<p>How to parse this example?</p>

#### [ None proffered (Aug 07 2018 at 20:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/How%20to%20parse%20this%20example%3F/near/131060265):
<p>example : (∃ x, p x → r) ↔ (∀ x, p x) → r</p>

#### [ None proffered (Aug 07 2018 at 20:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/How%20to%20parse%20this%20example%3F/near/131060288):
<p>(deleted)</p>

#### [ None proffered (Aug 07 2018 at 20:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/How%20to%20parse%20this%20example%3F/near/131060615):
<p>Is it (1) [(∃ x, p x → r)] ↔[ (∀ x, p x) → r] for CCCC CCCC TNTN TTTT in M8/VL4; or <br>
Is it (2)  [(∃ x, p x → r) ↔ (∀ x, p x)] → r for CCCC TTTT TNTN TTTT in M8/VL4.<br>
In either case, Eqs. 1 or 2 are not tautologous (all designated proof value of T).</p>

#### [ Kevin Buzzard (Aug 07 2018 at 22:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/How%20to%20parse%20this%20example%3F/near/131067561):
<div class="codehilite"><pre><span></span><span class="kn">variables</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">(</span><span class="n">p</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">)</span> <span class="o">(</span><span class="n">r</span> <span class="o">:</span> <span class="kt">Prop</span><span class="o">)</span>
<span class="kn">example</span> <span class="o">:</span> <span class="o">(</span> <span class="o">(</span><span class="bp">∃</span> <span class="n">x</span><span class="o">,</span> <span class="n">p</span> <span class="n">x</span> <span class="bp">→</span> <span class="n">r</span><span class="o">)</span> <span class="bp">↔</span> <span class="o">(</span><span class="bp">∀</span> <span class="n">x</span><span class="o">,</span> <span class="n">p</span> <span class="n">x</span><span class="o">)</span> <span class="bp">→</span> <span class="n">r</span> <span class="o">)</span> <span class="bp">=</span> <span class="o">(</span> <span class="o">(</span><span class="bp">∃</span> <span class="n">x</span><span class="o">,</span> <span class="n">p</span> <span class="n">x</span> <span class="bp">→</span> <span class="n">r</span><span class="o">)</span> <span class="bp">↔</span> <span class="o">(</span> <span class="o">(</span><span class="bp">∀</span> <span class="n">x</span><span class="o">,</span> <span class="n">p</span> <span class="n">x</span><span class="o">)</span> <span class="bp">→</span> <span class="n">r</span> <span class="o">)</span> <span class="o">)</span> <span class="o">:=</span> <span class="n">rfl</span>
</pre></div>


<p>Apparently it's the former: (1).</p>

#### [ Mario Carneiro (Aug 08 2018 at 02:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/How%20to%20parse%20this%20example%3F/near/131078022):
<p><span class="user-mention" data-user-id="125128">@None proffered</span> the parse is (1) as Kevin says. I don't know what "CCCC CCCC TNTN TTTT" means; what is M8/VL4? This theorem is not true when the domain of <code>x</code> is empty. I assume you got this example from <code>tests/finish3.lean</code>, which proves two versions of this:</p>
<div class="codehilite"><pre><span></span><span class="kn">variables</span> <span class="o">(</span><span class="n">A</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">(</span><span class="n">p</span> <span class="o">:</span> <span class="n">A</span> <span class="bp">→</span> <span class="kt">Prop</span><span class="o">)</span> <span class="o">(</span><span class="n">r</span> <span class="o">:</span> <span class="kt">Prop</span><span class="o">)</span>
<span class="kn">example</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">A</span><span class="o">)</span> <span class="o">:</span> <span class="o">(</span><span class="bp">∃</span> <span class="n">x</span><span class="o">,</span> <span class="n">p</span> <span class="n">x</span> <span class="bp">→</span> <span class="n">r</span><span class="o">)</span> <span class="bp">↔</span> <span class="o">(</span><span class="bp">∀</span> <span class="n">x</span><span class="o">,</span> <span class="n">p</span> <span class="n">x</span><span class="o">)</span> <span class="bp">→</span> <span class="n">r</span> <span class="o">:=</span> <span class="k">begin</span> <span class="n">safe</span> <span class="o">[</span><span class="n">iff_def</span><span class="o">]</span><span class="bp">;</span> <span class="n">exact</span> <span class="n">h</span> <span class="n">a</span> <span class="kn">end</span>
<span class="kn">example</span> <span class="o">:</span> <span class="o">(</span><span class="bp">∃</span> <span class="n">x</span><span class="o">,</span> <span class="n">p</span> <span class="n">x</span> <span class="bp">→</span> <span class="n">r</span><span class="o">)</span> <span class="bp">→</span> <span class="o">(</span><span class="bp">∀</span> <span class="n">x</span><span class="o">,</span> <span class="n">p</span> <span class="n">x</span><span class="o">)</span> <span class="bp">→</span> <span class="n">r</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">finish</span>
</pre></div>


<p>So it is provable in one direction unconditionally, but the bidirectional version requires some <code>a : A</code>, i.e. <code>A</code> has to be nonempty.</p>


{% endraw %}
