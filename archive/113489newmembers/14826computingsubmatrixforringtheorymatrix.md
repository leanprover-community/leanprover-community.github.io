---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/14826computingsubmatrixforringtheorymatrix.html
---

## Stream: [new members](index.html)
### Topic: [computing submatrix for ring_theory.matrix](14826computingsubmatrixforringtheorymatrix.html)

---


{% raw %}
#### [ Tobias Grosser (Sep 29 2018 at 23:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134897036):
<p>On another lean saturday afternoon, I continued looked forther into formalizing another basic lean maths. This time I want to compute sub-matrixes for ring_theory.matrix.</p>
<p>This is what I came up with:</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">rsubmx</span> <span class="o">{</span><span class="n">m</span> <span class="n">n_left</span> <span class="n">n_right</span><span class="o">:</span> <span class="n">nat</span><span class="o">}</span> <span class="o">:</span>
<span class="bp">Π</span> <span class="o">(</span><span class="n">m</span> <span class="n">n_left</span> <span class="n">n_right</span><span class="o">),</span>
<span class="n">matrix</span> <span class="o">(</span><span class="n">fin</span> <span class="n">m</span><span class="o">)</span> <span class="o">(</span><span class="n">fin</span> <span class="o">(</span><span class="n">n_right</span> <span class="bp">+</span> <span class="n">n_left</span><span class="o">))</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">matrix</span> <span class="o">(</span><span class="n">fin</span> <span class="n">m</span><span class="o">)</span> <span class="o">(</span><span class="n">fin</span> <span class="o">(</span><span class="n">n_right</span><span class="o">))</span> <span class="n">α</span>
<span class="bp">|</span> <span class="n">x</span> <span class="n">y_l</span> <span class="n">y_r</span> <span class="n">A</span> <span class="o">:=</span>
  <span class="bp">λ</span> <span class="n">i</span> <span class="n">j</span><span class="o">,</span>
  <span class="k">let</span> <span class="o">(</span><span class="n">offset</span> <span class="o">:</span> <span class="n">fin</span> <span class="o">(</span><span class="n">y_r</span> <span class="bp">+</span> <span class="n">y_l</span><span class="o">))</span> <span class="o">:=</span> <span class="o">(</span><span class="n">fin</span><span class="bp">.</span><span class="n">add_nat</span> <span class="n">j</span> <span class="n">y_l</span><span class="o">)</span> <span class="k">in</span>
  <span class="n">A</span> <span class="n">i</span> <span class="n">offset</span>
</pre></div>


<p>It compiles without flaws, but looks very messy. Two things I feel should still be changed are:<br>
1) It would be nice if the function would not require m, n_right, n_left to be passed explicitly, but would instead automatically derive the relevant offsets.<br>
2) I keep getting type errors due to a fin(x + y) being not equal to fin(y + x) when using it. It would be great if one could automatically convert between the two.</p>

#### [ Tobias Grosser (Sep 29 2018 at 23:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134897038):
<p>Feedback very much appreciated.</p>

#### [ Kevin Buzzard (Sep 29 2018 at 23:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134897446):
<p>I think that I would have been tempted to move away from just adding an offset and would instead consider any increasing maps <code>fin m' -&gt; fin m</code> and <code>fin n' -&gt; fin n</code>. Isn't that what people usually look at -- all the m' x n' minors or something?</p>

#### [ Tobias Grosser (Sep 30 2018 at 00:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134898201):
<p>I am not sure I understand what interface you have in mind.</p>

#### [ Bryan Gin-ge Chen (Sep 30 2018 at 00:24)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134898247):
<p>For example, suppose I have a 5x5 matrix and want to extract the 3x3 matrix consisting of rows 1,2,4 and columns 1,3,4.</p>

#### [ Tobias Grosser (Sep 30 2018 at 00:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134898256):
<p>Right.</p>

#### [ Tobias Grosser (Sep 30 2018 at 00:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134898258):
<p>I mean, it makes sense to have a more generic interface that computes a minor.</p>

#### [ Tobias Grosser (Sep 30 2018 at 00:26)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134898297):
<p>Such a functionality could even be the basis for this function, I assume.</p>

#### [ Tobias Grosser (Sep 30 2018 at 00:29)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134898355):
<p>Still, I feel that it would not completely replace this function as the interface for the special case I propose could be simpler, as it could just derive the sizes from the types.</p>

#### [ Tobias Grosser (Sep 30 2018 at 00:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134898446):
<p>More from a practical perspective, I am not sure how a general minorification interface should look like. Would I ask for two more parameters fin m -&gt; Prop and fin n -&gt; Prop, which evaluate to true if the specific column should be included?</p>

#### [ Tobias Grosser (Sep 30 2018 at 00:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134898452):
<p>Computing the necessary offsets seems a little involved. Not sure how this will effect performance.</p>

#### [ Bryan Gin-ge Chen (Sep 30 2018 at 00:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134898699):
<p>I think the interface Kevin suggests is the following: to specify a general <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msup><mi>m</mi><mo mathvariant="normal">′</mo></msup><mo>×</mo><msup><mi>n</mi><mo mathvariant="normal">′</mo></msup></mrow><annotation encoding="application/x-tex">m' \times n'</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.751892em;"></span><span class="strut bottom" style="height:0.835222em;vertical-align:-0.08333em;"></span><span class="base"><span class="mord"><span class="mord mathit">m</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.751892em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathrm mtight">′</span></span></span></span></span></span></span></span></span><span class="mbin">×</span><span class="mord"><span class="mord mathit">n</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.751892em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mtight"><span class="mord mathrm mtight">′</span></span></span></span></span></span></span></span></span></span></span></span> submatrix of an <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>m</mi><mo>×</mo><mi>n</mi></mrow><annotation encoding="application/x-tex">m \times n</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.58333em;"></span><span class="strut bottom" style="height:0.66666em;vertical-align:-0.08333em;"></span><span class="base"><span class="mord mathit">m</span><span class="mbin">×</span><span class="mord mathit">n</span></span></span></span> matrix, it is sufficient to provide two increasing maps, one of type <code>fin m' → fin m</code> and one of type <code>fin n' → fin n</code>. No need to compute any offsets, so far as I can tell; simply pull out the specified matrix entries using the two maps to grab the row and column indices.</p>

#### [ Kevin Buzzard (Sep 30 2018 at 01:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134899303):
<p>And then the function you've already implemented could be a special case of this.</p>

#### [ Tobias Grosser (Sep 30 2018 at 08:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134910891):
<p>Right.</p>

#### [ Tobias Grosser (Sep 30 2018 at 08:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134910897):
<p>Here what I came up with:</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">ring_theory</span><span class="bp">.</span><span class="n">matrix</span>

