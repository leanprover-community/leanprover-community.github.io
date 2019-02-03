---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/86990letinstructure.html
---

## Stream: [general](index.html)
### Topic: [let in structure](86990letinstructure.html)

---


{% raw %}
#### [ Kevin Buzzard (Jun 02 2018 at 05:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127451506):
<div class="codehilite"><pre><span></span><span class="kn">structure</span> <span class="n">foo</span> <span class="o">:=</span>
<span class="k">let</span> <span class="n">bar</span> <span class="o">:=</span> <span class="bp">ℕ</span> <span class="k">in</span>
<span class="o">(</span><span class="mi">3</span> <span class="o">:</span> <span class="n">bar</span><span class="o">)</span>
</pre></div>

#### [ Kevin Buzzard (Jun 02 2018 at 05:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127451510):
<p>doesn't work</p>

#### [ Kevin Buzzard (Jun 02 2018 at 05:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127451512):
<p>moans about the let</p>

#### [ Kevin Buzzard (Jun 02 2018 at 05:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127451518):
<p>Am I doomed to write <code>power_bounded_elements R</code> throughout this entire definition?</p>

#### [ Johan Commelin (Jun 02 2018 at 05:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127451561):
<p>well, we can make some notation for it, right?</p>

#### [ Johan Commelin (Jun 02 2018 at 05:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127451618):
<p>Isn't double-superscript-circ common for this?</p>

#### [ Kevin Buzzard (Jun 02 2018 at 05:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127451693):
<p>aah here notation will solve my problem</p>

#### [ Kevin Buzzard (Jun 02 2018 at 05:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127451695):
<p>wait</p>

#### [ Kevin Buzzard (Jun 02 2018 at 05:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127451697):
<p>oh I have to leave the stupid gap</p>

#### [ Kevin Buzzard (Jun 02 2018 at 05:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127451738):
<p><span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>R</mi><mtext> </mtext><msup><mrow></mrow><mo>∘</mo></msup></mrow><annotation encoding="application/x-tex">R\ {}^\circ</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.00773em;">R</span><span class="mord"><span class="mspace"> </span><span class="mord"></span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.674115em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mbin mtight">∘</span></span></span></span></span></span></span></span></span></span></span></p>

#### [ Kevin Buzzard (Jun 02 2018 at 05:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127451740):
<p>need the gap because of some fussy tokenizer</p>

#### [ Johan Commelin (Jun 02 2018 at 05:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127451804):
<p>It feels a bit like we are back to the typography of SGA etc, doesn't it?</p>

#### [ Andrew Ashworth (Jun 02 2018 at 05:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127451805):
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">bar</span> <span class="o">:</span> <span class="kt">Type</span> <span class="o">:=</span> <span class="bp">ℕ</span>

<span class="kn">structure</span> <span class="n">foo</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">bar</span><span class="o">)</span>
</pre></div>


<p>I am unsure how to choose between notation and defs when you don't need infix/postfix parsing</p>

#### [ Simon Hudon (Jun 02 2018 at 05:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127451843):
<p>I assume you're making it into a postfix operator. Why not make the whole thing (<code>R∘</code>) a notation?</p>

#### [ Johan Commelin (Jun 02 2018 at 05:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127451851):
<p>You mean including the R?</p>

#### [ Simon Hudon (Jun 02 2018 at 05:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127451853):
<p>Exactly</p>

#### [ Johan Commelin (Jun 02 2018 at 05:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127451854):
<p>But that's variable</p>

#### [ Kevin Buzzard (Jun 02 2018 at 05:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127451861):
<p><code>notation : R `ᵒ` := power_bounded_subring R</code></p>

#### [ Kevin Buzzard (Jun 02 2018 at 05:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127451862):
<p>How does notation work? I never know. I need some notation notes</p>

#### [ Simon Hudon (Jun 02 2018 at 05:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127451863):
<p>If you declare it with <code>variable</code>, and make your notation local, that should be ok</p>

#### [ Kevin Buzzard (Jun 02 2018 at 05:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127451864):
<p>I know I can search through TPIL</p>

#### [ Johan Commelin (Jun 02 2018 at 05:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127451865):
<p>Yay for Zulip's parsing of "`".</p>

#### [ Simon Hudon (Jun 02 2018 at 05:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127451866):
<p>Use more ticks until it works</p>

