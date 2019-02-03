---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/94921teachinguseofquotientsinLean.html
---

## Stream: [maths](index.html)
### Topic: [teaching use of quotients in Lean](94921teachinguseofquotientsinLean.html)

---


{% raw %}
#### [ Kevin Buzzard (Aug 09 2018 at 19:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131184986):
<p>I once found it hard to use quotients in Lean. I typically wanted to use quotients to define mathematical objects (like quotient rings) and the example (unordered pairs) in TPIL was a bit CSish for me. The first time I needed them was for localisation of rings and Kenny wrote everything for me. But I needed them more and more, and eventually I had to learn how they worked. I wrote code for the integers mod n, but at the time I didn't understand the type class inference system very well either, and the code was not great. <span class="user-mention" data-user-id="120726">@Luca Gerolla</span> needs to work with quotients for his work on the fundamental group and it occurred to me that I should revisit the work and tidy it up. One problem with integers mod n which I think could confuse beginners was a problem discussed here once, namely that it's hard to use type classes to put the equivalence relation of being congruent mod n onto Z, because that's one equivalence relation per n, and type class inference would rather there just be one equivalence relation on a type. The fix suggested to me at the time was to use a new version of Z for each integer, but having mulled this over for a while I decided that it added another layer of complexity which was unsuitable for the beginner. So I decided to choose everyone (except Johan)'s favourite integer 37, and just construct the integers mod 37 instead.</p>
<p>I jump from tactic mode proofs to half-tactic half-term to full term mode proofs, depending on whether I'm trying to demonstrate something for the first time or just get things done. This code is supposed to be readable by learners who know a bit about Lean and are interested in decyphering all the <code>quotient.induction_on\2</code> stuff and want to see a relatively simple example. The code is here:</p>
<p><a href="https://github.com/kbuzzard/xena/blob/master/xenalib/m1f/zmod37.lean" target="_blank" title="https://github.com/kbuzzard/xena/blob/master/xenalib/m1f/zmod37.lean">https://github.com/kbuzzard/xena/blob/master/xenalib/m1f/zmod37.lean</a></p>

#### [ Patrick Massot (Aug 09 2018 at 19:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131185870):
<p>Why do you define a setoid instance instead of having a def?</p>

#### [ Mario Carneiro (Aug 09 2018 at 19:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131186089):
<p>I'm not seeing why 37 is better than n</p>

#### [ Kevin Buzzard (Aug 09 2018 at 19:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131186102):
<p>I want to give the same answer to both questions -- so I can use type class inference</p>

