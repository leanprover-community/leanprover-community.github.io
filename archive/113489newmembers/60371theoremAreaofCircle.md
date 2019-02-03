---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/60371theoremAreaofCircle.html
---

## Stream: [new members](https://leanprover-community.github.io/archive/113489newmembers/index.html)
### Topic: [theorem Area_of_Circle](https://leanprover-community.github.io/archive/113489newmembers/60371theoremAreaofCircle.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Mii Nguyen (Nov 28 2018 at 16:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/theorem%20Area_of_Circle/near/148720034):
<p>Hello. I'm My, a very new beginner of Lean user.  I come from Formal Abstract's group in Hanoi. Recently I try to formalize the theorem of  'Area of a circle'. So far I have</p>
<div class="codehilite"><pre><span></span>theorem Area_of_Circle (x: ℝ × ℝ) (r :ℝ) (r ≥ 0) [measure_theory.measure_space (ℝ × ℝ)] [measure_theory.measure_space (closed_ball (x) (r))]: measure_theory.volume(closed_ball (x) (r)) = 2 * real.pi * r^2 :=sorry
</pre></div>


<p>It seems to work. But if I defined the Circle, then use it in the theorem, it sends me an error 'don't know how to synthesize placeholder'</p>
<div class="codehilite"><pre><span></span>variables {x: ℝ × ℝ }{r: ℝ}

def Circle{x: ℝ × ℝ }{r: ℝ} {r ≥ 0} := closed_ball (x) (r)

theorem Area (r ≥ 0) [measure_theory.measure_space (ℝ × ℝ)] [measure_theory.measure_space (Circle)]: measure_theory.volume(Circle) = 2 * real.pi * r^2 :=sorry
#print Area
</pre></div>


<p>Could anyone please explain it to me?  How can I defind a set the use it in theorem? Thank you very much for your time,<br>
My</p>

