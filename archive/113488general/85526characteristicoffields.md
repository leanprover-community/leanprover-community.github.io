---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/85526characteristicoffields.html
---

## Stream: [general](index.html)
### Topic: [characteristic of fields](85526characteristicoffields.html)

---


{% raw %}
#### [ Kenny Lau (Oct 16 2018 at 20:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135921382):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> <span class="user-mention" data-user-id="112680">@Johan Commelin</span> <span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> how should we define the <code>char</code> of a field?</p>

#### [ Mario Carneiro (Oct 16 2018 at 20:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135921432):
<p>I think your definition should be on semirings instead of zero/one/mul classes</p>

#### [ Mario Carneiro (Oct 16 2018 at 20:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135921541):
<p>I guess it could be on rings, since a nonzero characteristic semiring is a ring</p>

#### [ Chris Hughes (Oct 16 2018 at 20:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135921546):
<p>Should it be a class or just a Prop?</p>

#### [ Mario Carneiro (Oct 16 2018 at 20:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135921574):
<p>a prop, it is a prop</p>

#### [ Mario Carneiro (Oct 16 2018 at 20:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135921587):
<p>oh wait you aren't asking about <code>char_p</code></p>

#### [ Kenny Lau (Oct 16 2018 at 20:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135921653):
<p>both</p>

#### [ Chris Hughes (Oct 16 2018 at 20:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135921654):
<p>I'm asking about <code>char</code>.</p>

#### [ Kenny Lau (Oct 16 2018 at 20:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135921657):
<p>I'm asking about this thing in general</p>

#### [ Kenny Lau (Oct 16 2018 at 20:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135921670):
<p>how did metamath / other languages deal with this?</p>

#### [ Kenny Lau (Oct 16 2018 at 20:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135921676):
<p>and is char(Q) 0 or 1?</p>

#### [ Mario Carneiro (Oct 16 2018 at 20:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135921705):
<p>char(Q) is 0</p>

#### [ Kenny Lau (Oct 16 2018 at 20:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135921712):
<p>in where?</p>

#### [ Mario Carneiro (Oct 16 2018 at 20:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135921720):
<p>in metamath</p>

#### [ Mario Carneiro (Oct 16 2018 at 20:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135921723):
<p>and in math</p>

#### [ Kenny Lau (Oct 16 2018 at 20:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135921730):
<p>but how is char defined?</p>

#### [ Kenny Lau (Oct 16 2018 at 20:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135921736):
<p>I feel like there's 1,000,000 subtleties</p>

#### [ Mario Carneiro (Oct 16 2018 at 21:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135921739):
<p>the order of 1</p>

#### [ Kenny Lau (Oct 16 2018 at 21:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135921811):
<p>how is order defined?</p>

#### [ Chris Hughes (Oct 16 2018 at 21:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135921818):
<p>We don't have <code>order_of</code> on non finite groups</p>

#### [ Mario Carneiro (Oct 16 2018 at 21:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135921840):
<p>and the order of a group element is the smallest nonzero power of the element that is 1</p>

#### [ Mario Carneiro (Oct 16 2018 at 21:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135921850):
<p>or 0 if it doesn't exist</p>

#### [ Kenny Lau (Oct 16 2018 at 21:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135921852):
<p>so that's a <code>def</code> not a <code>prop</code>?</p>

#### [ Kenny Lau (Oct 16 2018 at 21:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135921861):
<p>ok I don't like this</p>

#### [ Mario Carneiro (Oct 16 2018 at 21:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135921866):
<p>metamath doesn't care about computability tho</p>

#### [ Kenny Lau (Oct 16 2018 at 21:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135921867):
<p>do we have another approach?</p>

#### [ Mario Carneiro (Oct 16 2018 at 21:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135921873):
<p>there is a computable definition yielding a <code>roption nat</code></p>

#### [ Mario Carneiro (Oct 16 2018 at 21:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135921939):
<p>and if we define <code>get_or_else</code> for <code>roption</code> then we can make it 0 otherwise</p>

#### [ Kenny Lau (Oct 16 2018 at 21:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135921988):
<p>would it be usable?</p>

#### [ Mario Carneiro (Oct 16 2018 at 21:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135922050):
<p>I am a fan of <code>roption</code> definitions; it would give you a relational interface</p>

#### [ Mario Carneiro (Oct 16 2018 at 21:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135922054):
<p><code>p \in char R</code></p>

#### [ Kevin Buzzard (Oct 16 2018 at 21:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135922092):
<p>The characteristic of a ring is the kernel of the canonical ring homomorphism from the integers to the ring.</p>

#### [ Mario Carneiro (Oct 16 2018 at 21:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135922108):
<p>there is also the ideal option</p>

#### [ Kenny Lau (Oct 16 2018 at 21:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135922114):
<blockquote>
<p>The characteristic of a ring is the kernel of the canonical ring homomorphism from the integers to the ring.</p>
</blockquote>
<p>next</p>

#### [ Kevin Buzzard (Oct 16 2018 at 21:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135922123):
<p>That's the best definition.</p>

#### [ Mario Carneiro (Oct 16 2018 at 21:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135922145):
<p>that's just restating x^n = 0 though</p>

#### [ Mario Carneiro (Oct 16 2018 at 21:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135922199):
<p>maybe a better question is not what is the characteristic but what is it for</p>

#### [ Mario Carneiro (Oct 16 2018 at 21:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135922241):
<p>We have PID defined, right? Is it constructive exists?</p>

#### [ Kenny Lau (Oct 16 2018 at 21:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135922259):
<div class="codehilite"><pre><span></span><span class="n">class</span> <span class="n">is_principal_ideal</span> <span class="o">(</span><span class="n">S</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="kt">Prop</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">principal</span> <span class="o">:</span> <span class="bp">∃</span> <span class="n">a</span> <span class="o">:</span> <span class="n">α</span><span class="o">,</span> <span class="n">S</span> <span class="bp">=</span> <span class="o">{</span><span class="n">x</span> <span class="bp">|</span> <span class="n">a</span> <span class="err">∣</span> <span class="n">x</span><span class="o">})</span>

<span class="n">class</span> <span class="n">principal_ideal_domain</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">)</span> <span class="kn">extends</span> <span class="n">integral_domain</span> <span class="n">α</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">principal</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">(</span><span class="n">S</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">)</span> <span class="o">[</span><span class="n">is_ideal</span> <span class="n">S</span><span class="o">],</span> <span class="n">is_principal_ideal</span> <span class="n">S</span><span class="o">)</span>
</pre></div>

#### [ Kenny Lau (Oct 16 2018 at 21:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135922262):
<p>yes</p>

