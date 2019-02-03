---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/43084bounds.html
---

## Stream: [maths](https://leanprover-community.github.io/archive/116395maths/index.html)
### Topic: [bounds](https://leanprover-community.github.io/archive/116395maths/43084bounds.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kevin Buzzard (Nov 17 2018 at 12:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bounds/near/147874320):
<p>This is more of a funny story than anything else.</p>
<p>This week just gone at Imperial, we were looking at the real numbers and the completeness axiom in my class. Some of the students were involved in a (maths not Lean) project of constructing the real numbers as Dedekind cuts. The sheet started by defining totally ordered sets (the <code>linear_order</code> class in Lean) and the "least upper bound property" -- any non-empty bounded-above subset has a least upper bound. The sheet then remarked something I'd never realised -- there is no point defining also the "greatest lower bound property", because this follows from the least upper bound property. For the reals I had always imagined that this was proved by just considering <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mo>{</mo><mo>−</mo><mi>x</mi><mspace width="0.16667em"></mspace><mo>∣</mo><mspace width="0.16667em"></mspace><mi>x</mi><mo>∈</mo><mi>S</mi><mo>}</mo></mrow><annotation encoding="application/x-tex">\{-x\,\mid\,x\in S\}</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mopen">{</span><span class="mord">−</span><span class="mord mathit">x</span><span class="mrel"><span class="mspace thinspace"></span><span class="mrel">∣</span></span><span class="mord mathit"><span class="mspace thinspace"></span><span class="mord mathit">x</span></span><span class="mrel">∈</span><span class="mord mathit" style="margin-right:0.05764em;">S</span><span class="mclose">}</span></span></span></span> but actually there is a direct proof which only uses total orders. </p>
<div class="codehilite"><pre><span></span><span class="c1">-- from order/bounds.lean</span>