<span class="kn">variables</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">}</span>
<span class="kn">variables</span> <span class="o">{</span><span class="n">m</span> <span class="n">n</span> <span class="n">m&#39;</span> <span class="n">n&#39;</span><span class="o">:</span> <span class="kt">Type</span><span class="o">}</span> <span class="o">[</span><span class="n">fintype</span> <span class="n">m</span><span class="o">]</span> <span class="o">[</span><span class="n">fintype</span> <span class="n">n</span><span class="o">]</span> <span class="o">[</span><span class="n">fintype</span> <span class="n">m&#39;</span><span class="o">]</span> <span class="o">[</span><span class="n">fintype</span> <span class="n">n&#39;</span><span class="o">]</span>

<span class="n">def</span> <span class="n">minormx</span> <span class="o">:</span> <span class="n">matrix</span> <span class="n">m</span> <span class="n">n</span> <span class="n">α</span> <span class="bp">→</span> <span class="o">(</span><span class="n">m&#39;</span> <span class="bp">→</span> <span class="n">m</span><span class="o">)</span> <span class="bp">→</span> <span class="o">(</span><span class="n">n&#39;</span> <span class="bp">→</span> <span class="n">n</span><span class="o">)</span> <span class="bp">→</span> <span class="n">matrix</span> <span class="n">m&#39;</span> <span class="n">n&#39;</span> <span class="n">α</span> <span class="o">:=</span>
<span class="bp">λ</span> <span class="n">A</span> <span class="n">trans_col</span> <span class="n">trans_row</span> <span class="n">i</span> <span class="n">j</span><span class="o">,</span> <span class="n">A</span> <span class="o">(</span><span class="n">trans_col</span> <span class="n">i</span><span class="o">)</span> <span class="o">(</span><span class="n">trans_row</span> <span class="n">j</span><span class="o">)</span>

<span class="n">def</span> <span class="n">rsubmx</span> <span class="o">{</span><span class="n">m</span> <span class="n">n_left</span> <span class="n">n_right</span><span class="o">:</span> <span class="n">nat</span><span class="o">}</span> <span class="o">:</span>
  <span class="n">matrix</span> <span class="o">(</span><span class="n">fin</span> <span class="n">m</span><span class="o">)</span> <span class="o">(</span><span class="n">fin</span> <span class="o">(</span><span class="n">n_right</span> <span class="bp">+</span> <span class="n">n_left</span><span class="o">))</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">matrix</span> <span class="o">(</span><span class="n">fin</span> <span class="n">m</span><span class="o">)</span> <span class="o">(</span><span class="n">fin</span> <span class="o">(</span><span class="n">n_right</span><span class="o">))</span> <span class="n">α</span>
<span class="bp">|</span> <span class="n">A</span> <span class="o">:=</span> <span class="n">minormx</span> <span class="n">A</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">i</span><span class="o">,</span> <span class="n">i</span><span class="o">)</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">j</span><span class="o">,</span> <span class="n">fin</span><span class="bp">.</span><span class="n">add_nat</span> <span class="n">j</span> <span class="bp">_</span><span class="o">)</span>
</pre></div>

#### [ Tobias Grosser (Sep 30 2018 at 08:11)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134910905):
<p>(deleted)</p>

#### [ Tobias Grosser (Sep 30 2018 at 08:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134910948):
<p>(deleted)</p>

#### [ Tobias Grosser (Sep 30 2018 at 08:15)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134911004):
<p>I created a bunch of tests:</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">rsubmx_test_join_fail</span><span class="o">:</span>
<span class="n">matrix</span> <span class="o">(</span><span class="n">fin</span> <span class="mi">5</span><span class="o">)</span> <span class="o">(</span><span class="n">fin</span> <span class="mi">5</span><span class="o">)</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">matrix</span> <span class="o">(</span><span class="n">fin</span> <span class="mi">5</span><span class="o">)</span> <span class="o">(</span><span class="n">fin</span> <span class="mi">3</span><span class="o">)</span> <span class="n">α</span> <span class="o">:=</span>
<span class="bp">λ</span> <span class="n">A</span><span class="o">,</span> <span class="n">rsubmx</span> <span class="n">A</span>

<span class="n">def</span> <span class="n">rsubmx_test_split_const_ok</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">nat</span><span class="o">)</span> <span class="o">:</span>
<span class="n">matrix</span> <span class="o">(</span><span class="n">fin</span> <span class="mi">5</span><span class="o">)</span> <span class="o">(</span><span class="n">fin</span> <span class="o">(</span><span class="mi">3</span> <span class="bp">+</span> <span class="mi">2</span><span class="o">))</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">matrix</span> <span class="o">(</span><span class="n">fin</span> <span class="mi">5</span><span class="o">)</span> <span class="o">(</span><span class="n">fin</span> <span class="mi">3</span><span class="o">)</span> <span class="n">α</span> <span class="o">:=</span>
<span class="bp">λ</span> <span class="n">A</span><span class="o">,</span> <span class="n">rsubmx</span> <span class="n">A</span>

<span class="n">def</span> <span class="n">rsubmx_test_split_const_fail</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">nat</span><span class="o">)</span> <span class="o">:</span>
<span class="n">matrix</span> <span class="o">(</span><span class="n">fin</span> <span class="mi">5</span><span class="o">)</span> <span class="o">(</span><span class="n">fin</span> <span class="o">(</span><span class="mi">2</span> <span class="bp">+</span> <span class="mi">3</span><span class="o">))</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">matrix</span> <span class="o">(</span><span class="n">fin</span> <span class="mi">5</span><span class="o">)</span> <span class="o">(</span><span class="n">fin</span> <span class="mi">3</span><span class="o">)</span> <span class="n">α</span> <span class="o">:=</span>
<span class="bp">λ</span> <span class="n">A</span><span class="o">,</span> <span class="n">rsubmx</span> <span class="n">A</span>

<span class="n">def</span> <span class="n">rsubmx_test_split_param_ok</span> <span class="o">(</span><span class="n">x</span> <span class="n">y</span> <span class="o">:</span> <span class="n">nat</span><span class="o">)</span> <span class="o">:</span>
<span class="n">matrix</span> <span class="o">(</span><span class="n">fin</span> <span class="mi">5</span><span class="o">)</span> <span class="o">(</span><span class="n">fin</span> <span class="o">(</span><span class="n">x</span> <span class="bp">+</span> <span class="n">y</span><span class="o">))</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">matrix</span> <span class="o">(</span><span class="n">fin</span> <span class="mi">5</span><span class="o">)</span> <span class="o">(</span><span class="n">fin</span> <span class="o">(</span><span class="n">x</span><span class="o">))</span> <span class="n">α</span> <span class="o">:=</span>
<span class="bp">λ</span> <span class="n">A</span><span class="o">,</span> <span class="n">rsubmx</span> <span class="n">A</span>

<span class="n">def</span> <span class="n">rsubmx_test_split_param_fail</span> <span class="o">(</span><span class="n">x</span> <span class="n">y</span> <span class="o">:</span> <span class="n">nat</span><span class="o">)</span> <span class="o">:</span>
<span class="n">matrix</span> <span class="o">(</span><span class="n">fin</span> <span class="mi">5</span><span class="o">)</span> <span class="o">(</span><span class="n">fin</span> <span class="o">(</span><span class="n">y</span> <span class="bp">+</span> <span class="n">x</span><span class="o">))</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">matrix</span> <span class="o">(</span><span class="n">fin</span> <span class="mi">5</span><span class="o">)</span> <span class="o">(</span><span class="n">fin</span> <span class="o">(</span><span class="n">x</span><span class="o">))</span> <span class="n">α</span> <span class="o">:=</span>
<span class="bp">λ</span> <span class="n">A</span><span class="o">,</span> <span class="n">rsubmx</span> <span class="n">A</span>
</pre></div>


<p>Only if the fine type is split into a clear  "+" with the correct order of operands in the plus (the LHS operand must appear in the result type), this compiles. Automatic splitting or exploiting commutativity does not work.</p>
<p>Here the associated error messages:</p>
<div class="codehilite"><pre><span></span><span class="n">test</span><span class="bp">.</span><span class="n">lean</span><span class="o">:</span><span class="mi">16</span><span class="o">:</span><span class="mi">5</span><span class="o">:</span> <span class="n">error</span>

<span class="n">type</span> <span class="n">mismatch</span> <span class="n">at</span> <span class="n">application</span>
  <span class="n">rsubmx</span> <span class="n">A</span>
<span class="n">term</span>
  <span class="n">A</span>
<span class="n">has</span> <span class="n">type</span>
  <span class="n">matrix</span> <span class="o">(</span><span class="n">fin</span> <span class="mi">5</span><span class="o">)</span> <span class="o">(</span><span class="n">fin</span> <span class="mi">5</span><span class="o">)</span> <span class="n">α</span>
<span class="n">but</span> <span class="n">is</span> <span class="n">expected</span> <span class="n">to</span> <span class="k">have</span> <span class="n">type</span>
  <span class="n">matrix</span> <span class="o">(</span><span class="n">fin</span> <span class="mi">5</span><span class="o">)</span> <span class="o">(</span><span class="n">fin</span> <span class="o">(</span><span class="mi">3</span> <span class="bp">+</span> <span class="err">?</span><span class="n">m_1</span><span class="o">))</span> <span class="n">α</span>

<span class="n">type</span> <span class="n">mismatch</span> <span class="n">at</span> <span class="n">application</span>
  <span class="n">rsubmx</span> <span class="n">A</span>
<span class="n">term</span>
  <span class="n">A</span>
<span class="n">has</span> <span class="n">type</span>
  <span class="n">matrix</span> <span class="o">(</span><span class="n">fin</span> <span class="mi">5</span><span class="o">)</span> <span class="o">(</span><span class="n">fin</span> <span class="o">(</span><span class="mi">2</span> <span class="bp">+</span> <span class="mi">3</span><span class="o">))</span> <span class="n">α</span>
<span class="n">but</span> <span class="n">is</span> <span class="n">expected</span> <span class="n">to</span> <span class="k">have</span> <span class="n">type</span>
  <span class="n">matrix</span> <span class="o">(</span><span class="n">fin</span> <span class="mi">5</span><span class="o">)</span> <span class="o">(</span><span class="n">fin</span> <span class="o">(</span><span class="mi">3</span> <span class="bp">+</span> <span class="err">?</span><span class="n">m_1</span><span class="o">))</span> <span class="n">α</span>
<span class="n">test</span><span class="bp">.</span><span class="n">lean</span><span class="o">:</span><span class="mi">24</span><span class="o">:</span><span class="mi">5</span><span class="o">:</span> <span class="n">error</span>

<span class="n">type</span> <span class="n">mismatch</span> <span class="n">at</span> <span class="n">application</span>
  <span class="n">rsubmx</span> <span class="n">A</span>
<span class="n">term</span>
  <span class="n">A</span>
<span class="n">has</span> <span class="n">type</span>
  <span class="n">matrix</span> <span class="o">(</span><span class="n">fin</span> <span class="mi">5</span><span class="o">)</span> <span class="o">(</span><span class="n">fin</span> <span class="o">(</span><span class="n">y</span> <span class="bp">+</span> <span class="n">x</span><span class="o">))</span> <span class="n">α</span>
<span class="n">but</span> <span class="n">is</span> <span class="n">expected</span> <span class="n">to</span> <span class="k">have</span> <span class="n">type</span>
  <span class="n">matrix</span> <span class="o">(</span><span class="n">fin</span> <span class="mi">5</span><span class="o">)</span> <span class="o">(</span><span class="n">fin</span> <span class="o">(</span><span class="n">x</span> <span class="bp">+</span> <span class="err">?</span><span class="n">m_1</span><span class="o">))</span> <span class="n">α</span>
</pre></div>

#### [ Tobias Grosser (Sep 30 2018 at 08:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134911323):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> , any idea how to make my tests independent of the order of fin? This seems to require lean foo I am not yet capable of.</p>

#### [ Mario Carneiro (Sep 30 2018 at 08:31)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134911423):
<p>Use Kevin's suggestion</p>

#### [ Mario Carneiro (Sep 30 2018 at 08:31)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134911425):
<p>You should avoid algebra inside types like the plague</p>

#### [ Tobias Grosser (Sep 30 2018 at 08:34)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134911524):
<p>With</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">minormx</span> <span class="o">:</span> <span class="n">matrix</span> <span class="n">m</span> <span class="n">n</span> <span class="n">α</span> <span class="bp">→</span> <span class="o">(</span><span class="n">m&#39;</span> <span class="bp">→</span> <span class="n">m</span><span class="o">)</span> <span class="bp">→</span> <span class="o">(</span><span class="n">n&#39;</span> <span class="bp">→</span> <span class="n">n</span><span class="o">)</span> <span class="bp">→</span> <span class="n">matrix</span> <span class="n">m&#39;</span> <span class="n">n&#39;</span> <span class="n">α</span> <span class="o">:=</span>
<span class="bp">λ</span> <span class="n">A</span> <span class="n">trans_col</span> <span class="n">trans_row</span> <span class="n">i</span> <span class="n">j</span><span class="o">,</span> <span class="n">A</span> <span class="o">(</span><span class="n">trans_col</span> <span class="n">i</span><span class="o">)</span> <span class="o">(</span><span class="n">trans_row</span> <span class="n">j</span><span class="o">)</span>
</pre></div>


<p>I tried to implement Kevin's suggestion.</p>

#### [ Tobias Grosser (Sep 30 2018 at 08:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134911533):
<p>I now try to implement ssreflects</p>
<div class="codehilite"><pre><span></span>   <span class="o">[</span><span class="n">l</span><span class="o">|</span><span class="n">r</span><span class="o">]</span><span class="n">submx</span> <span class="n">A</span> <span class="o">==</span> <span class="n">the</span> <span class="k">left</span><span class="o">/</span><span class="k">right</span> <span class="n">submatrices</span> <span class="k">of</span> <span class="n">a</span> <span class="n">row</span> <span class="n">block</span> <span class="n">matrix</span> <span class="n">A</span><span class="o">.</span>
                   <span class="n">Note</span> <span class="n">that</span> <span class="n">the</span> <span class="n">type</span> <span class="k">of</span> <span class="n">A</span><span class="o">,</span> <span class="k">&#39;</span><span class="n">M_</span><span class="o">(</span><span class="n">m</span><span class="o">,</span> <span class="n">n1</span> <span class="o">+</span> <span class="n">n2</span><span class="o">)</span> <span class="n">indicates</span> <span class="n">how</span> <span class="n">A</span>
                   <span class="n">should</span> <span class="n">be</span> <span class="n">decomposed</span><span class="o">.</span>
</pre></div>


<p>on top of it.</p>

#### [ Tobias Grosser (Sep 30 2018 at 08:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134911571):
<p>It seems a nice feature that they can split just based on the type sizes.</p>

#### [ Tobias Grosser (Sep 30 2018 at 08:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134911578):
<p>Are you saying the interface they use in coq is not a good interface for lean?</p>

#### [ Mario Carneiro (Sep 30 2018 at 08:38)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134911625):
<p>That will only work when <code>n1</code> and <code>n2</code> are explicitly given, and they also have to be numerals not variables for it to be useful</p>

#### [ Mario Carneiro (Sep 30 2018 at 08:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134911629):
<p>Do you have any examples of use of this notation in Coq?</p>

#### [ Mario Carneiro (Sep 30 2018 at 08:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134911682):
<blockquote>
<p>Note that the type of A, 'M_(m, n1 + n2) indicates how A should be decomposed.</p>
</blockquote>
<p>This sounds to me like lean's behavior is consistent with coq's: You have to give an input of a matrix <code>matrix 5 (3 + 2)</code> rather than <code>matrix 5 5</code> to get the function to figure out <code>n1</code> and <code>n2</code></p>

#### [ Tobias Grosser (Sep 30 2018 at 08:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134911732):
<p>Sure, my guaussien elimination code:</p>
<div class="codehilite"><pre><span></span><span class="kn">Fixpoint</span> <span class="n">Gaussian_elimination</span> <span class="o">{</span><span class="n">m</span> <span class="n">n</span><span class="o">}</span> <span class="o">:</span> <span class="k">&#39;</span><span class="n">M_</span><span class="o">(</span><span class="n">m</span><span class="o">,</span> <span class="n">n</span><span class="o">)</span> <span class="err">→</span> <span class="k">&#39;</span><span class="n">M_m</span> <span class="err">×</span> <span class="k">&#39;</span><span class="n">M_n</span> <span class="err">×</span> <span class="kt">nat</span> <span class="o">:=</span>
  <span class="k">match</span> <span class="n">m</span><span class="o">,</span> <span class="n">n</span> <span class="k">with</span>
  <span class="o">|</span> <span class="o">_.+</span><span class="mi">1</span><span class="o">,</span> <span class="o">_.+</span><span class="mi">1</span> <span class="err">⇒</span> <span class="k">fun</span> <span class="n">A</span> <span class="o">:</span> <span class="k">&#39;</span><span class="n">M_</span><span class="o">(</span><span class="mi">1</span> <span class="o">+</span> <span class="o">_,</span> <span class="mi">1</span> <span class="o">+</span> <span class="o">_)</span> <span class="err">⇒</span>
    <span class="k">if</span> <span class="o">[</span><span class="n">pick</span> <span class="n">ij</span> <span class="o">|</span> <span class="n">A</span> <span class="n">ij</span><span class="o">.</span><span class="mi">1</span> <span class="n">ij</span><span class="o">.</span><span class="mi">2</span> <span class="o">!=</span> <span class="mi">0</span><span class="o">]</span> <span class="k">is</span> <span class="n">Some</span> <span class="o">(</span><span class="n">i</span><span class="o">,</span> <span class="n">j</span><span class="o">)</span> <span class="k">then</span>
      <span class="k">let</span> <span class="n">a</span> <span class="o">:=</span> <span class="n">A</span> <span class="n">i</span> <span class="n">j</span> <span class="k">in</span> <span class="k">let</span> <span class="n">A1</span> <span class="o">:=</span> <span class="n">xrow</span> <span class="n">i</span> <span class="mi">0</span> <span class="o">(</span><span class="n">xcol</span> <span class="n">j</span> <span class="mi">0</span> <span class="n">A</span><span class="o">)</span> <span class="k">in</span>
      <span class="k">let</span> <span class="n">u</span> <span class="o">:=</span> <span class="n">ursubmx</span> <span class="n">A1</span> <span class="k">in</span> <span class="k">let</span> <span class="n">v</span> <span class="o">:=</span> <span class="n">a</span><span class="o">^-</span><span class="mi">1</span> <span class="o">*:</span> <span class="n">dlsubmx</span> <span class="n">A1</span> <span class="k">in</span>
      <span class="k">let</span><span class="o">:</span> <span class="o">(</span><span class="n">L</span><span class="o">,</span> <span class="n">U</span><span class="o">,</span> <span class="n">r</span><span class="o">)</span> <span class="o">:=</span> <span class="n">Gaussian_elimination</span> <span class="o">(</span><span class="n">drsubmx</span> <span class="n">A1</span> <span class="o">-</span> <span class="n">v</span> <span class="err">×</span><span class="n">m</span> <span class="n">u</span><span class="o">)</span> <span class="k">in</span>
      <span class="o">(</span><span class="n">xrow</span> <span class="n">i</span> <span class="mi">0</span> <span class="o">(</span><span class="n">block_mx</span> <span class="mi">1</span> <span class="mi">0</span> <span class="n">v</span> <span class="n">L</span><span class="o">),</span> <span class="n">xcol</span> <span class="n">j</span> <span class="mi">0</span> <span class="o">(</span><span class="n">block_mx</span> <span class="n">a</span><span class="o">%:</span><span class="n">M</span> <span class="n">u</span> <span class="mi">0</span> <span class="n">U</span><span class="o">),</span> <span class="n">r</span><span class="o">.+</span><span class="mi">1</span><span class="o">)</span>
    <span class="k">else</span> <span class="o">(</span><span class="mi">1</span><span class="o">%:</span><span class="n">M</span><span class="o">,</span> <span class="mi">1</span><span class="o">%:</span><span class="n">M</span><span class="o">,</span> <span class="mi">0</span><span class="o">%</span><span class="n">N</span><span class="o">)</span>
  <span class="o">|</span> <span class="o">_,</span> <span class="o">_</span> <span class="err">⇒</span> <span class="k">fun</span> <span class="o">_</span> <span class="err">⇒</span> <span class="o">(</span><span class="mi">1</span><span class="o">%:</span><span class="n">M</span><span class="o">,</span> <span class="mi">1</span><span class="o">%:</span><span class="n">M</span><span class="o">,</span> <span class="mi">0</span><span class="o">%</span><span class="n">N</span><span class="o">)</span>
  <span class="k">end</span><span class="o">.</span>
</pre></div>


<p>it uses <code>dlsubmx</code> which again is defined as:</p>
<div class="codehilite"><pre><span></span><span class="kn">Definition</span> <span class="n">ulsubmx</span> <span class="o">:=</span> <span class="n">lsubmx</span> <span class="o">(</span><span class="n">usubmx</span> <span class="n">A</span><span class="o">).</span>
<span class="kn">Definition</span> <span class="n">ursubmx</span> <span class="o">:=</span> <span class="n">rsubmx</span> <span class="o">(</span><span class="n">usubmx</span> <span class="n">A</span><span class="o">).</span>
<span class="kn">Definition</span> <span class="n">dlsubmx</span> <span class="o">:=</span> <span class="n">lsubmx</span> <span class="o">(</span><span class="n">dsubmx</span> <span class="n">A</span><span class="o">).</span>
<span class="kn">Definition</span> <span class="n">drsubmx</span> <span class="o">:=</span> <span class="n">rsubmx</span> <span class="o">(</span><span class="n">dsubmx</span> <span class="n">A</span><span class="o">).</span>
</pre></div>


<p>which again uses</p>
<div class="codehilite"><pre><span></span><span class="kn">Fact</span> <span class="n">lsubmx_key</span> <span class="o">:</span> <span class="kt">unit</span><span class="o">.</span>
<span class="kn">Definition</span> <span class="n">lsubmx</span> <span class="o">(</span><span class="n">A</span> <span class="o">:</span> <span class="k">&#39;</span><span class="n">M</span><span class="o">[</span><span class="n">R</span><span class="o">]_(</span><span class="n">m</span><span class="o">,</span> <span class="n">n1</span> <span class="o">+</span> <span class="n">n2</span><span class="o">))</span> <span class="o">:=</span>
  <span class="err">\</span><span class="n">matrix</span><span class="o">[</span><span class="n">lsubmx_key</span><span class="o">]_(</span><span class="n">i</span><span class="o">,</span> <span class="n">j</span><span class="o">)</span> <span class="n">A</span> <span class="n">i</span> <span class="o">(</span><span class="n">lshift</span> <span class="n">n2</span> <span class="n">j</span><span class="o">).</span>

<span class="kn">Fact</span> <span class="n">rsubmx_key</span> <span class="o">:</span> <span class="kt">unit</span><span class="o">.</span>
<span class="kn">Definition</span> <span class="n">rsubmx</span> <span class="o">(</span><span class="n">A</span> <span class="o">:</span> <span class="k">&#39;</span><span class="n">M</span><span class="o">[</span><span class="n">R</span><span class="o">]_(</span><span class="n">m</span><span class="o">,</span> <span class="n">n1</span> <span class="o">+</span> <span class="n">n2</span><span class="o">))</span> <span class="o">:=</span>
  <span class="err">\</span><span class="n">matrix</span><span class="o">[</span><span class="n">rsubmx_key</span><span class="o">]_(</span><span class="n">i</span><span class="o">,</span> <span class="n">j</span><span class="o">)</span> <span class="n">A</span> <span class="n">i</span> <span class="o">(</span><span class="n">rshift</span> <span class="n">n1</span> <span class="n">j</span><span class="o">).</span>

<span class="kn">Fact</span> <span class="n">usubmx_key</span> <span class="o">:</span> <span class="kt">unit</span><span class="o">.</span>
<span class="kn">Definition</span> <span class="n">usubmx</span> <span class="o">(</span><span class="n">A</span> <span class="o">:</span> <span class="k">&#39;</span><span class="n">M</span><span class="o">[</span><span class="n">R</span><span class="o">]_(</span><span class="n">m1</span> <span class="o">+</span> <span class="n">m2</span><span class="o">,</span> <span class="n">n</span><span class="o">))</span> <span class="o">:=</span>
  <span class="err">\</span><span class="n">matrix</span><span class="o">[</span><span class="n">usubmx_key</span><span class="o">]_(</span><span class="n">i</span><span class="o">,</span> <span class="n">j</span><span class="o">)</span> <span class="n">A</span> <span class="o">(</span><span class="n">lshift</span> <span class="n">m2</span> <span class="n">i</span><span class="o">)</span> <span class="n">j</span><span class="o">.</span>

<span class="kn">Fact</span> <span class="n">dsubmx_key</span> <span class="o">:</span> <span class="kt">unit</span><span class="o">.</span>
<span class="kn">Definition</span> <span class="n">dsubmx</span> <span class="o">(</span><span class="n">A</span> <span class="o">:</span> <span class="k">&#39;</span><span class="n">M</span><span class="o">[</span><span class="n">R</span><span class="o">]_(</span><span class="n">m1</span> <span class="o">+</span> <span class="n">m2</span><span class="o">,</span> <span class="n">n</span><span class="o">))</span> <span class="o">:=</span>
  <span class="err">\</span><span class="n">matrix</span><span class="o">[</span><span class="n">dsubmx_key</span><span class="o">]_(</span><span class="n">i</span><span class="o">,</span> <span class="n">j</span><span class="o">)</span> <span class="n">A</span> <span class="o">(</span><span class="n">rshift</span> <span class="n">m1</span> <span class="n">i</span><span class="o">)</span> <span class="n">j</span><span class="o">.</span>
</pre></div>


<div class="codehilite"><pre><span></span><span class="kn">Lemma</span> <span class="n">lshift_subproof</span> <span class="n">m</span> <span class="n">n</span> <span class="o">(</span><span class="n">i</span> <span class="o">:</span> <span class="k">&#39;</span><span class="n">I_m</span><span class="o">)</span> <span class="o">:</span> <span class="n">i</span> <span class="o">&lt;</span> <span class="n">m</span> <span class="o">+</span> <span class="n">n</span><span class="o">.</span>

<span class="kn">Lemma</span> <span class="n">rshift_subproof</span> <span class="n">m</span> <span class="n">n</span> <span class="o">(</span><span class="n">i</span> <span class="o">:</span> <span class="k">&#39;</span><span class="n">I_n</span><span class="o">)</span> <span class="o">:</span> <span class="n">m</span> <span class="o">+</span> <span class="n">i</span> <span class="o">&lt;</span> <span class="n">m</span> <span class="o">+</span> <span class="n">n</span><span class="o">.</span>

<span class="kn">Definition</span> <span class="n">lshift</span> <span class="n">m</span> <span class="n">n</span> <span class="o">(</span><span class="n">i</span> <span class="o">:</span> <span class="k">&#39;</span><span class="n">I_m</span><span class="o">)</span> <span class="o">:=</span> <span class="n">Ordinal</span> <span class="o">(</span><span class="n">lshift_subproof</span> <span class="n">n</span> <span class="n">i</span><span class="o">).</span>
<span class="kn">Definition</span> <span class="n">rshift</span> <span class="n">m</span> <span class="n">n</span> <span class="o">(</span><span class="n">i</span> <span class="o">:</span> <span class="k">&#39;</span><span class="n">I_n</span><span class="o">)</span> <span class="o">:=</span> <span class="n">Ordinal</span> <span class="o">(</span><span class="n">rshift_subproof</span> <span class="n">m</span> <span class="n">i</span><span class="o">).</span>
</pre></div>

#### [ Tobias Grosser (Sep 30 2018 at 08:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134911822):
<blockquote>
<blockquote>
<p>Note that the type of A, 'M_(m, n1 + n2) indicates how A should be decomposed.</p>
</blockquote>
<p>This sounds to me like lean's behavior is consistent with coq's: You have to give an input of a matrix <code>matrix 5 (3 + 2)</code> rather than <code>matrix 5 5</code> to get the function to figure out <code>n1</code> and <code>n2</code></p>
</blockquote>
<p>If that's as good as it gets that's fine. I just had hoped lean would be able to figure out that 5 can be split into 3 + 2. If this not the case, I need to do this manually. Is there a function that does this type splitting for me?</p>

#### [ Mario Carneiro (Sep 30 2018 at 08:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134911829):
<p>what is the type of <code>A1</code>?</p>

#### [ Mario Carneiro (Sep 30 2018 at 08:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134911831):
<p>or <code>xrow</code> and <code>xcol</code></p>

#### [ Mario Carneiro (Sep 30 2018 at 08:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134911835):
<p>Lean can figure out that <code>5</code> is <code>3 + 2</code>, but it is ambiguous what to split it into</p>

#### [ Tobias Grosser (Sep 30 2018 at 08:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134911888):
<p>I see.</p>

#### [ Tobias Grosser (Sep 30 2018 at 08:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134911942):
<p>In my implementation in lean it is <code>A1 : matrix (fin (x + 1)) (fin (y + 1)) α</code></p>

#### [ Tobias Grosser (Sep 30 2018 at 08:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134911944):
<p>So what I have today might already be enough.</p>

#### [ Tobias Grosser (Sep 30 2018 at 08:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134911946):
<p>I learn that generalizing this further is not a good idea.</p>

#### [ Tobias Grosser (Sep 30 2018 at 08:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134911948):
<p>Thanks! I leave it at this generality.</p>

#### [ Tobias Grosser (Sep 30 2018 at 08:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134912144):
<p>Now I am only left with the problem of casting. I need the matrix to be of type  matrix (fin (1 + x)) (fin (1 + y)))</p>

#### [ Tobias Grosser (Sep 30 2018 at 08:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134912154):
<p>I tried to type-cast using:</p>
<div class="codehilite"><pre><span></span>    <span class="k">let</span> <span class="o">(</span><span class="n">A1&#39;</span><span class="o">:</span> <span class="n">matrix</span> <span class="o">(</span><span class="n">fin</span> <span class="o">(</span><span class="mi">1</span><span class="bp">+</span><span class="n">x</span><span class="o">))</span> <span class="o">(</span><span class="n">fin</span> <span class="o">(</span><span class="mi">1</span><span class="bp">+</span><span class="n">y</span><span class="o">))</span> <span class="n">α</span><span class="o">)</span> <span class="o">:=</span> <span class="n">A1</span> <span class="k">in</span>
</pre></div>


<p>but this just gives</p>
<div class="codehilite"><pre><span></span><span class="n">type</span> <span class="n">mismatch</span> <span class="n">at</span> <span class="n">application</span>
  <span class="bp">_</span><span class="n">let_match</span> <span class="n">A1&#39;</span>
<span class="n">term</span>
  <span class="n">A1&#39;</span>
<span class="n">has</span> <span class="n">type</span>
  <span class="n">matrix</span> <span class="o">(</span><span class="n">fin</span> <span class="o">(</span><span class="mi">1</span> <span class="bp">+</span> <span class="n">x</span><span class="o">))</span> <span class="o">(</span><span class="n">fin</span> <span class="o">(</span><span class="mi">1</span> <span class="bp">+</span> <span class="n">y</span><span class="o">))</span> <span class="n">α</span>
<span class="n">but</span> <span class="n">is</span> <span class="n">expected</span> <span class="n">to</span> <span class="k">have</span> <span class="n">type</span>
  <span class="n">matrix</span> <span class="o">(</span><span class="n">fin</span> <span class="o">(</span><span class="n">x</span> <span class="bp">+</span> <span class="mi">1</span><span class="o">))</span> <span class="o">(</span><span class="n">fin</span> <span class="o">(</span><span class="n">y</span> <span class="bp">+</span> <span class="mi">1</span><span class="o">))</span> <span class="n">α</span>
</pre></div>

#### [ Tobias Grosser (Sep 30 2018 at 08:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134912155):
<p>You said lean should be able to understand this.</p>

#### [ Tobias Grosser (Sep 30 2018 at 08:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134912158):
<p>This is no ambiguity</p>

#### [ Tobias Grosser (Sep 30 2018 at 09:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134912207):
<p>I just need to show that these two are equivalent types.</p>

#### [ Mario Carneiro (Sep 30 2018 at 09:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134912270):
<p>this is not ambiguous, but since <code>x</code> is not a numeral these aren't defeq</p>

#### [ Mario Carneiro (Sep 30 2018 at 09:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134912321):
<p>How do the <code>xrow i 0 (xcol j 0 A)</code> functions work?</p>

#### [ Mario Carneiro (Sep 30 2018 at 09:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134912324):
<p>are you building a new row on <code>A</code> or taking a minor?</p>

#### [ Tobias Grosser (Sep 30 2018 at 09:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134912386):
<p>They just interchange rows. AFAIU they don;t thange the type.</p>

#### [ Mario Carneiro (Sep 30 2018 at 09:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134912393):
<p>The fact that in coq <code>1+x = succ x</code> is definitional makes this translation more complicated, unless you reverse the <code>+</code> arguments in the minors function, or work from the bottom rather than the top of the matrix</p>

#### [ Mario Carneiro (Sep 30 2018 at 09:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134912434):
<p>In lean <code>x+1 = succ x</code> is definitional</p>

#### [ Tobias Grosser (Sep 30 2018 at 09:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134912435):
<p>My lean implementation is:</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">xrow</span> <span class="o">[</span><span class="n">decidable_eq</span> <span class="n">m</span><span class="o">]</span> <span class="o">(</span><span class="n">row1</span><span class="o">:</span> <span class="n">m</span><span class="o">)</span> <span class="o">(</span><span class="n">row2</span><span class="o">:</span> <span class="n">m</span><span class="o">)</span> <span class="o">(</span><span class="n">A</span><span class="o">:</span> <span class="n">matrix</span> <span class="n">m</span> <span class="n">n</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="n">matrix</span> <span class="n">m</span> <span class="n">n</span> <span class="n">α</span> <span class="o">:=</span>
<span class="bp">λ</span> <span class="n">x</span> <span class="n">y</span><span class="o">,</span> <span class="k">if</span> <span class="n">x</span> <span class="bp">=</span> <span class="n">row1</span>
         <span class="k">then</span>
           <span class="n">A</span> <span class="n">row2</span> <span class="n">y</span>
         <span class="k">else</span>
           <span class="k">if</span> <span class="n">x</span> <span class="bp">=</span> <span class="n">row2</span>
             <span class="k">then</span>
               <span class="n">A</span> <span class="n">row1</span> <span class="n">y</span>
             <span class="k">else</span>
               <span class="n">A</span> <span class="n">x</span> <span class="n">y</span>
</pre></div>

#### [ Mario Carneiro (Sep 30 2018 at 09:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134912437):
<p>right, I see, that shouldn't be a problem</p>

#### [ Mario Carneiro (Sep 30 2018 at 09:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134912448):
<p>you are still using the code you posted above for <code>rsubmx</code>?</p>

#### [ Mario Carneiro (Sep 30 2018 at 09:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134912449):
<p>with <code>n_right + n_left</code> in the type I mean</p>

#### [ Tobias Grosser (Sep 30 2018 at 09:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134912451):
<p>Yes.</p>

#### [ Tobias Grosser (Sep 30 2018 at 09:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134912494):
<p>I could move the zero columns/rows to position x+1 / y +1, then the types would work out.</p>

#### [ Tobias Grosser (Sep 30 2018 at 09:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134912497):
<p>But then the result matrices are layed out in a non-standard way.</p>

#### [ Mario Carneiro (Sep 30 2018 at 09:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134912499):
<p>so since <code>A</code> has type <code>(n+1) (n+1)</code> you can naturally strip off the left/top end</p>

#### [ Tobias Grosser (Sep 30 2018 at 09:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134912500):
<p>Right.</p>

#### [ Tobias Grosser (Sep 30 2018 at 09:11)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134912509):
<p>That's easy. Just that most textbook implementations of gaussian elimination build upper triangular matrices.</p>

#### [ Tobias Grosser (Sep 30 2018 at 09:11)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134912510):
<p>So the zeros should be at the lower left corner.</p>

#### [ Mario Carneiro (Sep 30 2018 at 09:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134912551):
<p>I think you can still build upper triangular if you also transpose the rows and columns</p>

#### [ Tobias Grosser (Sep 30 2018 at 09:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134912554):
<p>Sure, I could probably hack my way though this.</p>

#### [ Tobias Grosser (Sep 30 2018 at 09:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134912559):
<p>Just don't feel this is nice.</p>

#### [ Mario Carneiro (Sep 30 2018 at 09:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134912560):
<p>But I think that having reversed arguments to the minors function is also fine</p>

#### [ Tobias Grosser (Sep 30 2018 at 09:12)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134912562):
<p>Why again does this work in coq?</p>

#### [ Mario Carneiro (Sep 30 2018 at 09:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134912568):
<p>because they defined addition by recursion on the first argument rather than the second</p>

#### [ Mario Carneiro (Sep 30 2018 at 09:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134912573):
<p>Personally I prefer lean's definition (i.e. <code>x + succ y = succ (x + y)</code>)</p>

#### [ Tobias Grosser (Sep 30 2018 at 09:13)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134912575):
<p>They do?</p>

#### [ Tobias Grosser (Sep 30 2018 at 09:14)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134912607):
<p>I feel they also have this cast in their code.</p>

#### [ Tobias Grosser (Sep 30 2018 at 09:14)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134912616):
<div class="codehilite"><pre><span></span> <span class="o">|</span> <span class="o">_.+</span><span class="mi">1</span><span class="o">,</span> <span class="o">_.+</span><span class="mi">1</span> <span class="err">⇒</span> <span class="k">fun</span> <span class="n">A</span> <span class="o">:</span> <span class="k">&#39;</span><span class="n">M_</span><span class="o">(</span><span class="mi">1</span> <span class="o">+</span> <span class="o">_,</span> <span class="mi">1</span> <span class="o">+</span> <span class="o">_)</span> <span class="err">⇒</span>
</pre></div>

#### [ Mario Carneiro (Sep 30 2018 at 09:14)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134912619):
<p>That's why in the induction you notice the type is <code>1+_</code> instead of <code>_ +1</code></p>

#### [ Mario Carneiro (Sep 30 2018 at 09:15)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134912630):
<p>The <code>.+</code> is suspicious</p>

#### [ Mario Carneiro (Sep 30 2018 at 09:15)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134912633):
<p>do you know what it means?</p>

#### [ Tobias Grosser (Sep 30 2018 at 09:15)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134912635):
<div class="codehilite"><pre><span></span><span class="kn">Notation</span> <span class="s2">&quot;n .+1&quot;</span> <span class="o">:=</span> <span class="o">(</span><span class="n">succn</span> <span class="n">n</span><span class="o">)</span> <span class="o">(</span><span class="n">at</span> <span class="n">level</span> <span class="mi">2</span><span class="o">,</span> <span class="k">left</span> <span class="n">associativity</span><span class="o">,</span>
  <span class="n">format</span> <span class="s2">&quot;n .+1&quot;</span><span class="o">)</span> <span class="o">:</span> <span class="n">nat_scope</span><span class="o">.</span>
</pre></div>

#### [ Mario Carneiro (Sep 30 2018 at 09:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134912674):
<p>heh</p>

#### [ Tobias Grosser (Sep 30 2018 at 09:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134912678):
<p>So they define notation to allow RHS addition of +1?</p>

#### [ Mario Carneiro (Sep 30 2018 at 09:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134912679):
<p>so <code>1+n = n .+1</code></p>

#### [ Mario Carneiro (Sep 30 2018 at 09:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134912682):
<p>looks like it</p>

#### [ Tobias Grosser (Sep 30 2018 at 09:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134912683):
<p>This stuff is all crazy!</p>

#### [ Tobias Grosser (Sep 30 2018 at 09:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134912686):
<p>Now based on the way nat is defined I cannot write my algorithm the way I want it.</p>

#### [ Tobias Grosser (Sep 30 2018 at 09:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134912692):
<p>:(</p>

#### [ Mario Carneiro (Sep 30 2018 at 09:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134912693):
<p>You can also write <code>fin.add_nat</code> with an appropriate type</p>

#### [ Mario Carneiro (Sep 30 2018 at 09:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134912743):
<p>You can also <code>cast</code> to get <code>A1'</code> the way you were attempting, but this will cause more problems later on</p>

#### [ Tobias Grosser (Sep 30 2018 at 09:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134912799):
<p>OK, I will try to write add_nat after breakfast.</p>
<p>There is already</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">add_nat</span> <span class="o">{</span><span class="n">n</span><span class="o">}</span> <span class="o">(</span><span class="n">i</span> <span class="o">:</span> <span class="n">fin</span> <span class="n">n</span><span class="o">)</span> <span class="o">(</span><span class="n">k</span><span class="o">)</span> <span class="o">:</span> <span class="n">fin</span> <span class="o">(</span><span class="n">n</span> <span class="bp">+</span> <span class="n">k</span><span class="o">)</span> <span class="o">:=</span>
<span class="bp">⟨</span><span class="n">i</span><span class="bp">.</span><span class="mi">1</span> <span class="bp">+</span> <span class="n">k</span><span class="o">,</span> <span class="n">nat</span><span class="bp">.</span><span class="n">add_lt_add_right</span> <span class="n">i</span><span class="bp">.</span><span class="mi">2</span> <span class="bp">_⟩</span>
</pre></div>

#### [ Tobias Grosser (Sep 30 2018 at 09:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134912800):
<p>Seems trivial to write (assuming one knows what to write)</p>

#### [ Tobias Grosser (Sep 30 2018 at 09:21)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134912806):
<p>Now, I am not sure what I actually want here.</p>

#### [ Tobias Grosser (Sep 30 2018 at 09:21)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134912807):
<p>In some way I just want to cast from n + 1 to 1 + n.</p>

#### [ Tobias Grosser (Sep 30 2018 at 09:21)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134912809):
<p>Or pattern match based on 1 + n.</p>

#### [ Tobias Grosser (Sep 30 2018 at 09:21)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134912811):
<p>Would add_nat help me with the pattern matching?</p>

#### [ Mario Carneiro (Sep 30 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134912854):
<p>just swap the arguments, like this</p>
<div class="codehilite"><pre><span></span>def nat_add {n} (k) (i : fin n) : fin (k + n) :=
⟨k + i.1, nat.add_lt_add_left i.2 _⟩
</pre></div>

#### [ Mario Carneiro (Sep 30 2018 at 09:23)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134912857):
<p>then use it in your minors function</p>

#### [ Tobias Grosser (Sep 30 2018 at 09:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134912972):
<p>Are you suggeting to change the signature of my functions.</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">ursubmx</span> <span class="o">{</span><span class="n">m_bottom</span> <span class="n">m_top</span> <span class="n">n_left</span> <span class="n">n_right</span><span class="o">:</span> <span class="n">nat</span><span class="o">}</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">(</span><span class="n">m_bottom</span> <span class="n">m_top</span> <span class="n">n_left</span> <span class="n">n_right</span><span class="o">),</span>
  <span class="n">matrix</span> <span class="o">(</span><span class="n">fin</span> <span class="o">(</span><span class="n">m_bottom</span> <span class="bp">+</span> <span class="n">m_top</span><span class="o">))</span> <span class="o">(</span><span class="n">fin</span> <span class="o">(</span><span class="n">n_left</span> <span class="bp">+</span> <span class="n">n_right</span><span class="o">))</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">matrix</span> <span class="o">(</span><span class="n">fin</span> <span class="n">m_top</span><span class="o">)</span> <span class="o">(</span><span class="n">fin</span> <span class="o">(</span><span class="n">n_right</span><span class="o">))</span> <span class="n">α</span>
<span class="o">:=</span> <span class="n">sorry</span>

<span class="n">def</span> <span class="n">ursubmx2</span> <span class="o">{</span><span class="n">m_bottom</span> <span class="n">m_top</span> <span class="n">n_left</span> <span class="n">n_right</span><span class="o">:</span> <span class="n">nat</span><span class="o">}</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">(</span><span class="n">m_bottom</span> <span class="n">m_top</span> <span class="n">n_left</span> <span class="n">n_right</span><span class="o">),</span>
  <span class="n">matrix</span> <span class="o">(</span><span class="n">fin</span> <span class="o">(</span><span class="n">m_top</span> <span class="bp">+</span> <span class="n">m_bottom</span><span class="o">))</span> <span class="o">(</span><span class="n">fin</span> <span class="o">(</span><span class="n">n_right</span> <span class="bp">+</span> <span class="n">n_left</span><span class="o">))</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">matrix</span> <span class="o">(</span><span class="n">fin</span> <span class="n">m_top</span><span class="o">)</span> <span class="o">(</span><span class="n">fin</span> <span class="o">(</span><span class="n">n_right</span><span class="o">))</span> <span class="n">α</span>
<span class="o">:=</span> <span class="n">sorry</span>
</pre></div>

#### [ Mario Carneiro (Sep 30 2018 at 09:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134913014):
<p>yes... although I think this will make a cast required</p>

#### [ Tobias Grosser (Sep 30 2018 at 09:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134913015):
<p>I feel I have enough ideas to make things work. I can then later try to make the code nice.</p>

#### [ Tobias Grosser (Sep 30 2018 at 09:29)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134913018):
<p>This just screems ugly all over the place.</p>

#### [ Tobias Grosser (Sep 30 2018 at 09:29)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134913022):
<p>Need to get used to this more to see a beautiful solution.</p>

#### [ Tobias Grosser (Sep 30 2018 at 09:29)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134913024):
<p>Need to have breakfast now. Thanks a lot for the helpful discussion. I learned a lot!</p>

#### [ Mario Carneiro (Sep 30 2018 at 09:30)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134913071):
<p>Here's a trick: You can use Kevin's minors function as a cast</p>

#### [ Mario Carneiro (Sep 30 2018 at 09:30)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134913073):
<p>the identity function <code>fin (m+n) -&gt; fin (n+m)</code> is monotonic :)</p>

#### [ Kevin Buzzard (Sep 30 2018 at 10:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134914237):
<p>Is there an argument for not even using <code>fin n</code> at all and having a general class indexed over a pair of finite types?</p>
<p>Here's a result I'd like to see in Lean one day: if f(X) is the char poly of the n x n matrix M then the coefficient of X^(n-i) in f(X) is the sum of the (appropriately signed?) determinants of the i x i principal minors.</p>

#### [ Mario Carneiro (Sep 30 2018 at 10:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134914299):
<p>We already have that; Tobias is explicitly avoiding that because he wants to do induction on fin n</p>

#### [ Kevin Buzzard (Sep 30 2018 at 10:21)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134914352):
<p>Oh -- I'm behind the times :-)</p>

#### [ Mario Carneiro (Sep 30 2018 at 10:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134914394):
<p>If this is to be computationally efficient, it should probably use list representation though (a.k.a <code>fast_matrix</code>), and it might be possible to just ignore the dependent types and work with <code>list (list A)</code></p>

#### [ Tobias Grosser (Sep 30 2018 at 11:17)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134915836):
<p>I see.</p>

#### [ Tobias Grosser (Sep 30 2018 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134915876):
<p>I would certainly like this to be computationally efficient, but will take this a step at a time. I feel I am close to sth that could work. I will finish this up and polish it.</p>

#### [ Tobias Grosser (Sep 30 2018 at 11:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134915879):
<p>Then we have a first baseline implementation. I am then happy to take feedback on how to improve interface / performance / ...</p>

#### [ Mario Carneiro (Sep 30 2018 at 11:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134916119):
<p>I think that's a good idea</p>

#### [ Tobias Grosser (Sep 30 2018 at 14:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134921308):
<p>OK, I think I got a first implementation: <a href="https://gist.github.com/tobig/376e9a394c674474b8c1f6ecf9555478" target="_blank" title="https://gist.github.com/tobig/376e9a394c674474b8c1f6ecf9555478">https://gist.github.com/tobig/376e9a394c674474b8c1f6ecf9555478</a><br>
It compiles and gives expected results. Still a couple of sorry, but seems to work.</p>

#### [ Tobias Grosser (Sep 30 2018 at 14:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134921349):
<p>Need to clean up everything at some point.</p>

#### [ Tobias Grosser (Sep 30 2018 at 14:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134921353):
<p>But no today any more.</p>

#### [ Tobias Grosser (Sep 30 2018 at 14:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134921355):
<p>Also I learned it is indeed _very_ slow.</p>

#### [ Tobias Grosser (Sep 30 2018 at 14:36)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134921356):
<p>I need to wait 10s of seconds for results on a 3x3 matrix.</p>

#### [ Tobias Grosser (Sep 30 2018 at 14:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134921362):
<p>Oh dear, seems there is optimization potential.</p>

#### [ Kevin Buzzard (Sep 30 2018 at 15:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134922425):
<p>I think for your test matrix I would have been tempted to send x and y to <code>C[3*x+y]</code> with C a vector of the nine entries (<code>def C := [3,3,3,3,2,3,2,1,1]</code>)...hmm...one might then have to prove 3*x+y&lt;=8...</p>

#### [ Andrew Ashworth (Sep 30 2018 at 16:29)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134924823):
<p>hmm, are you aiming for speed? I believe <code>vector</code> has special support in the VM, so you might try defining matrix using that instead of an arbitrary <code>fintype</code></p>

#### [ Andrew Ashworth (Sep 30 2018 at 16:30)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134924884):
<p>iirc, and you would be more familiar than me on this topic, but doesn't SSReflect also define matrix as a vector of vectors?</p>

#### [ Tobias Grosser (Sep 30 2018 at 17:14)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134926152):
<p>I am not aiming for speed atm. I just want to get things working / defined and improve my lean-knowledge.</p>

#### [ Tobias Grosser (Sep 30 2018 at 17:15)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134926161):
<p>Eventually, I would like this to be fast and maybe even support exporting code to C++.</p>

#### [ Tobias Grosser (Sep 30 2018 at 17:15)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/134926164):
<p>However, this is a medium term only.</p>

#### [ Tobias Grosser (Oct 05 2018 at 07:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/135234645):
<p>My first pull request: <a href="https://github.com/leanprover/mathlib/pull/387" target="_blank" title="https://github.com/leanprover/mathlib/pull/387">https://github.com/leanprover/mathlib/pull/387</a></p>
<p>Still very small, but gets things rolling.</p>

#### [ Tobias Grosser (Oct 05 2018 at 08:15)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/135236714):
<p>I got an amazing review from <span class="user-mention" data-user-id="110026">@Simon Hudon</span> and <span class="user-mention" data-user-id="110045">@Sean Leather</span>. Thanks a lot!</p>

#### [ Simon Hudon (Oct 05 2018 at 08:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/135236765):
<p>The PR has my stamp of approval and, I think, that of <span class="user-mention" data-user-id="110045">@Sean Leather</span>, now we just need <span class="user-mention" data-user-id="110049">@Mario Carneiro</span> or <span class="user-mention" data-user-id="110294">@Johannes Hölzl</span> to merge it.</p>

#### [ Sean Leather (Oct 05 2018 at 08:18)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/135236826):
<p>Agreed.</p>

#### [ Mario Carneiro (Oct 05 2018 at 08:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/135236830):
<p>yeah okay</p>

#### [ Simon Hudon (Oct 05 2018 at 08:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/135236836):
<p>This must be some sort of record :D</p>

#### [ Tobias Grosser (Oct 05 2018 at 08:21)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/135236911):
<p>Impressive!</p>

#### [ Tobias Grosser (Oct 05 2018 at 10:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/135242622):
<p>I pushed anther pull request for fin in (<a href="https://github.com/leanprover/mathlib/pull/388" target="_blank" title="https://github.com/leanprover/mathlib/pull/388">https://github.com/leanprover/mathlib/pull/388</a>) as well as the submatrix definitions this thread was originally about in: <a href="https://github.com/leanprover/mathlib/pull/389" target="_blank" title="https://github.com/leanprover/mathlib/pull/389">https://github.com/leanprover/mathlib/pull/389</a>. The last PR uses <span class="user-mention" data-user-id="110038">@Kevin Buzzard</span>'s idea of using a general function minormx to implement this functionality.</p>

#### [ Tobias Grosser (Oct 05 2018 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/135242713):
<p>Especially the last one is more a RFC, as I am not sure if limiting these functionality to (fin n) makes sense.</p>

#### [ Tobias Grosser (Oct 05 2018 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/computing%20submatrix%20for%20ring_theory.matrix/near/135242722):
<p>My lean time is over for today. Will look at potential feedback later tonight. Thanks everyone again!</p>


{% endraw %}