#### [ Mario Carneiro (Oct 16 2018 at 21:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135922273):
<p>well no</p>

#### [ Kevin Buzzard (Oct 16 2018 at 21:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135922280):
<p>That looks right to me. Is Mario asking about whether there's a function from ideals to generators though?</p>

#### [ Mario Carneiro (Oct 16 2018 at 21:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135922284):
<p>yeah</p>

#### [ Kevin Buzzard (Oct 16 2018 at 21:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135922332):
<p>A maths PID is what Kenny just quoted.</p>

#### [ Mario Carneiro (Oct 16 2018 at 21:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135922341):
<p>I guess there is no constructive proof that Z is a PID then?</p>

#### [ Kevin Buzzard (Oct 16 2018 at 21:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135922345):
<p>Of course the notion of PID was not invented by constructivists.</p>

#### [ Kenny Lau (Oct 16 2018 at 21:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135922350):
<p>nothing involving arbitrary sets can be constructive</p>

#### [ Kevin Buzzard (Oct 16 2018 at 21:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135922351):
<p>History is written by the victors</p>

#### [ Mario Carneiro (Oct 16 2018 at 21:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135922383):
<p>that's not exactly true kenny, it's possible that the ideal structure can be leveraged to give a generator</p>

#### [ Kevin Buzzard (Oct 16 2018 at 21:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135922388):
<blockquote>
<p>I guess there is no constructive proof that Z is a PID then?</p>
</blockquote>
<p>The standard proof in textbooks ("if the ideal is zero then done, if not then choose the smallest positive integer") is constructive.</p>

#### [ Mario Carneiro (Oct 16 2018 at 21:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135922440):
<p>well, constructive with LEM</p>

#### [ Kenny Lau (Oct 16 2018 at 21:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135922465):
<p>you can't decide if the ideal is zero</p>

#### [ Mario Carneiro (Oct 16 2018 at 21:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135922466):
<p>you can't determine if an arbitrary ideal is zero</p>

#### [ Kevin Buzzard (Oct 16 2018 at 21:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135922471):
<p>In Z??</p>

#### [ Mario Carneiro (Oct 16 2018 at 21:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135922475):
<p>that's exactly the problem with defining characteristic</p>

#### [ Kenny Lau (Oct 16 2018 at 21:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135922477):
<p>give me an algorithm</p>

#### [ Mario Carneiro (Oct 16 2018 at 21:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135922490):
<p>the set of periods of an element is an ideal of Z</p>

#### [ Mario Carneiro (Oct 16 2018 at 21:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135922500):
<p>but you can't tell if it is zero</p>

#### [ Kevin Buzzard (Oct 16 2018 at 21:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135922506):
<p>I'm not going to talk about this any more. It's silly.</p>

#### [ Mario Carneiro (Oct 16 2018 at 21:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135922511):
<p>I think we have our answer Kenny</p>

#### [ Kevin Buzzard (Oct 16 2018 at 21:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135922516):
<p>:-)</p>

#### [ Mario Carneiro (Oct 16 2018 at 21:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135922518):
<p>totalize it</p>

#### [ Kenny Lau (Oct 16 2018 at 21:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135922565):
<p>could you summarize the answer?</p>

#### [ Kevin Buzzard (Oct 16 2018 at 21:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135922575):
<p>Are you going to assume LEM?</p>

#### [ Mario Carneiro (Oct 16 2018 at 21:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135922576):
<p>char Q = 0</p>

#### [ Mario Carneiro (Oct 16 2018 at 21:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135922579):
<p><code>noncomputable</code></p>

#### [ Mario Carneiro (Oct 16 2018 at 21:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135922584):
<p>live with it</p>

#### [ Kenny Lau (Oct 16 2018 at 21:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135922598):
<p>no roption?</p>

#### [ Mario Carneiro (Oct 16 2018 at 21:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135922599):
<p>if you insist, you can define <code>char' A : roption nat</code></p>

#### [ Mario Carneiro (Oct 16 2018 at 21:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135922611):
<p>and define <code>char</code> in terms of it</p>

#### [ Mario Carneiro (Oct 16 2018 at 21:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135922615):
<p>but most of the theory will be about <code>char</code></p>

#### [ Kenny Lau (Oct 16 2018 at 21:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135922618):
<p>it won't be a class then</p>

#### [ Patrick Massot (Oct 16 2018 at 21:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135922620):
<p><code>kenny_char : roption Prop</code> (because who knows?)</p>

#### [ Mario Carneiro (Oct 16 2018 at 21:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135922637):
<p>also, <code>char</code> is a type</p>

#### [ Kenny Lau (Oct 16 2018 at 21:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135922640):
<p>but every ring has a unique char</p>

#### [ Mario Carneiro (Oct 16 2018 at 21:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135922649):
<p>characters</p>

#### [ Mario Carneiro (Oct 16 2018 at 21:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135922699):
<p>there is also the ideal definition, dunno how useful it is but that's constructive too</p>

#### [ Patrick Massot (Oct 16 2018 at 21:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135922704):
<p>Let's write it in French then! <code>car</code></p>

#### [ Kenny Lau (Oct 16 2018 at 21:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135922705):
<p>I mean, it's useful to make "char A = p" into a class</p>

#### [ Mario Carneiro (Oct 16 2018 at 21:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135922710):
<p>I agree on that</p>

#### [ Mario Carneiro (Oct 16 2018 at 21:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135922715):
<p><code>char_p</code> is fine and unproblematic</p>

#### [ Kenny Lau (Oct 16 2018 at 21:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135922719):
<p>oh ok</p>

#### [ Reid Barton (Oct 16 2018 at 21:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135922722):
<blockquote>
<p>but every ring has a unique char</p>
</blockquote>
<p>isn't this not true constructively? or am I really confused</p>

#### [ Mario Carneiro (Oct 16 2018 at 21:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135922744):
<p>no, that's true</p>

#### [ Kenny Lau (Oct 16 2018 at 21:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135922750):
<p>I'm talking about the reason to make it into a typeclass</p>

#### [ Mario Carneiro (Oct 16 2018 at 21:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135922760):
<p>if a ring has two characteristics then they are equal</p>

#### [ Kenny Lau (Oct 16 2018 at 21:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135922763):
<div class="codehilite"><pre><span></span><span class="n">class</span> <span class="n">char_p</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">[</span><span class="n">has_zero</span> <span class="n">α</span><span class="o">]</span> <span class="o">[</span><span class="n">has_one</span> <span class="n">α</span><span class="o">]</span> <span class="o">[</span><span class="n">has_add</span> <span class="n">α</span><span class="o">]</span> <span class="o">(</span><span class="n">p</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="kt">Prop</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">cast_eq_zero</span> <span class="o">:</span> <span class="o">(</span><span class="n">p</span><span class="o">:</span><span class="n">α</span><span class="o">)</span> <span class="bp">=</span> <span class="mi">0</span><span class="o">)</span>
</pre></div>