#### [ Johan Commelin (Nov 28 2018 at 16:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/theorem%20Area_of_Circle/near/148720601):
<p>The <code>[measure_theory.measure_space (ℝ × ℝ)]</code> introduces a new measure (about which you can't say anything).</p>

#### [ Kevin Buzzard (Nov 28 2018 at 16:45)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/theorem%20Area_of_Circle/near/148720622):
<p>Yes -- you should delete this</p>

#### [ Johan Commelin (Nov 28 2018 at 16:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/theorem%20Area_of_Circle/near/148720633):
<p>You would want to use the existing measure. And probably you want to use integration to calculate the area.</p>

#### [ Johan Commelin (Nov 28 2018 at 16:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/theorem%20Area_of_Circle/near/148720691):
<p>So far there is very little about integration, as far as I know.</p>

#### [ Johan Commelin (Nov 28 2018 at 16:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/theorem%20Area_of_Circle/near/148720705):
<p>So I fear this is going to be a pretty hard exercise.</p>

#### [ Johan Commelin (Nov 28 2018 at 16:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/theorem%20Area_of_Circle/near/148721396):
<p>Or well, if you only want to state the theorem (not prove it), that should be possible.</p>

#### [ Johan Commelin (Nov 28 2018 at 16:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/theorem%20Area_of_Circle/near/148721494):
<p><span class="user-mention" data-user-id="138627">@Mii Nguyen</span> I think you should also make the <code>x</code> and <code>r</code> arguments to <code>Circle</code> explicit. (By using <code>()</code> instead of <code>{}</code>.) That way it is clearer about which circle you are talking.</p>

#### [ Patrick Massot (Nov 28 2018 at 16:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/theorem%20Area_of_Circle/near/148721933):
<p>I just had a look, it seems we have Lebesgue measure for R, but no product instance for measurable spaces, so that would be needed in order to state this theorem. It shouldn't be hard. As Johan wrote,  you also need better understanding of implicit vs explicit arguments. A better starting point would be:</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">analysis</span><span class="bp">.</span><span class="n">measure_theory</span><span class="bp">.</span><span class="n">lebesgue_measure</span>
<span class="kn">import</span> <span class="n">analysis</span><span class="bp">.</span><span class="n">exponential</span>
<span class="kn">open</span> <span class="n">real</span>

<span class="n">def</span> <span class="n">Circle</span> <span class="o">(</span><span class="n">x</span><span class="o">:</span> <span class="n">ℝ</span> <span class="bp">×</span> <span class="n">ℝ</span><span class="o">)</span> <span class="o">(</span><span class="n">r</span><span class="o">:</span> <span class="n">ℝ</span><span class="o">)</span>  <span class="o">:=</span> <span class="n">closed_ball</span> <span class="n">x</span> <span class="n">r</span>

<span class="kn">theorem</span> <span class="n">Area</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">ℝ</span> <span class="bp">×</span> <span class="n">ℝ</span><span class="o">)</span> <span class="o">{</span><span class="n">r</span> <span class="o">:</span> <span class="n">ℝ</span><span class="o">}</span> <span class="o">(</span><span class="n">H</span> <span class="o">:</span> <span class="n">r</span> <span class="bp">≥</span> <span class="mi">0</span><span class="o">)</span> <span class="o">:</span> <span class="n">measure_theory</span><span class="bp">.</span><span class="n">volume</span><span class="o">(</span><span class="n">Circle</span> <span class="n">x</span> <span class="n">r</span><span class="o">)</span> <span class="bp">=</span> <span class="n">some</span> <span class="bp">⟨</span><span class="mi">2</span> <span class="bp">*</span> <span class="n">pi</span> <span class="bp">*</span> <span class="n">r</span><span class="err">^</span><span class="mi">2</span><span class="o">,</span> <span class="bp">_⟩</span> <span class="o">:=</span><span class="n">sorry</span>
</pre></div>

#### [ Patrick Massot (Nov 28 2018 at 16:59)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/theorem%20Area_of_Circle/near/148722012):
<p>The underscore at the very end is an exercise to fill in, it must be replaced by a proof of <code>0 &lt;= 2 * pi * r^2</code></p>

#### [ Patrick Massot (Nov 28 2018 at 17:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/theorem%20Area_of_Circle/near/148722176):
<p>After filling in this proof, Lean will still complain it doesn't know what measure to use on ℝ × ℝ but, as  I wrote, this require adding something to mathlib</p>

#### [ Patrick Massot (Nov 28 2018 at 17:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/theorem%20Area_of_Circle/near/148722321):
<p>The <code>some</code> is a bit annoying, it's there in order to indicate that this disk has finite measure. I guess the interface is still very rough here</p>

#### [ Chris Hughes (Nov 28 2018 at 17:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/theorem%20Area_of_Circle/near/148722740):
<p>I thought the area of a circle was <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>π</mi><msup><mi>r</mi><mn>2</mn></msup></mrow><annotation encoding="application/x-tex">\pi r^2</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.8141079999999999em;"></span><span class="strut bottom" style="height:0.8141079999999999em;vertical-align:0em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.03588em;">π</span><span class="mord"><span class="mord mathit" style="margin-right:0.02778em;">r</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.8141079999999999em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathrm mtight">2</span></span></span></span></span></span></span></span></span></span></span> not <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mn>2</mn><mi>π</mi><msup><mi>r</mi><mn>2</mn></msup></mrow><annotation encoding="application/x-tex">2\pi r^2</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.8141079999999999em;"></span><span class="strut bottom" style="height:0.8141079999999999em;vertical-align:0em;"></span><span class="base"><span class="mord mathrm">2</span><span class="mord mathit" style="margin-right:0.03588em;">π</span><span class="mord"><span class="mord mathit" style="margin-right:0.02778em;">r</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.8141079999999999em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathrm mtight">2</span></span></span></span></span></span></span></span></span></span></span></p>

#### [ Patrick Massot (Nov 28 2018 at 17:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/theorem%20Area_of_Circle/near/148722777):
<p>also</p>

#### [ Patrick Massot (Nov 28 2018 at 17:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/theorem%20Area_of_Circle/near/148722858):
<p>And also I would call this a disk, not a circle, but that may be only in France</p>

#### [ Patrick Massot (Nov 28 2018 at 17:21)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/theorem%20Area_of_Circle/near/148723572):
<p><span class="user-mention" data-user-id="138627">@Mii Nguyen</span> do you want to work on the exercise of stating this theorem after admitting the existence of some relevant measure on the plane, or do you want to get an answer? I did the exercise, so I wouldn't cost me anything, but I don't want to ruin your training plan.</p>

#### [ Mii Nguyen (Nov 28 2018 at 17:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/theorem%20Area_of_Circle/near/148724576):
<p>Thank you for your advices!<br>
<span class="user-mention" data-user-id="112680">@Johan Commelin</span>  I  tried to use integration at the first time but I lost in the maze of <code>intergration.lean</code><br>
<span class="user-mention" data-user-id="112680">@Johan Commelin</span>  <span class="user-mention" data-user-id="110031">@Patrick Massot</span>  by that, I know that I need to work more in arguments. Thank you<br>
I need to declare that Circle (dist) is measurable, so I use [measure_theory.measure_space (Circle)]<br>
The exercise is good for me. So I will try to instance Lebesgue measure for RxR in mathlib.</p>

#### [ Patrick Massot (Nov 28 2018 at 17:38)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/theorem%20Area_of_Circle/near/148724821):
<p>Let me insist that correctly instantiating <code>measure_space (ℝ × ℝ)</code> is much harder than admitting its existence and finishing stating the disk area theorem. I suggest the later as a first exercise</p>


{% endraw %}