#### [ Kevin Buzzard (Jun 02 2018 at 05:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127451867):
<p>right</p>

#### [ Kevin Buzzard (Jun 02 2018 at 06:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127451870):
<p>I use two outer ticks</p>

#### [ Johan Commelin (Jun 02 2018 at 06:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127451919):
<p><span class="user-mention" data-user-id="110026">@Simon Hudon</span> Aah, it's not <code>variable</code> like that. It is really variable in the notation.</p>

#### [ Johan Commelin (Jun 02 2018 at 06:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127451920):
<p>Like <code>x</code> and <code>y</code> in <code>x + y</code>.</p>

#### [ Kevin Buzzard (Jun 02 2018 at 06:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127451923):
<p>I can't get the notation to work though</p>

#### [ Simon Hudon (Jun 02 2018 at 06:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127451934):
<p>I must have misunderstood. I thought you wanted a local shorthand for the current file.</p>

#### [ Johan Commelin (Jun 02 2018 at 06:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127451935):
<p>Hmm, but now you didn't leave a gap in the ticks.</p>

#### [ Johan Commelin (Jun 02 2018 at 06:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127451980):
<p>I think it wants spaces around the <code>\circ</code></p>

#### [ Simon Hudon (Jun 02 2018 at 06:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127451981):
<p>Otherwise, you can use <code>postfix `ᵒ` := power_bounded_subring</code></p>

#### [ Kevin Buzzard (Jun 02 2018 at 06:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127451983):
<p>oh that looks like a nicer way to do it</p>

#### [ Kevin Buzzard (Jun 02 2018 at 06:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127451988):
<p>it wants a number</p>

#### [ Kevin Buzzard (Jun 02 2018 at 06:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127451990):
<p><code>postfix `ᵒ` : 37 := power_bounded_subring</code></p>

#### [ Kevin Buzzard (Jun 02 2018 at 06:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452028):
<p>that should do it</p>

#### [ Kevin Buzzard (Jun 02 2018 at 06:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452034):
<p>I must say, operator precedence is something else I am not sure I have a good feeling about</p>

#### [ Kevin Buzzard (Jun 02 2018 at 06:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452035):
<p>I guess I want this one to be very sticky</p>

#### [ Kevin Buzzard (Jun 02 2018 at 06:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452042):
<p>so should it be like 6 or 999999?</p>

#### [ Simon Hudon (Jun 02 2018 at 06:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452044):
<p>To be fair, I'm not fond of putting precedence on a linear scale. I feel like specifying a partial order would be easier</p>

#### [ Kevin Buzzard (Jun 02 2018 at 06:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452083):
<p>OK how about this:</p>