<p>Do we all agree that this definition is deficit?</p>

#### [ Reid Barton (Oct 16 2018 at 21:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135922770):
<p>It's the "has" part I am worried about</p>

#### [ Reid Barton (Oct 16 2018 at 21:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135922780):
<p>I agree "unique" is okay.</p>

#### [ Mario Carneiro (Oct 16 2018 at 21:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135922831):
<p>no you can't prove existence of a characteristic (number) in general without LEM</p>

#### [ Mario Carneiro (Oct 16 2018 at 21:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135922835):
<p>the ideal is fine of course</p>

#### [ Reid Barton (Oct 16 2018 at 21:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135922838):
<p>right, okay</p>

#### [ Reid Barton (Oct 16 2018 at 21:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135923259):
<blockquote>
<p>I guess there is no constructive proof that Z is a PID then?</p>
</blockquote>
<p>I think you can even prove constructively that "Z is a PID" =&gt; LEM</p>

#### [ Reid Barton (Oct 16 2018 at 21:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135923313):
<p>by taking a proposition P and defining the ideal I = {x | x = 0 \/ P}</p>

#### [ Reid Barton (Oct 16 2018 at 21:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135923331):
<p>and then looking at whether its generator is zero or not</p>

#### [ Kenny Lau (Oct 16 2018 at 21:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135923475):
<div class="codehilite"><pre><span></span><span class="n">class</span> <span class="n">char_p</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">[</span><span class="n">semiring</span> <span class="n">α</span><span class="o">]</span> <span class="o">(</span><span class="n">p</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="kt">Prop</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">cast_eq_zero_iff</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">x</span><span class="o">:</span><span class="bp">ℕ</span><span class="o">,</span> <span class="o">(</span><span class="n">x</span><span class="o">:</span><span class="n">α</span><span class="o">)</span> <span class="bp">=</span> <span class="mi">0</span> <span class="bp">↔</span> <span class="n">p</span> <span class="err">∣</span> <span class="n">x</span><span class="o">)</span>
</pre></div>

#### [ Kenny Lau (Oct 16 2018 at 21:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135923477):
<p>how about this</p>

#### [ Kenny Lau (Oct 16 2018 at 21:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135923619):
<div class="codehilite"><pre><span></span><span class="n">class</span> <span class="n">char_p</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">[</span><span class="n">semiring</span> <span class="n">α</span><span class="o">]</span> <span class="o">(</span><span class="n">p</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="kt">Prop</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">cast_eq_zero_iff</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">x</span><span class="o">:</span><span class="bp">ℕ</span><span class="o">,</span> <span class="o">(</span><span class="n">x</span><span class="o">:</span><span class="n">α</span><span class="o">)</span> <span class="bp">=</span> <span class="mi">0</span> <span class="bp">↔</span> <span class="n">p</span> <span class="err">∣</span> <span class="n">x</span><span class="o">)</span>

<span class="kn">theorem</span> <span class="n">char_p</span><span class="bp">.</span><span class="n">cast_eq_zero</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">[</span><span class="n">semiring</span> <span class="n">α</span><span class="o">]</span> <span class="o">{</span><span class="n">p</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">}</span> <span class="o">[</span><span class="n">char_p</span> <span class="n">α</span> <span class="n">p</span><span class="o">]</span> <span class="o">:</span> <span class="o">(</span><span class="n">p</span><span class="o">:</span><span class="n">α</span><span class="o">)</span> <span class="bp">=</span> <span class="mi">0</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">char_p</span><span class="bp">.</span><span class="n">cast_eq_zero_iff</span> <span class="n">α</span> <span class="n">p</span> <span class="n">p</span><span class="o">)</span><span class="bp">.</span><span class="mi">2</span> <span class="o">(</span><span class="n">dvd_refl</span> <span class="n">p</span><span class="o">)</span>

<span class="kn">theorem</span> <span class="n">char_p</span><span class="bp">.</span><span class="n">eq</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">[</span><span class="n">semiring</span> <span class="n">α</span><span class="o">]</span> <span class="o">(</span><span class="n">p</span> <span class="n">q</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">[</span><span class="n">char_p</span> <span class="n">α</span> <span class="n">p</span><span class="o">]</span> <span class="o">[</span><span class="n">char_p</span> <span class="n">α</span> <span class="n">q</span><span class="o">]</span> <span class="o">:</span> <span class="n">p</span> <span class="bp">=</span> <span class="n">q</span> <span class="o">:=</span>
<span class="n">nat</span><span class="bp">.</span><span class="n">dvd_antisymm</span>
  <span class="o">((</span><span class="n">char_p</span><span class="bp">.</span><span class="n">cast_eq_zero_iff</span> <span class="n">α</span> <span class="n">p</span> <span class="n">q</span><span class="o">)</span><span class="bp">.</span><span class="mi">1</span> <span class="n">char_p</span><span class="bp">.</span><span class="n">cast_eq_zero</span><span class="o">)</span>
  <span class="o">((</span><span class="n">char_p</span><span class="bp">.</span><span class="n">cast_eq_zero_iff</span> <span class="n">α</span> <span class="n">q</span> <span class="n">p</span><span class="o">)</span><span class="bp">.</span><span class="mi">1</span> <span class="n">char_p</span><span class="bp">.</span><span class="n">cast_eq_zero</span><span class="o">)</span>
</pre></div>

#### [ Kenny Lau (Oct 16 2018 at 21:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135923715):
<blockquote>
<p>I think your definition should be on semirings instead of zero/one/mul classes</p>
</blockquote>
<p>but <code>char_zero</code> is defined on <code>[add_monoid \a] [has_one \a]</code>?</p>

#### [ Mario Carneiro (Oct 16 2018 at 21:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135924255):
<p>or that</p>

#### [ Kenny Lau (Oct 16 2018 at 21:45)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135924367):
<p>existe uma diferencia?</p>

