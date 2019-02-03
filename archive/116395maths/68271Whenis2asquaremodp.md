---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/68271Whenis2asquaremodp.html
---

## Stream: [maths](https://leanprover-community.github.io/archive/116395maths/index.html)
### Topic: [When is -2 a square mod p?](https://leanprover-community.github.io/archive/116395maths/68271Whenis2asquaremodp.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kevin Buzzard (Apr 28 2018 at 00:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/When%20is%20-2%20a%20square%20mod%20p%3F/near/125797166):
<p>Is there a proof in Lean that if <code>p</code> is a prime congruent to <code>5</code> or <code>7</code> mod <code>8</code> then <code>-2</code> is not a square mod p?</p>

#### [ Kevin Buzzard (Apr 28 2018 at 00:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/When%20is%20-2%20a%20square%20mod%20p%3F/near/125797169):
<p>This result drops out rather nicely from the Gauss' lemma approach</p>

#### [ Kevin Buzzard (Apr 28 2018 at 00:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/When%20is%20-2%20a%20square%20mod%20p%3F/near/125797173):
<p>One counts the number of multiples of -2, mod p, which are negative</p>

#### [ Kevin Buzzard (Apr 28 2018 at 00:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/When%20is%20-2%20a%20square%20mod%20p%3F/near/125797178):
<p>and it's rather easy to do</p>

#### [ Kevin Buzzard (Apr 28 2018 at 00:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/When%20is%20-2%20a%20square%20mod%20p%3F/near/125797183):
<p>That's the simplest proof I know.</p>

#### [ Kevin Buzzard (Apr 28 2018 at 00:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/When%20is%20-2%20a%20square%20mod%20p%3F/near/125797188):
<p>I don't know of an elementary trick (in contrast to -1 and -3 which can be done by hand using roots of unity)</p>

#### [ Kevin Buzzard (Apr 28 2018 at 01:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/When%20is%20-2%20a%20square%20mod%20p%3F/near/125797241):
<p><a href="https://en.wikipedia.org/wiki/Gauss%27s_lemma_(number_theory)" target="_blank" title="https://en.wikipedia.org/wiki/Gauss%27s_lemma_(number_theory)">https://en.wikipedia.org/wiki/Gauss%27s_lemma_(number_theory)</a></p>

#### [ Kevin Buzzard (Apr 28 2018 at 01:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/When%20is%20-2%20a%20square%20mod%20p%3F/near/125797248):
<p>Uses Euler's criterion</p>

#### [ Kevin Buzzard (Apr 28 2018 at 01:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/When%20is%20-2%20a%20square%20mod%20p%3F/near/125797261):
<p>which uses that the Sylow 2-subgroup of <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mo>(</mo><mi>Z</mi><mi mathvariant="normal">/</mi><mi>p</mi><mi>Z</mi><msup><mo>)</mo><mo>∗</mo></msup></mrow><annotation encoding="application/x-tex">(Z/pZ)^*</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mopen">(</span><span class="mord mathit" style="margin-right:0.07153em;">Z</span><span class="mord mathrm">/</span><span class="mord mathit">p</span><span class="mord mathit" style="margin-right:0.07153em;">Z</span><span class="mclose"><span class="mclose">)</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.688696em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mbin mtight">∗</span></span></span></span></span></span></span></span></span></span></span> is cyclic</p>

#### [ Kevin Buzzard (Apr 28 2018 at 01:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/When%20is%20-2%20a%20square%20mod%20p%3F/near/125797266):
<p>which follows from <code>x^2-1=(x+1)(x-1)</code></p>

#### [ Kevin Buzzard (Apr 28 2018 at 01:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/When%20is%20-2%20a%20square%20mod%20p%3F/near/125797325):
<p>Assuming Gauss' lemma, then you look at the sequence <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mo>−</mo><mn>2</mn><mo separator="true">,</mo><mo>−</mo><mn>4</mn><mo separator="true">,</mo><mo>−</mo><mn>6</mn><mo separator="true">,</mo><mi mathvariant="normal">.</mi><mi mathvariant="normal">.</mi><mi mathvariant="normal">.</mi><mo>−</mo><mo>(</mo><mi>p</mi><mo>−</mo><mn>1</mn><mo>)</mo></mrow><annotation encoding="application/x-tex">-2,-4,-6,...-(p-1)</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mord">−</span><span class="mord mathrm">2</span><span class="mpunct">,</span><span class="mord">−</span><span class="mord mathrm">4</span><span class="mpunct">,</span><span class="mord">−</span><span class="mord mathrm">6</span><span class="mpunct">,</span><span class="mord mathrm">.</span><span class="mord mathrm">.</span><span class="mord mathrm">.</span><span class="mbin">−</span><span class="mopen">(</span><span class="mord mathit">p</span><span class="mbin">−</span><span class="mord mathrm">1</span><span class="mclose">)</span></span></span></span></p>