#### [ Kevin Buzzard (Jun 02 2018 at 06:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452086):
<div class="codehilite"><pre><span></span><span class="kn">structure</span> <span class="n">perfectoid_ring</span> <span class="o">(</span><span class="n">R</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">(</span><span class="n">p</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">[</span><span class="n">is_prime</span> <span class="n">p</span><span class="o">]</span> <span class="kn">extends</span> <span class="n">Tate_ring</span> <span class="n">R</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">is_complete</span> <span class="o">:</span> <span class="n">complete</span> <span class="n">R</span><span class="o">)</span>
<span class="o">(</span><span class="n">is_uniform</span>  <span class="o">:</span> <span class="n">uniform</span> <span class="n">R</span><span class="o">)</span>
<span class="o">(</span><span class="n">ramified</span>    <span class="o">:</span> <span class="bp">∃</span> <span class="n">ω</span> <span class="o">:</span> <span class="n">R</span> <span class="err">ᵒ</span><span class="o">,</span>
                 <span class="o">(</span><span class="n">is_pseudo_uniformizer</span> <span class="n">ω</span><span class="o">)</span> <span class="bp">∧</span> <span class="o">(</span><span class="n">ω</span> <span class="err">^</span> <span class="n">p</span> <span class="err">∣</span> <span class="n">p</span><span class="o">))</span>
 <span class="o">(</span><span class="n">Frob</span>       <span class="o">:</span> <span class="bp">∀</span> <span class="n">a</span> <span class="o">:</span> <span class="n">R</span> <span class="err">ᵒ</span><span class="o">,</span>
                 <span class="bp">∃</span> <span class="n">b</span> <span class="n">c</span> <span class="o">:</span> <span class="n">R</span> <span class="err">ᵒ</span><span class="o">,</span> <span class="n">a</span> <span class="bp">=</span> <span class="n">b</span> <span class="err">^</span> <span class="n">p</span> <span class="bp">+</span> <span class="n">p</span> <span class="bp">*</span> <span class="n">c</span><span class="o">)</span>
</pre></div>

#### [ Simon Hudon (Jun 02 2018 at 06:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452087):
<p>Think about the operators that are likely to appear in the same formula (including <code>=</code>) and what should take precedence</p>

#### [ Kevin Buzzard (Jun 02 2018 at 06:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452094):
<p>I want the circ to take precedence in the sense that I want R circ being evaluated ASAP</p>

#### [ Kevin Buzzard (Jun 02 2018 at 06:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452097):
<p>i.e. <code>A x B o</code> is definitely <code>A x (B o)</code></p>

#### [ Simon Hudon (Jun 02 2018 at 06:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452098):
<p>precedence and evaluation order are not the same</p>

#### [ Kevin Buzzard (Jun 02 2018 at 06:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452099):
<p><span class="user-mention" data-user-id="112680">@Johan Commelin</span> I reckon that looks fairly readable</p>

#### [ Kevin Buzzard (Jun 02 2018 at 06:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452139):
<p>Simon I don't know anything about this stuff</p>

#### [ Johan Commelin (Jun 02 2018 at 06:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452140):
<p>Yes, this looks very good. I hope you can maintain this throughout the top-down approach.</p>

#### [ Kevin Buzzard (Jun 02 2018 at 06:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452141):
<p>and I know I can learn it but I'm not that interested in it</p>

#### [ Simon Hudon (Jun 02 2018 at 06:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452144):
<p>I'll leave you guys to it</p>

#### [ Kevin Buzzard (Jun 02 2018 at 06:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452145):
<p>do you have a good suggestion for a number?</p>

#### [ Kevin Buzzard (Jun 02 2018 at 06:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452150):
<p>or else I'll leave it as 37 :-/</p>

#### [ Mario Carneiro (Jun 02 2018 at 06:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452151):
<p>same as unary minus?</p>

#### [ Mario Carneiro (Jun 02 2018 at 06:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452157):
<p>which is 65</p>

#### [ Simon Hudon (Jun 02 2018 at 06:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452159):
<p>That looks like asking for trouble. Go one over or one below</p>

#### [ Johan Commelin (Jun 02 2018 at 06:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452198):
<p>Is there anything below <code>50</code> at the moment?</p>

#### [ Mario Carneiro (Jun 02 2018 at 06:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452201):
<p>tons</p>

#### [ Mario Carneiro (Jun 02 2018 at 06:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452203):
<p>propositional stuff mostly</p>

#### [ Mario Carneiro (Jun 02 2018 at 06:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452208):
<p>50 is <code>=</code>, so that's about as low as you get for atomic propositions</p>

#### [ Kevin Buzzard (Jun 02 2018 at 06:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452209):
<p>ha ha (-Ro) -- is that what you're worried about Simon?</p>

#### [ Mario Carneiro (Jun 02 2018 at 06:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452212):
<p>but types go lower than that</p>

#### [ Kevin Buzzard (Jun 02 2018 at 06:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452213):
<p>can that sort of thing be an issue?</p>

#### [ Mario Carneiro (Jun 02 2018 at 06:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452216):
<p>equal isn't really a problem</p>

#### [ Mario Carneiro (Jun 02 2018 at 06:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452219):
<p>in fact it's important for having things be at the same level, like <code>a + b - c</code></p>

#### [ Mario Carneiro (Jun 02 2018 at 06:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452220):
<p>which is left associated regardless of whether <code>+</code> or <code>-</code> comes first</p>

#### [ Johan Commelin (Jun 02 2018 at 06:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452267):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> If you want to squeeze out a little bit more readability, then maybe <code>Frob</code> should be phrased as a statement modulo <code>p</code>.</p>

#### [ Mario Carneiro (Jun 02 2018 at 06:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452268):
<p>there aren't many postfix operators in standard lean; there is <code>⁻¹</code> which has a crazy high precedence <code>max+10</code></p>

#### [ Simon Hudon (Jun 02 2018 at 06:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452307):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> I'm not sure what Lean does in that kind of situation and I can't think of reasons why either of (-R)o or -(Ro) would be always the best default</p>

#### [ Kevin Buzzard (Jun 02 2018 at 06:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452309):
<p>I wasn't sure how to do quotient rings in Lean</p>

#### [ Johan Commelin (Jun 02 2018 at 06:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452310):
<p>But I guess, you rather prefer avoiding quotients.</p>

#### [ Kevin Buzzard (Jun 02 2018 at 06:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452311):
<p>actually I recently learnt how to use quotient types</p>

#### [ Kevin Buzzard (Jun 02 2018 at 06:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452312):
<p>I was forced to</p>

#### [ Mario Carneiro (Jun 02 2018 at 06:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452313):
<p>All notations come with a binding power, whichever is higher wins</p>

#### [ Kevin Buzzard (Jun 02 2018 at 06:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452315):
<p>I needed direct limits and Kenny's work is still not in mathlib</p>

#### [ Mario Carneiro (Jun 02 2018 at 06:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452321):
<p>that includes mixing pre/postfix</p>

#### [ Johan Commelin (Jun 02 2018 at 06:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452322):
<p><span class="user-mention" data-user-id="110026">@Simon Hudon</span> In both cases the unary minus doens't make much sense. (At least not in contemporary maths. Maybe someone wants to overload it, but that thought gives me shudders...)</p>

#### [ Johan Commelin (Jun 02 2018 at 06:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452324):
<p>So I guess in practice there won't be a problem.</p>

#### [ Mario Carneiro (Jun 02 2018 at 06:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452364):
<p>Since <code>R o</code> here is a type it really doesn't matter as long as it's higher than 50 or so</p>

#### [ Johan Commelin (Jun 02 2018 at 06:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452372):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> I told you before that <code>57</code> is a better default value than <code>37</code>! Grothendieck was careful when choosing his prime!</p>

#### [ Mario Carneiro (Jun 02 2018 at 06:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452378):
<p>lol it would be funny if all the notation precedences were primes just because</p>

#### [ Johan Commelin (Jun 02 2018 at 06:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452379):
<p>Ooh, now I have a crazy question. What is the type of <code>65</code> in the notation for unary minus? Does it even have a type?</p>

#### [ Mario Carneiro (Jun 02 2018 at 06:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452420):
<p>It was once <code>num</code>, which was for a long time the only use of <code>num</code>. Now it's <code>nat</code></p>

#### [ Kevin Buzzard (Jun 02 2018 at 06:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452423):
<p><code>instance p : nat</code></p>

#### [ Kevin Buzzard (Jun 02 2018 at 06:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452424):
<p>Does this lead me into trouble?</p>

#### [ Kevin Buzzard (Jun 02 2018 at 06:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452425):
<p>I am sick of this p</p>

#### [ Kevin Buzzard (Jun 02 2018 at 06:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452430):
<p>I want access to it at all times and yet I never want to carry it around</p>

#### [ Kevin Buzzard (Jun 02 2018 at 06:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452434):
<p>It's a global variable</p>

#### [ Mario Carneiro (Jun 02 2018 at 06:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452435):
<p>see e.g. <code>std.prec.max</code></p>

#### [ Mario Carneiro (Jun 02 2018 at 06:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452437):
<p>In actual notation commands though the number is not an expression of type nat, it's a literal number string</p>

#### [ Mario Carneiro (Jun 02 2018 at 06:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452478):
<p>although you can use <code>max</code> and other things in that spot too</p>

#### [ Kevin Buzzard (Jun 02 2018 at 06:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452482):
<p>wait</p>

#### [ Kevin Buzzard (Jun 02 2018 at 06:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452483):
<p>I have to make nat a class</p>

#### [ Kevin Buzzard (Jun 02 2018 at 06:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452484):
<p>oh jeez where's that bit in the manual</p>

#### [ Kevin Buzzard (Jun 02 2018 at 06:20)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452485):
<p>now I finally want to do it</p>

#### [ Johan Commelin (Jun 02 2018 at 06:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452532):
<p>Do you mean like <code>attribute [class] nat</code>?</p>

#### [ Mario Carneiro (Jun 02 2018 at 06:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452581):
<p>don't make <code>nat</code> a class</p>

#### [ Mario Carneiro (Jun 02 2018 at 06:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452590):
<p>make <code>Prime</code> a class</p>

#### [ Johan Commelin (Jun 02 2018 at 06:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452635):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> Can't you have</p>
<div class="codehilite"><pre><span></span><span class="kn">variables</span> <span class="o">(</span><span class="n">p</span> <span class="o">:</span> <span class="n">nat</span><span class="o">)</span> <span class="o">(</span><span class="n">hp</span> <span class="o">:</span> <span class="n">prime</span> <span class="n">p</span><span class="o">)</span>
<span class="n">include</span> <span class="n">p</span> <span class="n">hp</span>
</pre></div>

#### [ Johan Commelin (Jun 02 2018 at 06:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452638):
<p>Does that make <code>p</code> and <code>hp</code> available everywhere you want them?</p>

#### [ Kevin Buzzard (Jun 02 2018 at 06:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452689):
<p>I'm using type class inference to carry around primality of p</p>

#### [ Mario Carneiro (Jun 02 2018 at 06:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452690):
<div class="codehilite"><pre><span></span>import data.nat.prime algebra.group_power

class Prime :=
(p : ℕ) (pp : nat.prime p)
open Prime

section
variable [Prime]

example (R) [ring R] (x : R) : x ^ 2 = x ^ p := sorry

end
</pre></div>

#### [ Kevin Buzzard (Jun 02 2018 at 06:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452737):
<p>I thought <code>Prime</code> was supposed to be the subtype</p>

#### [ Mario Carneiro (Jun 02 2018 at 06:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452738):
<p>it is</p>

#### [ Kevin Buzzard (Jun 02 2018 at 06:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452739):
<p>I suppose</p>

#### [ Kevin Buzzard (Jun 02 2018 at 06:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452746):
<p>this way you get to change the name from <code>val</code> to <code>p</code></p>

#### [ Mario Carneiro (Jun 02 2018 at 06:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452748):
<p>Actually I said "bundled structure", so this is in some sense more faithful to the convention</p>

#### [ Kevin Buzzard (Jun 02 2018 at 06:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452749):
<p>Is this sort of stuff mathlib-acceptable?</p>

#### [ Mario Carneiro (Jun 02 2018 at 06:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452788):
<p>only if you use it a lot</p>

#### [ Mario Carneiro (Jun 02 2018 at 06:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452791):
<p>I would prefer that you postprocess all your final theorems or whatever to make the prime explicit, but you can do this within the development if it helps</p>

#### [ Andrew Ashworth (Jun 02 2018 at 06:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452806):
<p>is <code>p</code> actually <code>default nat</code> in that code snippet?</p>

#### [ Mario Carneiro (Jun 02 2018 at 06:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452846):
<p>it's like <code>default nat</code> but not the same value</p>

#### [ Mario Carneiro (Jun 02 2018 at 06:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452847):
<p>This is one of the important aspects of creating a new <code>class</code> - you get to create your own typeclass graph</p>

#### [ Mario Carneiro (Jun 02 2018 at 06:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452853):
<p>in this case, since there are no instances of <code>Prime</code>, it will only ever pick up <code>[Prime]</code> in the context</p>

#### [ Mario Carneiro (Jun 02 2018 at 06:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452895):
<p>maybe <code>fixed_prime</code> is a better name for this typeclass</p>

#### [ Andrew Ashworth (Jun 02 2018 at 06:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452896):
<p>at first glance, this seems kinda hackish to me, but I need to think about it some</p>

#### [ Kevin Buzzard (Jun 02 2018 at 06:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452897):
<p>It very much conveys what's going on</p>

#### [ Andrew Ashworth (Jun 02 2018 at 06:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452901):
<p>the whole <code>variable [Prime]</code> has me for a loop</p>

#### [ Kevin Buzzard (Jun 02 2018 at 06:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452905):
<p>I won't be using it a lot for the definition of perfectoid spaces</p>

#### [ Johan Commelin (Jun 02 2018 at 06:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452906):
<p>Same here. I still don't get how Lean figures out what <code>p</code> means in the line<br>
<code>example (R) [ring R] (x : R) : x ^ 2 = x ^ p := sorry</code></p>

#### [ Kevin Buzzard (Jun 02 2018 at 06:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452907):
<p>it's just you'll use it all the time the moment you start proving theorems about them</p>

#### [ Mario Carneiro (Jun 02 2018 at 06:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452908):
<p>Since <code>Prime</code> was opened, that's <code>Prime.p</code></p>

#### [ Johan Commelin (Jun 02 2018 at 06:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452947):
<p>Aah, cool!</p>

#### [ Mario Carneiro (Jun 02 2018 at 06:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452948):
<p>which has an implicit typeclass argument <code>[Prime]</code>, which is discovered in the context</p>

#### [ Johan Commelin (Jun 02 2018 at 06:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452951):
<p>So then once we start doing etale cohomology we want another class <code>fixed_coprime_prime</code>, and constructor <code>ℓ</code></p>

#### [ Johan Commelin (Jun 02 2018 at 06:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452954):
<p>And a proof that it is not <code>p</code></p>

#### [ Mario Carneiro (Jun 02 2018 at 06:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127452998):
<div class="codehilite"><pre><span></span>class fixed_prime :=
(p : ℕ)
(pp : nat.prime p)
open fixed_prime

class fixed_coprime [fixed_prime] :=
(q : ℕ)
(co : nat.coprime p q)
</pre></div>

#### [ Johan Commelin (Jun 02 2018 at 06:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127453000):
<p>Mario, I really like this! I hope that it is not to hackish for Lean. This reflects how <code>p</code> is used in a lot of number theory/alg.geom. You just fix <code>p</code> at the beginning of your paper, and it doesn't change for 50 pages.</p>

#### [ Johan Commelin (Jun 02 2018 at 06:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127453006):
<p>Yes, but the <code>ℓ</code> has to be prime as well. As in "ℓ-adic cohomology" etc...</p>

#### [ Mario Carneiro (Jun 02 2018 at 06:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127453007):
<p>I haven't attempted to use this technique before. I'd be interested to see how it goes</p>

#### [ Andrew Ashworth (Jun 02 2018 at 06:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127453008):
<p>it feels like an end run around <code>parameter</code></p>

#### [ Mario Carneiro (Jun 02 2018 at 06:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127453047):
<p>you get the idea</p>

#### [ Johan Commelin (Jun 02 2018 at 06:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127453050):
<p>Sure.</p>

#### [ Johan Commelin (Jun 02 2018 at 06:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127453051):
<p>I will try to use it in the stuff on p-adic valuations.</p>

#### [ Mario Carneiro (Jun 02 2018 at 06:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127453056):
<p>Note that actually applying this for real primes, like if you want 57-adic cohomology, is a bit of a pain</p>

#### [ Johan Commelin (Jun 02 2018 at 06:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127453091):
<p>Hmm, I see.</p>

#### [ Mario Carneiro (Jun 02 2018 at 06:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127453097):
<p>well, maybe not so bad, you can use <code>local instance</code>s or <code>haveI</code> to introduce a <code>fixed_prime</code> without doing so globally</p>

#### [ Johan Commelin (Jun 02 2018 at 06:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127453098):
<p>That's a bit of a problem, I guess. For example squares in Q_2 behave different from squares in Q_p for p ≠ 2.</p>

#### [ Mario Carneiro (Jun 02 2018 at 06:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127453145):
<p>I mean, worst case scenario is you have to write <code>@thm</code> whenever you want to apply the theorem in a non <code>p</code> case</p>

#### [ Johan Commelin (Jun 02 2018 at 06:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127453146):
<p>Yes, I see. That makes sense.</p>

#### [ Mario Carneiro (Jun 02 2018 at 06:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127453148):
<p>also you can prove things with the assumption <code>p = 2</code></p>

#### [ Johan Commelin (Jun 02 2018 at 06:46)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127453150):
<p>Right.</p>

#### [ Johan Commelin (Jun 02 2018 at 06:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127453157):
<p>Actually the <code>@</code> notation reflects exactly how most mathematicians feel about working with one concrete prime. (Of course not the symbol "@", but the fact that all of a sudden you want to be specific about <code>p</code>.)</p>

#### [ Johan Commelin (Jun 02 2018 at 06:48)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127453194):
<p>You only do this in 1% of the time. And it always feels a bit disorienting.</p>

#### [ Mario Carneiro (Jun 02 2018 at 06:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127453198):
<p>whence the 57 thing</p>

#### [ Johan Commelin (Jun 02 2018 at 06:49)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127453202):
<p>I really think that we have theorems about <code>Q_p</code>, <code>Q_ℓ</code> and <code>Q_2</code>, and that is about it (-;</p>

#### [ Mario Carneiro (Jun 02 2018 at 06:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127453247):
<p>one other messy thing is if you want to use <code>l</code> as your <code>p</code></p>

#### [ Johan Commelin (Jun 02 2018 at 06:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127453252):
<p>So, have to unpack stuff with <code>@</code> is expected behaviour.</p>

#### [ Johan Commelin (Jun 02 2018 at 06:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127453253):
<p>Aah, yes, that might get messy...</p>

#### [ Johan Commelin (Jun 02 2018 at 06:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127453254):
<p>Also, there is a very delicate theory about what happens when <code>ℓ = p</code>...</p>

#### [ Johan Commelin (Jun 02 2018 at 06:50)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127453255):
<p>Headache ensues</p>

#### [ Johan Commelin (Jun 02 2018 at 06:51)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127453261):
<p>(Note: this is not relevant for defining perfectoid spaces. But it will definitely pop up later.)</p>

#### [ Mario Carneiro (Jun 02 2018 at 06:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127453302):
<p>Long story short, this technique is useful for fixing a value for a long time, with the downside being it makes unfixing it hard</p>

#### [ Mario Carneiro (Jun 02 2018 at 06:52)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127453303):
<p>parameters are easier to unfix, but then they stay unfixed</p>

#### [ Johan Commelin (Jun 02 2018 at 06:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127453347):
<p>Ok, so maybe we should do the same thing as with multiplicative groups and additive groups. And just develop the theory both for <code>p</code> and for <code>ℓ</code>...</p>

#### [ Mario Carneiro (Jun 02 2018 at 06:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127453351):
<p>That's not unreasonable; the theorems are defeq so you just have to state them</p>

#### [ Johan Commelin (Jun 02 2018 at 06:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127453354):
<p>Hmm, but sometimes you also want to compare what happens at <code>ℓ_1</code> and <code>ℓ_2</code>... and both are different from <code>p</code>.</p>

#### [ Mario Carneiro (Jun 02 2018 at 06:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127453360):
<p>maybe <code> ℓ</code> shouldn't be as fixed as <code>p</code></p>

#### [ Johan Commelin (Jun 02 2018 at 06:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127453361):
<p>Or statements like <code>\forall ℓ : (ℓ ≠ p) blabla</code>.</p>

#### [ Andrew Ashworth (Jun 02 2018 at 06:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127453401):
<p>an argument for using a parameter might be that when you use <code>haveI</code> and friends, you don't get to benefit from type class caching... although I am unsure how much time Lean spends searching the type class graph - it's not something I have a good feel for</p>

#### [ Mario Carneiro (Jun 02 2018 at 06:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127453402):
<p>in practice I've never seen an appreciable difference from using <code>haveI</code></p>

#### [ Johan Commelin (Jun 02 2018 at 06:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127453407):
<p>Ok, maybe <code>ℓ</code> should indeed have less fixiness than <code>p</code>.</p>

#### [ Andrew Ashworth (Jun 02 2018 at 07:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127453505):
<p>I think it might be a bigger deal for people working in interactive tactic mode... who have very large proofs / definitions</p>

#### [ Andrew Ashworth (Jun 02 2018 at 07:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127453512):
<p>again, it ::sounds:: scary to me, also because I don't mind at all being explicit, but that may be because I don't have enough Lean experience</p>

#### [ Andrew Ashworth (Jun 02 2018 at 07:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/let%20in%20structure/near/127453756):
<p>would it affect memoization? suppose you had</p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">myDef</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">expensive_tac1</span><span class="o">,</span>  <span class="c1">-- uses typeclass inference somewhere</span>
  <span class="n">expensive_tac2</span>  <span class="c1">-- does this mean we can&#39;t memoize the results of expensive_tac1 if we disable type class cache?</span>
<span class="kn">end</span>
</pre></div>


{% endraw %}