#### [ Kenny Lau (Oct 16 2018 at 22:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135925799):
<div class="codehilite"><pre><span></span><span class="n">class</span> <span class="n">char_p</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">[</span><span class="n">semiring</span> <span class="n">α</span><span class="o">]</span> <span class="o">(</span><span class="n">p</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="kt">Prop</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">cast_eq_zero_iff</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">x</span><span class="o">:</span><span class="bp">ℕ</span><span class="o">,</span> <span class="o">(</span><span class="n">x</span><span class="o">:</span><span class="n">α</span><span class="o">)</span> <span class="bp">=</span> <span class="mi">0</span> <span class="bp">↔</span> <span class="n">p</span> <span class="err">∣</span> <span class="n">x</span><span class="o">)</span>

<span class="kn">theorem</span> <span class="n">char_p</span><span class="bp">.</span><span class="n">cast_eq_zero</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">[</span><span class="n">semiring</span> <span class="n">α</span><span class="o">]</span> <span class="o">(</span><span class="n">p</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">[</span><span class="n">char_p</span> <span class="n">α</span> <span class="n">p</span><span class="o">]</span> <span class="o">:</span> <span class="o">(</span><span class="n">p</span><span class="o">:</span><span class="n">α</span><span class="o">)</span> <span class="bp">=</span> <span class="mi">0</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">char_p</span><span class="bp">.</span><span class="n">cast_eq_zero_iff</span> <span class="n">α</span> <span class="n">p</span> <span class="n">p</span><span class="o">)</span><span class="bp">.</span><span class="mi">2</span> <span class="o">(</span><span class="n">dvd_refl</span> <span class="n">p</span><span class="o">)</span>