<span class="kn">variables</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">[</span><span class="n">preorder</span> <span class="n">α</span><span class="o">]</span>
<span class="n">def</span> <span class="n">upper_bounds</span> <span class="o">(</span><span class="n">s</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span> <span class="o">:=</span> <span class="o">{</span> <span class="n">x</span> <span class="bp">|</span> <span class="bp">∀</span><span class="n">a</span> <span class="err">∈</span> <span class="n">s</span><span class="o">,</span> <span class="n">a</span> <span class="bp">≤</span> <span class="n">x</span> <span class="o">}</span>
<span class="n">def</span> <span class="n">lower_bounds</span> <span class="o">(</span><span class="n">s</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span> <span class="o">:=</span> <span class="o">{</span> <span class="n">x</span> <span class="bp">|</span> <span class="bp">∀</span><span class="n">a</span> <span class="err">∈</span> <span class="n">s</span><span class="o">,</span> <span class="n">x</span> <span class="bp">≤</span> <span class="n">a</span> <span class="o">}</span>
<span class="n">def</span> <span class="n">is_least</span> <span class="o">(</span><span class="n">s</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="kt">Prop</span> <span class="o">:=</span> <span class="n">a</span> <span class="err">∈</span> <span class="n">s</span> <span class="bp">∧</span> <span class="n">a</span> <span class="err">∈</span> <span class="n">lower_bounds</span> <span class="n">s</span>
<span class="n">def</span> <span class="n">is_greatest</span> <span class="o">(</span><span class="n">s</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="kt">Prop</span> <span class="o">:=</span> <span class="n">a</span> <span class="err">∈</span> <span class="n">s</span> <span class="bp">∧</span> <span class="n">a</span> <span class="err">∈</span> <span class="n">upper_bounds</span> <span class="n">s</span>
<span class="n">def</span> <span class="n">is_lub</span> <span class="o">(</span><span class="n">s</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Prop</span> <span class="o">:=</span> <span class="n">is_least</span> <span class="o">(</span><span class="n">upper_bounds</span> <span class="n">s</span><span class="o">)</span>
<span class="n">def</span> <span class="n">is_glb</span> <span class="o">(</span><span class="n">s</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Prop</span> <span class="o">:=</span> <span class="n">is_greatest</span> <span class="o">(</span><span class="n">lower_bounds</span> <span class="n">s</span><span class="o">)</span>

<span class="kn">theorem</span> <span class="n">warm_up</span> <span class="o">(</span><span class="n">S</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">[</span><span class="n">linear_order</span> <span class="n">S</span><span class="o">]</span> <span class="o">:</span>
<span class="o">(</span><span class="bp">∀</span> <span class="n">E</span> <span class="o">:</span> <span class="n">set</span> <span class="n">S</span><span class="o">,</span> <span class="o">(</span><span class="bp">∃</span> <span class="n">a</span><span class="o">,</span> <span class="n">a</span> <span class="err">∈</span> <span class="n">E</span><span class="o">)</span> <span class="bp">∧</span> <span class="o">(</span><span class="bp">∃</span> <span class="n">b</span><span class="o">,</span> <span class="n">b</span> <span class="err">∈</span> <span class="n">upper_bounds</span> <span class="n">E</span><span class="o">)</span> <span class="bp">→</span> <span class="bp">∃</span> <span class="n">s</span> <span class="o">:</span> <span class="n">S</span><span class="o">,</span> <span class="n">is_lub</span> <span class="n">E</span> <span class="n">s</span><span class="o">)</span> <span class="bp">→</span>
<span class="o">(</span><span class="bp">∀</span> <span class="n">E</span> <span class="o">:</span> <span class="n">set</span> <span class="n">S</span><span class="o">,</span> <span class="o">(</span><span class="bp">∃</span> <span class="n">a</span><span class="o">,</span> <span class="n">a</span> <span class="err">∈</span> <span class="n">E</span><span class="o">)</span> <span class="bp">∧</span> <span class="o">(</span><span class="bp">∃</span> <span class="n">b</span><span class="o">,</span> <span class="n">b</span> <span class="err">∈</span> <span class="n">lower_bounds</span> <span class="n">E</span><span class="o">)</span> <span class="bp">→</span> <span class="bp">∃</span> <span class="n">s</span> <span class="o">:</span> <span class="n">S</span><span class="o">,</span> <span class="n">is_glb</span> <span class="n">E</span> <span class="n">s</span><span class="o">)</span> <span class="o">:=</span> <span class="n">sorry</span>
</pre></div>


<p>Of course the proof requires a mathematical idea -- knowing any non-empty bounded-above set has a sup, and given a non-empty bounded-below set, we need to produce an inf without this involution which we have on the reals.</p>

#### [ Kevin Buzzard (Nov 17 2018 at 12:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bounds/near/147874402):
<p>So I could see what the idea must be, and knocked up a tactic proof without too much trouble.</p>
<p>And then because the bounds definitions applied not just to <code>linear_order</code> but to <code>preorder</code>, Chris asked whether my proof also worked for partial orders or preorders. So the question became -- what do you actually need to assume about your order to prove this warm-up question? I'll post our conclusions later on today if nobody else fancies trying to figure this out :-)</p>

#### [ Kevin Buzzard (Nov 17 2018 at 12:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bounds/near/147874403):
<p>No spoilers Kenny/Chris, if you're reading :-)</p>

#### [ Johannes Hölzl (Nov 17 2018 at 12:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bounds/near/147875349):
<p>This is a standard construction at least for complete lattices, there often one defines the supremum or infimum and derives the other exterma. And these structures where the extrema only exists for non-empty bounded sets are called "conditionally complete lattices"</p>

#### [ Kevin Buzzard (Nov 17 2018 at 14:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bounds/near/147878523):
<p>Right. So the question is: you might well know already that if, in a lattice, all non-empty bounded-above sets have a sup, then all non-empty bounded-below sets have an inf. This is a pleasant exercise. The question is whether you can get away with less than a lattice.</p>

#### [ Mario Carneiro (Nov 17 2018 at 14:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bounds/near/147878636):
<p>if every set has a least upper bound, then it's already a lattice</p>

#### [ Kevin Buzzard (Nov 17 2018 at 14:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bounds/near/147878638):
<p>I am only demanding on my order that every non-empty bounded above set has a least upper bound.</p>

#### [ Mario Carneiro (Nov 17 2018 at 15:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bounds/near/147878687):
<p>then you get a conditionally complete lattice</p>

#### [ Kevin Buzzard (Nov 17 2018 at 15:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bounds/near/147878690):
<p>but I need enough from my order to be able to deduce from this that every non-empty bounded-below set has a greatest lower bound.</p>

#### [ Mario Carneiro (Nov 17 2018 at 15:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bounds/near/147878699):
<p>You might have to be careful about how you say bounded below, but the usual proof should go through</p>

#### [ Kevin Buzzard (Nov 17 2018 at 15:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bounds/near/147878709):
<p>I explain exactly what I mean by all of these terms in the original post</p>

#### [ Kevin Buzzard (Nov 17 2018 at 15:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bounds/near/147878711):
<p>The question is how much you can relax the typeclasses and still be able to fill in the sorry</p>

#### [ Kevin Buzzard (Nov 17 2018 at 15:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bounds/near/147878753):
<p>e.g. can you prove</p>
<div class="codehilite"><pre><span></span><span class="kn">variables</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">[</span><span class="n">preorder</span> <span class="n">α</span><span class="o">]</span>
<span class="n">def</span> <span class="n">upper_bounds</span> <span class="o">(</span><span class="n">s</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span> <span class="o">:=</span> <span class="o">{</span> <span class="n">x</span> <span class="bp">|</span> <span class="bp">∀</span><span class="n">a</span> <span class="err">∈</span> <span class="n">s</span><span class="o">,</span> <span class="n">a</span> <span class="bp">≤</span> <span class="n">x</span> <span class="o">}</span>
<span class="n">def</span> <span class="n">lower_bounds</span> <span class="o">(</span><span class="n">s</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span> <span class="o">:=</span> <span class="o">{</span> <span class="n">x</span> <span class="bp">|</span> <span class="bp">∀</span><span class="n">a</span> <span class="err">∈</span> <span class="n">s</span><span class="o">,</span> <span class="n">x</span> <span class="bp">≤</span> <span class="n">a</span> <span class="o">}</span>
<span class="n">def</span> <span class="n">is_least</span> <span class="o">(</span><span class="n">s</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="kt">Prop</span> <span class="o">:=</span> <span class="n">a</span> <span class="err">∈</span> <span class="n">s</span> <span class="bp">∧</span> <span class="n">a</span> <span class="err">∈</span> <span class="n">lower_bounds</span> <span class="n">s</span>
<span class="n">def</span> <span class="n">is_greatest</span> <span class="o">(</span><span class="n">s</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="kt">Prop</span> <span class="o">:=</span> <span class="n">a</span> <span class="err">∈</span> <span class="n">s</span> <span class="bp">∧</span> <span class="n">a</span> <span class="err">∈</span> <span class="n">upper_bounds</span> <span class="n">s</span>
<span class="n">def</span> <span class="n">is_lub</span> <span class="o">(</span><span class="n">s</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Prop</span> <span class="o">:=</span> <span class="n">is_least</span> <span class="o">(</span><span class="n">upper_bounds</span> <span class="n">s</span><span class="o">)</span>
<span class="n">def</span> <span class="n">is_glb</span> <span class="o">(</span><span class="n">s</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Prop</span> <span class="o">:=</span> <span class="n">is_greatest</span> <span class="o">(</span><span class="n">lower_bounds</span> <span class="n">s</span><span class="o">)</span>

<span class="kn">theorem</span> <span class="n">warm_up</span> <span class="o">(</span><span class="n">S</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">[</span><span class="n">preorder</span> <span class="n">S</span><span class="o">]</span> <span class="o">:</span>
<span class="o">(</span><span class="bp">∀</span> <span class="n">E</span> <span class="o">:</span> <span class="n">set</span> <span class="n">S</span><span class="o">,</span> <span class="o">(</span><span class="bp">∃</span> <span class="n">a</span><span class="o">,</span> <span class="n">a</span> <span class="err">∈</span> <span class="n">E</span><span class="o">)</span> <span class="bp">∧</span> <span class="o">(</span><span class="bp">∃</span> <span class="n">b</span><span class="o">,</span> <span class="n">b</span> <span class="err">∈</span> <span class="n">upper_bounds</span> <span class="n">E</span><span class="o">)</span> <span class="bp">→</span> <span class="bp">∃</span> <span class="n">s</span> <span class="o">:</span> <span class="n">S</span><span class="o">,</span> <span class="n">is_lub</span> <span class="n">E</span> <span class="n">s</span><span class="o">)</span> <span class="bp">→</span>
<span class="o">(</span><span class="bp">∀</span> <span class="n">E</span> <span class="o">:</span> <span class="n">set</span> <span class="n">S</span><span class="o">,</span> <span class="o">(</span><span class="bp">∃</span> <span class="n">a</span><span class="o">,</span> <span class="n">a</span> <span class="err">∈</span> <span class="n">E</span><span class="o">)</span> <span class="bp">∧</span> <span class="o">(</span><span class="bp">∃</span> <span class="n">b</span><span class="o">,</span> <span class="n">b</span> <span class="err">∈</span> <span class="n">lower_bounds</span> <span class="n">E</span><span class="o">)</span> <span class="bp">→</span> <span class="bp">∃</span> <span class="n">s</span> <span class="o">:</span> <span class="n">S</span><span class="o">,</span> <span class="n">is_glb</span> <span class="n">E</span> <span class="n">s</span><span class="o">)</span> <span class="o">:=</span> <span class="n">sorry</span>
</pre></div>

#### [ Mario Carneiro (Nov 17 2018 at 15:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bounds/near/147878808):
<p>I think so</p>

#### [ Kevin Buzzard (Nov 17 2018 at 15:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bounds/near/147878810):
<p>so now begin dropping the axioms of a preorder</p>

#### [ Kevin Buzzard (Nov 17 2018 at 15:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bounds/near/147878818):
<p>and how far can you get?</p>

#### [ Mario Carneiro (Nov 17 2018 at 15:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bounds/near/147878822):
<p>if you take <code>E := lower_bounds E</code> then it's nonempty, and an element of <code>E</code> is an upper bound for <code>lower_bounds E</code></p>

#### [ Kevin Buzzard (Nov 17 2018 at 15:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bounds/near/147878825):
<p>right. And which axioms for a preorder do you use in this proof?</p>

#### [ Mario Carneiro (Nov 17 2018 at 15:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bounds/near/147878866):
<p>if <code>a in E</code> and <code>b in lower_bounds E</code> then <code>b &lt;= a</code> so <code>a</code> is an upper bound of <code>lower_bounds E</code></p>

#### [ Mario Carneiro (Nov 17 2018 at 15:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bounds/near/147878867):
<p>it uses nothing</p>

#### [ Kevin Buzzard (Nov 17 2018 at 15:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bounds/near/147878872):
<div class="codehilite"><pre><span></span><span class="kn">variables</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">[</span><span class="n">has_le</span> <span class="n">α</span><span class="o">]</span>
<span class="n">def</span> <span class="n">upper_bounds</span> <span class="o">(</span><span class="n">s</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span> <span class="o">:=</span> <span class="o">{</span> <span class="n">x</span> <span class="bp">|</span> <span class="bp">∀</span><span class="n">a</span> <span class="err">∈</span> <span class="n">s</span><span class="o">,</span> <span class="n">a</span> <span class="bp">≤</span> <span class="n">x</span> <span class="o">}</span>
<span class="n">def</span> <span class="n">lower_bounds</span> <span class="o">(</span><span class="n">s</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span> <span class="o">:=</span> <span class="o">{</span> <span class="n">x</span> <span class="bp">|</span> <span class="bp">∀</span><span class="n">a</span> <span class="err">∈</span> <span class="n">s</span><span class="o">,</span> <span class="n">x</span> <span class="bp">≤</span> <span class="n">a</span> <span class="o">}</span>
<span class="n">def</span> <span class="n">is_least</span> <span class="o">(</span><span class="n">s</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="kt">Prop</span> <span class="o">:=</span> <span class="n">a</span> <span class="err">∈</span> <span class="n">s</span> <span class="bp">∧</span> <span class="n">a</span> <span class="err">∈</span> <span class="n">lower_bounds</span> <span class="n">s</span>
<span class="n">def</span> <span class="n">is_greatest</span> <span class="o">(</span><span class="n">s</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="kt">Prop</span> <span class="o">:=</span> <span class="n">a</span> <span class="err">∈</span> <span class="n">s</span> <span class="bp">∧</span> <span class="n">a</span> <span class="err">∈</span> <span class="n">upper_bounds</span> <span class="n">s</span>
<span class="n">def</span> <span class="n">is_lub</span> <span class="o">(</span><span class="n">s</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Prop</span> <span class="o">:=</span> <span class="n">is_least</span> <span class="o">(</span><span class="n">upper_bounds</span> <span class="n">s</span><span class="o">)</span>
<span class="n">def</span> <span class="n">is_glb</span> <span class="o">(</span><span class="n">s</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="kt">Prop</span> <span class="o">:=</span> <span class="n">is_greatest</span> <span class="o">(</span><span class="n">lower_bounds</span> <span class="n">s</span><span class="o">)</span>

<span class="kn">theorem</span> <span class="n">warm_up</span> <span class="o">(</span><span class="n">S</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">[</span><span class="n">has_le</span> <span class="n">S</span><span class="o">]</span> <span class="o">:</span>
<span class="o">(</span><span class="bp">∀</span> <span class="n">E</span> <span class="o">:</span> <span class="n">set</span> <span class="n">S</span><span class="o">,</span> <span class="o">(</span><span class="bp">∃</span> <span class="n">a</span><span class="o">,</span> <span class="n">a</span> <span class="err">∈</span> <span class="n">E</span><span class="o">)</span> <span class="bp">∧</span> <span class="o">(</span><span class="bp">∃</span> <span class="n">b</span><span class="o">,</span> <span class="n">b</span> <span class="err">∈</span> <span class="n">upper_bounds</span> <span class="n">E</span><span class="o">)</span> <span class="bp">→</span> <span class="bp">∃</span> <span class="n">s</span> <span class="o">:</span> <span class="n">S</span><span class="o">,</span> <span class="n">is_lub</span> <span class="n">E</span> <span class="n">s</span><span class="o">)</span> <span class="bp">→</span>
<span class="o">(</span><span class="bp">∀</span> <span class="n">E</span> <span class="o">:</span> <span class="n">set</span> <span class="n">S</span><span class="o">,</span> <span class="o">(</span><span class="bp">∃</span> <span class="n">a</span><span class="o">,</span> <span class="n">a</span> <span class="err">∈</span> <span class="n">E</span><span class="o">)</span> <span class="bp">∧</span> <span class="o">(</span><span class="bp">∃</span> <span class="n">b</span><span class="o">,</span> <span class="n">b</span> <span class="err">∈</span> <span class="n">lower_bounds</span> <span class="n">E</span><span class="o">)</span> <span class="bp">→</span> <span class="bp">∃</span> <span class="n">s</span> <span class="o">:</span> <span class="n">S</span><span class="o">,</span> <span class="n">is_glb</span> <span class="n">E</span> <span class="n">s</span><span class="o">)</span> <span class="o">:=</span>
<span class="bp">λ</span> <span class="n">H</span> <span class="n">E</span> <span class="bp">⟨⟨</span><span class="n">a</span><span class="o">,</span> <span class="n">haE</span><span class="bp">⟩</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">b</span><span class="o">,</span> <span class="n">hbuE</span><span class="bp">⟩⟩</span><span class="o">,</span>
<span class="k">let</span> <span class="bp">⟨</span><span class="n">s</span><span class="o">,</span> <span class="n">hs1</span><span class="o">,</span> <span class="n">hs2</span><span class="bp">⟩</span> <span class="o">:=</span> <span class="n">H</span> <span class="o">(</span><span class="n">lower_bounds</span> <span class="n">E</span><span class="o">)</span> <span class="bp">⟨⟨</span><span class="n">b</span><span class="o">,</span> <span class="n">hbuE</span><span class="bp">⟩</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">a</span><span class="o">,</span> <span class="bp">λ</span> <span class="n">s</span> <span class="n">hs</span><span class="o">,</span> <span class="n">hs</span> <span class="n">a</span> <span class="n">haE</span><span class="bp">⟩⟩</span> <span class="k">in</span>
<span class="bp">⟨</span><span class="n">s</span><span class="o">,</span> <span class="bp">λ</span> <span class="n">t</span> <span class="n">htE</span><span class="o">,</span> <span class="n">hs2</span> <span class="n">t</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">z</span> <span class="n">hzLE</span><span class="o">,</span> <span class="n">hzLE</span> <span class="n">t</span> <span class="n">htE</span><span class="o">),</span> <span class="n">hs1</span><span class="bp">⟩</span>
</pre></div>

#### [ Kevin Buzzard (Nov 17 2018 at 15:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bounds/near/147878874):
<p>punchline achieved</p>

#### [ Mario Carneiro (Nov 17 2018 at 15:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bounds/near/147878877):
<p>it could be any relation</p>

#### [ Kevin Buzzard (Nov 17 2018 at 15:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bounds/near/147878878):
<p>This made me wonder why preorder was assumed in bounds.lean</p>

#### [ Mario Carneiro (Nov 17 2018 at 15:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bounds/near/147878922):
<p>because preorder is our weakest "lawful" order class</p>

#### [ Kevin Buzzard (Nov 17 2018 at 15:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bounds/near/147878923):
<p>surely has_le is weaker?</p>

#### [ Kevin Buzzard (Nov 17 2018 at 15:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bounds/near/147878925):
<p>It's surely an order class</p>

#### [ Kevin Buzzard (Nov 17 2018 at 15:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bounds/near/147878926):
<p>because of the notation</p>

#### [ Kevin Buzzard (Nov 17 2018 at 15:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bounds/near/147878938):
<p>you yourself know that has_add and has_mul are two completely different classes</p>

#### [ Kevin Buzzard (Nov 17 2018 at 15:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bounds/near/147878939):
<p>that's why you had to define groups twice</p>

#### [ Mario Carneiro (Nov 17 2018 at 15:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bounds/near/147878994):
<p>if it's not a preorder, you probably shouldn't be using <code>&lt;=</code></p>

#### [ Mario Carneiro (Nov 17 2018 at 15:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bounds/near/147879007):
<p>plus all the terminology there doesn't really make sense without some transitivity</p>

#### [ Kevin Buzzard (Nov 17 2018 at 15:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bounds/near/147879514):
<p>I am surprised that this is your attitude. I think the notation implies a "way of thinking" about the structure, but why can't I define the "upper bounds" of a set with has_le to be the obvious things? I thought that this was the mathlib philosophy -- you define things in the max generality that they parse, and for these definitions like upper_bounds we need nothing more than the predicate.</p>

#### [ Kevin Buzzard (Nov 17 2018 at 15:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bounds/near/147879519):
<p>Octonians aren't associative, and yet people still use <code>*</code> to multiply them</p>

#### [ Mario Carneiro (Nov 17 2018 at 15:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bounds/near/147879616):
<p>octonions aren't completely lawless though</p>

#### [ Mario Carneiro (Nov 17 2018 at 15:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bounds/near/147879619):
<p>If we cared about them we would define loops or power-associative monoids or whatever</p>

#### [ Mario Carneiro (Nov 17 2018 at 15:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bounds/near/147879676):
<p>I think it helps to be at least a little application-driven here. If it's only ever used on preorders then why the suprious generalization?</p>

#### [ Mario Carneiro (Nov 17 2018 at 15:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bounds/near/147879678):
<p>note also that typeclass inference is a bit longer for lower classes, although this is probably a small effect</p>

#### [ Mario Carneiro (Nov 17 2018 at 15:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bounds/near/147879731):
<p>I would recommend using pure notation classes only in lawless situations like <code>meta</code> programming</p>

#### [ Kevin Buzzard (Nov 17 2018 at 15:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bounds/near/147880123):
<p>Oh that's an interesting comment. So there is a place for the has_lt typeclass beyond just a notational trick?</p>

#### [ Kevin Buzzard (Nov 17 2018 at 15:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/bounds/near/147880125):
<p>It's just in lawless metaland :-)</p>


{% endraw %}