#### [ Kevin Buzzard (Aug 09 2018 at 19:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131186108):
<p>I wanted access to the \[[ notation etc</p>

#### [ Mario Carneiro (Aug 09 2018 at 19:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131186114):
<p>make a notation for that</p>

#### [ Kevin Buzzard (Aug 09 2018 at 19:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131186129):
<p>I didn't want to make it harder. I wanted to show Luca how to do it</p>

#### [ Kevin Buzzard (Aug 09 2018 at 19:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131186132):
<p>That's the actual answer.</p>

#### [ Kevin Buzzard (Aug 09 2018 at 19:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131186147):
<p>I want <em>him</em> to use type class inference</p>

#### [ Mario Carneiro (Aug 09 2018 at 19:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131186235):
<p>I think <code>setoid</code> is one of the more poorly thought out typeclasses</p>

#### [ Chris Hughes (Aug 09 2018 at 19:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131186259):
<p>Are we still going to be stuck with those things in lean4?</p>

#### [ Mario Carneiro (Aug 09 2018 at 19:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131186284):
<p>no idea</p>

#### [ Mario Carneiro (Aug 09 2018 at 19:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131186302):
<p>I think it should be called <code>has_equiv</code> and be tied to the <code>\approx</code> notation, but the <code>\[[</code> notation should be inferred by unification</p>

#### [ Kenny Lau (Aug 09 2018 at 19:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131186335):
<p>in lean4 we wouldn't have to worry about + and * being different things right</p>

#### [ Mario Carneiro (Aug 09 2018 at 19:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131186342):
<p>that's a bit vague</p>

#### [ Chris Hughes (Aug 09 2018 at 19:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131186375):
<p>I think the idea is that we won't have both <code>add_group</code> and <code>group</code></p>

#### [ Mario Carneiro (Aug 09 2018 at 19:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131186403):
<p>we won't have either</p>

#### [ Kevin Buzzard (Aug 09 2018 at 19:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131186410):
<blockquote>
<p>I think <code>setoid</code> is one of the more poorly thought out typeclasses</p>
</blockquote>
<p>Sure, but I am teaching Lean 3.4.1 so I went with it.</p>

#### [ Mario Carneiro (Aug 09 2018 at 19:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131186413):
<p>presumably that's moving to mathlib</p>

#### [ Kevin Buzzard (Aug 09 2018 at 19:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131186424):
<p>we could have <code>heartsuit_group</code></p>

#### [ Kevin Buzzard (Aug 09 2018 at 19:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131186431):
<p>the possibilities are endless</p>

#### [ Mario Carneiro (Aug 09 2018 at 19:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131186432):
<p>my point is that it's not a great example if you are teaching typeclasses</p>

#### [ Kevin Buzzard (Aug 09 2018 at 19:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131186593):
<p>I'm not teaching typeclasses, I'm teaching Luca how to work with the quotient of the paths from x to x by the is_homotopic relation which he's shown is an equivalence relation. He now has to define a group structure on the quotient, and I looked at his code, and he defined the group law by using <code>quotient.out</code> to choose two random lifts, composed the paths, and went back down again. He was not using type class inference either, so it was <code>@quotient.out [insert proof of equiv reln here]</code> I needed to show him how to do it properly. I agree that the file doesn't do everything, but hopefully it does what it needs to do.</p>

#### [ Kevin Buzzard (Aug 09 2018 at 19:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131186610):
<p>It is also the file I wished I had when I was trying to figure out how to use quotients for the first time.</p>

#### [ Mario Carneiro (Aug 09 2018 at 19:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131186629):
<p>maybe it should be</p>

#### [ Mario Carneiro (Aug 09 2018 at 19:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131186646):
<p>rather than showing people Z/37Z, show them the fundamental group</p>

#### [ Mario Carneiro (Aug 09 2018 at 19:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131186686):
<p>it's surely more interesting for students with more mathematical sophistication</p>

#### [ Mario Carneiro (Aug 09 2018 at 19:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131186824):
<p>then prove the fundamental group of the circle is Z and PR it :D</p>

#### [ Kevin Buzzard (Aug 09 2018 at 19:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131186893):
<blockquote>
<p>then prove the fundamental group of the circle is Z and PR it :D</p>
</blockquote>
<p>You mean do an _example_???</p>

#### [ Kevin Buzzard (Aug 09 2018 at 19:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131186908):
<p>Oh, is this just a way of proving that the definition is correct?</p>

#### [ Kevin Buzzard (Aug 09 2018 at 19:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131186946):
<p>The proof of pi_1(S^1)=Z I know involves constructing going via a triangulation and using some simplicial approximation theorem stuff</p>

#### [ Kevin Buzzard (Aug 09 2018 at 19:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131186973):
<p>it would not surprise me if there were a cute proof though</p>

#### [ Mario Carneiro (Aug 09 2018 at 19:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131186997):
<p>that is not what I expected</p>

#### [ Mario Carneiro (Aug 09 2018 at 19:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131187011):
<p>the proof I know uses covering maps and winding numbers</p>

#### [ Johan Commelin (Aug 09 2018 at 19:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131187038):
<p><code>S^1 = real/int</code>, and <code>real</code> is contractible. So <code>int</code> is the fundamental group.</p>

#### [ Johan Commelin (Aug 09 2018 at 19:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131187047):
<p>Now, how do we explain that to Lean?</p>

#### [ Mario Carneiro (Aug 09 2018 at 19:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131187054):
<p>wait what</p>

#### [ Mario Carneiro (Aug 09 2018 at 19:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131187098):
<p>how does that last step work?</p>

#### [ Johan Commelin (Aug 09 2018 at 19:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131187132):
<p>I guess you need to know that <code>S^1</code> is a <em>nice</em> space...</p>

#### [ Mario Carneiro (Aug 09 2018 at 19:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131187146):
<p>I believe the first line, that's not hard to prove</p>

#### [ Johan Commelin (Aug 09 2018 at 19:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131187147):
<p>Where <em>nice</em> means locally compact and t2, or something similar.</p>

#### [ Mario Carneiro (Aug 09 2018 at 19:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131187170):
<p>and you should get niceness that way</p>

#### [ Johan Commelin (Aug 09 2018 at 19:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131187189):
<p>And then you know that S^1 has a universal covering space, and you get a group structure on the fibre, which is exactly pi_1</p>

#### [ Mario Carneiro (Aug 09 2018 at 19:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131187203):
<p>are you still elucidating your one line proof?</p>

#### [ Johan Commelin (Aug 09 2018 at 19:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131187215):
<p>Yes... I'm sorry.</p>

#### [ Mario Carneiro (Aug 09 2018 at 19:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131187223):
<p>I'm trying to figure out how R is contractible plays into this</p>

#### [ Johan Commelin (Aug 09 2018 at 19:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131187235):
<p>Well, that is supposed to convince you that R is the universal covering space...</p>

#### [ Johan Commelin (Aug 09 2018 at 19:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131187327):
<p>We could prove a general lemma of the form <code>simply_connected X</code> implies <code>pi_1(X/G) = G</code></p>

#### [ Mario Carneiro (Aug 09 2018 at 19:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131187337):
<p>oh so that's true in generality?</p>

#### [ Johan Commelin (Aug 09 2018 at 19:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131187345):
<p>If <code>X</code> is nice.</p>

#### [ Johan Commelin (Aug 09 2018 at 19:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131187350):
<p>Maybe even in general.</p>

#### [ Mario Carneiro (Aug 09 2018 at 19:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131187354):
<p>G is discrete?</p>

#### [ Mario Carneiro (Aug 09 2018 at 19:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131187413):
<p>i.e. pi_1(X/X) is not X</p>

#### [ Johan Commelin (Aug 09 2018 at 19:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131187429):
<p>True.</p>

#### [ Mario Carneiro (Aug 09 2018 at 19:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131187451):
<p>to make X a covering map you need it to be locally like a quotient by a discrete space</p>

#### [ Johan Commelin (Aug 09 2018 at 19:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131187456):
<p>So there are some conditions. G needs to be discrete (topologically) and act freely on X, and the action must be continuous.</p>

#### [ Johan Commelin (Aug 09 2018 at 19:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131187468):
<p>So <code>G</code> is a discrete subgroup of <code>Aut_Top(X)</code>.</p>

#### [ Mario Carneiro (Aug 09 2018 at 19:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131187536):
<p>which kind of quotient are we talking about here?</p>

#### [ Johan Commelin (Aug 09 2018 at 19:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131187537):
<p>But I haven't formalised this... so I don't know what I'm talking about.</p>

#### [ Johan Commelin (Aug 09 2018 at 19:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131187557):
<p>X/G as a set, with quotient topology, I think.</p>

#### [ Mario Carneiro (Aug 09 2018 at 19:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131187558):
<p>If X is a topological group and G a discrete subgroup you get the other conditions</p>

#### [ Mario Carneiro (Aug 09 2018 at 19:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131187627):
<p>R/Z as a set is garbage, that just identifies the points of Z in R making it a bouquet of circles</p>

#### [ Johan Commelin (Aug 09 2018 at 19:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131187650):
<p>Aah, sorry. I meant as group action of sets.</p>

#### [ Kevin Buzzard (Aug 09 2018 at 19:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131187660):
<p>this is the quotient of a group acting on a nice top space</p>

#### [ Kevin Buzzard (Aug 09 2018 at 19:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131187664):
<p>so the quotient space is the set of orbits</p>

#### [ Kevin Buzzard (Aug 09 2018 at 19:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131187676):
<p>An example is the quotient of a group by a subgroup</p>

#### [ Kevin Buzzard (Aug 09 2018 at 19:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131187749):
<p>but if <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi mathvariant="normal">Γ</mi></mrow><annotation encoding="application/x-tex">\Gamma</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord mathrm">Γ</span></span></span></span> is a subgroup of <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>S</mi><mi>L</mi><mo>(</mo><mn>2</mn><mo separator="true">,</mo><mrow><mi mathvariant="double-struck">Z</mi></mrow><mo>)</mo></mrow><annotation encoding="application/x-tex">SL(2,\mathbb{Z})</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.75em;"></span><span class="strut bottom" style="height:1em;vertical-align:-0.25em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.05764em;">S</span><span class="mord mathit">L</span><span class="mopen">(</span><span class="mord mathrm">2</span><span class="mpunct">,</span><span class="mord"><span class="mord mathbb">Z</span></span><span class="mclose">)</span></span></span></span> with no torsion (e.g. the elements congruent to the identity modulo <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>N</mi></mrow><annotation encoding="application/x-tex">N</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.10903em;">N</span></span></span></span> for any <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi>N</mi><mo>&gt;</mo><mo>=</mo><mn>3</mn></mrow><annotation encoding="application/x-tex">N&gt;=3</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.72243em;vertical-align:-0.0391em;"></span><span class="base"><span class="mord mathit" style="margin-right:0.10903em;">N</span><span class="mrel">&gt;</span><span class="mrel">=</span><span class="mord mathrm">3</span></span></span></span>) then <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi mathvariant="normal">Γ</mi></mrow><annotation encoding="application/x-tex">\Gamma</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord mathrm">Γ</span></span></span></span> acts on the upper half plane (which is nice and contractible) discretely, and the quotient is a non-compact Riemann surface with fundamental group <span class="katex"><span class="katex-mathml"><math><semantics><mrow><mi mathvariant="normal">Γ</mi></mrow><annotation encoding="application/x-tex">\Gamma</annotation></semantics></math></span><span aria-hidden="true" class="katex-html"><span class="strut" style="height:0.68333em;"></span><span class="strut bottom" style="height:0.68333em;vertical-align:0em;"></span><span class="base"><span class="mord mathrm">Γ</span></span></span></span>.</p>

#### [ Johan Commelin (Aug 09 2018 at 19:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131187808):
<p>What would the definition of <code>S^1</code> be in Lean?</p>

#### [ Kevin Buzzard (Aug 09 2018 at 19:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131187823):
<p>You could certainly define it to be the closed subspace of R^2</p>

#### [ Johan Commelin (Aug 09 2018 at 19:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131187837):
<p>Right, that is maybe a more reasonable definition.</p>

#### [ Mario Carneiro (Aug 09 2018 at 19:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131187839):
<p>that's my thought as well, it's true to the literature and also generalizes to using circles as... circles</p>

#### [ Kevin Buzzard (Aug 09 2018 at 19:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131187840):
<p>and IF WE EVER MANAGED TO GET THE EXPONENTIAL FUNCTION INTO MATHLIB then you could even prove it was R mod Z :-)</p>

#### [ Johan Commelin (Aug 09 2018 at 19:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131187841):
<p>And then identify it with the unit circle in C</p>

#### [ Johan Commelin (Aug 09 2018 at 19:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131187845):
<p>Right.</p>

#### [ Kevin Buzzard (Aug 09 2018 at 20:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131187911):
<p><a href="#narrow/stream/116395-maths/topic/Trivial.20things.20about.20convergent.20power.20series" title="#narrow/stream/116395-maths/topic/Trivial.20things.20about.20convergent.20power.20series">https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/Trivial.20things.20about.20convergent.20power.20series</a></p>

#### [ Johan Commelin (Aug 09 2018 at 20:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131187915):
<p>Maybe exp should move to the community fork. Who knows if that would move it forward...</p>

#### [ Mario Carneiro (Aug 09 2018 at 20:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131187918):
<p>pff, use rational trig and you don't need exp</p>

#### [ Kevin Buzzard (Aug 09 2018 at 20:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131187926):
<p>:-)</p>

#### [ Kevin Buzzard (Aug 09 2018 at 20:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131187935):
<p>Who needs to be complex when you can just be rational.</p>

#### [ Mario Carneiro (Aug 09 2018 at 20:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131187976):
<p>that's actually a good idea Johan</p>

#### [ Kevin Buzzard (Aug 09 2018 at 20:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131188024):
<p>Or you could just come to the xena project, we use it freely over there :-)</p>

#### [ Kevin Buzzard (Aug 09 2018 at 20:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131188035):
<p>warning: not all code compiles</p>

#### [ Mario Carneiro (Aug 09 2018 at 20:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131188043):
<p>which is why it is a good community fork project</p>

#### [ Mario Carneiro (Aug 09 2018 at 20:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131188061):
<p>you are already using it but the PR needs more work</p>

#### [ Mario Carneiro (Aug 09 2018 at 20:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131188077):
<p>or at least I need to spend more time on it</p>

#### [ Kevin Buzzard (Aug 09 2018 at 20:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131188135):
<p>I don't even know which PR it is any more. Is it in the binomial theorem one or the limits one?</p>

#### [ Kevin Buzzard (Aug 09 2018 at 20:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131188145):
<p>I can't find it in either</p>

#### [ Mario Carneiro (Aug 09 2018 at 20:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131188153):
<p>surely it's not in the binomial theorem</p>

#### [ Johan Commelin (Aug 09 2018 at 20:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131188155):
<p>I think anyone can pull that branch into the community fork, right? (After we found it)</p>

#### [ Mario Carneiro (Aug 09 2018 at 20:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131188163):
<p>yes</p>

#### [ Kevin Buzzard (Aug 09 2018 at 20:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131188178):
<p>I think he needed the binomial theorem to prove exp(x+y)=exp(x)exp(y)</p>

#### [ Mario Carneiro (Aug 09 2018 at 20:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131188188):
<p>I suppose you do</p>

#### [ Kevin Buzzard (Aug 09 2018 at 20:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131188262):
<p>By the way, another random PR we use a lot at Imperial is Chris' zmod work. But I hear you didn't like pos_nat and I believe Chris is now re-doing everything with pnat and prime</p>

#### [ Kevin Buzzard (Aug 09 2018 at 20:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131188285):
<p>I can't find exp. Did he close it?</p>

#### [ Kevin Buzzard (Aug 09 2018 at 20:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131188293):
<p>No wonder it didn't get accepted :-)</p>

#### [ Johan Commelin (Aug 09 2018 at 20:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131188299):
<p><span class="user-mention" data-user-id="110044">@Chris Hughes</span> We need you (-;</p>

#### [ Kevin Buzzard (Aug 09 2018 at 20:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131188322):
<p>he's too busy helping all the other Imperial UGs while I'm on holiday :-)</p>

#### [ Mario Carneiro (Aug 09 2018 at 20:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131188323):
<p><a href="https://github.com/leanprover/mathlib/pull/43" target="_blank" title="https://github.com/leanprover/mathlib/pull/43">https://github.com/leanprover/mathlib/pull/43</a></p>

#### [ Johan Commelin (Aug 09 2018 at 20:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131188395):
<p>branch is no longer there.</p>

#### [ Johan Commelin (Aug 09 2018 at 20:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131188398):
<p>So we will need to get the stuff out of Xena.</p>

#### [ Kevin Buzzard (Aug 09 2018 at 20:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131188401):
<p>so it looks like the ball's in Chris' court.</p>

#### [ Mario Carneiro (Aug 09 2018 at 20:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131188402):
<p>no wait it's <a href="https://github.com/leanprover/mathlib/pull/41" target="_blank" title="https://github.com/leanprover/mathlib/pull/41">https://github.com/leanprover/mathlib/pull/41</a></p>

#### [ Mario Carneiro (Aug 09 2018 at 20:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131188414):
<p>it says it is a PR from <code>unknown repository</code></p>

#### [ Kevin Buzzard (Aug 09 2018 at 20:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131188466):
<p>I'd be quite happy if he were to concentrate on zmod at the minute, we've all found this very helpful. There's a bunch of people doing number theory and group theory, some of whom use it.</p>

#### [ Johan Commelin (Aug 09 2018 at 20:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131188467):
<p>Which means that the repo was deleted from github, I think</p>

#### [ Chris Hughes (Aug 09 2018 at 20:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131188476):
<p>I think I deleted my fork of mathlib at some point when I was frustratedly trying to learn how to use git.</p>

#### [ Kevin Buzzard (Aug 09 2018 at 20:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131188485):
<p>They don't teach mathematicians git :-(</p>

#### [ Johan Commelin (Aug 09 2018 at 20:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131188497):
<p>Chapter 0 in your book is about git, right?</p>

#### [ Mario Carneiro (Aug 09 2018 at 20:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131188499):
<p>I think those files should all be dumped in the community fork, and we can come back to it at some point</p>

#### [ Kevin Buzzard (Aug 09 2018 at 20:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131188500):
<p>I'm not competent to write it</p>

#### [ Johan Commelin (Aug 09 2018 at 20:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131188509):
<p>You could have a foreword by someone else... Mario for example</p>

#### [ Mario Carneiro (Aug 09 2018 at 20:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131188563):
<p>Step 1: <a href="http://git-scm.com" target="_blank" title="http://git-scm.com">git-scm.com</a>, step 2: profit</p>

#### [ Andrew Ashworth (Aug 09 2018 at 20:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131191018):
<p>Install sourcetree while you're at it</p>

#### [ Andrew Ashworth (Aug 09 2018 at 20:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131191048):
<p>Nobody has time to remember all the magic git invocations, so a gui wrapper really helps</p>

#### [ Patrick Massot (Aug 09 2018 at 23:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/teaching%20use%20of%20quotients%20in%20Lean/near/131197153):
<p>I used to believe that. So I advised computer afraid colleagues to use source tree and, after many rescuing operations, I realized command line is much simpler. Because you don't have to know about all commands and options that are not written in your git cheat sheet.</p>


{% endraw %}
