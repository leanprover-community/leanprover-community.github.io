---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/53771natpowandring.html
---

## Stream: [maths](index.html)
### Topic: [nat.pow and ring](53771natpowandring.html)

---


{% raw %}
#### [ Kevin Buzzard (Jun 09 2018 at 03:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat.pow%20and%20ring/near/127802027):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">ring</span>

<span class="kn">example</span> <span class="o">(</span><span class="n">d</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="n">d</span> <span class="err">^</span> <span class="mi">2</span> <span class="bp">+</span> <span class="o">(</span><span class="mi">2</span> <span class="bp">*</span> <span class="n">d</span> <span class="bp">+</span> <span class="mi">1</span><span class="o">)</span> <span class="bp">=</span> <span class="o">(</span><span class="n">d</span> <span class="bp">+</span> <span class="mi">1</span><span class="o">)</span> <span class="err">^</span> <span class="mi">2</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">unfold</span> <span class="n">has_pow</span><span class="bp">.</span><span class="n">pow</span> <span class="n">monoid</span><span class="bp">.</span><span class="n">pow</span> <span class="n">nat</span><span class="bp">.</span><span class="n">pow</span><span class="o">,</span>
  <span class="n">ring</span>
<span class="kn">end</span>
</pre></div>

#### [ Kevin Buzzard (Jun 09 2018 at 03:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat.pow%20and%20ring/near/127802028):
<p>Could I have done that in one line with <code>ring</code>? [using some options or something]</p>

#### [ Andrew Ashworth (Jun 09 2018 at 03:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat.pow%20and%20ring/near/127802751):
<p>[deleted - incorrect information]</p>

#### [ Kevin Buzzard (Jun 09 2018 at 03:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat.pow%20and%20ring/near/127802943):
<p>So I could make an even cooler ring tactic by writing a tactic which tries to do those unfolds and then applies ring?</p>

#### [ Kevin Buzzard (Jun 09 2018 at 03:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat.pow%20and%20ring/near/127802946):
<p>Is life that easy?</p>

#### [ Andrew Ashworth (Jun 09 2018 at 03:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat.pow%20and%20ring/near/127803089):
<p>[deleted - incorrect information]</p>

#### [ Andrew Ashworth (Jun 09 2018 at 03:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat.pow%20and%20ring/near/127803099):
<p>[deleted - incorrect information]</p>

#### [ Mario Carneiro (Jun 09 2018 at 07:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat.pow%20and%20ring/near/127808199):
<p>ring should handle powers... it automatically handles ring like operations that make sense as polynomial expressions, although it can't handle x^n for nonconstant n</p>

#### [ Mario Carneiro (Jun 09 2018 at 07:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat.pow%20and%20ring/near/127808250):
<p>in particular it has optimizations for sparse polynomials like x^100 + x, which requires interpreting ^</p>

#### [ Andrew Ashworth (Jun 09 2018 at 08:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat.pow%20and%20ring/near/127809868):
<p>that's pretty sweet! I didn't expect that you'd put that much effort into the tactic. thanks for writing it!</p>

#### [ Kevin Buzzard (Jun 09 2018 at 12:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat.pow%20and%20ring/near/127816599):
<p>Yes thanks very much indeed for writing it. It is an essential part of the "mathematician's interface" to Lean. Writing it was I'm sure nontrivial but at the end of the day, as I know I've said before, if a mathematician can't prove things like the example above with one or two lines then they will never take to Lean.</p>

#### [ Kevin Buzzard (Jun 09 2018 at 12:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat.pow%20and%20ring/near/127816655):
<p>Just to be clear -- in the example above <code>ring</code> falls without the initial unfolding</p>

#### [ Patrick Massot (Jun 09 2018 at 12:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat.pow%20and%20ring/near/127816664):
<p>The <code>ring</code> tactic is already very useful but it has bugs</p>

#### [ Johan Commelin (Jun 09 2018 at 16:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/nat.pow%20and%20ring/near/127822932):
<p>How hard would it be to state a theorem about the <code>ring</code> tactic, and prove that the implementation is compliant? Then we are sure we won't have bugs. But I guess that the <code>meta</code> stuff makes this complicated.</p>


{% endraw %}