<span class="kn">theorem</span> <span class="n">char_p</span><span class="bp">.</span><span class="n">eq</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">[</span><span class="n">semiring</span> <span class="n">α</span><span class="o">]</span> <span class="o">(</span><span class="n">p</span> <span class="n">q</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">[</span><span class="n">char_p</span> <span class="n">α</span> <span class="n">p</span><span class="o">]</span> <span class="o">[</span><span class="n">char_p</span> <span class="n">α</span> <span class="n">q</span><span class="o">]</span> <span class="o">:</span> <span class="n">p</span> <span class="bp">=</span> <span class="n">q</span> <span class="o">:=</span>
<span class="n">nat</span><span class="bp">.</span><span class="n">dvd_antisymm</span>
  <span class="o">((</span><span class="n">char_p</span><span class="bp">.</span><span class="n">cast_eq_zero_iff</span> <span class="n">α</span> <span class="n">p</span> <span class="n">q</span><span class="o">)</span><span class="bp">.</span><span class="mi">1</span> <span class="o">(</span><span class="n">char_p</span><span class="bp">.</span><span class="n">cast_eq_zero</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">))</span>
  <span class="o">((</span><span class="n">char_p</span><span class="bp">.</span><span class="n">cast_eq_zero_iff</span> <span class="n">α</span> <span class="n">q</span> <span class="n">p</span><span class="o">)</span><span class="bp">.</span><span class="mi">1</span> <span class="o">(</span><span class="n">char_p</span><span class="bp">.</span><span class="n">cast_eq_zero</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">))</span>

<span class="kn">instance</span> <span class="n">char_p</span><span class="bp">.</span><span class="n">of_char_zero</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">[</span><span class="n">semiring</span> <span class="n">α</span><span class="o">]</span> <span class="o">[</span><span class="n">char_zero</span> <span class="n">α</span><span class="o">]</span> <span class="o">:</span> <span class="n">char_p</span> <span class="n">α</span> <span class="mi">0</span> <span class="o">:=</span>
<span class="bp">⟨λ</span> <span class="n">x</span><span class="o">,</span> <span class="k">by</span> <span class="n">rw</span> <span class="o">[</span><span class="n">zero_dvd_iff</span><span class="o">,</span> <span class="err">←</span> <span class="n">nat</span><span class="bp">.</span><span class="n">cast_zero</span><span class="o">,</span> <span class="n">nat</span><span class="bp">.</span><span class="n">cast_inj</span><span class="o">]</span><span class="bp">⟩</span>

<span class="kn">theorem</span> <span class="n">char_p</span><span class="bp">.</span><span class="n">exists</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">[</span><span class="n">semiring</span> <span class="n">α</span><span class="o">]</span> <span class="o">:</span> <span class="bp">∃</span> <span class="n">p</span><span class="o">,</span> <span class="n">char_p</span> <span class="n">α</span> <span class="n">p</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">letI</span> <span class="o">:=</span> <span class="n">classical</span><span class="bp">.</span><span class="n">dec_eq</span> <span class="n">α</span><span class="bp">;</span> <span class="n">exact</span>
<span class="n">classical</span><span class="bp">.</span><span class="n">by_cases</span>
  <span class="o">(</span><span class="k">assume</span> <span class="n">H</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">p</span><span class="o">:</span><span class="bp">ℕ</span><span class="o">,</span> <span class="o">(</span><span class="n">p</span><span class="o">:</span><span class="n">α</span><span class="o">)</span> <span class="bp">=</span> <span class="mi">0</span> <span class="bp">→</span> <span class="n">p</span> <span class="bp">=</span> <span class="mi">0</span><span class="o">,</span> <span class="bp">⟨</span><span class="mi">0</span><span class="o">,</span>
    <span class="bp">⟨λ</span> <span class="n">x</span><span class="o">,</span> <span class="k">by</span> <span class="n">rw</span> <span class="o">[</span><span class="n">zero_dvd_iff</span><span class="o">]</span><span class="bp">;</span> <span class="n">exact</span> <span class="bp">⟨</span><span class="n">H</span> <span class="n">x</span><span class="o">,</span> <span class="k">by</span> <span class="n">rintro</span> <span class="n">rfl</span><span class="bp">;</span> <span class="n">refl</span><span class="bp">⟩⟩⟩</span><span class="o">)</span>
  <span class="o">(</span><span class="bp">λ</span> <span class="n">H</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">nat</span><span class="bp">.</span><span class="n">find</span> <span class="o">(</span><span class="n">classical</span><span class="bp">.</span><span class="n">not_forall</span><span class="bp">.</span><span class="mi">1</span> <span class="n">H</span><span class="o">),</span> <span class="bp">⟨λ</span> <span class="n">x</span><span class="o">,</span>
    <span class="bp">⟨λ</span> <span class="n">H1</span><span class="o">,</span> <span class="n">nat</span><span class="bp">.</span><span class="n">dvd_of_mod_eq_zero</span> <span class="o">(</span><span class="n">by_contradiction</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">H2</span><span class="o">,</span>
      <span class="n">nat</span><span class="bp">.</span><span class="n">find_min</span> <span class="o">(</span><span class="n">classical</span><span class="bp">.</span><span class="n">not_forall</span><span class="bp">.</span><span class="mi">1</span> <span class="n">H</span><span class="o">)</span>
        <span class="o">(</span><span class="n">nat</span><span class="bp">.</span><span class="n">mod_lt</span> <span class="n">x</span> <span class="err">$</span> <span class="n">nat</span><span class="bp">.</span><span class="n">pos_of_ne_zero</span> <span class="err">$</span> <span class="n">not_of_not_imp</span> <span class="err">$</span>
          <span class="n">nat</span><span class="bp">.</span><span class="n">find_spec</span> <span class="o">(</span><span class="n">classical</span><span class="bp">.</span><span class="n">not_forall</span><span class="bp">.</span><span class="mi">1</span> <span class="n">H</span><span class="o">))</span>
        <span class="o">(</span><span class="n">not_imp_of_and_not</span> <span class="bp">⟨</span><span class="k">by</span> <span class="n">rwa</span> <span class="o">[</span><span class="err">←</span> <span class="n">nat</span><span class="bp">.</span><span class="n">mod_add_div</span> <span class="n">x</span> <span class="o">(</span><span class="n">nat</span><span class="bp">.</span><span class="n">find</span> <span class="o">(</span><span class="n">classical</span><span class="bp">.</span><span class="n">not_forall</span><span class="bp">.</span><span class="mi">1</span> <span class="n">H</span><span class="o">)),</span>
          <span class="n">nat</span><span class="bp">.</span><span class="n">cast_add</span><span class="o">,</span> <span class="n">nat</span><span class="bp">.</span><span class="n">cast_mul</span><span class="o">,</span> <span class="n">of_not_not</span> <span class="o">(</span><span class="n">not_not_of_not_imp</span> <span class="err">$</span> <span class="n">nat</span><span class="bp">.</span><span class="n">find_spec</span> <span class="o">(</span><span class="n">classical</span><span class="bp">.</span><span class="n">not_forall</span><span class="bp">.</span><span class="mi">1</span> <span class="n">H</span><span class="o">)),</span>
          <span class="n">zero_mul</span><span class="o">,</span> <span class="n">add_zero</span><span class="o">]</span> <span class="n">at</span> <span class="n">H1</span><span class="o">,</span> <span class="n">H2</span><span class="bp">⟩</span><span class="o">)),</span>
    <span class="bp">λ</span> <span class="n">H1</span><span class="o">,</span> <span class="k">by</span> <span class="n">rw</span> <span class="o">[</span><span class="err">←</span> <span class="n">nat</span><span class="bp">.</span><span class="n">mul_div_cancel&#39;</span> <span class="n">H1</span><span class="o">,</span> <span class="n">nat</span><span class="bp">.</span><span class="n">cast_mul</span><span class="o">,</span>
      <span class="n">of_not_not</span> <span class="o">(</span><span class="n">not_not_of_not_imp</span> <span class="err">$</span> <span class="n">nat</span><span class="bp">.</span><span class="n">find_spec</span> <span class="o">(</span><span class="n">classical</span><span class="bp">.</span><span class="n">not_forall</span><span class="bp">.</span><span class="mi">1</span> <span class="n">H</span><span class="o">)),</span> <span class="n">zero_mul</span><span class="o">]</span><span class="bp">⟩⟩⟩</span><span class="o">)</span>

<span class="kn">theorem</span> <span class="n">char_p</span><span class="bp">.</span><span class="n">exists_unique</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">[</span><span class="n">semiring</span> <span class="n">α</span><span class="o">]</span> <span class="o">:</span> <span class="bp">∃!</span> <span class="n">p</span><span class="o">,</span> <span class="n">char_p</span> <span class="n">α</span> <span class="n">p</span> <span class="o">:=</span>
<span class="k">let</span> <span class="bp">⟨</span><span class="n">c</span><span class="o">,</span> <span class="n">H</span><span class="bp">⟩</span> <span class="o">:=</span> <span class="n">char_p</span><span class="bp">.</span><span class="n">exists</span> <span class="n">α</span> <span class="k">in</span>
<span class="bp">⟨</span><span class="n">c</span><span class="o">,</span> <span class="n">H</span><span class="o">,</span> <span class="bp">λ</span> <span class="n">y</span> <span class="n">H2</span><span class="o">,</span> <span class="k">by</span> <span class="n">resetI</span><span class="bp">;</span> <span class="n">apply</span> <span class="n">char_p</span><span class="bp">.</span><span class="n">eq</span> <span class="n">α</span><span class="bp">⟩</span>
</pre></div>

#### [ Kenny Lau (Oct 16 2018 at 22:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135925803):
<p>How does this look? <span class="user-mention" data-user-id="110049">@Mario Carneiro</span> <span class="user-mention" data-user-id="110031">@Patrick Massot</span></p>

#### [ Kenny Lau (Oct 16 2018 at 22:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135925816):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span></p>

#### [ Kevin Buzzard (Oct 16 2018 at 22:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135925950):
<blockquote>
<div class="codehilite"><pre><span></span><span class="n">class</span> <span class="n">char_p</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">[</span><span class="n">semiring</span> <span class="n">α</span><span class="o">]</span> <span class="o">(</span><span class="n">p</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="kt">Prop</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">cast_eq_zero_iff</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">x</span><span class="o">:</span><span class="bp">ℕ</span><span class="o">,</span> <span class="o">(</span><span class="n">x</span><span class="o">:</span><span class="n">α</span><span class="o">)</span> <span class="bp">=</span> <span class="mi">0</span> <span class="bp">↔</span> <span class="n">p</span> <span class="err">∣</span> <span class="n">x</span><span class="o">)</span>
</pre></div>


</blockquote>
<p>I see you went for the ideal idea after all ;-)</p>

#### [ Mario Carneiro (Oct 16 2018 at 22:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135925962):
<p><code>char_p.eq</code> should definitely not have square brackets</p>

#### [ Kevin Buzzard (Oct 16 2018 at 22:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135925979):
<p><code>is_char_p</code>?</p>

#### [ Mario Carneiro (Oct 16 2018 at 22:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135926065):
<p>Maybe it should be a property of Z, then you can literally say <code>is_ideal (char_p A)</code></p>

#### [ Kenny Lau (Oct 16 2018 at 22:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135926427):
<p>wait I'm confused</p>

#### [ Kenny Lau (Oct 16 2018 at 22:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135926429):
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">char_p</span><span class="bp">.</span><span class="n">eq</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">[</span><span class="n">semiring</span> <span class="n">α</span><span class="o">]</span> <span class="o">(</span><span class="n">p</span> <span class="n">q</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">c1</span> <span class="o">:</span> <span class="n">char_p</span> <span class="n">α</span> <span class="n">p</span><span class="o">)</span> <span class="o">(</span><span class="n">c2</span> <span class="o">:</span> <span class="n">char_p</span> <span class="n">α</span> <span class="n">q</span><span class="o">)</span> <span class="o">:</span> <span class="n">p</span> <span class="bp">=</span> <span class="n">q</span> <span class="o">:=</span>
<span class="n">nat</span><span class="bp">.</span><span class="n">dvd_antisymm</span>
  <span class="o">((</span><span class="n">char_p</span><span class="bp">.</span><span class="n">cast_eq_zero_iff</span> <span class="n">α</span> <span class="n">p</span> <span class="n">q</span><span class="o">)</span><span class="bp">.</span><span class="mi">1</span> <span class="o">(</span><span class="n">char_p</span><span class="bp">.</span><span class="n">cast_eq_zero</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">))</span>
  <span class="o">((</span><span class="n">char_p</span><span class="bp">.</span><span class="n">cast_eq_zero_iff</span> <span class="n">α</span> <span class="n">q</span> <span class="n">p</span><span class="o">)</span><span class="bp">.</span><span class="mi">1</span> <span class="o">(</span><span class="n">char_p</span><span class="bp">.</span><span class="n">cast_eq_zero</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">))</span>
</pre></div>

#### [ Kenny Lau (Oct 16 2018 at 22:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135926434):
<p>how can the proof still work now that I turned <code>[]</code> to <code>()</code>?</p>

#### [ Mario Carneiro (Oct 16 2018 at 22:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135926462):
<p>maybe kevin knows... I told him the solution to this puzzle a few weeks ago</p>

#### [ Kenny Lau (Oct 16 2018 at 22:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135926477):
<p>anyway how is this now?</p>
<div class="codehilite"><pre><span></span><span class="n">class</span> <span class="n">char_p</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">[</span><span class="n">semiring</span> <span class="n">α</span><span class="o">]</span> <span class="o">(</span><span class="n">p</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">:</span> <span class="kt">Prop</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">cast_eq_zero_iff</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">x</span><span class="o">:</span><span class="bp">ℕ</span><span class="o">,</span> <span class="o">(</span><span class="n">x</span><span class="o">:</span><span class="n">α</span><span class="o">)</span> <span class="bp">=</span> <span class="mi">0</span> <span class="bp">↔</span> <span class="n">p</span> <span class="err">∣</span> <span class="n">x</span><span class="o">)</span>

<span class="kn">theorem</span> <span class="n">char_p</span><span class="bp">.</span><span class="n">cast_eq_zero</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">[</span><span class="n">semiring</span> <span class="n">α</span><span class="o">]</span> <span class="o">(</span><span class="n">p</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">[</span><span class="n">char_p</span> <span class="n">α</span> <span class="n">p</span><span class="o">]</span> <span class="o">:</span> <span class="o">(</span><span class="n">p</span><span class="o">:</span><span class="n">α</span><span class="o">)</span> <span class="bp">=</span> <span class="mi">0</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">char_p</span><span class="bp">.</span><span class="n">cast_eq_zero_iff</span> <span class="n">α</span> <span class="n">p</span> <span class="n">p</span><span class="o">)</span><span class="bp">.</span><span class="mi">2</span> <span class="o">(</span><span class="n">dvd_refl</span> <span class="n">p</span><span class="o">)</span>

<span class="kn">theorem</span> <span class="n">char_p</span><span class="bp">.</span><span class="n">eq</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">[</span><span class="n">semiring</span> <span class="n">α</span><span class="o">]</span> <span class="o">{</span><span class="n">p</span> <span class="n">q</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">}</span> <span class="o">(</span><span class="n">c1</span> <span class="o">:</span> <span class="n">char_p</span> <span class="n">α</span> <span class="n">p</span><span class="o">)</span> <span class="o">(</span><span class="n">c2</span> <span class="o">:</span> <span class="n">char_p</span> <span class="n">α</span> <span class="n">q</span><span class="o">)</span> <span class="o">:</span> <span class="n">p</span> <span class="bp">=</span> <span class="n">q</span> <span class="o">:=</span>
<span class="n">nat</span><span class="bp">.</span><span class="n">dvd_antisymm</span>
  <span class="o">((</span><span class="n">char_p</span><span class="bp">.</span><span class="n">cast_eq_zero_iff</span> <span class="n">α</span> <span class="n">p</span> <span class="n">q</span><span class="o">)</span><span class="bp">.</span><span class="mi">1</span> <span class="o">(</span><span class="n">char_p</span><span class="bp">.</span><span class="n">cast_eq_zero</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">))</span>
  <span class="o">((</span><span class="n">char_p</span><span class="bp">.</span><span class="n">cast_eq_zero_iff</span> <span class="n">α</span> <span class="n">q</span> <span class="n">p</span><span class="o">)</span><span class="bp">.</span><span class="mi">1</span> <span class="o">(</span><span class="n">char_p</span><span class="bp">.</span><span class="n">cast_eq_zero</span> <span class="bp">_</span> <span class="bp">_</span><span class="o">))</span>

<span class="kn">instance</span> <span class="n">char_p</span><span class="bp">.</span><span class="n">of_char_zero</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">[</span><span class="n">semiring</span> <span class="n">α</span><span class="o">]</span> <span class="o">[</span><span class="n">char_zero</span> <span class="n">α</span><span class="o">]</span> <span class="o">:</span> <span class="n">char_p</span> <span class="n">α</span> <span class="mi">0</span> <span class="o">:=</span>
<span class="bp">⟨λ</span> <span class="n">x</span><span class="o">,</span> <span class="k">by</span> <span class="n">rw</span> <span class="o">[</span><span class="n">zero_dvd_iff</span><span class="o">,</span> <span class="err">←</span> <span class="n">nat</span><span class="bp">.</span><span class="n">cast_zero</span><span class="o">,</span> <span class="n">nat</span><span class="bp">.</span><span class="n">cast_inj</span><span class="o">]</span><span class="bp">⟩</span>

<span class="kn">theorem</span> <span class="n">char_p</span><span class="bp">.</span><span class="n">exists</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">[</span><span class="n">semiring</span> <span class="n">α</span><span class="o">]</span> <span class="o">:</span> <span class="bp">∃</span> <span class="n">p</span><span class="o">,</span> <span class="n">char_p</span> <span class="n">α</span> <span class="n">p</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">letI</span> <span class="o">:=</span> <span class="n">classical</span><span class="bp">.</span><span class="n">dec_eq</span> <span class="n">α</span><span class="bp">;</span> <span class="n">exact</span>
<span class="n">classical</span><span class="bp">.</span><span class="n">by_cases</span>
  <span class="o">(</span><span class="k">assume</span> <span class="n">H</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">p</span><span class="o">:</span><span class="bp">ℕ</span><span class="o">,</span> <span class="o">(</span><span class="n">p</span><span class="o">:</span><span class="n">α</span><span class="o">)</span> <span class="bp">=</span> <span class="mi">0</span> <span class="bp">→</span> <span class="n">p</span> <span class="bp">=</span> <span class="mi">0</span><span class="o">,</span> <span class="bp">⟨</span><span class="mi">0</span><span class="o">,</span>
    <span class="bp">⟨λ</span> <span class="n">x</span><span class="o">,</span> <span class="k">by</span> <span class="n">rw</span> <span class="o">[</span><span class="n">zero_dvd_iff</span><span class="o">]</span><span class="bp">;</span> <span class="n">exact</span> <span class="bp">⟨</span><span class="n">H</span> <span class="n">x</span><span class="o">,</span> <span class="k">by</span> <span class="n">rintro</span> <span class="n">rfl</span><span class="bp">;</span> <span class="n">refl</span><span class="bp">⟩⟩⟩</span><span class="o">)</span>
  <span class="o">(</span><span class="bp">λ</span> <span class="n">H</span><span class="o">,</span> <span class="bp">⟨</span><span class="n">nat</span><span class="bp">.</span><span class="n">find</span> <span class="o">(</span><span class="n">classical</span><span class="bp">.</span><span class="n">not_forall</span><span class="bp">.</span><span class="mi">1</span> <span class="n">H</span><span class="o">),</span> <span class="bp">⟨λ</span> <span class="n">x</span><span class="o">,</span>
    <span class="bp">⟨λ</span> <span class="n">H1</span><span class="o">,</span> <span class="n">nat</span><span class="bp">.</span><span class="n">dvd_of_mod_eq_zero</span> <span class="o">(</span><span class="n">by_contradiction</span> <span class="err">$</span> <span class="bp">λ</span> <span class="n">H2</span><span class="o">,</span>
      <span class="n">nat</span><span class="bp">.</span><span class="n">find_min</span> <span class="o">(</span><span class="n">classical</span><span class="bp">.</span><span class="n">not_forall</span><span class="bp">.</span><span class="mi">1</span> <span class="n">H</span><span class="o">)</span>
        <span class="o">(</span><span class="n">nat</span><span class="bp">.</span><span class="n">mod_lt</span> <span class="n">x</span> <span class="err">$</span> <span class="n">nat</span><span class="bp">.</span><span class="n">pos_of_ne_zero</span> <span class="err">$</span> <span class="n">not_of_not_imp</span> <span class="err">$</span>
          <span class="n">nat</span><span class="bp">.</span><span class="n">find_spec</span> <span class="o">(</span><span class="n">classical</span><span class="bp">.</span><span class="n">not_forall</span><span class="bp">.</span><span class="mi">1</span> <span class="n">H</span><span class="o">))</span>
        <span class="o">(</span><span class="n">not_imp_of_and_not</span> <span class="bp">⟨</span><span class="k">by</span> <span class="n">rwa</span> <span class="o">[</span><span class="err">←</span> <span class="n">nat</span><span class="bp">.</span><span class="n">mod_add_div</span> <span class="n">x</span> <span class="o">(</span><span class="n">nat</span><span class="bp">.</span><span class="n">find</span> <span class="o">(</span><span class="n">classical</span><span class="bp">.</span><span class="n">not_forall</span><span class="bp">.</span><span class="mi">1</span> <span class="n">H</span><span class="o">)),</span>
          <span class="n">nat</span><span class="bp">.</span><span class="n">cast_add</span><span class="o">,</span> <span class="n">nat</span><span class="bp">.</span><span class="n">cast_mul</span><span class="o">,</span> <span class="n">of_not_not</span> <span class="o">(</span><span class="n">not_not_of_not_imp</span> <span class="err">$</span> <span class="n">nat</span><span class="bp">.</span><span class="n">find_spec</span> <span class="o">(</span><span class="n">classical</span><span class="bp">.</span><span class="n">not_forall</span><span class="bp">.</span><span class="mi">1</span> <span class="n">H</span><span class="o">)),</span>
          <span class="n">zero_mul</span><span class="o">,</span> <span class="n">add_zero</span><span class="o">]</span> <span class="n">at</span> <span class="n">H1</span><span class="o">,</span> <span class="n">H2</span><span class="bp">⟩</span><span class="o">)),</span>
    <span class="bp">λ</span> <span class="n">H1</span><span class="o">,</span> <span class="k">by</span> <span class="n">rw</span> <span class="o">[</span><span class="err">←</span> <span class="n">nat</span><span class="bp">.</span><span class="n">mul_div_cancel&#39;</span> <span class="n">H1</span><span class="o">,</span> <span class="n">nat</span><span class="bp">.</span><span class="n">cast_mul</span><span class="o">,</span>
      <span class="n">of_not_not</span> <span class="o">(</span><span class="n">not_not_of_not_imp</span> <span class="err">$</span> <span class="n">nat</span><span class="bp">.</span><span class="n">find_spec</span> <span class="o">(</span><span class="n">classical</span><span class="bp">.</span><span class="n">not_forall</span><span class="bp">.</span><span class="mi">1</span> <span class="n">H</span><span class="o">)),</span> <span class="n">zero_mul</span><span class="o">]</span><span class="bp">⟩⟩⟩</span><span class="o">)</span>

<span class="kn">theorem</span> <span class="n">char_p</span><span class="bp">.</span><span class="n">exists_unique</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">[</span><span class="n">semiring</span> <span class="n">α</span><span class="o">]</span> <span class="o">:</span> <span class="bp">∃!</span> <span class="n">p</span><span class="o">,</span> <span class="n">char_p</span> <span class="n">α</span> <span class="n">p</span> <span class="o">:=</span>
<span class="k">let</span> <span class="bp">⟨</span><span class="n">c</span><span class="o">,</span> <span class="n">H</span><span class="bp">⟩</span> <span class="o">:=</span> <span class="n">char_p</span><span class="bp">.</span><span class="n">exists</span> <span class="n">α</span> <span class="k">in</span>
<span class="bp">⟨</span><span class="n">c</span><span class="o">,</span> <span class="n">H</span><span class="o">,</span> <span class="bp">λ</span> <span class="n">y</span> <span class="n">H2</span><span class="o">,</span> <span class="n">char_p</span><span class="bp">.</span><span class="n">eq</span> <span class="n">α</span> <span class="n">H2</span> <span class="n">H</span><span class="bp">⟩</span>
</pre></div>

#### [ Mario Carneiro (Oct 16 2018 at 22:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135926549):
<p><code>char_p.exists</code> should be defining a function... called <code>char</code></p>

#### [ Kenny Lau (Oct 16 2018 at 22:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135926554):
<p>we can functionize that</p>

#### [ Kevin Buzzard (Oct 16 2018 at 22:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135926587):
<p>He told Johannes too.</p>

#### [ Kenny Lau (Oct 16 2018 at 22:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135926599):
<div class="codehilite"><pre><span></span>invalid definition, a declaration named &#39;char&#39; has already been declared
</pre></div>

#### [ Kenny Lau (Oct 16 2018 at 22:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135926600):
<p>hard luck</p>

#### [ Kenny Lau (Oct 16 2018 at 22:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135926906):
<div class="codehilite"><pre><span></span><span class="n">noncomputable</span> <span class="n">def</span> <span class="n">ring_char</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">[</span><span class="n">semiring</span> <span class="n">α</span><span class="o">]</span> <span class="o">:</span> <span class="bp">ℕ</span> <span class="o">:=</span>
<span class="n">classical</span><span class="bp">.</span><span class="n">some</span> <span class="o">(</span><span class="n">char_p</span><span class="bp">.</span><span class="n">exists_unique</span> <span class="n">α</span><span class="o">)</span>

<span class="kn">theorem</span> <span class="n">ring_char</span><span class="bp">.</span><span class="n">spec</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">[</span><span class="n">semiring</span> <span class="n">α</span><span class="o">]</span> <span class="o">:</span> <span class="bp">∀</span> <span class="n">x</span><span class="o">:</span><span class="bp">ℕ</span><span class="o">,</span> <span class="o">(</span><span class="n">x</span><span class="o">:</span><span class="n">α</span><span class="o">)</span> <span class="bp">=</span> <span class="mi">0</span> <span class="bp">↔</span> <span class="n">ring_char</span> <span class="n">α</span> <span class="err">∣</span> <span class="n">x</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">letI</span> <span class="o">:=</span> <span class="o">(</span><span class="n">classical</span><span class="bp">.</span><span class="n">some_spec</span> <span class="o">(</span><span class="n">char_p</span><span class="bp">.</span><span class="n">exists_unique</span> <span class="n">α</span><span class="o">))</span><span class="bp">.</span><span class="mi">1</span><span class="bp">;</span>
<span class="n">unfold</span> <span class="n">ring_char</span><span class="bp">;</span> <span class="n">exact</span> <span class="n">char_p</span><span class="bp">.</span><span class="n">cast_eq_zero_iff</span> <span class="n">α</span> <span class="o">(</span><span class="n">ring_char</span> <span class="n">α</span><span class="o">)</span>

<span class="kn">theorem</span> <span class="n">ring_char</span><span class="bp">.</span><span class="n">eq</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">[</span><span class="n">semiring</span> <span class="n">α</span><span class="o">]</span> <span class="o">{</span><span class="n">p</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">}</span> <span class="o">(</span><span class="n">C</span> <span class="o">:</span> <span class="n">char_p</span> <span class="n">α</span> <span class="n">p</span><span class="o">)</span> <span class="o">:</span> <span class="n">p</span> <span class="bp">=</span> <span class="n">ring_char</span> <span class="n">α</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">classical</span><span class="bp">.</span><span class="n">some_spec</span> <span class="o">(</span><span class="n">char_p</span><span class="bp">.</span><span class="n">exists_unique</span> <span class="n">α</span><span class="o">))</span><span class="bp">.</span><span class="mi">2</span> <span class="n">p</span> <span class="n">C</span>
</pre></div>

#### [ Kenny Lau (Oct 16 2018 at 22:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135926909):
<p>how is this?</p>

#### [ Kevin Buzzard (Oct 16 2018 at 22:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135927432):
<blockquote>
<p>how can the proof still work now that I turned <code>[]</code> to <code>()</code>?</p>
</blockquote>
<p>Type class inference just grabs anything it can find to the left of the colon. The round and square brackets are just for the signature of the theorem, they don't affect how type class inference works in the proof. This is not so well-known because it's not common to put a typeclass left of the colon and not in a square bracket.</p>

#### [ Kevin Buzzard (Oct 16 2018 at 22:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135927447):
<p>I discovered it a few weeks ago when I was trying to understand Patrick's type class hell with his completions and had exactly the same reaction.</p>

#### [ Kevin Buzzard (Oct 16 2018 at 22:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135927490):
<p>I've had to construct that argument from memory because my search for the conversation failed. Hopefully it's some sort of approximation to the truth.</p>

#### [ Bryan Gin-ge Chen (Oct 16 2018 at 22:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135927856):
<p>I guess it's <a href="#narrow/stream/116395-maths/subject/Separation.20stuff/near/134261338" title="#narrow/stream/116395-maths/subject/Separation.20stuff/near/134261338">this conversation?</a> I found it by searching for "left of colon".</p>

#### [ Kenny Lau (Oct 16 2018 at 22:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135927950):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> Could you help me with some typeclass problems? It's in L324 here: <a href="https://github.com/kckennylau/Lean/blob/master/perfect_closure.lean#L324" target="_blank" title="https://github.com/kckennylau/Lean/blob/master/perfect_closure.lean#L324">https://github.com/kckennylau/Lean/blob/master/perfect_closure.lean#L324</a></p>

#### [ Kenny Lau (Oct 16 2018 at 22:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135927966):
<p>Lean can't figure out the coercion in <code>(↑x : perfect_closure α p)</code></p>

#### [ Kevin Buzzard (Oct 16 2018 at 22:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135928018):
<p><a href="#narrow/stream/116395-maths/subject/Separation.20stuff/near/134261591" title="#narrow/stream/116395-maths/subject/Separation.20stuff/near/134261591">https://leanprover.zulipchat.com/#narrow/stream/116395-maths/subject/Separation.20stuff/near/134261591</a></p>

#### [ Kevin Buzzard (Oct 16 2018 at 22:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135928021):
<p>You owe Mario a light bulb</p>

#### [ Kenny Lau (Oct 16 2018 at 22:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135928069):
<p>done</p>

#### [ Kevin Buzzard (Oct 16 2018 at 22:44)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135928099):
<p>(thanks Bryan)</p>

#### [ Kenny Lau (Oct 16 2018 at 22:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/characteristic%20of%20fields/near/135928788):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> never mind it's stupid</p>


{% endraw %}
