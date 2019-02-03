---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/36914howdoestacticringwork.html
---

## Stream: [general](https://leanprover-community.github.io/archive/113488general/index.html)
### Topic: [how does tactic.ring work?](https://leanprover-community.github.io/archive/113488general/36914howdoestacticringwork.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kevin Buzzard (Jun 11 2018 at 10:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127888870):
<p>I have read through programming in Lean a couple of times and now wonder if it's time I started reading something else. I decided to read the ring tactic (not least because it failed to prove something relatively simple the last time I tried to use it and I'd rather fix it myself than pester Mario, not that I have any idea about how far I need to go before I am anywhere close to being able to fix it).</p>

#### [ Kevin Buzzard (Jun 11 2018 at 10:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127888871):
<p>Anyway, I started to read it:</p>

#### [ Kevin Buzzard (Jun 11 2018 at 10:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127888874):
<p><a href="https://github.com/kbuzzard/mathlib/blob/tactic_doc/docs/ring_tactic.rst" target="_blank" title="https://github.com/kbuzzard/mathlib/blob/tactic_doc/docs/ring_tactic.rst">https://github.com/kbuzzard/mathlib/blob/tactic_doc/docs/ring_tactic.rst</a></p>

#### [ Kevin Buzzard (Jun 11 2018 at 10:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127888882):
<p>There are my comments on the first 30 or so lines, plus a long intro summarising programming in lean</p>

#### [ Kevin Buzzard (Jun 11 2018 at 10:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127888901):
<p>There's a link to programming in lean: <a href="https://leanprover.github.io/programming_in_lean/programming_in_lean.pdf" target="_blank" title="https://leanprover.github.io/programming_in_lean/programming_in_lean.pdf">https://leanprover.github.io/programming_in_lean/programming_in_lean.pdf</a></p>

#### [ Kevin Buzzard (Jun 11 2018 at 10:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127888951):
<p>Here's Patrick's secret gem: <a href="https://hanoifabs.files.wordpress.com/2018/05/slides.pdf" target="_blank" title="https://hanoifabs.files.wordpress.com/2018/05/slides.pdf">https://hanoifabs.files.wordpress.com/2018/05/slides.pdf</a> (thanks Johannes)</p>

#### [ Kevin Buzzard (Jun 11 2018 at 10:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127888964):
<p>and that is pretty much every online resource for Lean tactics. Here's the file I want to understand:</p>

#### [ Kevin Buzzard (Jun 11 2018 at 10:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127888974):
<p><a href="https://github.com/leanprover/mathlib/blob/master/tactic/ring.lean" target="_blank" title="https://github.com/leanprover/mathlib/blob/master/tactic/ring.lean">https://github.com/leanprover/mathlib/blob/master/tactic/ring.lean</a></p>

#### [ Kevin Buzzard (Jun 11 2018 at 10:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127888989):
<p>if anyone wants to help me understand it, they're welcome to edit the rst file. Note: I wrote <code>ring_ractic.rst</code> in sphinx not markdown. It's still human-readable and pretty easy to pick up.</p>

#### [ Johan Commelin (Jun 11 2018 at 12:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127893407):
<p>Typo: "especially if one does it within Lean (thus gaining the ability to hover over or click on functions and see their type, definition and so on)." &lt;-- you mean VScode instead of Lean, right?<br>
Another typo: "Note that evem though" &lt;-- s/evem/even/</p>

#### [ Kevin Buzzard (Jun 11 2018 at 14:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127896619):
<p>Thanks. I had a look through all of tactic.ring and really it doesn't look too bad. I'm currently reading <a href="http://www.cs.ru.nl/~freek/courses/tt-2014/read/10.1.1.61.3041.pdf" target="_blank" title="http://www.cs.ru.nl/~freek/courses/tt-2014/read/10.1.1.61.3041.pdf">http://www.cs.ru.nl/~freek/courses/tt-2014/read/10.1.1.61.3041.pdf</a> Assia's take on the matter (which I think was Mario's source for his code)</p>

#### [ Kevin Buzzard (Jun 11 2018 at 18:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127907285):
<p>in fact I know it was Mario's source for the code because I've just noticed that it says this in the comments at the top.</p>