#### [ Kevin Buzzard (Apr 28 2018 at 01:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/When%20is%20-2%20a%20square%20mod%20p%3F/near/125797340):
<p>and mod <code>p</code> this set is the same as <code>1,3,5,...,p-2</code> (reverse the order)</p>

#### [ Kevin Buzzard (Apr 28 2018 at 01:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/When%20is%20-2%20a%20square%20mod%20p%3F/near/125797346):
<p>and Gauss' Lemma says that the number of elements of this sequence which are <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mo>&gt;</mo><mi>p</mi><mi mathvariant="normal">/</mi><mn>2</mn></mrow><annotation encoding="application/x-tex">&gt;p/2</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mrel">&gt;</span><span class="mord mathit">p</span><span class="mord mathrm">/</span><span class="mord mathrm">2</span></span></span></span></p>

#### [ Kevin Buzzard (Apr 28 2018 at 01:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/When%20is%20-2%20a%20square%20mod%20p%3F/near/125797390):
<p>is <code>odd</code> if <code>-2</code> is a non-square and even otherwise</p>

#### [ Kenny Lau (Apr 28 2018 at 05:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/When%20is%20-2%20a%20square%20mod%20p%3F/near/125805619):
<p><a href="/user_uploads/3121/ek7lPaRVtdjGMhhBY2BebHzC/2018-04-28.png" target="_blank" title="2018-04-28.png">2018-04-28.png</a></p>
<div class="message_inline_image"><a href="/user_uploads/3121/ek7lPaRVtdjGMhhBY2BebHzC/2018-04-28.png" target="_blank" title="2018-04-28.png"><img src="/user_uploads/3121/ek7lPaRVtdjGMhhBY2BebHzC/2018-04-28.png"></a></div>

#### [ Kenny Lau (Apr 28 2018 at 05:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/When%20is%20-2%20a%20square%20mod%20p%3F/near/125805622):
<p>From the lecture notes of number theory (M345P14)</p>

#### [ Kenny Lau (Apr 28 2018 at 05:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/When%20is%20-2%20a%20square%20mod%20p%3F/near/125805623):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span></p>

#### [ Kevin Buzzard (Apr 28 2018 at 05:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/When%20is%20-2%20a%20square%20mod%20p%3F/near/125805634):
<p>That's 2</p>

#### [ Kevin Buzzard (Apr 28 2018 at 05:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/When%20is%20-2%20a%20square%20mod%20p%3F/near/125805635):
<p>we need -2</p>

#### [ Kenny Lau (Apr 28 2018 at 05:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/When%20is%20-2%20a%20square%20mod%20p%3F/near/125805636):
<p>oh well</p>

#### [ Kenny Lau (Apr 28 2018 at 05:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/When%20is%20-2%20a%20square%20mod%20p%3F/near/125805638):
<p>the symbol is multiplicative :P</p>

#### [ Kenny Lau (Apr 28 2018 at 05:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/When%20is%20-2%20a%20square%20mod%20p%3F/near/125805686):
<p>proof by euler criterion, I hope</p>

#### [ Kevin Buzzard (Apr 28 2018 at 05:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/When%20is%20-2%20a%20square%20mod%20p%3F/near/125805688):
<p>that's slightly deeper than you want</p>

#### [ Kevin Buzzard (Apr 28 2018 at 05:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/When%20is%20-2%20a%20square%20mod%20p%3F/near/125805689):
<p>yes</p>

#### [ Kenny Lau (Apr 28 2018 at 05:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/When%20is%20-2%20a%20square%20mod%20p%3F/near/125805692):
<p>which is elementary enough?</p>

#### [ Kevin Buzzard (Apr 28 2018 at 05:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/When%20is%20-2%20a%20square%20mod%20p%3F/near/125805693):
<p>You can generalise the link you sent me to deal with the -2 case</p>

