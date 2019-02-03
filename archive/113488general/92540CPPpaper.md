---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/92540CPPpaper.html
---

## Stream: [general](index.html)
### Topic: [CPP paper](92540CPPpaper.html)

---


{% raw %}
#### [ Rob Lewis (Oct 16 2018 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP%20paper/near/135887180):
<p>I'm submitting a paper about the p-adics and Hensel's lemma to CPP. If anyone is interested in taking a look, the paper is here: <a href="http://robertylewis.com/padics/padics.pdf" target="_blank" title="http://robertylewis.com/padics/padics.pdf">http://robertylewis.com/padics/padics.pdf</a> I'm happy to hear any comments before or after the submission deadline on Thursday!</p>

#### [ Rob Lewis (Oct 16 2018 at 10:56)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP%20paper/near/135887286):
<p>By the way, CPP (<a href="https://popl19.sigplan.org/track/CPP-2019" target="_blank" title="https://popl19.sigplan.org/track/CPP-2019">https://popl19.sigplan.org/track/CPP-2019#</a>) is one of the main venues for publishing about formalizations. ITP (<a href="http://itp19.cecs.pdx.edu/" target="_blank" title="http://itp19.cecs.pdx.edu/">http://itp19.cecs.pdx.edu/</a>) is another.</p>

#### [ Kevin Buzzard (Oct 16 2018 at 11:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP%20paper/near/135887709):
<p>I am really interested in this idea and in the CS culture in general. Mathematicially you have done something which is 100 years old so the new ideas are not there. In computer science I would <em>imagine</em> that you are not the first person to formalise Hensel's Lemma. Am I wrong about this? And even if someone else had done it in Mizar in 2009 or whatever -- would this matter? I am trying to work out which notions of "value" a potential referee would attach to a paper such as this.</p>

#### [ Kevin Buzzard (Oct 16 2018 at 11:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP%20paper/near/135887744):
<p>Obviously I ask because if I get the schemes repo and/or the perfectoid repo into shape then I will be thinking about the same sort of thing, but I have no idea how it works.</p>

#### [ Kevin Buzzard (Oct 16 2018 at 11:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP%20paper/near/135887824):
<p>I see -- in section 6 you are perhaps claiming that as far as you know, Hensel's Lemma for the p-adics has not ever been done before.</p>

#### [ Johan Commelin (Oct 16 2018 at 11:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP%20paper/near/135887905):
<p><span class="user-mention" data-user-id="110596">@Rob Lewis</span> Typo in section 6. You write "Metmath"</p>

#### [ Johan Commelin (Oct 16 2018 at 11:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP%20paper/near/135887919):
<p>Also, congrats with the draft <span class="emoji emoji-1f609" title="wink">:wink:</span></p>

#### [ Kevin Buzzard (Oct 16 2018 at 11:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP%20paper/near/135887927):
<p>If I were supervising a Masters student who wanted to do something involving Hensel's Lemma I would have told them to prove it for an arbitrary complete DVR and then prove that the p-adic numbers are a complete DVR. The fact that this machinery is not in Lean somehow makes this less convenient. Yes, let me also congratulate you on the draft :-)</p>

#### [ Kevin Buzzard (Oct 16 2018 at 11:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP%20paper/near/135888115):
<p>The philosophy here is that proving Hensel's Lemma for the p-adics is a way of putting the library through its paces. How did you get the status of Hensel's Lemma in all the gazillion other proof assistants? Presumably I'll have to do this with schemes one day.</p>

#### [ Johan Commelin (Oct 16 2018 at 11:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP%20paper/near/135888233):
<blockquote>
<p>Presumably I'll have to do this with schemes one day.</p>
</blockquote>
<p>I think that is a lot easier. I'm pretty sure nobody has done that before. (Although I've seen slides by Coquand on constructive algebraic geometry. But that didn't do any sheaves. It just defined <code>Spec A</code> as a locale [~~ <code>open_set</code>].)</p>

#### [ Rob Lewis (Oct 16 2018 at 11:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP%20paper/near/135888258):
<p>The expectation for this kind of paper is that the subject hasn't been formalized before, or that you've formalized it in a novel and interesting way, and typically that it's part of some broader project. It isn't novel math, but it's a novel formalization, that shows off features of Lean and mathlib, that's a building block for work we plan to do in the future. And of course there's no guarantee that it gets accepted!</p>

#### [ Rob Lewis (Oct 16 2018 at 11:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP%20paper/near/135888317):
<p><span class="user-mention" data-user-id="112680">@Johan Commelin</span> Thanks, fixed <span class="emoji emoji-1f642" title="slight smile">:slight_smile:</span></p>

#### [ Rob Lewis (Oct 16 2018 at 11:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP%20paper/near/135888347):
<p>There aren't really a gazillion other proof assistants to check. It's easy enough to see what's in the Isabelle AFP, Mizar MML, and HOL Light library, they're all pretty self-contained.</p>

#### [ Rob Lewis (Oct 16 2018 at 11:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP%20paper/near/135888401):
<p>Coq is trickier since it's a bit more fragmented, but Google "p-adic numbers coq" or "hensel's lemma coq" turns up what exists.</p>

#### [ Kevin Buzzard (Oct 16 2018 at 14:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP%20paper/near/135895307):
<blockquote>
<p>There aren't really a gazillion other proof assistants to check. It's easy enough to see what's in the Isabelle AFP, Mizar MML, and HOL Light library, they're all pretty self-contained.</p>
</blockquote>
<p>Maybe for you -- it sounds a bit scary to me! I can't even read mathlib, and that's in a language that I kind-of know! Have schemes or perfectoid spaces been done before?</p>
<p>But your message answers my question very well -- thanks. I saw that someone had a paper or some sort of a write-up at least on formalising localisation of a ring in some other theorem prover and my first thought was "Kenny did that in Lean when he was a first year undergrad". If you want to explain another reason why it's part of a broader project, you can say that it's part of the 4th year undergrad curriculum at Imperial College London (p-adic numbers and Hensel's Lemma are part of the elliptic curves course, which I designed about 15 years ago) so they're an essential part of my plan to digitise the entire pure maths curriculum! And anyway, this universe is so real-number-centred and I've never understood why, the p-adic numbers are just another completion of the rationals, I don't know why we don't teach them to schoolkids.</p>

#### [ Rob Lewis (Oct 16 2018 at 14:11)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP%20paper/near/135895805):
<blockquote>
<p>Have schemes or perfectoid spaces been done before?</p>
</blockquote>
<p>I strongly suspect that they haven't. A quick look at Google doesn't turn up anything relevant for perfectoid spaces. This is a new and deep concept, if it's been formalized it won't have been done silently. Schemes are harder to search for because the word is used another way in logic, but I don't see anything at a glance.</p>

#### [ Rob Lewis (Oct 16 2018 at 14:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP%20paper/near/135895866):
<p><a href="http://fm.mizar.org/fm.bib" target="_blank" title="http://fm.mizar.org/fm.bib">http://fm.mizar.org/fm.bib</a> is a quick way to search through the Mizar library. <a href="https://www.isa-afp.org/topics.html" target="_blank" title="https://www.isa-afp.org/topics.html">https://www.isa-afp.org/topics.html</a> to see significant developments in Isabelle, although not everything done in Isabelle is there.</p>

#### [ Rob Lewis (Oct 16 2018 at 14:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP%20paper/near/135896017):
<p><a href="https://github.com/math-comp/math-comp" target="_blank" title="https://github.com/math-comp/math-comp">https://github.com/math-comp/math-comp</a> is maybe the most likely place to find these sorts of things in Coq, and you can use the normal GitHub search there. But there are other unconnected Coq libraries.</p>

#### [ Kevin Buzzard (Oct 16 2018 at 14:17)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP%20paper/near/135896096):
<p>Thanks so much for the algorithm Rob!</p>

#### [ Rob Lewis (Oct 16 2018 at 14:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP%20paper/near/135896164):
<p>Just remember it isn't a decision procedure!</p>

#### [ Tobias Grosser (Oct 16 2018 at 17:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP%20paper/near/135909496):
<p>Very nice!</p>

#### [ Tobias Grosser (Oct 16 2018 at 17:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP%20paper/near/135909524):
<p>Does it make sense to reference the git hash of mathlib/lean version u are using in the paper?</p>

#### [ Tobias Grosser (Oct 16 2018 at 18:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP%20paper/near/135909795):
<p>Also, I spend some time reading about math yesterday to learn about p-adic numbers. So your paper comes at a very convenient point.</p>

#### [ Tobias Grosser (Oct 16 2018 at 18:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP%20paper/near/135909805):
<p>Put it already on my reading list.</p>

#### [ Tobias Grosser (Oct 16 2018 at 18:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP%20paper/near/135909833):
<p>I already have one question: "AFAIU 2's complement representation used to represent numbers in computers is a special case of p-adic number, right?"</p>

#### [ Tobias Grosser (Oct 16 2018 at 18:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP%20paper/near/135909907):
<p>Does your representation require p to be prime?</p>

#### [ Tobias Grosser (Oct 16 2018 at 18:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP%20paper/near/135909967):
<p>I wonder if existing decision procedures for Presburger arithmetic could apply directly to p-adic numbers or if instead one would need to explicitly model the "wrapping" using existentially quantified variables over a domain <code>\mathbb{Z}</code>.</p>

#### [ Kenny Lau (Oct 16 2018 at 18:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP%20paper/near/135910024):
<p>nothing uncountable can be decidable</p>

#### [ Tobias Grosser (Oct 16 2018 at 18:07)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP%20paper/near/135910072):
<p>OK, I need to understand this in more detail.</p>

#### [ Tobias Grosser (Oct 16 2018 at 18:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP%20paper/near/135910141):
<p>Likely p-adic numbers in full generality may be undecidable, but the special case of 2's complement representation used on computers is certainly decidable.</p>

#### [ Tobias Grosser (Oct 16 2018 at 18:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP%20paper/near/135910171):
<p>I am not sure what the delta is in between.</p>

#### [ Tobias Grosser (Oct 16 2018 at 18:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP%20paper/near/135910585):
<p><a href="http://www.numericana.com/answer/p-adic.htm" target="_blank" title="http://www.numericana.com/answer/p-adic.htm">http://www.numericana.com/answer/p-adic.htm</a></p>

#### [ Tobias Grosser (Oct 16 2018 at 18:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP%20paper/near/135910590):
<p>Explains how two's complements in computers related to p-adic numbers.</p>

#### [ Kevin Buzzard (Oct 16 2018 at 18:18)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP%20paper/near/135910715):
<p>The problem is that a 2-adic number is an infinite string of 0s and 1s</p>

#### [ Kevin Buzzard (Oct 16 2018 at 18:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP%20paper/near/135910764):
<p>so just like the reals there's no way to decide if two 2-adic numbers are equal because you don't know whether they're going to be different at the term after you got tired checking</p>

#### [ Tobias Grosser (Oct 16 2018 at 18:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP%20paper/near/135910916):
<p>Right. So in computers we always have finite lenght integers, such that after bit 32 all outer bits are dropped, aka assumed to have the same value than bit 32.</p>

#### [ Kevin Buzzard (Oct 16 2018 at 18:21)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP%20paper/near/135910935):
<p>that would be like doing real numbers to 32 significant figures</p>

#### [ Tobias Grosser (Oct 16 2018 at 18:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP%20paper/near/135910979):
<p>Right.</p>

#### [ Tobias Grosser (Oct 16 2018 at 18:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP%20paper/near/135910997):
<p>That should then be trivially decidable, afaiu.</p>

#### [ Kevin Buzzard (Oct 16 2018 at 18:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP%20paper/near/135911019):
<p>so your system sounds more like <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mrow><mi mathvariant="double-struck">Z</mi></mrow><mi mathvariant="normal">/</mi><msup><mn>2</mn><mi>n</mi></msup><mrow><mi mathvariant="double-struck">Z</mi></mrow></mrow><annotation encoding="application/x-tex">\mathbb{Z}/2^n\mathbb{Z}</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mord"><span class="mord mathbb">Z</span></span><span class="mord mathrm">/</span><span class="mord"><span class="mord mathrm">2</span><span class="msupsub"><span class="vlist-t"><span class="vlist-r"><span class="vlist" style="height:0.664392em;"><span style="top:-3.063em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight">n</span></span></span></span></span></span></span></span><span class="mord"><span class="mord mathbb">Z</span></span></span></span></span> where <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>n</mi></mrow><annotation encoding="application/x-tex">n</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.43056em;"></span><span class="strut bottom" style="height:0.43056em;vertical-align:0em;"></span><span class="base"><span class="mord mathit">n</span></span></span></span> is the number of bits you want to spend storing your numbers</p>

#### [ Kevin Buzzard (Oct 16 2018 at 18:23)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP%20paper/near/135911056):
<p>but the 2-adic integers are the limit of these things -- the projective limit, if you're a mathematician -- as <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>n</mi></mrow><annotation encoding="application/x-tex">n</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.43056em;"></span><span class="strut bottom" style="height:0.43056em;vertical-align:0em;"></span><span class="base"><span class="mord mathit">n</span></span></span></span> goes to infinity.</p>

#### [ Tobias Grosser (Oct 16 2018 at 18:24)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP%20paper/near/135911117):
<p>I see.</p>

#### [ Tobias Grosser (Oct 16 2018 at 18:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP%20paper/near/135911160):
<p>AFAIU Z/2^n Z gives just positive numbers</p>

#### [ Tobias Grosser (Oct 16 2018 at 18:25)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP%20paper/near/135911193):
<p>2's complement representation allows to reason about positive and negative numbers with one bit indicating the sign and n-1 bits indicating the value.</p>

#### [ Kevin Buzzard (Oct 16 2018 at 18:26)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP%20paper/near/135911244):
<p>but that bit which indicates the sign is just disappearing off to infinity in the limit, and disappears completely by the time you got there</p>

#### [ Kevin Buzzard (Oct 16 2018 at 18:27)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP%20paper/near/135911277):
<p>The CS model isn't a very good one for understanding the 2-adic integers. You could think of it as an infinite string of bits, and at some point you're hoping that you'll be told what the sign is, but actually you never get to that information.</p>

#### [ Tobias Grosser (Oct 16 2018 at 18:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP%20paper/near/135911368):
<p>Is the reason that towards infinity the digits might switch from 0 to 1 and vice versa?</p>

#### [ Tobias Grosser (Oct 16 2018 at 18:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP%20paper/near/135911387):
<p>So only if you know that all what is left is an infinite sequence of '0' and '1' you know the sign, right?</p>

#### [ Johan Commelin (Oct 16 2018 at 18:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP%20paper/near/135911421):
<p>No, there is no notion of positivity for <code>p</code>-adics. This is one of the main "problems" in arithmetic.</p>

#### [ Kenny Lau (Oct 16 2018 at 18:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP%20paper/near/135911489):
<p>so we can represent each 2-adic integer as a sequence (A, BA, CBA, DCBA, EDCBA, ...) where each letter is 0 or 1.<br>
-5 would correspond to (1, 11, 011, 1011, 11011, 111011, 1111011, ...)</p>

#### [ Kenny Lau (Oct 16 2018 at 18:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP%20paper/near/135911509):
<p>5 would correspond to (1, 01, 101, 0101, 00101, 000101, 0000101, ...)</p>

#### [ Kenny Lau (Oct 16 2018 at 18:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP%20paper/near/135911543):
<p>and you can write them more compactly as ....1111111011 and .....000000101</p>

#### [ Kevin Buzzard (Oct 16 2018 at 18:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP%20paper/near/135911546):
<p>The problem with saying "we can define the sign if it's all 1's from here" is that you've only defined the sign on 0% of the 2-adic numbers.</p>

#### [ Kevin Buzzard (Oct 16 2018 at 18:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP%20paper/near/135911560):
<p>For a general 2-adic number there is no good notion of sign</p>

#### [ Kenny Lau (Oct 16 2018 at 18:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP%20paper/near/135911565):
<p>but a dense set :P</p>

#### [ Tobias Grosser (Oct 16 2018 at 18:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP%20paper/near/135911576):
<p>In CS, we are only interested in this finite subset of the p-adic numbers, I feel.</p>

#### [ Kevin Buzzard (Oct 16 2018 at 18:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP%20paper/near/135911615):
<p>(i.e. not one which is continuous, or which has basic algebraic properties etc)</p>

#### [ Tobias Grosser (Oct 16 2018 at 18:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP%20paper/near/135911630):
<p>Probably the concept is way too general for what I would like to use it for.</p>

#### [ Kevin Buzzard (Oct 16 2018 at 18:32)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP%20paper/near/135911652):
<p>Modelling an abstract mathematical object like the reals by a concrete CS type such as a <code>float</code> means that you lose information (as far as we are concerned). In applications this might not be an issue, but in maths it is.</p>

#### [ Tobias Grosser (Oct 16 2018 at 18:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP%20paper/near/135911674):
<p>Sure, I don't want to squeeze all 2-adic numbers in fixed-size integers.</p>

#### [ Tobias Grosser (Oct 16 2018 at 18:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP%20paper/near/135911679):
<p>This is hopeless.</p>

#### [ Mario Carneiro (Oct 16 2018 at 18:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP%20paper/near/135911733):
<p>The two's complement representation of an integer coincides with its 2-adic expansion as <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi mathvariant="double-struck">Z</mi></mrow><annotation encoding="application/x-tex">\mathbb Z</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68889em;"></span><span class="strut bottom" style="height:0.68889em;vertical-align:0em;"></span><span class="base"><span class="mord mathbb">Z</span></span></span></span> embedded in <span class="katex"><span class="katex-mathml"><math><semantics><mrow><msub><mi mathvariant="double-struck">Z</mi><mn>2</mn></msub></mrow><annotation encoding="application/x-tex">\mathbb Z_2</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68889em;"></span><span class="strut bottom" style="height:0.83889em;vertical-align:-0.15em;"></span><span class="base"><span class="mord"><span class="mord mathbb">Z</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.30110799999999993em;"><span style="top:-2.5500000000000003em;margin-left:0em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathrm mtight">2</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"></span></span></span></span></span></span></span></span></p>

#### [ Tobias Grosser (Oct 16 2018 at 18:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP%20paper/near/135911756):
<p>I see.</p>

#### [ Tobias Grosser (Oct 16 2018 at 18:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP%20paper/near/135911761):
<p>Thanks <span class="user-mention" data-user-id="110049">@Mario Carneiro</span> for explaining this.</p>

#### [ Kevin Buzzard (Oct 16 2018 at 18:34)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP%20paper/near/135911764):
<p>Just like you can't squeeze all real numbers into 32 bits. But here is a consequence -- it means that you have trouble distinguishing rational from irrational numbers in <code>float</code> because you've lost information which from a "am I far from the right answer" position is small, but from a "have I lost any arithmetic information" is big</p>

#### [ Tobias Grosser (Oct 16 2018 at 18:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP%20paper/near/135911784):
<p>Would it make sense to e.g. define Cooper over this domain?</p>

#### [ Kevin Buzzard (Oct 16 2018 at 18:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP%20paper/near/135911797):
<p>There's no inequalities either, if you need inequalities</p>

#### [ Mario Carneiro (Oct 16 2018 at 18:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP%20paper/near/135911800):
<p>sure, I mean it's still the integers, but it's not easier</p>

#### [ Mario Carneiro (Oct 16 2018 at 18:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP%20paper/near/135911886):
<blockquote>
<p>nothing uncountable can be decidable</p>
</blockquote>
<p>This is an interesting statement. I wonder how you would prove this</p>

#### [ Kenny Lau (Oct 16 2018 at 18:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP%20paper/near/135911887):
<p>however given two <em>explicit</em> terms of type <code>p_adic_integer -&gt; nat</code>, you can decide if they are equal. (This is a meta-theorem, not a theorem)</p>

#### [ Kenny Lau (Oct 16 2018 at 18:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP%20paper/near/135911893):
<blockquote>
<blockquote>
<p>nothing uncountable can be decidable</p>
</blockquote>
<p>This is an interesting statement. I wonder how you would prove this</p>
</blockquote>
<p>that's a meta-theorem as well</p>

#### [ Mario Carneiro (Oct 16 2018 at 18:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP%20paper/near/135911894):
<p>false</p>

#### [ Kenny Lau (Oct 16 2018 at 18:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP%20paper/near/135911906):
<p>hmm?</p>

#### [ Mario Carneiro (Oct 16 2018 at 18:37)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP%20paper/near/135911912):
<p>You can do the same tricks as in R to construct numbers whose equality is equivalent to the halting problem</p>

#### [ Kenny Lau (Oct 16 2018 at 18:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP%20paper/near/135911972):
<p>right, but I mean terms that are constructed explicitly and constructively</p>

#### [ Mario Carneiro (Oct 16 2018 at 18:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP%20paper/near/135911977):
<p>even so</p>

#### [ Kenny Lau (Oct 16 2018 at 18:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP%20paper/near/135911980):
<p>i.e. computable functions</p>

#### [ Tobias Grosser (Oct 16 2018 at 18:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP%20paper/near/135911982):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span>, I need to read more of this but this is a paper I want to read regarding this issue: <a href="https://arxiv.org/pdf/1602.07209.pdf" target="_blank" title="https://arxiv.org/pdf/1602.07209.pdf">https://arxiv.org/pdf/1602.07209.pdf</a></p>

#### [ Mario Carneiro (Oct 16 2018 at 18:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP%20paper/near/135911992):
<p>computable number equality is not decidable</p>

#### [ Mario Carneiro (Oct 16 2018 at 18:38)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP%20paper/near/135912004):
<p>even though it is a countable set</p>

#### [ Mario Carneiro (Oct 16 2018 at 18:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP%20paper/near/135912007):
<p>so the converse of your statement is false</p>

#### [ Kenny Lau (Oct 16 2018 at 18:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP%20paper/near/135912009):
<p>i.e. you can't say "the n-th bit is 1 if this program terminates at the n-th step"</p>

#### [ Kenny Lau (Oct 16 2018 at 18:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP%20paper/near/135912025):
<p>that won't be a computable function</p>

#### [ Mario Carneiro (Oct 16 2018 at 18:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP%20paper/near/135912027):
<p>that's a computable function</p>

#### [ Kenny Lau (Oct 16 2018 at 18:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP%20paper/near/135912039):
<p>ah wait</p>

#### [ Mario Carneiro (Oct 16 2018 at 18:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP%20paper/near/135912041):
<p>termination in n steps is decidable</p>

#### [ Kenny Lau (Oct 16 2018 at 18:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP%20paper/near/135912113):
<p>wait no</p>

#### [ Kenny Lau (Oct 16 2018 at 18:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP%20paper/near/135912116):
<p>that isn't what I said</p>

#### [ Kenny Lau (Oct 16 2018 at 18:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP%20paper/near/135912118):
<blockquote>
<p>however given two <em>explicit</em> terms of type <code>p_adic_integer -&gt; nat</code>, you can decide if they are equal. (This is a meta-theorem, not a theorem)</p>
</blockquote>
<p>here</p>

#### [ Kenny Lau (Oct 16 2018 at 18:40)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP%20paper/near/135912128):
<p>you gave me two terms of type <code>p_adic_integer</code></p>

#### [ Mario Carneiro (Oct 16 2018 at 18:41)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP%20paper/near/135912138):
<p>what is an explicit term of <code>p_adic_integer</code>? It is a lambda, which is a computable function</p>

#### [ Kenny Lau (Oct 16 2018 at 18:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP%20paper/near/135912221):
<p>right</p>

#### [ Kenny Lau (Oct 16 2018 at 18:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP%20paper/near/135912230):
<p>but I'm talking about terms which have type <code>p_adic_integer -&gt; nat</code></p>

#### [ Mario Carneiro (Oct 16 2018 at 18:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP%20paper/near/135912239):
<p>oh you are using Andrej Bauer's trick</p>

#### [ Kenny Lau (Oct 16 2018 at 18:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP%20paper/near/135912241):
<p>right</p>

#### [ Kenny Lau (Oct 16 2018 at 18:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP%20paper/near/135912244):
<p>someone should make that a tactic :P</p>

#### [ Mario Carneiro (Oct 16 2018 at 18:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP%20paper/near/135912264):
<p>well, it's still false because <code>choice</code> is an explicit term</p>

#### [ Kenny Lau (Oct 16 2018 at 18:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP%20paper/near/135912270):
<p>constructive</p>

#### [ Tobias Grosser (Oct 16 2018 at 18:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP%20paper/near/135913075):
<p>Here the interesting part:</p>
<blockquote>
<p>Obviously  there  is  no  direct translation of concepts like linear inequalities and Barycentric Division to non-ordered fields, such as the p-adic ones. Nevertheless we want our p-adic polytopes and simplexes to be defined by conditions which are as simple as possible, to obtain a notion of faces satisfying all the above properties, and most of all to develop a flexible and powerful division tool. This is achieved here by first introducing and studying certain subsets of Γm called “largely continuous precells modN”, for a fixed m-tuple N of positive integers.  These sets will be defined by a very special triangular system of linear inequalities  and  congruence  relations  modN.   In  particular  they  are  defined simply by linear inequalities in the special case where N= (1,...,1) ...</p>
</blockquote>

#### [ Tobias Grosser (Oct 16 2018 at 18:58)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP%20paper/near/135913192):
<p>and</p>
<blockquote>
<p>We extend the binary congruence relations of Z to Γ with the convention that a≡+∞[N] for every a∈Γ and everyN∈N.  A subset A of FI(Γm) is a basic Presburger set if it is the set of solutions of finitely many linear inequalities and congruence relations.  Although we will not use it, it is worth mentioning that, by the quantifier elimination of the theory of Z in the language LP res, the definable subsets of Z d, and more generally of Γm, are exactly the finite unions of basic Presburger sets.</p>
</blockquote>

#### [ Tobias Grosser (Oct 16 2018 at 19:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP%20paper/near/135913312):
<p>Need to allocate a weekend to go through the paper carefully before i can have an in-depth discussion here.</p>

#### [ Tobias Grosser (Oct 16 2018 at 19:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP%20paper/near/135913315):
<p>Thanks for the comments.</p>

#### [ Mario Carneiro (Oct 16 2018 at 19:35)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP%20paper/near/135915767):
<p><span class="user-mention" data-user-id="110064">@Kenny Lau</span>  Here's a stab at your first statement: suppose P Is a program that decides equality for terms of type T. Given inputs (x, y), P will make some number of decisions (like if statements) before announcing true or false, which maps (x, y) in <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mrow><mi mathvariant="double-struck">Z</mi></mrow><mo>⊆</mo><msub><mi mathvariant="double-struck">Z</mi><mn>2</mn></msub></mrow><annotation encoding="application/x-tex">\mathbb{Z}\subseteq\mathbb{Z}_2</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68889em;"></span><span class="strut bottom" style="height:0.83889em;vertical-align:-0.15em;"></span><span class="base"><span class="mord"><span class="mord mathbb">Z</span></span><span class="mrel">⊆</span><span class="mord"><span class="mord"><span class="mord mathbb">Z</span></span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.30110799999999993em;"><span style="top:-2.5500000000000003em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathrm mtight">2</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.15em;"></span></span></span></span></span></span></span></span> where the ones and zeros correspond to the choices, and the termination is because P always halts. This is a mapping <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>F</mi><mo>:</mo><mi>T</mi><mo>×</mo><mi>T</mi><mo>→</mo><mrow><mi mathvariant="double-struck">Z</mi></mrow></mrow><annotation encoding="application/x-tex">F : T \times T \to \mathbb{Z}</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68889em;"></span><span class="strut bottom" style="height:0.77222em;vertical-align:-0.08333em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.13889em;">F</span><span class="mrel">:</span><span class="mord mathit" style="margin-right:0.13889em;">T</span><span class="mbin">×</span><span class="mord mathit" style="margin-right:0.13889em;">T</span><span class="mrel">→</span><span class="mord"><span class="mord mathbb">Z</span></span></span></span></span>, and there is some set <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>S</mi><mo>⊆</mo><mrow><mi mathvariant="double-struck">Z</mi></mrow></mrow><annotation encoding="application/x-tex">S\subseteq \mathbb{Z}</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68889em;"></span><span class="strut bottom" style="height:0.82486em;vertical-align:-0.13597em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.05764em;">S</span><span class="mrel">⊆</span><span class="mord"><span class="mord mathbb">Z</span></span></span></span></span> of "accepting states" where the program announces equality; correctness of P implies <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>F</mi><mo>(</mo><mi>x</mi><mo separator="true">,</mo><mi>y</mi><mo>)</mo><mo>∈</mo><mi>S</mi><mspace width="0.277778em"></mspace><mo>⟺</mo><mspace width="0.277778em"></mspace><mi>x</mi><mo>=</mo><mi>y</mi></mrow><annotation encoding="application/x-tex">F(x,y)\in S\iff x=y</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.13889em;">F</span><span class="mopen">(</span><span class="mord mathit">x</span><span class="mpunct">,</span><span class="mord mathit" style="margin-right:0.03588em;">y</span><span class="mclose">)</span><span class="mrel">∈</span><span class="mord mathit" style="margin-right:0.05764em;">S</span><span class="mrel"><span class="mspace thickspace"></span><span class="mrel">⟺</span></span><span class="mord mathit"><span class="mspace thickspace"></span><span class="mord mathit">x</span></span><span class="mrel">=</span><span class="mord mathit" style="margin-right:0.03588em;">y</span></span></span></span>.</p>
<p>If P has access to mysterious operations that measure x and y jointly, then it is possible that x=y is just a single instruction in the machine and so the theorem won't hold. Instead, we assume that each branching operation measures some property of either x or y but not both at the same time. (Stuff like comparing the first bit of x against the first bit of y can be split into two branches to measure first x then y.)</p>
<p>Now if <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>F</mi><mo>(</mo><mi>x</mi><mo separator="true">,</mo><mi>x</mi><mo>)</mo><mo>=</mo><mi>F</mi><mo>(</mo><mi>y</mi><mo separator="true">,</mo><mi>y</mi><mo>)</mo></mrow><annotation encoding="application/x-tex">F(x,x) = F(y,y)</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.13889em;">F</span><span class="mopen">(</span><span class="mord mathit">x</span><span class="mpunct">,</span><span class="mord mathit">x</span><span class="mclose">)</span><span class="mrel">=</span><span class="mord mathit" style="margin-right:0.13889em;">F</span><span class="mopen">(</span><span class="mord mathit" style="margin-right:0.03588em;">y</span><span class="mpunct">,</span><span class="mord mathit" style="margin-right:0.03588em;">y</span><span class="mclose">)</span></span></span></span>, meaning that the same sequence of operations that lead to the decision <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>x</mi><mo>=</mo><mi>x</mi></mrow><annotation encoding="application/x-tex">x=x</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.43056em;"></span><span class="strut bottom" style="height:0.43056em;vertical-align:0em;"></span><span class="base"><span class="mord mathit">x</span><span class="mrel">=</span><span class="mord mathit">x</span></span></span></span> or <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>y</mi><mo>=</mo><mi>y</mi></mrow><annotation encoding="application/x-tex">y=y</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.43056em;"></span><span class="strut bottom" style="height:0.625em;vertical-align:-0.19444em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.03588em;">y</span><span class="mrel">=</span><span class="mord mathit" style="margin-right:0.03588em;">y</span></span></span></span>, then we also have <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>F</mi><mo>(</mo><mi>x</mi><mo separator="true">,</mo><mi>x</mi><mo>)</mo><mo>=</mo><mi>F</mi><mo>(</mo><mi>x</mi><mo separator="true">,</mo><mi>y</mi><mo>)</mo></mrow><annotation encoding="application/x-tex">F(x,x)=F(x,y)</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.13889em;">F</span><span class="mopen">(</span><span class="mord mathit">x</span><span class="mpunct">,</span><span class="mord mathit">x</span><span class="mclose">)</span><span class="mrel">=</span><span class="mord mathit" style="margin-right:0.13889em;">F</span><span class="mopen">(</span><span class="mord mathit">x</span><span class="mpunct">,</span><span class="mord mathit" style="margin-right:0.03588em;">y</span><span class="mclose">)</span></span></span></span> because both execution paths make the same decisions regardless of whether they are examining <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>x</mi></mrow><annotation encoding="application/x-tex">x</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.43056em;"></span><span class="strut bottom" style="height:0.43056em;vertical-align:0em;"></span><span class="base"><span class="mord mathit">x</span></span></span></span> or <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>y</mi></mrow><annotation encoding="application/x-tex">y</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.43056em;"></span><span class="strut bottom" style="height:0.625em;vertical-align:-0.19444em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.03588em;">y</span></span></span></span>. Thus <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>x</mi><mo>=</mo><mi>y</mi></mrow><annotation encoding="application/x-tex">x=y</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.43056em;"></span><span class="strut bottom" style="height:0.625em;vertical-align:-0.19444em;"></span><span class="base"><span class="mord mathit">x</span><span class="mrel">=</span><span class="mord mathit" style="margin-right:0.03588em;">y</span></span></span></span>, so <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>F</mi></mrow><annotation encoding="application/x-tex">F</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.13889em;">F</span></span></span></span> is injective on the diagonal and hence <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>T</mi></mrow><annotation encoding="application/x-tex">T</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.13889em;">T</span></span></span></span> is countable.</p>

#### [ Rob Lewis (Oct 16 2018 at 20:57)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP%20paper/near/135921571):
<p>Looks like I missed an interesting conversation, but just to answer the easy questions at the beginning! <span class="user-mention" data-user-id="122318">@Tobias Grosser</span> indeed, referencing a git hash would be ugly but more stable. I'll try it out. The construction does require <code>p</code> to be prime. I don't even have a picture of what Presburger arithmetic over Z_p would look like since there's no ordering. Maybe there's an answer in the polytope paper you linked, that looks super interesting.</p>

#### [ Tobias Grosser (Oct 16 2018 at 20:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP%20paper/near/135921698):
<p>Thanks <span class="user-mention" data-user-id="110596">@Rob Lewis</span> for the answer. I would really like to discuss some of these topics in Freiburg.</p>

#### [ Tobias Grosser (Oct 16 2018 at 20:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP%20paper/near/135921722):
<p>Need to do more reading to be able to have at least a somehow sensible conversation.</p>

#### [ Tobias Grosser (Oct 16 2018 at 20:59)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP%20paper/near/135921728):
<p>Getting your opinion on this topic would be very useful.</p>

#### [ Rob Lewis (Oct 16 2018 at 21:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP%20paper/near/135921807):
<p>For sure!</p>

#### [ Tobias Grosser (Oct 16 2018 at 21:01)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP%20paper/near/135921893):
<p>Regarding the lack of ordering, in our compiler we associate to comparisions the information if a comparision should be interpreted as signed or unsigned.</p>

#### [ Tobias Grosser (Oct 16 2018 at 21:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP%20paper/near/135921947):
<p>In this sense, hence there are two "order" relations.</p>

#### [ Tobias Grosser (Oct 16 2018 at 21:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP%20paper/near/135921957):
<p>When when interpreting the values as signed integers, the other when interpreting them as unsigned.</p>

#### [ Tobias Grosser (Oct 16 2018 at 21:02)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP%20paper/near/135921960):
<p>They are to my understanding not compatible.</p>

#### [ Tobias Grosser (Oct 16 2018 at 21:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP%20paper/near/135921996):
<p>And maybe don't work  for generic p-adic numbers, but just the finite bitwidth numbers we are interested in.</p>

#### [ Reid Barton (Oct 16 2018 at 21:03)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP%20paper/near/135922000):
<p>They're also both not compatible with other structure like addition. For example if <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>a</mi><mo>≥</mo><mi>b</mi></mrow><annotation encoding="application/x-tex">a \ge b</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.69444em;"></span><span class="strut bottom" style="height:0.83041em;vertical-align:-0.13597em;"></span><span class="base"><span class="mord mathit">a</span><span class="mrel">≥</span><span class="mord mathit">b</span></span></span></span> (in either sense), then it does not follow that <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>a</mi><mo>+</mo><mi>c</mi><mo>≥</mo><mi>b</mi><mo>+</mo><mi>c</mi></mrow><annotation encoding="application/x-tex">a + c \ge b + c</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.69444em;"></span><span class="strut bottom" style="height:0.83041em;vertical-align:-0.13597em;"></span><span class="base"><span class="mord mathit">a</span><span class="mbin">+</span><span class="mord mathit">c</span><span class="mrel">≥</span><span class="mord mathit">b</span><span class="mbin">+</span><span class="mord mathit">c</span></span></span></span>, unless you know that the additions do not overflow somehow</p>

#### [ Tobias Grosser (Oct 16 2018 at 21:04)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP%20paper/near/135922052):
<p>Right.</p>

#### [ Reid Barton (Oct 16 2018 at 21:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP%20paper/near/135922101):
<p>If you tried to define inequalities similarly for the 2-adics, then you should "start from the left-most bit"--but there is no left-most bit of a 2-adic number</p>

#### [ Tobias Grosser (Oct 16 2018 at 21:05)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP%20paper/near/135922149):
<p>Right. Many things don't fully checkout here.</p>

#### [ Reid Barton (Oct 16 2018 at 21:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP%20paper/near/135922197):
<p>I took a quick look at that paper and it was a bit hard to understand what their goal was, in part because the paper seemed to be setting up some background theory for a subsequent paper. But as far as I can tell, it talks about Presburger arithmetic not on Z_p or Q_p directly but on N or Z via the p-adic valuation.</p>

#### [ Reid Barton (Oct 16 2018 at 21:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP%20paper/near/135922360):
<p>You could also say that Presburger arithmetic on N is really just the first order theory of addition (and zero) because an inequality <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>a</mi><mo>≤</mo><mi>b</mi></mrow><annotation encoding="application/x-tex">a \le b</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.69444em;"></span><span class="strut bottom" style="height:0.83041em;vertical-align:-0.13597em;"></span><span class="base"><span class="mord mathit">a</span><span class="mrel">≤</span><span class="mord mathit">b</span></span></span></span> can be represented by <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi mathvariant="normal">∃</mi><mi>c</mi><mo separator="true">,</mo><mi>a</mi><mo>+</mo><mi>c</mi><mo>=</mo><mi>b</mi></mrow><annotation encoding="application/x-tex">\exists c, a + c = b</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.69444em;"></span><span class="strut bottom" style="height:0.8888799999999999em;vertical-align:-0.19444em;"></span><span class="base"><span class="mord mathrm">∃</span><span class="mord mathit">c</span><span class="mpunct">,</span><span class="mord mathit">a</span><span class="mbin">+</span><span class="mord mathit">c</span><span class="mrel">=</span><span class="mord mathit">b</span></span></span></span>. So then you could ask about the first order theory of addition for Z_p. I think it would just reduce to making statements about the p-adic valuations.</p>

#### [ Tobias Grosser (Oct 16 2018 at 21:12)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP%20paper/near/135922570):
<p>Interesting.</p>

#### [ Siddharth Bhat (Oct 21 2018 at 20:39)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP%20paper/near/136224451):
<p><span class="user-mention" data-user-id="110032">@Reid Barton</span>  what does it mean to perform presburger arithmetic on the p-adic valuation?</p>

#### [ Reid Barton (Oct 21 2018 at 20:42)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP%20paper/near/136224600):
<p>Well the p-adic valuation of a p-adic integer is a natural number, and Presburger arithmetic is the theory of natural numbers under zero and addition. So we're talking about formulas like "<span class="katex"><span class="katex-mathml"><math><semantics><mrow><msub><mi>v</mi><mi>p</mi></msub><mo>(</mo><mi>x</mi><mo>)</mo><mo>=</mo><msub><mi>v</mi><mi>p</mi></msub><mo>(</mo><mi>y</mi><mo>)</mo><mo>+</mo><msub><mi>v</mi><mi>p</mi></msub><mo>(</mo><mi>y</mi><mo>)</mo><mo>+</mo><mn>1</mn></mrow><annotation encoding="application/x-tex">v_p(x) = v_p(y) + v_p(y) + 1</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1.036108em;vertical-align:-0.286108em;"></span><span class="base"><span class="mord"><span class="mord mathit" style="margin-right:0.03588em;">v</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.15139200000000003em;"><span style="top:-2.5500000000000003em;margin-left:-0.03588em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight">p</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.286108em;"></span></span></span></span></span><span class="mopen">(</span><span class="mord mathit">x</span><span class="mclose">)</span><span class="mrel">=</span><span class="mord"><span class="mord mathit" style="margin-right:0.03588em;">v</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.15139200000000003em;"><span style="top:-2.5500000000000003em;margin-left:-0.03588em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight">p</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.286108em;"></span></span></span></span></span><span class="mopen">(</span><span class="mord mathit" style="margin-right:0.03588em;">y</span><span class="mclose">)</span><span class="mbin">+</span><span class="mord"><span class="mord mathit" style="margin-right:0.03588em;">v</span><span class="msupsub"><span class="vlist-t vlist-t2"><span class="vlist-r"><span class="vlist" style="height:0.15139200000000003em;"><span style="top:-2.5500000000000003em;margin-left:-0.03588em;margin-right:0.05em;"><span class="pstrut" style="height:2.7em;"></span><span class="sizing reset-size6 size3 mtight"><span class="mord mathit mtight">p</span></span></span></span><span class="vlist-s">​</span></span><span class="vlist-r"><span class="vlist" style="height:0.286108em;"></span></span></span></span></span><span class="mopen">(</span><span class="mord mathit" style="margin-right:0.03588em;">y</span><span class="mclose">)</span><span class="mbin">+</span><span class="mord mathrm">1</span></span></span></span>".</p>

#### [ Siddharth Bhat (Oct 21 2018 at 20:47)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP%20paper/near/136224767):
<p>Ah, hm.</p>

#### [ Siddharth Bhat (Oct 21 2018 at 20:53)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/CPP%20paper/near/136225013):
<p><span class="user-mention" data-user-id="110032">@Reid Barton</span> Do you know, how much of the geometry of presburger sets is left over when you move to p-adics?</p>


{% endraw %}