#### [ Kevin Buzzard (Jun 12 2018 at 11:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127945351):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">ring</span>
<span class="kn">variables</span> <span class="o">(</span><span class="n">R</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">[</span><span class="n">comm_ring</span> <span class="n">R</span><span class="o">]</span>

<span class="kn">example</span> <span class="o">(</span><span class="n">a</span> <span class="n">b</span> <span class="o">:</span> <span class="n">R</span><span class="o">)</span> <span class="o">:</span>
  <span class="n">a</span> <span class="bp">*</span> <span class="o">(</span><span class="n">b</span> <span class="bp">*</span> <span class="n">b</span><span class="o">)</span> <span class="bp">+</span> <span class="o">(</span><span class="n">b</span> <span class="bp">*</span> <span class="o">(</span><span class="n">a</span> <span class="bp">*</span> <span class="n">a</span><span class="o">)</span> <span class="bp">+</span> <span class="o">(</span><span class="n">b</span> <span class="bp">*</span> <span class="o">(</span><span class="n">b</span> <span class="bp">*</span> <span class="n">b</span><span class="o">)</span> <span class="bp">+</span> <span class="o">(</span><span class="n">a</span> <span class="bp">*</span> <span class="o">(</span><span class="mi">2</span> <span class="bp">*</span> <span class="n">a</span> <span class="bp">*</span> <span class="n">b</span><span class="o">)</span> <span class="bp">+</span> <span class="n">b</span> <span class="bp">*</span> <span class="o">(</span><span class="mi">2</span> <span class="bp">*</span> <span class="n">a</span> <span class="bp">*</span> <span class="n">b</span><span class="o">))))</span> <span class="bp">=</span>
  <span class="n">b</span> <span class="bp">*</span> <span class="o">(</span><span class="n">b</span> <span class="bp">*</span> <span class="n">b</span><span class="o">)</span> <span class="bp">+</span> <span class="o">(</span><span class="mi">3</span> <span class="bp">*</span> <span class="n">a</span> <span class="bp">*</span> <span class="o">(</span><span class="n">b</span> <span class="bp">*</span> <span class="n">b</span><span class="o">)</span> <span class="bp">+</span> <span class="mi">3</span> <span class="bp">*</span> <span class="o">(</span><span class="n">a</span> <span class="bp">*</span> <span class="n">a</span><span class="o">)</span> <span class="bp">*</span> <span class="n">b</span><span class="o">)</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">ring</span><span class="o">,</span>
  <span class="c1">-- goal now (b * a + (2 * b * a + 3 * b ^ 2)) * a + b ^ 3 = (3 * b * a + 3 * b ^ 2) * a + b ^ 3</span>
  <span class="n">simp</span><span class="o">,</span>
  <span class="c1">-- goal now (b * a + (2 * b * a + 3 * b ^ 2)) * a = (3 * b * a + 3 * b ^ 2) * a</span>
  <span class="n">ring</span> <span class="c1">-- works</span>
<span class="kn">end</span>
</pre></div>

#### [ Kevin Buzzard (Jun 12 2018 at 11:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127945353):
<div class="codehilite"><pre><span></span>elaboration: tactic execution took 2.23s
num. allocated objects:  8522
num. allocated closures: 2163
 2229ms   100.0%   scope_trace
 2229ms   100.0%   tactic.istep._lambda_1
 2229ms   100.0%   tactic.istep
 2229ms   100.0%   tactic.step
 2229ms   100.0%   _interaction._lambda_2
 1987ms    89.1%   interaction_monad_orelse
 1929ms    86.5%   tactic.ring.eval
 1156ms    51.9%   tactic.interactive.ring1
 1156ms    51.9%   tactic.interactive.ring._lambda_1
 1156ms    51.9%   tactic.interactive.ring
 1057ms    47.4%   tactic.ring.eval_mul
</pre></div>

#### [ Kevin Buzzard (Jun 12 2018 at 11:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127945354):
<p>etc etc</p>

#### [ Kevin Buzzard (Jun 12 2018 at 11:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127945358):
<p>This tactic doesn't quite work yet as far as I can see.</p>

#### [ Kevin Buzzard (Jun 12 2018 at 11:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127945366):
<p>(noticable pause in <code>ring</code> whilst it's failing to prove it the first time)</p>

#### [ Kevin Buzzard (Jun 12 2018 at 11:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127945407):
<p>But I want to fix it.</p>

#### [ Kevin Buzzard (Jun 12 2018 at 11:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127945415):
<p>I re-read the "rings done right" paper and I understood _much_ more of it this time around.</p>

#### [ Kevin Buzzard (Jun 12 2018 at 11:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127945427):
<p>One insight which dawned on me is that there are two completely different issues involved with writing a ring tactic. Maybe everyone else is aware of this.</p>

#### [ Kevin Buzzard (Jun 12 2018 at 11:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127945430):
<p>Let me explain my understanding of what the ring tactic does.</p>

#### [ Kevin Buzzard (Jun 12 2018 at 11:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127945444):
<p>Let's say <code>d : int</code> and we want to prove <code>d^2 + 2*d + 1 = (d+1)^2</code></p>

#### [ Kevin Buzzard (Jun 12 2018 at 11:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127945497):
<p>If we want to prove this using <code>ring</code> then we are saying "this is not true because of something specific to int, this is a general fact about rings"</p>

#### [ Kevin Buzzard (Jun 12 2018 at 11:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127945501):
<p>So what we actually want to do is to prove that <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msup><mi>X</mi><mn>2</mn></msup><mo>+</mo><mn>2</mn><mi>X</mi><mo>+</mo><mn>1</mn><mo>=</mo><mo>(</mo><mi>X</mi><mo>+</mo><mn>1</mn><msup><mo>)</mo><mn>2</mn></msup></mrow><annotation encoding="application/x-tex">X^2+2X+1=(X+1)^2</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.8141079999999999em;"></span><span class="strut bottom" style="height:1.064108em;vertical-align:-0.25em;"></span><span class="base"><span class="mord"><span class="mord mathit" style="margin-right:0.07847em;">X</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.8141079999999999em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathrm mtight">2</span></span></span></span></span></span></span></span><span class="mbin">+</span><span class="mord mathrm">2</span><span class="mord mathit" style="margin-right:0.07847em;">X</span><span class="mbin">+</span><span class="mord mathrm">1</span><span class="mrel">=</span><span class="mopen">(</span><span class="mord mathit" style="margin-right:0.07847em;">X</span><span class="mbin">+</span><span class="mord mathrm">1</span><span class="mclose"><span class="mclose">)</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.8141079999999999em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathrm mtight">2</span></span></span></span></span></span></span></span></span></span></span> in <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mrow><mi mathvariant="double-struck">Z</mi></mrow><mo>[</mo><mi>X</mi><mo>]</mo></mrow><annotation encoding="application/x-tex">\mathbb{Z}[X]</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mord"><span class="mord mathbb">Z</span></span><span class="mopen">[</span><span class="mord mathit" style="margin-right:0.07847em;">X</span><span class="mclose">]</span></span></span></span></p>

#### [ Kevin Buzzard (Jun 12 2018 at 11:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127945513):
<p>and then deduce our goal by specialising to <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>X</mi><mo>=</mo><mi>d</mi></mrow><annotation encoding="application/x-tex">X=d</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.69444em;"></span><span class="strut bottom" style="height:0.69444em;vertical-align:0em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.07847em;">X</span><span class="mrel">=</span><span class="mord mathit">d</span></span></span></span></p>

#### [ Kevin Buzzard (Jun 12 2018 at 11:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127945521):
<p>This makes it clear what we have to do here.</p>

#### [ Kevin Buzzard (Jun 12 2018 at 11:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127945565):
<p>First we need to build a new type in Lean corresponding to polynomials in one variable</p>

#### [ Kevin Buzzard (Jun 12 2018 at 11:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127945572):
<p>or more generally, if we want to prove stuff like <code>(a+b)^2=a^2+2*a*b+b^2</code> for ints a,b</p>

#### [ Kevin Buzzard (Jun 12 2018 at 11:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127945576):
<p>we will need polynomials in a finite set of variables.</p>

#### [ Kevin Buzzard (Jun 12 2018 at 11:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127945580):
<p>Of course Lean has these.</p>

#### [ Kevin Buzzard (Jun 12 2018 at 11:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127945588):
<p>Once we have this new type, we need to prove an "evaluation theorem", saying that if <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>f</mi><mo>(</mo><mi>X</mi><mo>)</mo><mo>=</mo><mi>g</mi><mo>(</mo><mi>X</mi><mo>)</mo></mrow><annotation encoding="application/x-tex">f(X)=g(X)</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.10764em;">f</span><span class="mopen">(</span><span class="mord mathit" style="margin-right:0.07847em;">X</span><span class="mclose">)</span><span class="mrel">=</span><span class="mord mathit" style="margin-right:0.03588em;">g</span><span class="mopen">(</span><span class="mord mathit" style="margin-right:0.07847em;">X</span><span class="mclose">)</span></span></span></span> in our polynomial ring</p>

#### [ Kevin Buzzard (Jun 12 2018 at 11:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127945589):
<p>then <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>f</mi><mo>(</mo><mi>d</mi><mo>)</mo><mo>=</mo><mi>g</mi><mo>(</mo><mi>d</mi><mo>)</mo></mrow><annotation encoding="application/x-tex">f(d)=g(d)</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.10764em;">f</span><span class="mopen">(</span><span class="mord mathit">d</span><span class="mclose">)</span><span class="mrel">=</span><span class="mord mathit" style="margin-right:0.03588em;">g</span><span class="mopen">(</span><span class="mord mathit">d</span><span class="mclose">)</span></span></span></span> in int</p>

#### [ Kevin Buzzard (Jun 12 2018 at 11:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127945634):
<p>Along the way it would be natural to prove things like <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>f</mi><mo>(</mo><mi>d</mi><mo>)</mo><mo>+</mo><mi>g</mi><mo>(</mo><mi>d</mi><mo>)</mo><mo>=</mo><mo>(</mo><mi>f</mi><mo>+</mo><mi>g</mi><mo>)</mo><mo>(</mo><mi>d</mi><mo>)</mo></mrow><annotation encoding="application/x-tex">f(d)+g(d)=(f+g)(d)</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.10764em;">f</span><span class="mopen">(</span><span class="mord mathit">d</span><span class="mclose">)</span><span class="mbin">+</span><span class="mord mathit" style="margin-right:0.03588em;">g</span><span class="mopen">(</span><span class="mord mathit">d</span><span class="mclose">)</span><span class="mrel">=</span><span class="mopen">(</span><span class="mord mathit" style="margin-right:0.10764em;">f</span><span class="mbin">+</span><span class="mord mathit" style="margin-right:0.03588em;">g</span><span class="mclose">)</span><span class="mopen">(</span><span class="mord mathit">d</span><span class="mclose">)</span></span></span></span> and so on</p>

#### [ Kevin Buzzard (Jun 12 2018 at 11:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127945646):
<p>So we define our new polynomial type, define evaluation, prove nice properties about the evaluation map</p>

#### [ Kevin Buzzard (Jun 12 2018 at 11:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127945648):
<p>and now all that's left is the following problem:</p>

#### [ Kevin Buzzard (Jun 12 2018 at 11:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127945650):
<p>given <code>d^2+2*d+1</code> with <code>d : int</code></p>

#### [ Kevin Buzzard (Jun 12 2018 at 11:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127945653):
<p>we need to manufacture <code>X^2+2*X+1</code> in our polynomial ring type.</p>

#### [ Kevin Buzzard (Jun 12 2018 at 11:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127945714):
<p>And for this we really need to take apart <code>d^2+2*d+1</code> and see how it is built from <code>d</code> and stuff that has analogues in the polynomial ring.</p>

#### [ Kevin Buzzard (Jun 12 2018 at 11:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127945719):
<p>(+,^,2,1)</p>

#### [ Kevin Buzzard (Jun 12 2018 at 11:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127945734):
<p>and I think that it's at this point that the non-tactic-user gets stuck.</p>

#### [ Kevin Buzzard (Jun 12 2018 at 11:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127945904):
<p><span class="user-mention" data-user-id="110026">@Simon Hudon</span> Assume Lean has a working polynomial ring type <code>ZX</code> (there are some kicking around, but perhaps none in mathlib) representing polynomials with integer coefficients in one variable <code>X</code>.  Am I right in thinking that it doesn't even make sense to ask for a function (in Lean's sense) which sends <code>d^2+2*d+1</code> to <code>X^2+2*X+1</code> where <code>d : int</code> is some variable? I can't even imagine what the domain of such a function would be. On the other hand, would I be able to write a tactic which took the expression <code>d^2+2*d+1</code> as an input and spat out <code>X^2+2*X+1</code>?</p>

#### [ Kevin Buzzard (Jun 12 2018 at 11:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127945920):
<p>Or is life not even that easy?</p>

#### [ Scott Morrison (Jun 12 2018 at 12:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127947136):
<p>certainly given <code>d^2+2*d+1</code> as an <code>expr</code> (and let's say <code>d</code> is also given, as an <code>expr</code>), in meta land we can construct <code>X^2+2*X+1</code>.</p>

#### [ Scott Morrison (Jun 12 2018 at 12:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127947142):
<p>(Mario's implementation does clever things, including a representation of sparse polynomials, but if you just want the stupid version I could probably manage that function.)</p>

#### [ Simon Hudon (Jun 12 2018 at 14:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127950108):
<p>Is this simply renaming variables in the goal?</p>

#### [ Scott Morrison (Jun 12 2018 at 14:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127950557):
<p>Sorry, the example wasn't very helpful: I just meant, determine if some expression is in fact a polynomial in some other expr, and if so, present it as such in some form (list of coefficients, map of coefficients, etc).</p>

#### [ Kevin Buzzard (Jun 12 2018 at 14:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127951731):
<blockquote>
<p>Is this simply renaming variables in the goal?</p>
</blockquote>
<p><span class="user-mention" data-user-id="110026">@Simon Hudon</span> No I think it's more. X is a genuine polynomial variable, we have a type <code>ZX</code> with an inclusion from int into ZX and also some element <code>X : ZX</code> which is not in the image of <code>int</code>, it's an abstract polynomial variable</p>

#### [ Kevin Buzzard (Jun 12 2018 at 14:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127951740):
<p><span class="user-mention" data-user-id="110087">@Scott Morrison</span> do we _have_ to do this in meta-land?</p>

#### [ Simon Hudon (Jun 12 2018 at 14:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127951793):
<p>ah! i see. So a kind of parser.</p>

#### [ Kevin Buzzard (Jun 12 2018 at 14:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127951794):
<p>I can see that Mario's implementation uses "Horner form" of a polynomial, so sparse polys are handled better.</p>

#### [ Kevin Buzzard (Jun 12 2018 at 14:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127951798):
<p>Yes, I was interested in building the stupid version of tactic.ring</p>

#### [ Simon Hudon (Jun 12 2018 at 14:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127951805):
<p>Yes, I think it has to be in meta because you need access to the <code>expr</code> syntax tree</p>

#### [ Kevin Buzzard (Jun 12 2018 at 14:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127951812):
<p>What I see in Mario's file seems to me to be a construction of an abstract polynomial ring but completely in meta-land</p>

#### [ Kevin Buzzard (Jun 12 2018 at 14:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127951818):
<p>Here is a concrete question.</p>

#### [ Kevin Buzzard (Jun 12 2018 at 14:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127951823):
<p>Would it be possible to just define the polynomial ring Z[X] in "normal" Lean</p>

#### [ Kevin Buzzard (Jun 12 2018 at 14:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127951830):
<p>e.g. in a non-efficient way, using lists for coefficients</p>

#### [ Simon Hudon (Jun 12 2018 at 14:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127951837):
<p>I believe so</p>

#### [ Kevin Buzzard (Jun 12 2018 at 14:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127951841):
<p>and then write a much simpler tactic than <code>tactic/ring.lean</code></p>

#### [ Kevin Buzzard (Jun 12 2018 at 14:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127951893):
<p>which can prove statements of the form "forall d : int, (d+1)^3=d^3+3d^2+3d+1"</p>

#### [ Kevin Buzzard (Jun 12 2018 at 14:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127951901):
<p>by temporarily dipping into meta-land to construct the polynomials (X+1)^3 and X^3+3X^2+3X+1</p>

#### [ Kevin Buzzard (Jun 12 2018 at 14:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127951904):
<p>and then checking that they're equal in Z[X]</p>

#### [ Kevin Buzzard (Jun 12 2018 at 14:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127951907):
<p>and then evaluating at d</p>

#### [ Kevin Buzzard (Jun 12 2018 at 14:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127951914):
<p>and deducing the result?</p>

#### [ Kevin Buzzard (Jun 12 2018 at 14:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127951927):
<p>Or is it an essential part of the tactic.ring tactic that one builds some version of Z[X] in meta-land?</p>

#### [ Kevin Buzzard (Jun 12 2018 at 14:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127951988):
<p>It seems to me that Mario writes <code>horner</code> in normal-land and proves some lemmas about it in normal-land</p>

#### [ Kevin Buzzard (Jun 12 2018 at 14:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127952002):
<p>but the key facts are things like <code>eval_add</code>, which is meta</p>

#### [ Kevin Buzzard (Jun 12 2018 at 14:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127952175):
<p><code>eval_add</code> seems to be some sort of theorem of the form "if this expr represents f and this expr represents g, then I will return an expr plus a proof that it is the evaluation of f plus the evaluation of g"</p>

#### [ Kevin Buzzard (Jun 12 2018 at 14:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127952239):
<p>I was wondering whether one could instead use a non-expr version</p>

#### [ Simon Hudon (Jun 12 2018 at 14:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127952242):
<p>Because <code>expr</code> is in meta land, you can't do any of that stuff in non-meta land</p>

#### [ Kevin Buzzard (Jun 12 2018 at 14:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127952247):
<p>right</p>

#### [ Kevin Buzzard (Jun 12 2018 at 14:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127952253):
<p>but if I had a tactic which took d^2+2*d+1</p>

#### [ Kevin Buzzard (Jun 12 2018 at 14:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127952259):
<p>and returned X^2+2*X+1</p>

#### [ Simon Hudon (Jun 12 2018 at 14:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127952261):
<p>I see ok yes that's possible</p>

#### [ Simon Hudon (Jun 12 2018 at 14:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127952267):
<p>That's called a proof by reflection</p>

#### [ Kevin Buzzard (Jun 12 2018 at 14:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127952270):
<p>plus a proof that X^2+X+1 evaluated at d was d^2+2*d+1</p>

#### [ Kevin Buzzard (Jun 12 2018 at 14:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127952294):
<p>then it seems to me that there's a chance that I can prove d^2+2*d+1=(d+1)^2 using this tactic</p>

#### [ Kevin Buzzard (Jun 12 2018 at 15:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127952373):
<p>because I feed in both sides to the tactic</p>

#### [ Kevin Buzzard (Jun 12 2018 at 15:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127952376):
<p>prove they're equal in <code>ZX</code></p>

#### [ Kevin Buzzard (Jun 12 2018 at 15:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127952382):
<p>and deduce that their valuations are equal</p>

#### [ Kevin Buzzard (Jun 12 2018 at 15:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127952390):
<p>I am trying to get as much of the proof out of meta-land as I can</p>

#### [ Reid Barton (Jun 12 2018 at 15:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127952404):
<p>Regarding lands, have you looked at the slides on metaprogramming <a href="https://hanoifabs.files.wordpress.com/2018/05/slides.pdf" target="_blank" title="https://hanoifabs.files.wordpress.com/2018/05/slides.pdf">https://hanoifabs.files.wordpress.com/2018/05/slides.pdf</a>?</p>

#### [ Reid Barton (Jun 12 2018 at 15:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127952408):
<p>In particular page 4</p>

#### [ Kevin Buzzard (Jun 12 2018 at 15:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127952433):
<p>This is part of the reason I'm thinking about this now</p>

#### [ Kevin Buzzard (Jun 12 2018 at 15:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127952485):
<p>I have looked through all of tactic/ring.lean and all of a sudden it doesn't look as intimidating as it used ti</p>

#### [ Kevin Buzzard (Jun 12 2018 at 15:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127952486):
<p>to</p>

#### [ Kevin Buzzard (Jun 12 2018 at 15:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127952586):
<p><a href="https://github.com/kbuzzard/mathlib/blob/ring_tactic_comments/tactic/ring.lean" target="_blank" title="https://github.com/kbuzzard/mathlib/blob/ring_tactic_comments/tactic/ring.lean">https://github.com/kbuzzard/mathlib/blob/ring_tactic_comments/tactic/ring.lean</a></p>

#### [ Reid Barton (Jun 12 2018 at 15:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127952590):
<p>If you don't need access to meta-land features like general recursion or <code>expr</code> then you can stay in normal-land; and surely the theory of <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mrow><mi mathvariant="double-struck">Z</mi></mrow><mo>[</mo><mi>X</mi><mo>]</mo></mrow><annotation encoding="application/x-tex">\mathbb{Z}[X]</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mord"><span class="mord mathbb">Z</span></span><span class="mopen">[</span><span class="mord mathit" style="margin-right:0.07847em;">X</span><span class="mclose">]</span></span></span></span> doesn't need these things. On the other hand, you may want to avoid using noncomputable things if you want your tactic to, for example, be able to decide whether two polynomials in <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mrow><mi mathvariant="double-struck">Z</mi></mrow><mo>[</mo><mi>X</mi><mo>]</mo></mrow><annotation encoding="application/x-tex">\mathbb{Z}[X]</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mord"><span class="mord mathbb">Z</span></span><span class="mopen">[</span><span class="mord mathit" style="margin-right:0.07847em;">X</span><span class="mclose">]</span></span></span></span> are equal so that it can decide whether to succeed or fail.</p>

#### [ Kevin Buzzard (Jun 12 2018 at 15:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127952593):
<p>I am trying to write a comment about every definition and theorem in that link</p>

#### [ Kevin Buzzard (Jun 12 2018 at 15:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127952613):
<p>So one can certainly make Z[X], indeed it's been done several times although I don't think it's in mathlib yet</p>

#### [ Kevin Buzzard (Jun 12 2018 at 15:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127952618):
<p>The problem is the function sending d^2+2d+1 to X^2+2X+1</p>

#### [ Reid Barton (Jun 12 2018 at 15:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127952671):
<p>Right, so I guess the approach used here by <code>ring</code> is to represent a variable (which is basically something the tactic can't break down into further ring operations) by its <code>expr</code></p>

#### [ Kevin Buzzard (Jun 12 2018 at 15:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127952678):
<p>right</p>

#### [ Reid Barton (Jun 12 2018 at 15:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127952679):
<p>Here the variable is simply <code>d</code>, but it could have been more complicated, e.g. <code>sin t</code></p>

#### [ Kevin Buzzard (Jun 12 2018 at 15:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127952681):
<p>right</p>

#### [ Kevin Buzzard (Jun 12 2018 at 15:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127952683):
<p>or there could be several variables</p>

#### [ Reid Barton (Jun 12 2018 at 15:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127952755):
<p>So that must be why the <code>destruct_ty</code> thing is in <code>meta</code>, though if you wanted it to be in normal-land, you could probably just parameterize it on the expression type.</p>

#### [ Reid Barton (Jun 12 2018 at 15:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127952758):
<p>BTW, <code>_ty</code> probably just stands for "type"</p>

#### [ Kevin Buzzard (Jun 12 2018 at 15:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127952829):
<p>So completely independent of the ring tactic</p>

#### [ Kevin Buzzard (Jun 12 2018 at 15:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127952830):
<p>there is this horner thing</p>

#### [ Kevin Buzzard (Jun 12 2018 at 15:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127952832):
<p>and what seems to be going on there</p>

#### [ Kevin Buzzard (Jun 12 2018 at 15:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127952834):
<p>is that (and this is Assia's insight, or her joint insight with her co-author)</p>

#### [ Kevin Buzzard (Jun 12 2018 at 15:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127952844):
<p>storing polynomials as lists of coefficients might suck</p>

#### [ Kevin Buzzard (Jun 12 2018 at 15:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127952888):
<p>especially if you want to work out x^100 * x^100 without doing 10000 computations</p>

#### [ Kevin Buzzard (Jun 12 2018 at 15:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127952898):
<p>so they store e.g. x^100+3x^2+7 as (1*x^98+3)*x^2+7</p>

#### [ Kevin Buzzard (Jun 12 2018 at 15:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127952903):
<p>iterating the "x maps to a*x^n+b" map</p>

#### [ Kevin Buzzard (Jun 12 2018 at 15:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127952918):
<p>and so this is some sort of normal form for polynomials</p>

#### [ Kevin Buzzard (Jun 12 2018 at 15:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127952922):
<p>which we could call "horner normal form"</p>

#### [ Kevin Buzzard (Jun 12 2018 at 15:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127952925):
<p>and if you store polynomials in this way then it's a PITA to add or multiply them</p>

#### [ Kevin Buzzard (Jun 12 2018 at 15:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127952929):
<p>but this is OK because somehow this isn't the bottleneck</p>

#### [ Reid Barton (Jun 12 2018 at 15:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127952978):
<p>I see, and <code>eval_add</code> is basically implementing addition of polynomials in this form, it looks like?</p>

#### [ Kevin Buzzard (Jun 12 2018 at 15:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127952979):
<p>So one could envisage writing a second ring tactic which (a) was far less efficient and (b) worked in some situations where Mario's doesn't (because Mario's is currently buggy)</p>

#### [ Kevin Buzzard (Jun 12 2018 at 15:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127952984):
<p>where you just use lists for coefficients</p>

#### [ Kevin Buzzard (Jun 12 2018 at 15:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127953003):
<p>and then the resulting tactic file would have this extra obfuscating layer of difficulty removed</p>

#### [ Kevin Buzzard (Jun 12 2018 at 15:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127953012):
<p>and this was what got me into wondering whether I could even just use one of the already-existing polynomial ring Lean implementations</p>

#### [ Kevin Buzzard (Jun 12 2018 at 15:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127953016):
<p>instead of making Z[X] in meta-land</p>

#### [ Kevin Buzzard (Jun 12 2018 at 15:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127953098):
<blockquote>
<p>I see, and <code>eval_add</code> is basically implementing addition of polynomials in this form, it looks like?</p>
</blockquote>
<p>Yes, it's perhaps doing something clever like not just implementing addition, it's also collecting the proofs that addition commutes with evaluation, but the five lemmas before <code>eval_add</code> are precisely the five lemmas you need to add polynomials in "Horner form"</p>

#### [ Kevin Buzzard (Jun 12 2018 at 15:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127953111):
<p>You add <code>ax^n+b</code> and <code>a'x^n'+b'</code></p>

#### [ Kevin Buzzard (Jun 12 2018 at 15:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127953152):
<p>where a and a' are allowed to be polynomials in horner form</p>

#### [ Kevin Buzzard (Jun 12 2018 at 15:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127953158):
<p>and you have to do the three cases n&lt;n', n=n', n&gt;n'</p>

#### [ Kevin Buzzard (Jun 12 2018 at 15:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127953162):
<p>and then also you have to add <code>ax^n+b</code> to c where c is a constant</p>

#### [ Kevin Buzzard (Jun 12 2018 at 15:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127953163):
<p>both ways around</p>

#### [ Kevin Buzzard (Jun 12 2018 at 15:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127953168):
<p>and there's some implicit inductive type horner_form</p>

#### [ Kevin Buzzard (Jun 12 2018 at 15:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127953182):
<p>which is defined by: a constant is in horner_form, and if a is in horner_form then so is a*x^n+b</p>

#### [ Kevin Buzzard (Jun 12 2018 at 15:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127953187):
<p>and then every polynomial has a canonical horner form</p>

#### [ Kevin Buzzard (Jun 12 2018 at 15:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127953198):
<p>and also perhaps some non-canonical ones</p>

#### [ Kevin Buzzard (Jun 12 2018 at 15:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127953343):
<p>I haven't got down as far as <code>normalize</code> but this might be the function which puts something in horner form into its normalised state (which you need because you need an algorithm for figuring out when two polynomials are equal)</p>

#### [ Reid Barton (Jun 12 2018 at 15:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127953437):
<blockquote>
<p>and this was what got me into wondering whether I could even just use one of the already-existing polynomial ring Lean implementations</p>
</blockquote>
<p>I don't see why not. Probably you can even use the one in <code>linear_algebra.multivariate_polynomial</code></p>

#### [ Kevin Buzzard (Jun 12 2018 at 15:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127953586):
<p>You understand that I am not looking for some sort of uber-efficient ring tactic, like the one Mario wrote. I am trying to see in some sense what the minimal amount of work would be, if I wanted to write a more inefficient ring tactic of my own</p>

#### [ Kevin Buzzard (Jun 12 2018 at 15:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127953590):
<p>and the more I can get out of meta-land the better</p>

#### [ Kevin Buzzard (Jun 12 2018 at 15:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127953599):
<p>Even for just equations involving one unknown, I would be interested</p>

#### [ Kevin Buzzard (Jun 12 2018 at 15:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127953672):
<p>not least because <code>example (d : ℕ) : d^2+2*d+1=(d+1)^2 := by ring </code> currently fails and rather than pestering Mario I thought it would be an interesting exercise to try and work out why.</p>

#### [ Reid Barton (Jun 12 2018 at 15:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127953697):
<p>Yes, I think a <code>ring</code> tactic optimized for simplicity would be valuable as a demonstration of how to write similar tactics, as well.</p>

#### [ Kevin Buzzard (Jun 12 2018 at 15:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127954108):
<p>Well maybe that's where this thread is going.</p>

#### [ Mario Carneiro (Jun 12 2018 at 15:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127954256):
<p>I'm not sure you can actually save that much work with a dumber <code>ring</code> tactic</p>

#### [ Mario Carneiro (Jun 12 2018 at 15:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127954307):
<p>Probably using dense polynomial representation is a bit easier, but I don't think proof by reflection is easier (although more of it can be verified)</p>

#### [ Mario Carneiro (Jun 12 2018 at 15:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127954313):
<p>but precisely because more of it is verified, there is more work to do</p>

#### [ Mario Carneiro (Jun 12 2018 at 15:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127954331):
<p>If <code>expr</code> was not meta, almost all of the ring tactic could be non-meta</p>

#### [ Simon Hudon (Jun 12 2018 at 15:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127954389):
<p>Do you know if there's any plan to make <code>expr</code> non-meta?</p>

#### [ Mario Carneiro (Jun 12 2018 at 15:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127954397):
<p>I have not investigated the <code>ring</code> bug, but one way to find out what is happening is to insert type checks in <code>eval_add</code> and such</p>

#### [ Reid Barton (Jun 12 2018 at 15:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127954407):
<p>By "simple", I really mean "easy to understand"</p>

#### [ Reid Barton (Jun 12 2018 at 15:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127954409):
<p>not necessarily short</p>

#### [ Mario Carneiro (Jun 12 2018 at 15:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127954412):
<p>There is no plan to make <code>expr</code> non-meta, and in fact I attempted such a plan and was rebuffed several months ago</p>

#### [ Mario Carneiro (Jun 12 2018 at 15:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127954463):
<p>The likely alternative is to have a mirror copy of <code>expr</code> that is non-meta</p>

#### [ Mario Carneiro (Jun 12 2018 at 15:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127954469):
<p>which would have to avoid certain meta things like macros</p>

#### [ Kevin Buzzard (Jun 12 2018 at 16:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127954787):
<blockquote>
<p>I'm not sure you can actually save that much work with a dumber <code>ring</code> tactic</p>
</blockquote>
<p>Yes, as Reid says, I'm not worried about work, I'm attempting to understand tactics in a way other than "read Programming In Lean again".</p>

#### [ Kevin Buzzard (Jun 12 2018 at 16:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127954848):
<p>The only other way I can think of is "read some tactic code and see if you can understand it, and see what questions arise because of it"</p>

#### [ Kevin Buzzard (Jun 12 2018 at 16:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127954852):
<p>and that's why I find myself in this thread</p>

#### [ Kevin Buzzard (Jun 12 2018 at 16:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127954862):
<p>One question: which is best? Documenting ring.lean like this <a href="https://github.com/kbuzzard/mathlib/blob/ring_tactic_comments/tactic/ring.lean" target="_blank" title="https://github.com/kbuzzard/mathlib/blob/ring_tactic_comments/tactic/ring.lean">https://github.com/kbuzzard/mathlib/blob/ring_tactic_comments/tactic/ring.lean</a></p>

#### [ Kevin Buzzard (Jun 12 2018 at 16:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127954873):
<p>or writing a stand-alone file with comments like this <a href="https://github.com/kbuzzard/mathlib/blob/tactic_doc/docs/ring_tactic.rst" target="_blank" title="https://github.com/kbuzzard/mathlib/blob/tactic_doc/docs/ring_tactic.rst">https://github.com/kbuzzard/mathlib/blob/tactic_doc/docs/ring_tactic.rst</a></p>

#### [ Kevin Buzzard (Jun 12 2018 at 16:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127954883):
<p>I currently find myself doing both</p>

#### [ Kevin Buzzard (Jun 12 2018 at 16:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127954892):
<p>As long as I get to the bottom using one method, I am sure I will have learnt a lot</p>

#### [ Kevin Buzzard (Jun 12 2018 at 16:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127954939):
<p>Currently the "adding comments to ring.lean" approach is winning</p>

#### [ Kevin Buzzard (Jun 12 2018 at 16:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127954988):
<p>but the waffle above about writing a simpler version -- which to be honest could I think turn into a great tutorial on how to write tactics, if we implement polynomials in one variable using some dumb list method or, even better, perhaps using some already-implemented method</p>

#### [ Kevin Buzzard (Jun 12 2018 at 16:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127955058):
<p>Maybe that's the goal of this thread. To write an  as-stupid-as-possible ring tactic which attempts to have as little in meta-land as possible, and then stick it up on my blog as some sort of tactic tutorial as an alternative for people to read</p>

#### [ Kevin Buzzard (Jun 12 2018 at 16:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127955071):
<p>Next term I'll be supervising a Masters project on how to write tactics so I'd better get my act together and learn it myself</p>

#### [ Kevin Buzzard (Jun 12 2018 at 16:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127955085):
<p>The student in question is currently doing an internship at INRIA learning how to do it in Coq so I'm hoping that they will learn quickly and then teach me</p>

#### [ Mario Carneiro (Jun 12 2018 at 17:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127957753):
<p>Maybe this will help: There is an implicit inductive type <code>horner_form_expr</code> with the following definition:</p>
<div class="codehilite"><pre><span></span>meta inductive horner_form_expr : Type
| const : expr → horner_form_expr
| horner (a : horner_form_expr) (x : expr) (n : nat) (b : horner_form_expr) : horner_form_expr
</pre></div>


<p>The job of <code>eval_add</code> and the other definitions is to rewrite any <code>expr</code> into a <code>horner_form_expr</code>. However, since <code>horner_form_expr</code> can be represented as an <code>expr</code>, the actual inductive type is omitted to avoid the overhead of converting back and forth. Furthermore, there is a normal form requirement, that says that the <code>x</code> expression must be lex_lt less than any other expressions in <code>x</code> slots of the <code>b</code> subtree.</p>

#### [ Mario Carneiro (Jun 12 2018 at 17:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127957847):
<p><code>destruct</code> is effectively the <code>cases_on</code> for this inductive type</p>

#### [ Kevin Buzzard (Jun 12 2018 at 17:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127959658):
<p>Right -- I had basically figured this out. But you see, in some educational blog post about this stuff you could put this type in, and furthermore make it work in a more stupid way using lists of coefficients. What I am still not clear about is whethet you can get away with making it not meta (and hence get away with not actually writing it at all, because it's already written)</p>

#### [ Kevin Buzzard (Jun 12 2018 at 17:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127959693):
<p>Because you're in meta-land you can just not even define the type, you can <code>destruct</code> it _assuming_ that it's in this form, and if it's not then big deal, things have gone wrong, just return <code>none</code></p>

#### [ Mario Carneiro (Jun 12 2018 at 17:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127959786):
<p>You can't make it non-meta and still retain the <code>x</code> payloads, which have to be kept as is as exprs</p>

#### [ Kevin Buzzard (Jun 12 2018 at 17:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127959808):
<p>My idea was to have a meta function sending d^2+2d+1 to X^2+2X+1</p>

#### [ Mario Carneiro (Jun 12 2018 at 17:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127959809):
<p>unless maybe you write them down somewhere else and only keep pointers to them in your non-meta data structure (i.e. indexes into a list of exprs)</p>

#### [ Mario Carneiro (Jun 12 2018 at 17:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127959864):
<p>which I guess is similar to your Z[X] suggestion</p>

#### [ Kevin Buzzard (Jun 12 2018 at 17:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127959867):
<p>The tactic would only work for goals with one unknown</p>

#### [ Mario Carneiro (Jun 12 2018 at 17:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127959874):
<p>but you have to remember these are multivariate polynomials</p>

#### [ Kevin Buzzard (Jun 12 2018 at 17:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127959877):
<p>I know yours are</p>

#### [ Kevin Buzzard (Jun 12 2018 at 17:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127959881):
<p>but I am suggesting writing a simplified version</p>

#### [ Kevin Buzzard (Jun 12 2018 at 17:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127959895):
<p>I want to isolate the "now here we have to write some meta stuff" and make it as small as possible</p>

#### [ Mario Carneiro (Jun 12 2018 at 17:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127959898):
<p>If you take <code>d</code> as an input, then there are lots of bad exprs now</p>

#### [ Mario Carneiro (Jun 12 2018 at 17:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127959906):
<p>In my approach, there aren't any bad exprs because anything it doesn't understand becomes a new atom</p>

#### [ Kevin Buzzard (Jun 12 2018 at 17:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127959948):
<p>I know your approach is better at getting things done</p>

#### [ Kevin Buzzard (Jun 12 2018 at 17:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127959956):
<p>I am happy to let both d and Z be inputs</p>

#### [ Mario Carneiro (Jun 12 2018 at 17:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127959964):
<p>but you want to have only one atom</p>

#### [ Kevin Buzzard (Jun 12 2018 at 17:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127959966):
<p>right</p>

#### [ Kevin Buzzard (Jun 12 2018 at 17:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127959969):
<p>and I want to store polynomials as lists</p>

#### [ Kevin Buzzard (Jun 12 2018 at 17:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127959974):
<p>these facts are not unrelated</p>

#### [ Mario Carneiro (Jun 12 2018 at 17:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127959987):
<p>what happens if I pass <code>d^2+x</code> to your function?</p>

#### [ Kevin Buzzard (Jun 12 2018 at 17:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127960000):
<p>my function will fail</p>

#### [ Kevin Buzzard (Jun 12 2018 at 17:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127960005):
<p>because my function is there to teach people how to write tactics</p>

#### [ Kevin Buzzard (Jun 12 2018 at 17:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127960006):
<p>not to actually be used in the wild</p>

#### [ Kevin Buzzard (Jun 12 2018 at 17:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127960013):
<p>I am writing code for a completely different reason to probably any code you ever wrote</p>

#### [ Kevin Buzzard (Jun 12 2018 at 17:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127960015):
<p>I am writing code to teach my students that tactics are not scary</p>

#### [ Kevin Buzzard (Jun 12 2018 at 17:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127960060):
<p>which is not the impression you get when reading PIL</p>

#### [ Mario Carneiro (Jun 12 2018 at 17:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127960068):
<p>Okay, let me think about this</p>

#### [ Mario Carneiro (Jun 12 2018 at 17:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127960076):
<p>In the mean time, the <code>ring</code> bug has been fixed.</p>

#### [ Kevin Buzzard (Jun 12 2018 at 17:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127960078):
<p>:D</p>

#### [ Kevin Buzzard (Jun 12 2018 at 17:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127960086):
<p>OK so forget this thread, main goal achieved ;-)</p>

#### [ Mario Carneiro (Jun 12 2018 at 17:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127960091):
<p>The problem was in <code>horner_add_horner_lt</code> (and <code>gt</code>). Suppose we are adding <code>(a1 * x^n1 + b1) + (a2 * x^n2 + b2)</code> where <code>n1 &gt; n2</code></p>

#### [ Kevin Buzzard (Jun 12 2018 at 17:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127960097):
<p>dammit I even looked at that function!</p>

#### [ Mario Carneiro (Jun 12 2018 at 17:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127960099):
<p>It's funny, the theorem is not wrong</p>

#### [ Mario Carneiro (Jun 12 2018 at 17:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127960146):
<p>but it doesn't normalize like it should</p>

#### [ Kevin Buzzard (Jun 12 2018 at 17:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127960148):
<p>in fact that's exactly the point I'm up to</p>

#### [ Kevin Buzzard (Jun 12 2018 at 17:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127960156):
<p><code>/-- This non-meta theorem just says a₁x^n₁+b₁+a₂x^(n₁+k)+b₂=(a₂x^k+a₁)x^n₁+(b₁+b₂) -/</code></p>

#### [ Andrew Ashworth (Jun 12 2018 at 17:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127960189):
<p>I think this is a great idea. It took me some time to understand reflection in Lean. Unfortunately, translating Chlipala's section on it (in CPDT) from Coq to Lean is quite difficult. So a "Lean-first" tutorial would be great.</p>

#### [ Mario Carneiro (Jun 12 2018 at 17:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127960192):
<p>The current implementation normalizes <code>b1 + b2 = b'</code>, calculates <code>k</code> such that <code>n2 + k = n1</code>, and then outputs the normal form <code>(a1 * x^k + a2) * x^n2 + b'</code></p>

#### [ Kevin Buzzard (Jun 12 2018 at 17:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127960249):
<p>yeah (modulo the fact that the (1,2) notation is switched in this thread from the conventions used in the actual code)</p>

#### [ Mario Carneiro (Jun 12 2018 at 17:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127960250):
<p>However, <code>a1 * x^k + a2</code> is not necessarily in normal form</p>

#### [ Kevin Buzzard (Jun 12 2018 at 17:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127960258):
<p>because x might not be lt the monomials showing up in a1?</p>

#### [ Mario Carneiro (Jun 12 2018 at 17:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127960276):
<p>Yes. In particular, <code>x</code> might appear in <code>a2</code></p>

#### [ Kevin Buzzard (Jun 12 2018 at 17:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127960282):
<p>or a1</p>

#### [ Kevin Buzzard (Jun 12 2018 at 17:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127960285):
<p>;-)</p>

#### [ Mario Carneiro (Jun 12 2018 at 17:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127960288):
<p>that's okay</p>

#### [ Kevin Buzzard (Jun 12 2018 at 17:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127960331):
<p>not when you switch it so your algebra is correct ;-)</p>

#### [ Kevin Buzzard (Jun 12 2018 at 17:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127960352):
<p>[you only did half the editing job]</p>

#### [ Mario Carneiro (Jun 12 2018 at 17:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127960365):
<p>the whole point of factorizing <code>a1 * x^k + a2</code> is that <code>a2</code> has no <code>x</code>'s and <code>a1</code> has all the high order terms</p>

#### [ Kevin Buzzard (Jun 12 2018 at 17:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127960372):
<p>a2 * x^k + a1</p>

#### [ Kevin Buzzard (Jun 12 2018 at 17:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127960388):
<p>I think this part of the thread is now beyond saving</p>

#### [ Kevin Buzzard (Jun 12 2018 at 17:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127960396):
<p>but I think we both know what the other is saying :-)</p>

#### [ Mario Carneiro (Jun 12 2018 at 17:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127960460):
<p>fixed</p>

#### [ Mario Carneiro (Jun 12 2018 at 17:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127960468):
<p>I actually noticed the problem in <code>gt</code>, but I was translating to the symmetric version and got confused</p>

#### [ Mario Carneiro (Jun 12 2018 at 17:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127960525):
<p>(in this thread, that's not the bug)</p>

#### [ Kevin Buzzard (Jun 12 2018 at 17:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127960552):
<p>[I posted my docstring for <code>lt</code>, but you are talking about <code>gt</code>, so now all is right with the world]</p>

#### [ Kevin Buzzard (Jun 12 2018 at 17:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127960559):
<p>Right, so let's focus on <code>gt</code></p>

#### [ Mario Carneiro (Jun 12 2018 at 17:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127960560):
<p>the bug is that since both <code>a1</code> and <code>a2</code> can contain <code>x</code>, we have a separate subproblem now, to normalize <code>(a1 * x^k + 0) + a2 = a'</code> and then output <code>a' * x^n2+ b'</code></p>

#### [ Kevin Buzzard (Jun 12 2018 at 17:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127960566):
<p><code>/-- This non-meta theorem just says a₁x^(n₂+k)+b₁+a₂x^n₂+b₂=(a₁x^k+a₂)x^n₂+(b₁+b₂) -/</code></p>

#### [ Mario Carneiro (Jun 12 2018 at 17:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127960611):
<p>so I did that and now it works</p>

#### [ Mario Carneiro (Jun 12 2018 at 17:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127960615):
<p>I'm compiling now, I'll post it soon</p>

#### [ Kevin Buzzard (Jun 12 2018 at 17:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127960626):
<p>I would have liked to find this bug</p>

#### [ Kevin Buzzard (Jun 12 2018 at 17:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127960636):
<p>Because you're in meta mode you don't have to be super-anal about making sure everything is in canonical form</p>

#### [ Kevin Buzzard (Jun 12 2018 at 17:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127960648):
<p>you just write procedural code which is supposed to do it</p>

#### [ Kevin Buzzard (Jun 12 2018 at 18:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127960715):
<p><span class="user-mention" data-user-id="110025">@Andrew Ashworth</span> I did the introductory compiler exercise in CPDT, in Lean, over the weekend.</p>

#### [ Mario Carneiro (Jun 12 2018 at 18:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127960717):
<p>I'll help you with a tutorial ring tactic later</p>

#### [ Mario Carneiro (Jun 12 2018 at 18:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127960732):
<p>But one thing to be careful about is if you do too much non-meta, you might actually end up writing a tactic that does proof by reflection which is a completely different method</p>

#### [ Kevin Buzzard (Jun 12 2018 at 18:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127960757):
<p>reflection is _different_? I thought that it was somehow some fundamental principle which was used everywhere?</p>

#### [ Mario Carneiro (Jun 12 2018 at 18:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127960760):
<p><code>ring</code> is an example of how to write tactics that build proofs by induction, but it's hard to do that non-meta</p>

#### [ Mario Carneiro (Jun 12 2018 at 18:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127960901):
<p>One way to see the difference is in the proof: A tactic that does proofs by meta-induction produces proofs that get longer as the theorem gets harder to prove, but a proof by reflection is relatively short, with the generated proof being proportional to the <em>statement</em> in length</p>

#### [ Mario Carneiro (Jun 12 2018 at 18:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127960916):
<p>Proofs by reflection are characterized by a "heavy" <code>rfl</code> proof somewhere in the middle</p>

#### [ Mario Carneiro (Jun 12 2018 at 18:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127960934):
<p><code>ring</code> produces no heavy steps, every single theorem applied exactly matches the type it should have</p>

#### [ Mario Carneiro (Jun 12 2018 at 18:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127960981):
<p>so the kernel never has to do any definitional reduction</p>

#### [ Kevin Buzzard (Jun 12 2018 at 18:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127961459):
<p>This is all very instructive and quite different from the PIL stuff which, inevitably,  is skewed towards CS applications</p>

#### [ Mario Carneiro (Jun 12 2018 at 19:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127964820):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> Here's a toy version of <code>ring</code> that works using computational reflection:</p>
<div class="codehilite"><pre><span></span>import tactic.basic data.num.lemmas

namespace ring_tac
open tactic

@[derive has_reflect]
inductive ring_expr : Type
| add : ring_expr → ring_expr → ring_expr
| mul : ring_expr → ring_expr → ring_expr
| const : znum → ring_expr
| X : ring_expr

meta def reflect_expr (X : expr) : expr → option ring_expr
| `(%%e₁ + %%e₂) := do
  p₁ ← reflect_expr e₁,
  p₂ ← reflect_expr e₂,
  return (ring_expr.add p₁ p₂)
| `(%%e₁ * %%e₂) := do
  p₁ ← reflect_expr e₁,
  p₂ ← reflect_expr e₂,
  return (ring_expr.mul p₁ p₂)
| e := if e = X then return ring_expr.X else
  do n ← expr.to_int e,
     return (ring_expr.const (znum.of_int&#39; n))

def poly := list znum

def poly.add : poly → poly → poly := λ _ _, []
def poly.mul : poly → poly → poly := λ _ _, []
def poly.const : znum → poly := sorry
def poly.X : poly := sorry

def to_poly : ring_expr → poly
| (ring_expr.add e₁ e₂) := (to_poly e₁).add (to_poly e₂)
| (ring_expr.mul e₁ e₂) := (to_poly e₁).mul (to_poly e₂)
| (ring_expr.const z) := poly.const z
| ring_expr.X := poly.X

def poly.eval {α} [comm_ring α] (X : α) : poly → α
| [] := 0
| (n::l) := n + X * poly.eval l

@[simp] theorem poly.eval_add {α} [comm_ring α] (X : α) : ∀ p₁ p₂ : poly,
  (p₁.add p₂).eval X = p₁.eval X + p₂.eval X := sorry

@[simp] theorem poly.eval_mul {α} [comm_ring α] (X : α) : ∀ p₁ p₂ : poly,
  (p₁.mul p₂).eval X = p₁.eval X * p₂.eval X := sorry

@[simp] theorem poly.eval_const {α} [comm_ring α] (X : α) : ∀ n : znum,
  (poly.const n).eval X = n := sorry

@[simp] theorem poly.eval_X {α} [comm_ring α] (X : α) : poly.X.eval X = X := sorry

def ring_expr.eval {α} [comm_ring α] (X : α) : ring_expr → α
| (ring_expr.add e₁ e₂) := e₁.eval + e₂.eval
| (ring_expr.mul e₁ e₂) := e₁.eval * e₂.eval
| (ring_expr.const z) := z
| ring_expr.X := X

theorem to_poly_eval {α} [comm_ring α] (X : α) (e) : (to_poly e).eval X = e.eval X :=
by induction e; simp [to_poly, ring_expr.eval, *]

theorem main_thm {α} [comm_ring α] (X : α) (e₁ e₂) {x₁ x₂}
  (H : to_poly e₁ = to_poly e₂) (R1 : e₁.eval X = x₁) (R2 : e₂.eval X = x₂) : x₁ = x₂ :=
by rw [← R1, ← R2, ← to_poly_eval, H, to_poly_eval]

meta def ring_tac (X : pexpr) : tactic unit := do
  X ← to_expr X,
  `(%%x₁ = %%x₂) ← target,
  r₁ ← reflect_expr X x₁,
  r₂ ← reflect_expr X x₂,
  let e₁ : expr := reflect r₁,
  let e₂ : expr := reflect r₂,
  `[refine main_thm %%X %%e₁ %%e₂ rfl _ _],
  all_goals `[simp only [ring_expr.eval,
    znum.cast_pos, znum.cast_neg, znum.cast_zero&#39;,
    pos_num.cast_bit0, pos_num.cast_bit1,
    pos_num.cast_one&#39;]]

example (x : ℤ) : (x + 1) * (x + 1) = x*x+2*x+1 :=
by do ring_tac ```(x)

end ring_tac
</pre></div>

#### [ Mario Carneiro (Jun 12 2018 at 19:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127964879):
<p>I have left the exercise of defining <code>poly.add</code>, <code>poly.mul</code>, <code>poly.const</code> and <code>poly.X</code>, and proving correctness of the functions in the <code>eval_*</code> theorems (all non-meta), to you.</p>

#### [ Mario Carneiro (Jun 12 2018 at 19:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127964910):
<p>Here the "heavy <code>rfl</code>" step is the <code>rfl</code> proof in <code>main_thm</code></p>

#### [ Mario Carneiro (Jun 12 2018 at 19:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127964970):
<p>you will need the mathlib update that just appeared</p>

#### [ Kevin Buzzard (Jun 12 2018 at 21:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127971021):
<p>wooah many thanks Mario!</p>

#### [ Kevin Buzzard (Jun 12 2018 at 22:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127972171):
<p><code>example (a b : int) : (a+b)^11=a^11 + 11*b*a^10 + 55*b^2*a^9 + 165*b^3*a^8 + 330*b^4*a^7 + 462*b^5*a^6 + 462*b^6*a^5 + 330*b^7*a^4 + 165*b^8*a^3 + 55*b^9*a^2 + 11*b^10*a + b^11:= by ring</code></p>

#### [ Kevin Buzzard (Jun 12 2018 at 22:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127972173):
<p>but 12 times out :-)</p>

#### [ Kevin Buzzard (Jun 12 2018 at 22:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127972177):
<p>[this is of course the official ring, not the one above]</p>

#### [ Kevin Buzzard (Jun 12 2018 at 22:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127972228):
<p><code>example (a b : int) : (a+b)^12=a^12 + 12*b*a^11 + 66*b^2*a^10 + 220*b^3*a^9 + 495*b^4*a^8 + 792*b^5*a^7 + 924*b^6*a^6 + 792*b^7*a^5 + 495*b^8*a^4 + 220*b^9*a^3 + 66*b^10*a^2 + 12*b^11*a + b^12:= by ring -- deterministic timeout</code></p>

#### [ Johan Commelin (Jun 12 2018 at 22:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127973037):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> So you need to teach <code>ring</code> about Chris's binomial theorem!</p>

#### [ Kevin Buzzard (Jun 13 2018 at 00:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127977028):
<p>Well, I'm not sure I would use Lean to check the binomial theorem for n=12 :-)</p>

#### [ Kevin Buzzard (Jun 13 2018 at 00:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127977076):
<p>Ironically I fired up pari-gp and computed (a+b)^12 in a gazillionth of a second and then cut and pasted the output into Lean in order to see if it could do something which I already had a much better tool for.</p>

#### [ Kevin Buzzard (Jun 13 2018 at 01:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127979328):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">tactic</span><span class="bp">.</span><span class="n">basic</span> <span class="n">data</span><span class="bp">.</span><span class="n">num</span><span class="bp">.</span><span class="n">lemmas</span> <span class="n">analysis</span><span class="bp">.</span><span class="n">real</span>

<span class="kn">namespace</span> <span class="n">ring_tac</span>
<span class="kn">open</span> <span class="n">tactic</span>

<span class="c1">-- why this line?</span>
<span class="bp">@</span><span class="o">[</span><span class="n">derive</span> <span class="n">has_reflect</span><span class="o">]</span>
<span class="kn">inductive</span> <span class="n">ring_expr</span> <span class="o">:</span> <span class="kt">Type</span>
<span class="bp">|</span> <span class="n">add</span> <span class="o">:</span> <span class="n">ring_expr</span> <span class="bp">→</span> <span class="n">ring_expr</span> <span class="bp">→</span> <span class="n">ring_expr</span>
<span class="bp">|</span> <span class="n">mul</span> <span class="o">:</span> <span class="n">ring_expr</span> <span class="bp">→</span> <span class="n">ring_expr</span> <span class="bp">→</span> <span class="n">ring_expr</span>
<span class="bp">|</span> <span class="n">const</span> <span class="o">:</span> <span class="n">znum</span> <span class="bp">→</span> <span class="n">ring_expr</span>
<span class="bp">|</span> <span class="n">X</span> <span class="o">:</span> <span class="n">ring_expr</span>

<span class="n">meta</span> <span class="n">def</span> <span class="n">reflect_expr</span> <span class="o">(</span><span class="n">X</span> <span class="o">:</span> <span class="n">expr</span><span class="o">)</span> <span class="o">:</span> <span class="n">expr</span> <span class="bp">→</span> <span class="n">option</span> <span class="n">ring_expr</span>
<span class="bp">|</span> <span class="bp">`</span><span class="o">(</span><span class="err">%%</span><span class="n">e₁</span> <span class="bp">+</span> <span class="err">%%</span><span class="n">e₂</span><span class="o">)</span> <span class="o">:=</span> <span class="n">do</span>
  <span class="n">p₁</span> <span class="err">←</span> <span class="n">reflect_expr</span> <span class="n">e₁</span><span class="o">,</span>
  <span class="n">p₂</span> <span class="err">←</span> <span class="n">reflect_expr</span> <span class="n">e₂</span><span class="o">,</span>
  <span class="n">return</span> <span class="o">(</span><span class="n">ring_expr</span><span class="bp">.</span><span class="n">add</span> <span class="n">p₁</span> <span class="n">p₂</span><span class="o">)</span>
<span class="bp">|</span> <span class="bp">`</span><span class="o">(</span><span class="err">%%</span><span class="n">e₁</span> <span class="bp">*</span> <span class="err">%%</span><span class="n">e₂</span><span class="o">)</span> <span class="o">:=</span> <span class="n">do</span>
  <span class="n">p₁</span> <span class="err">←</span> <span class="n">reflect_expr</span> <span class="n">e₁</span><span class="o">,</span>
  <span class="n">p₂</span> <span class="err">←</span> <span class="n">reflect_expr</span> <span class="n">e₂</span><span class="o">,</span>
  <span class="n">return</span> <span class="o">(</span><span class="n">ring_expr</span><span class="bp">.</span><span class="n">mul</span> <span class="n">p₁</span> <span class="n">p₂</span><span class="o">)</span>
<span class="bp">|</span> <span class="n">e</span> <span class="o">:=</span> <span class="k">if</span> <span class="n">e</span> <span class="bp">=</span> <span class="n">X</span> <span class="k">then</span> <span class="n">return</span> <span class="n">ring_expr</span><span class="bp">.</span><span class="n">X</span> <span class="k">else</span>
  <span class="n">do</span> <span class="n">n</span> <span class="err">←</span> <span class="n">expr</span><span class="bp">.</span><span class="n">to_int</span> <span class="n">e</span><span class="o">,</span>
     <span class="n">return</span> <span class="o">(</span><span class="n">ring_expr</span><span class="bp">.</span><span class="n">const</span> <span class="o">(</span><span class="n">znum</span><span class="bp">.</span><span class="n">of_int&#39;</span> <span class="n">n</span><span class="o">))</span>

<span class="c1">-- mathlib/data/num has znum and stuff like znum.of_int&#39; (see above)</span>
<span class="n">def</span> <span class="n">poly</span> <span class="o">:=</span> <span class="n">list</span> <span class="n">znum</span>
<span class="c1">-- but why use it?</span>

<span class="n">def</span> <span class="n">poly</span><span class="bp">.</span><span class="n">add</span> <span class="o">:</span> <span class="n">poly</span> <span class="bp">→</span> <span class="n">poly</span> <span class="bp">→</span> <span class="n">poly</span>
<span class="bp">|</span> <span class="o">[]</span> <span class="n">g</span> <span class="o">:=</span> <span class="n">g</span>
<span class="bp">|</span> <span class="n">f</span> <span class="o">[]</span> <span class="o">:=</span> <span class="n">f</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">a</span> <span class="bp">::</span> <span class="n">f&#39;</span><span class="o">)</span> <span class="o">(</span><span class="n">b</span> <span class="bp">::</span> <span class="n">g&#39;</span><span class="o">)</span> <span class="o">:=</span> <span class="o">(</span><span class="n">a</span> <span class="bp">+</span> <span class="n">b</span><span class="o">)</span> <span class="bp">::</span> <span class="n">poly</span><span class="bp">.</span><span class="n">add</span> <span class="n">f&#39;</span> <span class="n">g&#39;</span>

<span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="kn">lemma</span> <span class="n">poly</span><span class="bp">.</span><span class="n">zero_add</span> <span class="o">(</span><span class="n">p</span> <span class="o">:</span> <span class="n">poly</span><span class="o">)</span> <span class="o">:</span> <span class="n">poly</span><span class="bp">.</span><span class="n">add</span> <span class="o">[]</span> <span class="n">p</span> <span class="bp">=</span> <span class="n">p</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">induction</span> <span class="n">p</span><span class="bp">;</span><span class="n">refl</span>

<span class="n">def</span> <span class="n">poly</span><span class="bp">.</span><span class="n">smul</span> <span class="o">:</span> <span class="n">znum</span> <span class="bp">→</span> <span class="n">poly</span> <span class="bp">→</span> <span class="n">poly</span>
<span class="bp">|</span> <span class="bp">_</span> <span class="o">[]</span> <span class="o">:=</span> <span class="o">[]</span>
<span class="bp">|</span> <span class="n">z</span> <span class="o">(</span><span class="n">a</span> <span class="bp">::</span> <span class="n">f&#39;</span><span class="o">)</span> <span class="o">:=</span> <span class="o">(</span><span class="n">z</span> <span class="bp">*</span> <span class="n">a</span><span class="o">)</span> <span class="bp">::</span> <span class="n">poly</span><span class="bp">.</span><span class="n">smul</span> <span class="n">z</span> <span class="n">f&#39;</span>

<span class="n">def</span> <span class="n">poly</span><span class="bp">.</span><span class="n">mul</span> <span class="o">:</span> <span class="n">poly</span> <span class="bp">→</span> <span class="n">poly</span> <span class="bp">→</span> <span class="n">poly</span>
<span class="bp">|</span> <span class="o">[]</span> <span class="bp">_</span> <span class="o">:=</span> <span class="o">[]</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">a</span> <span class="bp">::</span> <span class="n">f&#39;</span><span class="o">)</span> <span class="n">g</span> <span class="o">:=</span> <span class="n">poly</span><span class="bp">.</span><span class="n">add</span> <span class="o">(</span><span class="n">poly</span><span class="bp">.</span><span class="n">smul</span> <span class="n">a</span> <span class="n">g</span><span class="o">)</span> <span class="o">(</span><span class="mi">0</span> <span class="bp">::</span> <span class="o">(</span><span class="n">poly</span><span class="bp">.</span><span class="n">mul</span> <span class="n">f&#39;</span> <span class="n">g</span><span class="o">))</span>

<span class="n">def</span> <span class="n">poly</span><span class="bp">.</span><span class="n">const</span> <span class="o">:</span> <span class="n">znum</span> <span class="bp">→</span> <span class="n">poly</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">z</span><span class="o">,</span> <span class="o">[</span><span class="n">z</span><span class="o">]</span>

<span class="n">def</span> <span class="n">poly</span><span class="bp">.</span><span class="n">X</span> <span class="o">:</span> <span class="n">poly</span> <span class="o">:=</span> <span class="o">[</span><span class="mi">0</span><span class="o">,</span><span class="mi">1</span><span class="o">]</span>

<span class="n">def</span> <span class="n">to_poly</span> <span class="o">:</span> <span class="n">ring_expr</span> <span class="bp">→</span> <span class="n">poly</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">ring_expr</span><span class="bp">.</span><span class="n">add</span> <span class="n">e₁</span> <span class="n">e₂</span><span class="o">)</span> <span class="o">:=</span> <span class="o">(</span><span class="n">to_poly</span> <span class="n">e₁</span><span class="o">)</span><span class="bp">.</span><span class="n">add</span> <span class="o">(</span><span class="n">to_poly</span> <span class="n">e₂</span><span class="o">)</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">ring_expr</span><span class="bp">.</span><span class="n">mul</span> <span class="n">e₁</span> <span class="n">e₂</span><span class="o">)</span> <span class="o">:=</span> <span class="o">(</span><span class="n">to_poly</span> <span class="n">e₁</span><span class="o">)</span><span class="bp">.</span><span class="n">mul</span> <span class="o">(</span><span class="n">to_poly</span> <span class="n">e₂</span><span class="o">)</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">ring_expr</span><span class="bp">.</span><span class="n">const</span> <span class="n">z</span><span class="o">)</span> <span class="o">:=</span> <span class="n">poly</span><span class="bp">.</span><span class="n">const</span> <span class="n">z</span>
<span class="bp">|</span> <span class="n">ring_expr</span><span class="bp">.</span><span class="n">X</span> <span class="o">:=</span> <span class="n">poly</span><span class="bp">.</span><span class="n">X</span>

<span class="n">def</span> <span class="n">poly</span><span class="bp">.</span><span class="kn">eval</span> <span class="o">{</span><span class="n">α</span><span class="o">}</span> <span class="o">[</span><span class="n">comm_ring</span> <span class="n">α</span><span class="o">]</span> <span class="o">(</span><span class="n">X</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="n">poly</span> <span class="bp">→</span> <span class="n">α</span>
<span class="bp">|</span> <span class="o">[]</span> <span class="o">:=</span> <span class="mi">0</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">n</span><span class="bp">::</span><span class="n">l</span><span class="o">)</span> <span class="o">:=</span> <span class="n">n</span> <span class="bp">+</span> <span class="n">X</span> <span class="bp">*</span> <span class="n">poly</span><span class="bp">.</span><span class="kn">eval</span> <span class="n">l</span>

<span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="kn">lemma</span> <span class="n">poly</span><span class="bp">.</span><span class="n">eval_zero</span> <span class="o">{</span><span class="n">α</span><span class="o">}</span> <span class="o">[</span><span class="n">comm_ring</span> <span class="n">α</span><span class="o">]</span> <span class="o">(</span><span class="n">X</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="n">poly</span><span class="bp">.</span><span class="kn">eval</span> <span class="n">X</span> <span class="o">[]</span> <span class="bp">=</span> <span class="mi">0</span> <span class="o">:=</span> <span class="n">rfl</span>

<span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="kn">theorem</span> <span class="n">poly</span><span class="bp">.</span><span class="n">eval_add</span> <span class="o">{</span><span class="n">α</span><span class="o">}</span> <span class="o">[</span><span class="n">comm_ring</span> <span class="n">α</span><span class="o">]</span> <span class="o">(</span><span class="n">X</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">p₁</span> <span class="n">p₂</span> <span class="o">:</span> <span class="n">poly</span><span class="o">,</span>
  <span class="o">(</span><span class="n">p₁</span><span class="bp">.</span><span class="n">add</span> <span class="n">p₂</span><span class="o">)</span><span class="bp">.</span><span class="kn">eval</span> <span class="n">X</span> <span class="bp">=</span> <span class="n">p₁</span><span class="bp">.</span><span class="kn">eval</span> <span class="n">X</span> <span class="bp">+</span> <span class="n">p₂</span><span class="bp">.</span><span class="kn">eval</span> <span class="n">X</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">intro</span> <span class="n">p₁</span><span class="o">,</span>
  <span class="n">induction</span> <span class="n">p₁</span> <span class="k">with</span> <span class="n">h₁</span> <span class="n">t₁</span> <span class="n">H</span><span class="o">,</span>
    <span class="c1">-- base case</span>
    <span class="n">intros</span><span class="o">,</span><span class="n">simp</span> <span class="o">[</span><span class="n">poly</span><span class="bp">.</span><span class="kn">eval</span><span class="o">],</span>
  <span class="c1">-- inductive step</span>
  <span class="n">intro</span> <span class="n">p₂</span><span class="o">,</span>
  <span class="n">cases</span> <span class="n">p₂</span> <span class="k">with</span> <span class="n">h₂</span> <span class="n">t₂</span><span class="o">,</span>
    <span class="n">simp</span> <span class="o">[</span><span class="n">poly</span><span class="bp">.</span><span class="n">add</span><span class="o">],</span>
  <span class="n">unfold</span> <span class="n">poly</span><span class="bp">.</span><span class="kn">eval</span> <span class="n">poly</span><span class="bp">.</span><span class="n">add</span><span class="o">,</span>
  <span class="n">rw</span> <span class="o">(</span><span class="n">H</span> <span class="n">t₂</span><span class="o">),</span>
  <span class="n">simp</span> <span class="o">[</span><span class="n">mul_add</span><span class="o">]</span>
<span class="kn">end</span>

<span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="kn">lemma</span> <span class="n">poly</span><span class="bp">.</span><span class="n">eval_mul_zero</span> <span class="o">{</span><span class="n">α</span><span class="o">}</span> <span class="o">[</span><span class="n">comm_ring</span> <span class="n">α</span><span class="o">]</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">poly</span><span class="o">)</span> <span class="o">(</span><span class="n">X</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span>
  <span class="n">poly</span><span class="bp">.</span><span class="kn">eval</span> <span class="n">X</span> <span class="o">(</span><span class="n">poly</span><span class="bp">.</span><span class="n">mul</span> <span class="n">f</span> <span class="o">[])</span> <span class="bp">=</span> <span class="mi">0</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">induction</span> <span class="n">f</span> <span class="k">with</span> <span class="n">h</span> <span class="n">t</span> <span class="n">H</span><span class="o">,</span>
    <span class="n">refl</span><span class="o">,</span>
  <span class="n">unfold</span> <span class="n">poly</span><span class="bp">.</span><span class="n">mul</span> <span class="n">poly</span><span class="bp">.</span><span class="n">smul</span> <span class="n">poly</span><span class="bp">.</span><span class="n">add</span> <span class="n">poly</span><span class="bp">.</span><span class="n">mul</span> <span class="n">poly</span><span class="bp">.</span><span class="kn">eval</span><span class="o">,</span>
  <span class="n">rw</span> <span class="n">H</span><span class="o">,</span><span class="n">simp</span>
<span class="kn">end</span>

<span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="kn">lemma</span> <span class="n">poly</span><span class="bp">.</span><span class="n">eval_smul</span> <span class="o">{</span><span class="n">α</span><span class="o">}</span> <span class="o">[</span><span class="n">comm_ring</span> <span class="n">α</span><span class="o">]</span> <span class="o">(</span><span class="n">X</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">z</span> <span class="o">:</span> <span class="n">znum</span><span class="o">)</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">poly</span><span class="o">)</span> <span class="o">:</span>
  <span class="n">poly</span><span class="bp">.</span><span class="kn">eval</span> <span class="n">X</span> <span class="o">(</span><span class="n">poly</span><span class="bp">.</span><span class="n">smul</span> <span class="n">z</span> <span class="n">f</span><span class="o">)</span> <span class="bp">=</span> <span class="n">z</span> <span class="bp">*</span> <span class="n">poly</span><span class="bp">.</span><span class="kn">eval</span> <span class="n">X</span> <span class="n">f</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">induction</span> <span class="n">f</span> <span class="k">with</span> <span class="n">h</span> <span class="n">t</span> <span class="n">H</span><span class="o">,</span> <span class="n">simp</span> <span class="o">[</span><span class="n">poly</span><span class="bp">.</span><span class="n">smul</span><span class="o">,</span><span class="n">poly</span><span class="bp">.</span><span class="kn">eval</span><span class="o">,</span><span class="n">mul_zero</span><span class="o">],</span>
  <span class="n">unfold</span> <span class="n">poly</span><span class="bp">.</span><span class="n">smul</span> <span class="n">poly</span><span class="bp">.</span><span class="kn">eval</span><span class="o">,</span>
  <span class="n">rw</span> <span class="n">H</span><span class="o">,</span>
  <span class="n">simp</span> <span class="o">[</span><span class="n">mul_add</span><span class="o">,</span><span class="n">znum</span><span class="bp">.</span><span class="n">cast_mul</span><span class="o">,</span><span class="n">mul_assoc</span><span class="o">,</span><span class="n">mul_comm</span><span class="o">]</span>
<span class="kn">end</span>

<span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="kn">theorem</span> <span class="n">poly</span><span class="bp">.</span><span class="n">eval_mul</span> <span class="o">{</span><span class="n">α</span><span class="o">}</span> <span class="o">[</span><span class="n">comm_ring</span> <span class="n">α</span><span class="o">]</span> <span class="o">(</span><span class="n">X</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">p₁</span> <span class="n">p₂</span> <span class="o">:</span> <span class="n">poly</span><span class="o">,</span>
  <span class="o">(</span><span class="n">p₁</span><span class="bp">.</span><span class="n">mul</span> <span class="n">p₂</span><span class="o">)</span><span class="bp">.</span><span class="kn">eval</span> <span class="n">X</span> <span class="bp">=</span> <span class="n">p₁</span><span class="bp">.</span><span class="kn">eval</span> <span class="n">X</span> <span class="bp">*</span> <span class="n">p₂</span><span class="bp">.</span><span class="kn">eval</span> <span class="n">X</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">intro</span> <span class="n">p₁</span><span class="o">,</span><span class="n">induction</span> <span class="n">p₁</span> <span class="k">with</span> <span class="n">h₁</span> <span class="n">t₁</span> <span class="n">H</span><span class="o">,</span>
    <span class="n">simp</span> <span class="o">[</span><span class="n">poly</span><span class="bp">.</span><span class="n">mul</span><span class="o">],</span>
  <span class="n">intro</span> <span class="n">p₂</span><span class="o">,</span>
  <span class="n">unfold</span> <span class="n">poly</span><span class="bp">.</span><span class="n">mul</span><span class="o">,</span>
  <span class="n">rw</span> <span class="n">poly</span><span class="bp">.</span><span class="n">eval_add</span><span class="o">,</span>
  <span class="n">unfold</span> <span class="n">poly</span><span class="bp">.</span><span class="kn">eval</span><span class="o">,</span>
  <span class="n">rw</span> <span class="o">[</span><span class="n">H</span> <span class="n">p₂</span><span class="o">,</span><span class="n">znum</span><span class="bp">.</span><span class="n">cast_zero</span><span class="o">,</span><span class="n">zero_add</span><span class="o">,</span><span class="n">add_mul</span><span class="o">,</span><span class="n">poly</span><span class="bp">.</span><span class="n">eval_smul</span><span class="o">,</span><span class="n">mul_assoc</span><span class="o">]</span>
<span class="kn">end</span>


<span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="kn">theorem</span> <span class="n">poly</span><span class="bp">.</span><span class="n">eval_const</span> <span class="o">{</span><span class="n">α</span><span class="o">}</span> <span class="o">[</span><span class="n">comm_ring</span> <span class="n">α</span><span class="o">]</span> <span class="o">(</span><span class="n">X</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">n</span> <span class="o">:</span> <span class="n">znum</span><span class="o">,</span>
  <span class="o">(</span><span class="n">poly</span><span class="bp">.</span><span class="n">const</span> <span class="n">n</span><span class="o">)</span><span class="bp">.</span><span class="kn">eval</span> <span class="n">X</span> <span class="bp">=</span> <span class="n">n</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">intro</span> <span class="n">n</span><span class="o">,</span>
  <span class="n">unfold</span> <span class="n">poly</span><span class="bp">.</span><span class="n">const</span> <span class="n">poly</span><span class="bp">.</span><span class="kn">eval</span><span class="o">,</span><span class="n">simp</span>
<span class="kn">end</span>

<span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="kn">theorem</span> <span class="n">poly</span><span class="bp">.</span><span class="n">eval_X</span> <span class="o">{</span><span class="n">α</span><span class="o">}</span> <span class="o">[</span><span class="n">comm_ring</span> <span class="n">α</span><span class="o">]</span> <span class="o">(</span><span class="n">X</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="n">poly</span><span class="bp">.</span><span class="n">X</span><span class="bp">.</span><span class="kn">eval</span> <span class="n">X</span> <span class="bp">=</span> <span class="n">X</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">unfold</span> <span class="n">poly</span><span class="bp">.</span><span class="n">X</span> <span class="n">poly</span><span class="bp">.</span><span class="kn">eval</span><span class="o">,</span><span class="n">simp</span>
<span class="kn">end</span>


<span class="n">def</span> <span class="n">ring_expr</span><span class="bp">.</span><span class="kn">eval</span> <span class="o">{</span><span class="n">α</span><span class="o">}</span> <span class="o">[</span><span class="n">comm_ring</span> <span class="n">α</span><span class="o">]</span> <span class="o">(</span><span class="n">X</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="n">ring_expr</span> <span class="bp">→</span> <span class="n">α</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">ring_expr</span><span class="bp">.</span><span class="n">add</span> <span class="n">e₁</span> <span class="n">e₂</span><span class="o">)</span> <span class="o">:=</span> <span class="n">e₁</span><span class="bp">.</span><span class="kn">eval</span> <span class="bp">+</span> <span class="n">e₂</span><span class="bp">.</span><span class="kn">eval</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">ring_expr</span><span class="bp">.</span><span class="n">mul</span> <span class="n">e₁</span> <span class="n">e₂</span><span class="o">)</span> <span class="o">:=</span> <span class="n">e₁</span><span class="bp">.</span><span class="kn">eval</span> <span class="bp">*</span> <span class="n">e₂</span><span class="bp">.</span><span class="kn">eval</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">ring_expr</span><span class="bp">.</span><span class="n">const</span> <span class="n">z</span><span class="o">)</span> <span class="o">:=</span> <span class="n">z</span>
<span class="bp">|</span> <span class="n">ring_expr</span><span class="bp">.</span><span class="n">X</span> <span class="o">:=</span> <span class="n">X</span>

<span class="kn">theorem</span> <span class="n">to_poly_eval</span> <span class="o">{</span><span class="n">α</span><span class="o">}</span> <span class="o">[</span><span class="n">comm_ring</span> <span class="n">α</span><span class="o">]</span> <span class="o">(</span><span class="n">X</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">e</span><span class="o">)</span> <span class="o">:</span> <span class="o">(</span><span class="n">to_poly</span> <span class="n">e</span><span class="o">)</span><span class="bp">.</span><span class="kn">eval</span> <span class="n">X</span> <span class="bp">=</span> <span class="n">e</span><span class="bp">.</span><span class="kn">eval</span> <span class="n">X</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">induction</span> <span class="n">e</span><span class="bp">;</span> <span class="n">simp</span> <span class="o">[</span><span class="n">to_poly</span><span class="o">,</span> <span class="n">ring_expr</span><span class="bp">.</span><span class="kn">eval</span><span class="o">,</span> <span class="bp">*</span><span class="o">]</span>

<span class="kn">theorem</span> <span class="n">main_thm</span> <span class="o">{</span><span class="n">α</span><span class="o">}</span> <span class="o">[</span><span class="n">comm_ring</span> <span class="n">α</span><span class="o">]</span> <span class="o">(</span><span class="n">X</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">e₁</span> <span class="n">e₂</span><span class="o">)</span> <span class="o">{</span><span class="n">x₁</span> <span class="n">x₂</span><span class="o">}</span>
  <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="n">to_poly</span> <span class="n">e₁</span> <span class="bp">=</span> <span class="n">to_poly</span> <span class="n">e₂</span><span class="o">)</span> <span class="o">(</span><span class="n">R1</span> <span class="o">:</span> <span class="n">e₁</span><span class="bp">.</span><span class="kn">eval</span> <span class="n">X</span> <span class="bp">=</span> <span class="n">x₁</span><span class="o">)</span> <span class="o">(</span><span class="n">R2</span> <span class="o">:</span> <span class="n">e₂</span><span class="bp">.</span><span class="kn">eval</span> <span class="n">X</span> <span class="bp">=</span> <span class="n">x₂</span><span class="o">)</span> <span class="o">:</span> <span class="n">x₁</span> <span class="bp">=</span> <span class="n">x₂</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">rw</span> <span class="o">[</span><span class="err">←</span> <span class="n">R1</span><span class="o">,</span> <span class="err">←</span> <span class="n">R2</span><span class="o">,</span> <span class="err">←</span> <span class="n">to_poly_eval</span><span class="o">,</span> <span class="n">H</span><span class="o">,</span> <span class="n">to_poly_eval</span><span class="o">]</span>

<span class="n">meta</span> <span class="n">def</span> <span class="n">ring_tac</span> <span class="o">(</span><span class="n">X</span> <span class="o">:</span> <span class="n">pexpr</span><span class="o">)</span> <span class="o">:</span> <span class="n">tactic</span> <span class="n">unit</span> <span class="o">:=</span> <span class="n">do</span>
  <span class="n">X</span> <span class="err">←</span> <span class="n">to_expr</span> <span class="n">X</span><span class="o">,</span>
  <span class="bp">`</span><span class="o">(</span><span class="err">%%</span><span class="n">x₁</span> <span class="bp">=</span> <span class="err">%%</span><span class="n">x₂</span><span class="o">)</span> <span class="err">←</span> <span class="n">target</span><span class="o">,</span>
  <span class="n">r₁</span> <span class="err">←</span> <span class="n">reflect_expr</span> <span class="n">X</span> <span class="n">x₁</span><span class="o">,</span>
  <span class="n">r₂</span> <span class="err">←</span> <span class="n">reflect_expr</span> <span class="n">X</span> <span class="n">x₂</span><span class="o">,</span>
  <span class="k">let</span> <span class="n">e₁</span> <span class="o">:</span> <span class="n">expr</span> <span class="o">:=</span> <span class="n">reflect</span> <span class="n">r₁</span><span class="o">,</span>
  <span class="k">let</span> <span class="n">e₂</span> <span class="o">:</span> <span class="n">expr</span> <span class="o">:=</span> <span class="n">reflect</span> <span class="n">r₂</span><span class="o">,</span>
  <span class="bp">`</span><span class="o">[</span><span class="n">refine</span> <span class="n">main_thm</span> <span class="err">%%</span><span class="n">X</span> <span class="err">%%</span><span class="n">e₁</span> <span class="err">%%</span><span class="n">e₂</span> <span class="n">rfl</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">],</span>
  <span class="n">all_goals</span> <span class="bp">`</span><span class="o">[</span><span class="n">simp</span> <span class="n">only</span> <span class="o">[</span><span class="n">ring_expr</span><span class="bp">.</span><span class="kn">eval</span><span class="o">,</span>
    <span class="n">znum</span><span class="bp">.</span><span class="n">cast_pos</span><span class="o">,</span> <span class="n">znum</span><span class="bp">.</span><span class="n">cast_neg</span><span class="o">,</span> <span class="n">znum</span><span class="bp">.</span><span class="n">cast_zero&#39;</span><span class="o">,</span>
    <span class="n">pos_num</span><span class="bp">.</span><span class="n">cast_bit0</span><span class="o">,</span> <span class="n">pos_num</span><span class="bp">.</span><span class="n">cast_bit1</span><span class="o">,</span>
    <span class="n">pos_num</span><span class="bp">.</span><span class="n">cast_one&#39;</span><span class="o">]]</span>

<span class="kn">theorem</span> <span class="n">X</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span> <span class="o">:</span> <span class="o">(</span><span class="n">x</span> <span class="bp">+</span> <span class="mi">1</span><span class="o">)</span> <span class="bp">*</span> <span class="o">(</span><span class="n">x</span> <span class="bp">+</span> <span class="mi">1</span><span class="o">)</span> <span class="bp">=</span> <span class="n">x</span><span class="bp">*</span><span class="n">x</span><span class="bp">+</span><span class="mi">2</span><span class="bp">*</span><span class="n">x</span><span class="bp">+</span><span class="mi">1</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">do</span> <span class="n">ring_tac</span> <span class="bp">```</span><span class="o">(</span><span class="n">x</span><span class="o">)</span>

<span class="bp">#</span><span class="kn">print</span> <span class="n">axioms</span> <span class="n">X</span>

<span class="kn">end</span> <span class="n">ring_tac</span>
</pre></div>

#### [ Kevin Buzzard (Jun 13 2018 at 01:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127979329):
<p>Did my homework</p>

#### [ Kevin Buzzard (Jun 13 2018 at 01:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127979333):
<p>I feel like an UG again</p>

#### [ Kevin Buzzard (Jun 13 2018 at 01:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127979394):
<p>Notes: I had to introduce poly.smul (scalar multiplication of poly by znum) for definition of multiplication. I really tried to make simp do most of the work in general but I still had to do a lot of unfolding before I could get it going.</p>

#### [ Kenny Lau (Jun 13 2018 at 01:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127979395):
<p>did you just write a tactic?</p>

#### [ Kevin Buzzard (Jun 13 2018 at 01:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127979401):
<p>Not really</p>

#### [ Kevin Buzzard (Jun 13 2018 at 01:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127979405):
<p>in the sense that no code I wrote started with <code>meta</code></p>

#### [ Kevin Buzzard (Jun 13 2018 at 01:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127979408):
<p>but check it out</p>

#### [ Kevin Buzzard (Jun 13 2018 at 01:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127979412):
<p>barely any code at all has <code>meta</code></p>

#### [ Kevin Buzzard (Jun 13 2018 at 01:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127979416):
<p>Just <code>reflect_expr</code> at the very top, and <code>ring_tac</code> at the very bottom. Mario wrote both of those</p>

#### [ Kevin Buzzard (Jun 13 2018 at 01:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127979480):
<p>Kenny here's the strat: to prove that for d : int we have (d+1)^2=d^2+2*d+1 we first prove that in a polynomial ring we have (X+1)^2=X^2+2X+1 and then deduce</p>

#### [ Kevin Buzzard (Jun 13 2018 at 01:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127979481):
<p>The problem is that if Lean just sees (d+1)^2 it can't create (X+1)^2</p>

#### [ Kevin Buzzard (Jun 13 2018 at 01:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127979489):
<p>so this part you have to do in meta-land</p>

#### [ Kevin Buzzard (Jun 13 2018 at 01:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127979491):
<p>but it's only this part</p>

#### [ Kevin Buzzard (Jun 13 2018 at 01:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127979496):
<p>unsurprisingly, this is what <code>reflect_expr</code> does</p>

#### [ Kevin Buzzard (Jun 13 2018 at 01:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127979537):
<p>So there's a basic one-variable ring tactic with a very small amount of meta indeed, and the meta is really not hard to comprehend. I mean, it might be hard to write, but it's not at all hard to read.</p>

#### [ Kevin Buzzard (Jun 13 2018 at 01:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127979539):
<p>I'll write a blog post explaining it but now it's bed time. Once again many thanks Mario.</p>

#### [ Kevin Buzzard (Jun 13 2018 at 01:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/127979604):
<p>Just to be clear <span class="user-mention" data-user-id="110064">@Kenny Lau</span> the code I posted does seem to be a fully working baby <code>ring</code></p>

#### [ Kevin Buzzard (Jun 13 2018 at 11:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/128000038):
<p>Actually it doesn't work in all cases, because there is currently no "canonical form" lemma. The polynomials <code>[1]</code> and <code>[1,0]</code> (=0*x+1) are different.</p>

#### [ Kevin Buzzard (Jun 13 2018 at 11:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/128000106):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> Here are the three questions I have about this project, which basically came up when trying to write a blog post. The first two are trivial for you: what is <code>@[derive has_reflect]</code> and why <code>znum</code> rather than <code>int</code>?</p>

#### [ Kevin Buzzard (Jun 13 2018 at 11:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/128000111):
<p>The third is a bit more annoying. Because there is no algorithm to put polynomials (= lists of znums) into "canonical form", <code>example (x : ℤ) : (x + 1) + ((-1)*x + 1) = 2 := by do ring_tac ```(x) </code> fails</p>

#### [ Kevin Buzzard (Jun 13 2018 at 11:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/128000156):
<p>I think this is because the polynomials <code>[2,0]</code> and <code>[2]</code> are considered distinct.</p>

#### [ Kevin Buzzard (Jun 13 2018 at 11:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/128000158):
<p>Aah, I think I can fix this.</p>

#### [ Kevin Buzzard (Jun 13 2018 at 11:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/128000161):
<p>I think I write some "canonical_form" function</p>

#### [ Kevin Buzzard (Jun 13 2018 at 11:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/128000162):
<p>(not in meta land)</p>

#### [ Kevin Buzzard (Jun 13 2018 at 11:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/128000171):
<p>and redefine add so that it puts the polynomial into canonical form afterwards.</p>

#### [ Kevin Buzzard (Jun 13 2018 at 11:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/128000180):
<p>yeah yeah OK I think I can do this one.</p>

#### [ Mario Carneiro (Jun 13 2018 at 12:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/128001631):
<blockquote>
<p>Why <code>@[derive has_reflect]</code></p>
</blockquote>
<p>This one is easy: otherwise you don't have a <code>reflect</code> instance for <code>ring_expr</code>. This function is used explicitly in <code>ring_tac</code>; the idea is that if <code>A</code> is a reflectable type then <code>reflect (a : A)</code> is an expr that denotes the same value as <code>a</code></p>

#### [ Mario Carneiro (Jun 13 2018 at 12:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/128001637):
<p>so for example <code>list</code> has a reflect that just turns each cons into a <code>expr.app ``list.cons a l</code></p>

#### [ Mario Carneiro (Jun 13 2018 at 12:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/128001644):
<p>and <code>nat</code> has a reflect that produces <code>bit0</code> and <code>bit1</code> expressions (which when printed appear as the number being denoted)</p>

#### [ Mario Carneiro (Jun 13 2018 at 12:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/128001686):
<p>But not all types have a reflect; in particular quotients and other things that make different expressions equal according to lean don't have a reflect, since you would have to open up the quotient to get the element to print</p>

#### [ Mario Carneiro (Jun 13 2018 at 12:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/128001696):
<p>In this case it is needed because <code>reflect_expr</code> produces a <code>ring_expr</code>, not an <code>expr</code> denoting a <code>ring_expr</code></p>

#### [ Mario Carneiro (Jun 13 2018 at 12:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/128001746):
<p>I think in this case you could skip the extra step and just produce an expr directly, but that would be less structured and more meta</p>

#### [ Mario Carneiro (Jun 13 2018 at 12:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/128001856):
<blockquote>
<p>Why <code>znum</code></p>
</blockquote>
<p>This one is more subtle, and actually I knew you would ask this question and I used it in part to prompt the question. You can view this as an efficiency move, but when there is an exponential performance gap I think it is close enough to essential to teach directly. Whenever you use proof by reflection, it is absolutely essential that you do everything you can to make the computation simple and direct, because you will be working with a fairly heavy handicap. A big no-no is using <code>nat</code> and <code>int</code> anywhere in your computation, because (as Seul has discovered) this works in unary and there is nothing you can do to prevent this when computing in the kernel</p>

#### [ Mario Carneiro (Jun 13 2018 at 12:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/128001891):
<p>This is in fact the raison d'etre for the <code>num</code> type - it allows for performing <em>kernel computations</em> on naturals and integers, with enough lemmas to relate them back to the more traditional <code>nat</code> type.</p>

#### [ Mario Carneiro (Jun 13 2018 at 12:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/128001947):
<p>It's a bit of a delicate move, since <code>int</code> and <code>nat</code> are in fact the more efficient ones in VM computations, so you want to convert from <code>int</code> to <code>znum</code> when storing the numbers inside the kernel data structure (<code>ring_expr</code>), but not before</p>

#### [ Mario Carneiro (Jun 13 2018 at 12:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/128002085):
<blockquote>
<p>The third is a bit more annoying. Because there is no algorithm to put polynomials (= lists of znums) into "canonical form", example (x : ℤ) : (x + 1) + ((-1)*x + 1) = 2 := by do ring_tac ```(x) fails</p>
</blockquote>
<p>I noticed this as well with your definition of <code>poly.add</code>. But there is actually another solution, which might be easier than applying a function that strips the high zeros after every operation. That is, define</p>
<div class="codehilite"><pre><span></span>def poly.is_eq : poly -&gt; poly -&gt; bool := sorry
</pre></div>


<p>so that trailing zeros are ignored in the equality test, and then replace <code>to_poly e1 = to_poly e2</code> with <code>poly.is_eq (to_poly e1) (to_poly e2)</code> in the <code>main_thm</code> and prove it with this (weaker) assumption</p>

#### [ Andrew Ashworth (Jun 13 2018 at 14:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/128005278):
<p>So, if I defined a new poly type quotiented with this equality relation, I'd have to explicitly define my denotation function? That doesn't sound so bad, I think... or would the kernel get stuck trying to reduce it?</p>

#### [ Andrew Ashworth (Jun 13 2018 at 14:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/128005285):
<p>maybe I should just try it out with the helpful reflection template that's just been posted :)</p>

#### [ Kevin Buzzard (Jun 13 2018 at 18:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/128015942):
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">poly</span><span class="bp">.</span><span class="n">is_eq_aux</span> <span class="o">:</span> <span class="n">list</span> <span class="n">znum</span> <span class="bp">-&gt;</span> <span class="n">list</span> <span class="n">znum</span> <span class="bp">-&gt;</span> <span class="n">bool</span>
<span class="bp">|</span> <span class="o">[]</span> <span class="o">[]</span> <span class="o">:=</span> <span class="n">tt</span>
<span class="bp">|</span> <span class="o">[]</span> <span class="o">(</span><span class="n">h₂</span> <span class="bp">::</span> <span class="n">t₂</span><span class="o">)</span> <span class="o">:=</span> <span class="k">if</span> <span class="o">(</span><span class="n">h₂</span> <span class="bp">=</span> <span class="mi">0</span><span class="o">)</span> <span class="k">then</span> <span class="n">poly</span><span class="bp">.</span><span class="n">is_eq_aux</span> <span class="o">[]</span> <span class="n">t₂</span> <span class="k">else</span> <span class="n">ff</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">h₁</span> <span class="bp">::</span> <span class="n">t₁</span><span class="o">)</span> <span class="o">[]</span> <span class="o">:=</span> <span class="k">if</span> <span class="o">(</span><span class="n">h₁</span> <span class="bp">=</span> <span class="mi">0</span><span class="o">)</span> <span class="k">then</span> <span class="n">poly</span><span class="bp">.</span><span class="n">is_eq_aux</span> <span class="n">t₁</span> <span class="o">[]</span> <span class="k">else</span> <span class="n">ff</span>
<span class="bp">|</span> <span class="o">(</span><span class="n">h₁</span> <span class="bp">::</span> <span class="n">t₁</span><span class="o">)</span> <span class="o">(</span><span class="n">h₂</span> <span class="bp">::</span> <span class="n">t₂</span><span class="o">)</span> <span class="o">:=</span> <span class="k">if</span> <span class="o">(</span><span class="n">h₁</span> <span class="bp">=</span> <span class="n">h₂</span><span class="o">)</span> <span class="k">then</span> <span class="n">poly</span><span class="bp">.</span><span class="n">is_eq_aux</span> <span class="n">t₁</span> <span class="n">t₂</span> <span class="k">else</span> <span class="n">ff</span>

<span class="n">def</span> <span class="n">poly</span><span class="bp">.</span><span class="n">is_eq</span> <span class="o">:</span> <span class="n">poly</span> <span class="bp">→</span> <span class="n">poly</span> <span class="bp">→</span> <span class="n">bool</span> <span class="o">:=</span> <span class="n">poly</span><span class="bp">.</span><span class="n">is_eq_aux</span>
</pre></div>

#### [ Kevin Buzzard (Jun 13 2018 at 18:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/128015985):
<p>[recursion on poly doesn't seem to work]</p>

#### [ Kevin Buzzard (Jun 13 2018 at 18:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/128015998):
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">poly</span><span class="bp">.</span><span class="n">eval_is_eq</span> <span class="o">{</span><span class="n">α</span><span class="o">}</span> <span class="o">[</span><span class="n">comm_ring</span> <span class="n">α</span><span class="o">]</span> <span class="o">(</span><span class="n">X</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">{</span><span class="n">p₁</span> <span class="n">p₂</span> <span class="o">:</span> <span class="n">poly</span><span class="o">}</span> <span class="o">:</span>
  <span class="n">poly</span><span class="bp">.</span><span class="n">is_eq</span> <span class="n">p₁</span> <span class="n">p₂</span> <span class="bp">→</span> <span class="n">p₁</span><span class="bp">.</span><span class="kn">eval</span> <span class="n">X</span> <span class="bp">=</span> <span class="n">p₂</span><span class="bp">.</span><span class="kn">eval</span> <span class="n">X</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">revert</span> <span class="n">p₂</span><span class="o">,</span>
  <span class="n">induction</span> <span class="n">p₁</span> <span class="k">with</span> <span class="n">h₁</span> <span class="n">t₁</span> <span class="n">H₁</span><span class="o">,</span>
  <span class="o">{</span> <span class="n">intros</span> <span class="n">p₂</span> <span class="n">H</span><span class="o">,</span>
    <span class="n">induction</span> <span class="n">p₂</span> <span class="k">with</span> <span class="n">h₁</span> <span class="n">t₁</span> <span class="n">H₂</span><span class="o">,</span><span class="n">refl</span><span class="o">,</span>
    <span class="n">unfold</span> <span class="n">poly</span><span class="bp">.</span><span class="kn">eval</span><span class="o">,</span>
    <span class="n">unfold</span> <span class="n">poly</span><span class="bp">.</span><span class="n">is_eq</span> <span class="n">poly</span><span class="bp">.</span><span class="n">is_eq_aux</span> <span class="n">at</span> <span class="n">H</span><span class="o">,</span>
    <span class="n">split_ifs</span> <span class="n">at</span> <span class="n">H</span><span class="o">,</span><span class="n">swap</span><span class="o">,</span><span class="n">cases</span> <span class="n">H</span><span class="o">,</span>
    <span class="n">rw</span> <span class="o">[</span><span class="n">h</span><span class="o">,</span><span class="err">←</span><span class="n">H₂</span> <span class="n">H</span><span class="o">],</span>
    <span class="n">simp</span><span class="o">,</span>
  <span class="o">},</span>
  <span class="o">{</span> <span class="n">intros</span> <span class="n">p₂</span> <span class="n">H</span><span class="o">,</span>
    <span class="n">induction</span> <span class="n">p₂</span> <span class="k">with</span> <span class="n">h₂</span> <span class="n">t₂</span> <span class="n">H₂</span><span class="o">,</span>
    <span class="o">{</span> <span class="n">unfold</span> <span class="n">poly</span><span class="bp">.</span><span class="kn">eval</span><span class="o">,</span>
      <span class="n">unfold</span> <span class="n">poly</span><span class="bp">.</span><span class="n">is_eq</span> <span class="n">poly</span><span class="bp">.</span><span class="n">is_eq_aux</span> <span class="n">at</span> <span class="n">H</span><span class="o">,</span>
      <span class="n">split_ifs</span> <span class="n">at</span> <span class="n">H</span><span class="o">,</span><span class="n">swap</span><span class="o">,</span><span class="n">cases</span> <span class="n">H</span><span class="o">,</span>
      <span class="n">rw</span> <span class="o">[</span><span class="n">h</span><span class="o">,</span><span class="n">H₁</span> <span class="n">H</span><span class="o">],</span>
      <span class="n">simp</span>
    <span class="o">},</span>
    <span class="o">{</span> <span class="n">unfold</span> <span class="n">poly</span><span class="bp">.</span><span class="kn">eval</span><span class="o">,</span>
      <span class="n">unfold</span> <span class="n">poly</span><span class="bp">.</span><span class="n">is_eq</span> <span class="n">poly</span><span class="bp">.</span><span class="n">is_eq_aux</span> <span class="n">at</span> <span class="n">H</span><span class="o">,</span>
      <span class="n">split_ifs</span> <span class="n">at</span> <span class="n">H</span><span class="o">,</span><span class="n">swap</span><span class="o">,</span><span class="n">cases</span> <span class="n">H</span><span class="o">,</span>
      <span class="n">unfold</span> <span class="n">poly</span><span class="bp">.</span><span class="n">is_eq</span> <span class="n">at</span> <span class="n">H₂</span><span class="o">,</span>
      <span class="n">rw</span> <span class="o">[</span><span class="n">h</span><span class="o">,</span><span class="n">H₁</span> <span class="n">H</span><span class="o">]</span>
    <span class="o">}</span>
  <span class="o">}</span>
</pre></div>

#### [ Kevin Buzzard (Jun 13 2018 at 18:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/128016003):
<p>and then all we need is</p>

#### [ Kevin Buzzard (Jun 13 2018 at 18:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/128016019):
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">main_thm</span> <span class="o">{</span><span class="n">α</span><span class="o">}</span> <span class="o">[</span><span class="n">comm_ring</span> <span class="n">α</span><span class="o">]</span> <span class="o">(</span><span class="n">X</span> <span class="o">:</span> <span class="n">α</span><span class="o">)</span> <span class="o">(</span><span class="n">e₁</span> <span class="n">e₂</span><span class="o">)</span> <span class="o">{</span><span class="n">x₁</span> <span class="n">x₂</span><span class="o">}</span>
  <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="n">poly</span><span class="bp">.</span><span class="n">is_eq</span> <span class="o">(</span><span class="n">to_poly</span> <span class="n">e₁</span><span class="o">)</span> <span class="o">(</span><span class="n">to_poly</span> <span class="n">e₂</span><span class="o">))</span> <span class="o">(</span><span class="n">R1</span> <span class="o">:</span> <span class="n">e₁</span><span class="bp">.</span><span class="kn">eval</span> <span class="n">X</span> <span class="bp">=</span> <span class="n">x₁</span><span class="o">)</span> <span class="o">(</span><span class="n">R2</span> <span class="o">:</span> <span class="n">e₂</span><span class="bp">.</span><span class="kn">eval</span> <span class="n">X</span> <span class="bp">=</span> <span class="n">x₂</span><span class="o">)</span> <span class="o">:</span> <span class="n">x₁</span> <span class="bp">=</span> <span class="n">x₂</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">rw</span> <span class="o">[</span><span class="err">←</span> <span class="n">R1</span><span class="o">,</span> <span class="err">←</span> <span class="n">R2</span><span class="o">,</span> <span class="err">←</span> <span class="n">to_poly_eval</span><span class="o">,</span><span class="n">poly</span><span class="bp">.</span><span class="n">eval_is_eq</span> <span class="n">X</span> <span class="n">H</span><span class="o">,</span> <span class="n">to_poly_eval</span><span class="o">]</span>
</pre></div>

#### [ Kevin Buzzard (Jun 13 2018 at 18:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/128016043):
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">)</span> <span class="o">:</span> <span class="o">(</span><span class="n">x</span> <span class="bp">+</span> <span class="mi">1</span><span class="o">)</span> <span class="bp">*</span> <span class="o">(</span><span class="n">x</span> <span class="bp">+</span> <span class="mi">1</span><span class="o">)</span> <span class="bp">=</span> <span class="n">x</span><span class="bp">*</span><span class="n">x</span><span class="bp">+</span><span class="mi">2</span><span class="bp">*</span><span class="n">x</span><span class="bp">+</span><span class="mi">1</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">do</span> <span class="n">ring_tac</span> <span class="bp">```</span><span class="o">(</span><span class="n">x</span><span class="o">)</span>

<span class="kn">example</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="bp">ℤ</span><span class="o">)</span> <span class="o">:</span> <span class="o">(</span><span class="n">x</span> <span class="bp">+</span> <span class="mi">1</span><span class="o">)</span> <span class="bp">+</span> <span class="o">((</span><span class="bp">-</span><span class="mi">1</span><span class="o">)</span><span class="bp">*</span><span class="n">x</span> <span class="bp">+</span> <span class="mi">1</span><span class="o">)</span> <span class="bp">=</span> <span class="mi">2</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">do</span> <span class="n">ring_tac</span> <span class="bp">```</span><span class="o">(</span><span class="n">x</span><span class="o">)</span>
</pre></div>

#### [ Kevin Buzzard (Jun 13 2018 at 18:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/128016051):
<p>they both work :-)</p>

#### [ Mario Carneiro (Jun 14 2018 at 00:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/128034425):
<p>I wouldn't recommend using a quotient, although it probably won't hurt</p>

#### [ Mario Carneiro (Jun 14 2018 at 00:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/128034426):
<p>The VM can erase that stuff but the kernel has to deal with it all</p>

#### [ Mario Carneiro (Jun 14 2018 at 00:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/128034427):
<p>if you keep all the functions simple and nondependent, the kernel doesn't have to carry around all the proof garbage</p>

#### [ Mario Carneiro (Jun 14 2018 at 00:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/128034428):
<p>for the reason of "working with a handicap" I mentioned</p>

#### [ Mario Carneiro (Jun 14 2018 at 01:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/128034990):
<p>Your definition didn't work on <code>poly</code> because it uses well founded recursion, which is another kernel no-no (it has to unfold the well foundedness proofs)</p>

#### [ Mario Carneiro (Jun 14 2018 at 01:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/128034994):
<p>Try this instead:</p>
<div class="codehilite"><pre><span></span>def poly.is_zero : poly → bool
| [] := tt
| (h :: t) := (h = 0) &amp;&amp; poly.is_zero t

def poly.is_eq : poly → poly → bool
| l₁ [] := poly.is_zero l₁
| [] l₂ := poly.is_zero l₂
| (h₁ :: t₁) (h₂ :: t₂) := if (h₁ = h₂) then poly.is_eq t₁ t₂ else ff
</pre></div>


<p>(sorry for all the proof obligations!)</p>

#### [ Mario Carneiro (Jun 14 2018 at 01:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/128035061):
<p>(Alternatively, if you defined subtraction or an equivalent you could use only <code>is_zero</code> and define <code>is_eq</code> by <code>(p1 - p2).is_zero</code>)</p>

#### [ Kevin Buzzard (Jun 14 2018 at 09:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/128050689):
<p>Why bool and not Prop?</p>

#### [ Moses Schönfinkel (Jun 14 2018 at 09:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/128050810):
<p>He did it on purpose to prompt this question! ;)</p>

#### [ Kevin Buzzard (Jun 14 2018 at 10:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/128054279):
<p><a href="https://xenaproject.wordpress.com/2018/06/13/ab3/" target="_blank" title="https://xenaproject.wordpress.com/2018/06/13/ab3/">https://xenaproject.wordpress.com/2018/06/13/ab3/</a></p>

#### [ Kevin Buzzard (Jun 14 2018 at 10:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/128054290):
<p>Comments welcome. That's how some baby version of tactic.ring works, at least. And of course many thanks to Mario, without whom that little project would have taken far longer to complete.</p>

#### [ Kevin Buzzard (Jun 14 2018 at 10:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/128054294):
<p>I know the post is mega-long but I am not sure I care.</p>

#### [ Johan Commelin (Jun 14 2018 at 11:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/128054577):
<p>This is chapter 3 of your book?</p>

#### [ Andrew Ashworth (Jun 14 2018 at 13:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/128059587):
<p>I read and enjoyed your blog post! My only comment is perhaps you might have a further reading section. It would be a good place to link <a href="http://adam.chlipala.net/cpdt/html/Reflection.html" target="_blank" title="http://adam.chlipala.net/cpdt/html/Reflection.html">http://adam.chlipala.net/cpdt/html/Reflection.html</a> and <a href="https://softwarefoundations.cis.upenn.edu/vfa-current/Decide.html#lab185" target="_blank" title="https://softwarefoundations.cis.upenn.edu/vfa-current/Decide.html#lab185">https://softwarefoundations.cis.upenn.edu/vfa-current/Decide.html#lab185</a> for people who are trying to seriously write a reflective tactic (although, unfortunately, you have to read Coq to understand what's going on... but I think at this stage of Lean's popularity, this is somewhat necessary regardless in the tactics game). Also, minor nitpick, but <code>znum</code> is only uber-efficient when it is used in <code>rfl</code> proofs, otherwise <code>int</code> has special fast support</p>

#### [ Kevin Buzzard (Jun 14 2018 at 16:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/128067635):
<p>Many thanks Andrew. I am not a computer scientist as I'm sure you know and I don't really know about references. I have looked, briefly, at both of the things you mention, but I have never really substantially engaged with them -- I tend to stop reading when things get "too CS" because they become less relevant to what I am trying to do in Lean. Thanks for the nitpick too.</p>

#### [ Mario Carneiro (Jun 14 2018 at 16:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/128067751):
<blockquote>
<p>Why bool and not Prop?</p>
</blockquote>
<p>Because you can't compute with Props. You could get roughly the same behavior by using <code>decidable p</code> instead of <code>bool</code> (+ soundness proof), but since there are more dependency tricks there I suspect it's marginally slower than using bool (but not by any large margin).</p>

#### [ Mario Carneiro (Jun 14 2018 at 16:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/128067896):
<p>In this case, the bool definition functions both as the relation itself and its decidability proof. If you wanted to use decidable, then, it would be two definitions and a soundness proof</p>

#### [ Kevin Buzzard (Jun 14 2018 at 19:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/how%20does%20tactic.ring%20work%3F/near/128074464):
<blockquote>
<p>This is chapter 3 of your book?</p>
</blockquote>
<p>I am not sure if this is book material.</p>


{% endraw %}