#### [ Kenny Lau (Apr 28 2018 at 05:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/When%20is%20-2%20a%20square%20mod%20p%3F/near/125805694):
<p>I see</p>

#### [ Kevin Buzzard (Apr 28 2018 at 05:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/When%20is%20-2%20a%20square%20mod%20p%3F/near/125805695):
<p>and in fact the -2 case comes out slightly nicer than the +2 case</p>

#### [ Kenny Lau (Apr 28 2018 at 05:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/When%20is%20-2%20a%20square%20mod%20p%3F/near/125805703):
<p>so we consider (-2)^q q! instead?</p>

#### [ Kenny Lau (Apr 28 2018 at 05:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/When%20is%20-2%20a%20square%20mod%20p%3F/near/125805705):
<p>and then after rearranging it turns out to be q!?</p>

#### [ Kevin Buzzard (Apr 28 2018 at 05:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/When%20is%20-2%20a%20square%20mod%20p%3F/near/125805857):
<p>I can't guess what you mean</p>

#### [ Kevin Buzzard (Apr 28 2018 at 05:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/When%20is%20-2%20a%20square%20mod%20p%3F/near/125805863):
<p>There's something called Gauss' Lemma</p>

#### [ Kevin Buzzard (Apr 28 2018 at 05:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/When%20is%20-2%20a%20square%20mod%20p%3F/near/125805864):
<p>and it follows from that</p>

#### [ Kenny Lau (Apr 28 2018 at 05:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/When%20is%20-2%20a%20square%20mod%20p%3F/near/125805865):
<p>I think we should prove quadratic reciprocity :P</p>

#### [ Kevin Buzzard (Apr 28 2018 at 05:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/When%20is%20-2%20a%20square%20mod%20p%3F/near/125805905):
<p>that would be call</p>

#### [ Kevin Buzzard (Apr 28 2018 at 05:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/When%20is%20-2%20a%20square%20mod%20p%3F/near/125805906):
<p>cool</p>

#### [ Kevin Buzzard (Apr 28 2018 at 05:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/When%20is%20-2%20a%20square%20mod%20p%3F/near/125805908):
<p>See if Mario already did it</p>

#### [ Kenny Lau (Apr 28 2018 at 05:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/When%20is%20-2%20a%20square%20mod%20p%3F/near/125805909):
<p>I don't think it's done</p>

#### [ Kenny Lau (Apr 28 2018 at 06:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/When%20is%20-2%20a%20square%20mod%20p%3F/near/125805968):
<p>I reckon I'll need 1000 lines to do it lol</p>

#### [ Kevin Buzzard (Apr 28 2018 at 06:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/When%20is%20-2%20a%20square%20mod%20p%3F/near/125805973):
<p>Do it after exams and write your M1R project on it</p>

#### [ Kenny Lau (Apr 28 2018 at 06:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/When%20is%20-2%20a%20square%20mod%20p%3F/near/125805976):
<p>heh...</p>

#### [ Kenny Lau (Apr 28 2018 at 06:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/When%20is%20-2%20a%20square%20mod%20p%3F/near/125805987):
<p>are you sure I should use QR as project... seems quite well known</p>

#### [ Kevin Buzzard (Apr 28 2018 at 06:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/When%20is%20-2%20a%20square%20mod%20p%3F/near/125806517):
<p>It would not be the first time that a 1st year undergraduate had done a project on something which some of the professors think is "quite well-known".</p>

#### [ Kevin Buzzard (Apr 28 2018 at 06:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/When%20is%20-2%20a%20square%20mod%20p%3F/near/125806521):
<p>On the other hand if you want to be top</p>

#### [ Kevin Buzzard (Apr 28 2018 at 06:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/When%20is%20-2%20a%20square%20mod%20p%3F/near/125806524):
<p>then you have to do something hard and do it well</p>

#### [ Kevin Buzzard (Apr 28 2018 at 06:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/When%20is%20-2%20a%20square%20mod%20p%3F/near/125806525):
<p>You could do affine schemes</p>

#### [ Kevin Buzzard (Apr 28 2018 at 06:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/When%20is%20-2%20a%20square%20mod%20p%3F/near/125806527):
<p>That would be impressive</p>

#### [ Kenny Lau (Apr 28 2018 at 06:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/When%20is%20-2%20a%20square%20mod%20p%3F/near/125806528):
<p>lol</p>


{% endraw %}
