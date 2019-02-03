---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/116395maths/85554ZFCequality.html
---

## Stream: [maths](https://leanprover-community.github.io/archive/116395maths/index.html)
### Topic: [ZFC equality](https://leanprover-community.github.io/archive/116395maths/85554ZFCequality.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Kevin Buzzard (May 28 2018 at 11:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127197270):
<p>There were a couple of times in the schemes project when I really had to think "beyond ZFC" -- I had to write down a map, and there were two ways of doing it, and in ZFC they were the <em>literally the same way</em> but in Lean they were different. In this example I just chose a random Lean route to model my ZFC thoughts and it got me in to real trouble later.</p>

#### [ Kevin Buzzard (May 28 2018 at 11:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127197324):
<p>Here's a naive definition of the image of a morphism in ZFC, translated seamlessly into Lean:</p>

#### [ Kevin Buzzard (May 28 2018 at 11:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127197326):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">set</span>

<span class="c1">-- ZFC-safe! The below code uses only Prop and Type</span>

<span class="kn">variables</span> <span class="o">{</span><span class="n">X</span> <span class="n">Y</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">}</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">X</span> <span class="bp">→</span> <span class="n">Y</span><span class="o">)</span> <span class="o">(</span><span class="n">U</span> <span class="o">:</span> <span class="n">set</span> <span class="n">X</span><span class="o">)</span>

<span class="kn">definition</span> <span class="n">image</span> <span class="o">:=</span> <span class="o">{</span><span class="n">y</span> <span class="o">:</span> <span class="n">Y</span> <span class="bp">|</span> <span class="bp">∃</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">U</span><span class="o">,</span> <span class="n">f</span> <span class="n">x</span> <span class="bp">=</span> <span class="n">y</span><span class="o">}</span>
</pre></div>

#### [ Kevin Buzzard (May 28 2018 at 11:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127197328):
<p>And now here's something which doesn't work</p>

#### [ Kevin Buzzard (May 28 2018 at 11:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127197333):
<p><code>theorem they_are_not_defeq : image (@id X) U = U := rfl -- fails</code></p>

#### [ Kevin Buzzard (May 28 2018 at 11:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127197336):
<p>Does that mean that my definition of image is wrong?</p>

#### [ Kevin Buzzard (May 28 2018 at 11:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127197337):
<p>Or is there literally no way to make that happen in dependent type theory</p>

#### [ Kenny Lau (May 28 2018 at 11:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127197379):
<p>they are definitely not defeq</p>

#### [ Kenny Lau (May 28 2018 at 11:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127197384):
<p>you see, a set is nothing more than a function to Prop</p>

#### [ Kevin Buzzard (May 28 2018 at 11:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127197385):
<p>Is that because I am bad at writing the image function?</p>

#### [ Kevin Buzzard (May 28 2018 at 11:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127197386):
<p>Can you write a better one for me</p>

#### [ Kenny Lau (May 28 2018 at 11:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127197387):
<p>no, it isn't</p>

#### [ Kevin Buzzard (May 28 2018 at 11:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127197388):
<p>where they are defeq</p>

#### [ Kenny Lau (May 28 2018 at 11:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127197391):
<p>you can't</p>

#### [ Kenny Lau (May 28 2018 at 11:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127197392):
<p>you have to have an existential quantifier</p>

#### [ Kevin Buzzard (May 28 2018 at 11:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127197393):
<p>can you prove that you can't?</p>

#### [ Kevin Buzzard (May 28 2018 at 11:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127197395):
<p>in Lean</p>

#### [ Kevin Buzzard (May 28 2018 at 11:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127197396):
<p>3.4.1</p>

#### [ Mario Carneiro (May 28 2018 at 11:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127197403):
<p>not in lean</p>

#### [ Mario Carneiro (May 28 2018 at 11:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127197405):
<p>it's a metatheorem</p>

#### [ Kevin Buzzard (May 28 2018 at 11:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127197406):
<p>Great.</p>

#### [ Kenny Lau (May 28 2018 at 11:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127197408):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> can it actually be proved?</p>

#### [ Mario Carneiro (May 28 2018 at 11:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127197410):
<p>probably</p>

#### [ Kevin Buzzard (May 28 2018 at 11:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127197411):
<p>Well you know what</p>

#### [ Kevin Buzzard (May 28 2018 at 11:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127197413):
<p>I think defeq is rubbish</p>

#### [ Kevin Buzzard (May 28 2018 at 11:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127197414):
<p>because those two sets are <em>equal</em></p>

#### [ Kenny Lau (May 28 2018 at 11:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127197452):
<p>f(x) = x^2 and f(x) = x^2+1-1 are <em>equal</em></p>

#### [ Kevin Buzzard (May 28 2018 at 11:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127197453):
<p>and mathematicians have been thinking of those sets as <em>equal</em> since they started formalizing mathematics</p>

#### [ Kenny Lau (May 28 2018 at 11:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127197454):
<p>but not definitionally equal</p>

#### [ Kevin Buzzard (May 28 2018 at 11:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127197455):
<p>so what has gone wrong?</p>

#### [ Mario Carneiro (May 28 2018 at 11:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127197468):
<p>nothing is wrong</p>

#### [ Mario Carneiro (May 28 2018 at 11:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127197470):
<p>defeq is not ZFC equality</p>

#### [ Kevin Buzzard (May 28 2018 at 11:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127197471):
<p>Kenny -- the ZFC analogues of the two concepts <code>U</code> and <code>image id U</code> are <em>identical</em></p>

#### [ Kevin Buzzard (May 28 2018 at 11:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127197475):
<p>I mean equal in the purest form</p>

#### [ Kenny Lau (May 28 2018 at 11:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127197479):
<p>are they?</p>

#### [ Kevin Buzzard (May 28 2018 at 11:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127197480):
<p>they are indistinguishable with the tools of ZFC</p>

#### [ Mario Carneiro (May 28 2018 at 11:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127197481):
<p>no, there is more to prove under one definition than the other in ZFC</p>

#### [ Kenny Lau (May 28 2018 at 11:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127197482):
<p>the latter is <code>{ y in U | exists x, x = y }</code></p>

#### [ Kevin Buzzard (May 28 2018 at 11:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127197483):
<p>In ZFC they are the same object</p>

#### [ Mario Carneiro (May 28 2018 at 11:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127197484):
<p>in lean they are the same object</p>

#### [ Kenny Lau (May 28 2018 at 11:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127197485):
<p>sure, but they aren't equal by definition</p>

#### [ Kenny Lau (May 28 2018 at 11:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127197486):
<p>they are equivalent</p>

#### [ Kenny Lau (May 28 2018 at 11:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127197488):
<p><code>exists x, x = y</code> is equivalent to <code>true</code></p>

#### [ Kevin Buzzard (May 28 2018 at 11:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127197531):
<p>How is one supposed to prove that stupid lemma anyway?</p>

#### [ Mario Carneiro (May 28 2018 at 11:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127197535):
<p><code>ext (by simp)</code></p>

#### [ Mario Carneiro (May 28 2018 at 11:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127197539):
<p>I would guess</p>

#### [ Mario Carneiro (May 28 2018 at 11:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127197541):
<p>actually it's probably already a theorem</p>

#### [ Kevin Buzzard (May 28 2018 at 11:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127197552):
<div class="codehilite"><pre><span></span><span class="c1">-- What actually happens in my head when proving the lemma id(U) = U for sets in Lean.</span>

<span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">set</span>

<span class="c1">-- ZFC-safe! The below code uses only Prop and Type</span>
<span class="c1">-- (I didn&#39;t check the imports though)</span>
<span class="kn">variables</span> <span class="o">{</span><span class="n">X</span> <span class="n">Y</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">}</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">X</span> <span class="bp">→</span> <span class="n">Y</span><span class="o">)</span> <span class="o">(</span><span class="n">U</span> <span class="o">:</span> <span class="n">set</span> <span class="n">X</span><span class="o">)</span>

<span class="kn">definition</span> <span class="n">image</span> <span class="o">:=</span> <span class="o">{</span><span class="n">y</span> <span class="o">:</span> <span class="n">Y</span> <span class="bp">|</span> <span class="bp">∃</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">U</span><span class="o">,</span> <span class="n">f</span> <span class="n">x</span> <span class="bp">=</span> <span class="n">y</span><span class="o">}</span>

<span class="kn">theorem</span> <span class="n">are_they_equal</span> <span class="o">:</span> <span class="n">image</span> <span class="o">(</span><span class="bp">@</span><span class="n">id</span> <span class="n">X</span><span class="o">)</span> <span class="n">U</span> <span class="bp">=</span> <span class="n">U</span> <span class="o">:=</span> <span class="k">begin</span>
<span class="c">/-</span><span class="cm"></span>
<span class="cm">why am I wasting my time proving this stupid theorem. These</span>
<span class="cm">objects are ZFC-equal and thus equal. I will not even try.</span>
<span class="cm">-/</span>
<span class="c1">-- rfl, -- fails</span>
<span class="c1">-- simp, -- fails -- *rolls eyes*</span>
<span class="c1">-- finish, -- I don&#39;t even understand what this one does but it sometimes works</span>
<span class="c1">-- cc (see comment above)</span>
<span class="c1">-- dsimp -- thought unlikely but maybe worth trying</span>
<span class="c1">-- can&#39;t think of any more tactics</span>
<span class="n">unfold</span> <span class="n">image</span><span class="o">,</span>
<span class="n">apply</span> <span class="n">set</span><span class="bp">.</span><span class="n">eq_of_subset_of_subset</span><span class="o">,</span>
<span class="o">{</span> <span class="n">intros</span> <span class="n">x</span> <span class="n">Hx</span><span class="o">,</span>
  <span class="n">simpa</span> <span class="kn">using</span> <span class="n">Hx</span><span class="o">},</span>
<span class="o">{</span> <span class="n">intros</span> <span class="n">x</span> <span class="n">Hx</span><span class="o">,</span>
  <span class="n">simpa</span> <span class="kn">using</span> <span class="n">Hx</span><span class="o">,</span>
<span class="o">}</span>
<span class="c1">-- thank goodness it&#39;s over</span>
<span class="kn">end</span>
</pre></div>

#### [ Kevin Buzzard (May 28 2018 at 11:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127197553):
<p>That's what actually happened</p>

#### [ Mario Carneiro (May 28 2018 at 11:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127197555):
<p><code>set.image_id</code></p>

#### [ Mario Carneiro (May 28 2018 at 11:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127197559):
<p>why are you proving trivial set theorems?</p>

#### [ Kevin Buzzard (May 28 2018 at 11:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127197561):
<p>It's hard for me to prove that  ZFC-equal things are equal</p>

#### [ Kevin Buzzard (May 28 2018 at 11:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127197617):
<p>because the tools I have honed in my brain to solve these problems</p>

#### [ Kevin Buzzard (May 28 2018 at 11:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127197618):
<p>are ZFC tools</p>

#### [ Mario Carneiro (May 28 2018 at 11:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127197626):
<p>that theorem is just as hard in zfc land</p>

#### [ Kevin Buzzard (May 28 2018 at 11:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127197627):
<p>and here for some reason ZFC tools are not adequate</p>

#### [ Mario Carneiro (May 28 2018 at 11:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127197633):
<p>the proof is literally no different</p>

#### [ Kevin Buzzard (May 28 2018 at 11:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127197644):
<p>why does simp fail?</p>

#### [ Kevin Buzzard (May 28 2018 at 11:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127197646):
<p>This proof is simple</p>

#### [ Kenny Lau (May 28 2018 at 11:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127197647):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> I tell you, when a mathematician says they work in ZFC, they actually don't. They won't even be able to name all of the ZFC axioms.</p>

#### [ Kevin Buzzard (May 28 2018 at 11:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127197650):
<p>That's true for a general mathematician</p>

#### [ Mario Carneiro (May 28 2018 at 11:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127197654):
<p>I can tell you I have worked in ZFC</p>

#### [ Kevin Buzzard (May 28 2018 at 11:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127197656):
<p>but I know the axioms of ZFC and I've been working happily in it for years</p>

#### [ Mario Carneiro (May 28 2018 at 11:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127197657):
<p>like for real</p>

#### [ Kevin Buzzard (May 28 2018 at 11:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127197697):
<p>You mean "not using pen and paper"</p>

#### [ Kenny Lau (May 28 2018 at 11:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127197702):
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">(</span><span class="n">s</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="n">id</span> <span class="err">&#39;&#39;</span> <span class="n">s</span> <span class="bp">=</span> <span class="n">s</span> <span class="o">:=</span>
<span class="n">set</span><span class="bp">.</span><span class="n">ext</span> <span class="o">(</span><span class="k">by</span> <span class="n">simp</span> <span class="o">[</span><span class="bp">-</span><span class="n">set</span><span class="bp">.</span><span class="n">image_id</span><span class="o">])</span>
</pre></div>

#### [ Mario Carneiro (May 28 2018 at 11:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127197707):
<p>I've done ZFC with pen and paper too, but that gets old fast</p>

#### [ Kevin Buzzard (May 28 2018 at 11:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127197709):
<p>I guess LaTeX is the true home of ZFC.</p>

#### [ Kevin Buzzard (May 28 2018 at 11:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127197713):
<p>For most people.</p>

#### [ Andrew Ashworth (May 28 2018 at 11:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127197722):
<p>... isn't metamath basically zfc on pen and paper</p>

#### [ Kevin Buzzard (May 28 2018 at 11:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127197726):
<p>OK so I think dependent type theory is stupid and I've decided to go back to ZFC and formulate perfectoid spaces there instead where I don't have to waste my time worrying about whether or not id U is equal to U.</p>

#### [ Kevin Buzzard (May 28 2018 at 11:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127197727):
<p>So where do I start?</p>

#### [ Kevin Buzzard (May 28 2018 at 11:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127197767):
<p>if I want to do it on a computer</p>

#### [ Kenny Lau (May 28 2018 at 11:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127197771):
<p>I thought Isabelle works in ZFC</p>

#### [ Kevin Buzzard (May 28 2018 at 11:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127197773):
<p>I don't even know what Isabelle is</p>

#### [ Mario Carneiro (May 28 2018 at 11:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127197775):
<p>It uses HOL for all the good stuff</p>

#### [ Kevin Buzzard (May 28 2018 at 11:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127197778):
<p>so Isabelle-ZFC is a thing?</p>

#### [ Mario Carneiro (May 28 2018 at 11:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127197779):
<p>Isabelle/ZFC is more of a proof of concept</p>

#### [ Kevin Buzzard (May 28 2018 at 11:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127197780):
<p>that doesn't sound good</p>

#### [ Kevin Buzzard (May 28 2018 at 11:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127197782):
<p>does it have number fields?</p>

#### [ Kenny Lau (May 28 2018 at 11:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127197788):
<p>and secondly, nobody works in ZFC. they work in ZFC + definitorial expansion</p>

#### [ Mario Carneiro (May 28 2018 at 11:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127197791):
<p>If you want to really use ZFC on the computer, you should use Mizar or Metamath</p>

#### [ Kevin Buzzard (May 28 2018 at 11:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127197795):
<p>Why not Isabelle-ZFC?</p>

#### [ Mario Carneiro (May 28 2018 at 11:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127197798):
<p>because it is not mature enough</p>

#### [ Mario Carneiro (May 28 2018 at 11:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127197810):
<p>maybe mature is the wrong word, it's been around for a while but it doesn't have enough theorems</p>

#### [ Kevin Buzzard (May 28 2018 at 11:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127197811):
<p>Which of the three possibilities for computer-ZFC is most mathematician-friendly?</p>

#### [ Kevin Buzzard (May 28 2018 at 11:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127197852):
<p>Or is it a case of "learn one of them, you just learned all of them"</p>

#### [ Kevin Buzzard (May 28 2018 at 11:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127197857):
<p>I have no idea</p>

#### [ Kevin Buzzard (May 28 2018 at 11:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127197863):
<p>I just play ZFC internally on my own emulator</p>

#### [ Mario Carneiro (May 28 2018 at 11:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127197864):
<p>Mizar was written by mathematicians for mathematicians</p>

#### [ Mario Carneiro (May 28 2018 at 11:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127197866):
<p>this is not necessarily a good thing</p>

#### [ Kevin Buzzard (May 28 2018 at 11:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127197867):
<p>In ZFC</p>

#### [ Mario Carneiro (May 28 2018 at 11:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127197869):
<p>in TG set theory</p>

#### [ Kevin Buzzard (May 28 2018 at 11:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127197879):
<p>If ZFC and DTT had a race to perfectoid spaces, and you could choose your foundational system, and we started tomorrow, who would win?</p>

#### [ Mario Carneiro (May 28 2018 at 11:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127197883):
<p>ZFC is an axiom system not a program</p>

#### [ Kevin Buzzard (May 28 2018 at 11:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127197888):
<p>I am not CS-wise enough to understand the difference</p>

#### [ Kevin Buzzard (May 28 2018 at 11:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127197893):
<p>I want a program whose only commands are things allowed in ZFC</p>

#### [ Kevin Buzzard (May 28 2018 at 11:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127197895):
<p>and all things allowed in ZFC are commands</p>

#### [ Mario Carneiro (May 28 2018 at 11:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127197933):
<p>You aren't choosing ZFC or DTT, you're choosing Mizar or Lean or Coq or Isabelle</p>

#### [ Kevin Buzzard (May 28 2018 at 11:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127197939):
<p>Does this make sense -- "I choose Mizar, and therefore I choose ZFC"</p>

#### [ Mario Carneiro (May 28 2018 at 11:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127197941):
<p>sure</p>

#### [ Kevin Buzzard (May 28 2018 at 11:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127197942):
<p>I don't know what Mizar is</p>

#### [ Kevin Buzzard (May 28 2018 at 11:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127197946):
<p>but I do know what ZFC is</p>

#### [ Kevin Buzzard (May 28 2018 at 11:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127197951):
<p>And "I choose Lean, and therefore I choose dependent type theory"</p>

#### [ Mario Carneiro (May 28 2018 at 11:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127197959):
<p>right, lean doesn't give you a choice here</p>

#### [ Mario Carneiro (May 28 2018 at 11:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127197963):
<p>same with most other systems</p>

#### [ Kevin Buzzard (May 28 2018 at 11:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127197971):
<p>So who would win the perfectoid space showdown between Lean and "insert computer program which models ZFC in some way"</p>

#### [ Kevin Buzzard (May 28 2018 at 11:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198017):
<p>If I got cloned into two people and just had a race with myself</p>

#### [ Mario Carneiro (May 28 2018 at 11:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198018):
<p>Isabelle and Metamath are a bit special since they are foundational frameworks, so you can technically pick your favorite axiom system, but in practice all the theorems go to one particular axiom system</p>

#### [ Mario Carneiro (May 28 2018 at 11:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198031):
<p>If you got cloned? Lean of course</p>

#### [ Kevin Buzzard (May 28 2018 at 11:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198032):
<p>Are there more mathematical theorems in Mathlib than in any library for any ZFC system?</p>

#### [ Mario Carneiro (May 28 2018 at 11:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198036):
<p>because you know lean better than any other system</p>

#### [ Kevin Buzzard (May 28 2018 at 11:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198040):
<p>But Mario, I speak <em>fluent</em> ZFC</p>

#### [ Mario Carneiro (May 28 2018 at 11:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198049):
<p>and you will find that it doesn't matter</p>

#### [ Kevin Buzzard (May 28 2018 at 11:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198051):
<p>It's my native language</p>

#### [ Mario Carneiro (May 28 2018 at 11:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198055):
<p>because you will be struggling with formal details the whole way</p>

#### [ Mario Carneiro (May 28 2018 at 11:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198060):
<p>that's always the way it goes</p>

#### [ Kevin Buzzard (May 28 2018 at 11:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198063):
<p>I think this is precisely the point I don't understand</p>

#### [ Kevin Buzzard (May 28 2018 at 11:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198138):
<p>let me rephrase that -- the distinction between "Lean" and "Dependent type theory" is quite blurred in my mind</p>

#### [ Kevin Buzzard (May 28 2018 at 11:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198148):
<p>I thought I could just define dependent type theory to be Lean</p>

#### [ Kenny Lau (May 28 2018 at 11:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198151):
<p>it's one thing to know the theory behind Python</p>

#### [ Kenny Lau (May 28 2018 at 11:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198154):
<p>it's a completely other thing to use Python</p>

#### [ Kevin Buzzard (May 28 2018 at 11:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198158):
<p>I guess</p>

#### [ Kevin Buzzard (May 28 2018 at 11:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198160):
<p>I completely understand that</p>

#### [ Kevin Buzzard (May 28 2018 at 11:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198162):
<p>I see</p>

#### [ Kevin Buzzard (May 28 2018 at 11:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198205):
<p>But this is a really easy problem</p>

#### [ Kevin Buzzard (May 28 2018 at 11:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198206):
<p>I just get the CS people to write python for me</p>

#### [ Kevin Buzzard (May 28 2018 at 11:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198207):
<p>so they are the same thing</p>

#### [ Kevin Buzzard (May 28 2018 at 11:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198210):
<p>Now who wrote ZFC for me?</p>

#### [ Mario Carneiro (May 28 2018 at 11:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198214):
<p>but you don't want ZFC, not really</p>

#### [ Kevin Buzzard (May 28 2018 at 11:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198218):
<p>I love ZFC Mario</p>

#### [ Mario Carneiro (May 28 2018 at 11:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198219):
<p>you want by schoolkid and tactics and magic</p>

#### [ Kevin Buzzard (May 28 2018 at 11:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198223):
<p>Yeah and we _need_ schoolkid</p>

#### [ Mario Carneiro (May 28 2018 at 11:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198227):
<p>ZFC is an axiom system, it made no magical promises</p>

#### [ Kevin Buzzard (May 28 2018 at 11:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198230):
<p>no but you CS guys will just sort all that out</p>

#### [ Kevin Buzzard (May 28 2018 at 11:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198234):
<p>that's just some stupid engineering issue</p>

#### [ Kevin Buzzard (May 28 2018 at 11:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198237):
<p>I want to do ZFC, like I do Python in Python</p>

#### [ Mario Carneiro (May 28 2018 at 11:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198238):
<p>but it's a really important engineering issue for you</p>

#### [ Kenny Lau (May 28 2018 at 11:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198239):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> how would you prove in ZFC that <code>id '' U = U</code>?</p>

#### [ Mario Carneiro (May 28 2018 at 11:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198279):
<p>I dare say it's far more important than the underlying axiom system</p>

#### [ Kevin Buzzard (May 28 2018 at 11:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198286):
<p>id(u) is the same as u</p>

#### [ Kenny Lau (May 28 2018 at 11:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198290):
<p>no they aren't</p>

#### [ Kevin Buzzard (May 28 2018 at 11:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198292):
<p>sure it is</p>

#### [ Kenny Lau (May 28 2018 at 11:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198294):
<p>how would you prove it?</p>

#### [ Mario Carneiro (May 28 2018 at 11:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198295):
<p>that's not a proof</p>

#### [ Kevin Buzzard (May 28 2018 at 11:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198297):
<p>id is a big set of ordered pairs</p>

#### [ Kevin Buzzard (May 28 2018 at 11:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198301):
<p>and they're all just (u,u)</p>

#### [ Kenny Lau (May 28 2018 at 11:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198302):
<p>a proper class</p>

#### [ Kevin Buzzard (May 28 2018 at 11:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198303):
<p>no it's a set</p>

#### [ Kevin Buzzard (May 28 2018 at 11:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198307):
<p>don't be silly</p>

#### [ Mario Carneiro (May 28 2018 at 11:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198309):
<p>wha...</p>

#### [ Kenny Lau (May 28 2018 at 11:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198310):
<p>ok</p>

#### [ Kevin Buzzard (May 28 2018 at 11:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198312):
<p>it's a function from U to U</p>

#### [ Kenny Lau (May 28 2018 at 11:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198319):
<p>but here it isn't</p>

#### [ Mario Carneiro (May 28 2018 at 11:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198324):
<p>ZFC warning</p>

#### [ Kenny Lau (May 28 2018 at 11:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198325):
<p>it's a function from alpha to alpha, U is just a subset</p>

#### [ Kevin Buzzard (May 28 2018 at 11:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198326):
<p>but here is stupid. I'm telling you the right way.</p>

#### [ Mario Carneiro (May 28 2018 at 11:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198328):
<p>that's doing to make your job messy</p>

#### [ Kevin Buzzard (May 28 2018 at 11:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198329):
<p>so id(u) is <em>equal</em> to u OK</p>

#### [ Kevin Buzzard (May 28 2018 at 11:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198331):
<p>so {id(u) : u in U}</p>

#### [ Kevin Buzzard (May 28 2018 at 11:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198332):
<p>EQUALS</p>

#### [ Kevin Buzzard (May 28 2018 at 11:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198333):
<p>{u : u in U}</p>

#### [ Kevin Buzzard (May 28 2018 at 11:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198334):
<p>which</p>

#### [ Kenny Lau (May 28 2018 at 11:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198335):
<blockquote>
<p>so id(u) is <em>equal</em> to u OK</p>
</blockquote>
<p>you still haven't proved it. what after id being a big set of pairs</p>

#### [ Kevin Buzzard (May 28 2018 at 11:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198337):
<p>EQUALS</p>

#### [ Kevin Buzzard (May 28 2018 at 11:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198339):
<p>U</p>

#### [ Kevin Buzzard (May 28 2018 at 11:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198382):
<p>I don't understand which bit I missed</p>

#### [ Kenny Lau (May 28 2018 at 11:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198384):
<p>you're abusing notations.</p>

#### [ Kevin Buzzard (May 28 2018 at 11:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198385):
<p>oh</p>

#### [ Mario Carneiro (May 28 2018 at 11:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198389):
<p>yes, you unfold the definitions, that {id(u) : u in U} thing becomes {y : \ex u, id(u) = y}</p>

#### [ Kenny Lau (May 28 2018 at 11:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198390):
<p>{u : u in U} isn't equal to {u in U | true}</p>

#### [ Kevin Buzzard (May 28 2018 at 11:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198393):
<p>I thought I was using "=" as in the underlying logic or syntax or whatever it's called of ZFC or logic or</p>

#### [ Kenny Lau (May 28 2018 at 11:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198394):
<p>you mixed comprehension notation and subset notation</p>

#### [ Kevin Buzzard (May 28 2018 at 11:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198395):
<p>I am not clear about what = is in ZFC</p>

#### [ Kevin Buzzard (May 28 2018 at 11:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198396):
<p>I forgot the details</p>

#### [ Mario Carneiro (May 28 2018 at 11:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198397):
<p>and then you have a lemma proving that id(u) = u since (u,u) in id</p>

#### [ Kevin Buzzard (May 28 2018 at 11:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198400):
<p>but it just means they're the same object</p>

#### [ Kenny Lau (May 28 2018 at 11:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198401):
<p>by "isn't equal to" I mean "you haven't proved that they are equal"</p>

#### [ Mario Carneiro (May 28 2018 at 11:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198402):
<p>and id is a function because ...</p>

#### [ Kenny Lau (May 28 2018 at 11:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198407):
<blockquote>
<p>but it just means they're the same object</p>
</blockquote>
<p>but it needs to be proved</p>

#### [ Kenny Lau (May 28 2018 at 11:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198412):
<p>you can't just say "they must be equal"</p>

#### [ Kenny Lau (May 28 2018 at 11:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198415):
<p>you see, the problem is not in the axioms</p>

#### [ Kenny Lau (May 28 2018 at 11:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198416):
<p>but in the formality</p>

#### [ Mario Carneiro (May 28 2018 at 11:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198417):
<p>and then you get \ex u in U, u = y &lt;-&gt; u in U</p>

#### [ Mario Carneiro (May 28 2018 at 11:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198421):
<p>and hey presto it's the lean proof</p>

#### [ Kevin Buzzard (May 28 2018 at 11:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198425):
<p>But in the world where proofs are free and can be appealed to at will using good tactics, "simp" would prove this</p>

#### [ Kenny Lau (May 28 2018 at 12:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198428):
<p>right, so ZFC isn't the problem at all</p>

#### [ Mario Carneiro (May 28 2018 at 12:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198429):
<p>SIMP CAN PROVE THIS</p>

#### [ Kenny Lau (May 28 2018 at 12:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198470):
<p>yes</p>

#### [ Kevin Buzzard (May 28 2018 at 12:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198471):
<p>because my definition of "simp" is the ZFC tactic "this is simple if you use ZFC"</p>

#### [ Mario Carneiro (May 28 2018 at 12:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198481):
<p>That's not a tactic, that's magic</p>

#### [ Kevin Buzzard (May 28 2018 at 12:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198482):
<p>I think that's why my understanding of tactics is so poor</p>

#### [ Kenny Lau (May 28 2018 at 12:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198483):
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="bp">*</span><span class="o">}</span> <span class="o">(</span><span class="n">s</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span><span class="o">)</span> <span class="o">:</span> <span class="n">id</span> <span class="err">&#39;&#39;</span> <span class="n">s</span> <span class="bp">=</span> <span class="n">s</span> <span class="o">:=</span>
<span class="n">set</span><span class="bp">.</span><span class="n">ext</span> <span class="err">$</span> <span class="k">by</span> <span class="n">simp</span> <span class="o">[</span><span class="bp">-</span><span class="n">set</span><span class="bp">.</span><span class="n">image_id</span><span class="o">]</span>
</pre></div>

#### [ Kenny Lau (May 28 2018 at 12:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198484):
<p>simp <strong>can</strong> prove this</p>

#### [ Kevin Buzzard (May 28 2018 at 12:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198488):
<p>There are a whole bunch of distinct things in dependent type theory which I have truly identified in my head</p>

#### [ Kevin Buzzard (May 28 2018 at 12:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198490):
<p>and the big question is</p>

#### [ Kevin Buzzard (May 28 2018 at 12:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198497):
<p>is that going to give you problems down the line</p>

#### [ Kevin Buzzard (May 28 2018 at 12:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198499):
<p>by which I mean me</p>

#### [ Kevin Buzzard (May 28 2018 at 12:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198500):
<p>the ZFCist</p>

#### [ Kevin Buzzard (May 28 2018 at 12:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198505):
<p>I got lucky. I needed a map <code>F U -&gt; F (id '' U)</code></p>

#### [ Kevin Buzzard (May 28 2018 at 12:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198545):
<p>and I chose wrong. I proved <code>id '' U = U</code> and then did a rewrite and used id.</p>

#### [ Kevin Buzzard (May 28 2018 at 12:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198547):
<p>because they're the SAME OBJECT</p>

#### [ Kevin Buzzard (May 28 2018 at 12:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198552):
<p>and the identity map from an object to itself is called id.</p>

#### [ Mario Carneiro (May 28 2018 at 12:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198561):
<p>this is a better argument</p>

#### [ Kevin Buzzard (May 28 2018 at 12:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198565):
<p>So I used id and instantly got into all manner of trouble the moment I tried to prove things</p>

#### [ Kenny Lau (May 28 2018 at 12:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198567):
<p>1. you don't really work in pure ZFC. you work in ZFC + definitorial expansion + a whole bunch of other things</p>

#### [ Kenny Lau (May 28 2018 at 12:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198584):
<p>in ZFC <code>id '' U</code> isn't even defined</p>

#### [ Kenny Lau (May 28 2018 at 12:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198597):
<p>ZFC says that there exists such an object</p>

#### [ Mario Carneiro (May 28 2018 at 12:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198598):
<p>The dtt analogue of this is called equality reflection</p>

#### [ Kenny Lau (May 28 2018 at 12:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198611):
<p>you're using the axiom of replacement</p>

#### [ Kevin Buzzard (May 28 2018 at 12:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198615):
<p>And then I went back and thought "do you know what -- I could use res!"</p>

#### [ Mario Carneiro (May 28 2018 at 12:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198618):
<p>it says that if <code>x = y</code> then <code>x</code> and <code>y</code> are defeq</p>

#### [ Kenny Lau (May 28 2018 at 12:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198620):
<p>it begins <code>forall A exists B</code></p>

#### [ Kevin Buzzard (May 28 2018 at 12:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198623):
<p>And I thought "that's funny, because it's an <em>axiom of a functor</em> that res U U = id"</p>

#### [ Kenny Lau (May 28 2018 at 12:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198624):
<p>in ZFC everything is Prop</p>

#### [ Mario Carneiro (May 28 2018 at 12:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198626):
<p>This is needed to typecheck things like <code>id : F U -&gt; F (id '' U)</code></p>

#### [ Kevin Buzzard (May 28 2018 at 12:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198629):
<p>"so res is <em>the same as</em> id"</p>

#### [ Kevin Buzzard (May 28 2018 at 12:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198674):
<p>and I tried res</p>

#### [ Kevin Buzzard (May 28 2018 at 12:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198676):
<p>and then all my one page long goals were rfl</p>

#### [ Kevin Buzzard (May 28 2018 at 12:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198689):
<p>because I gave same ZFC answer in two different ways, the first arguably being "more natural for the ZFC-ist", and the second apparently being "more natural for the DTT-ist".</p>

#### [ Kevin Buzzard (May 28 2018 at 12:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198694):
<p>I don't understand why my id is the wrong idea.</p>

#### [ Patrick Massot (May 28 2018 at 12:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198695):
<p>Kevin, formalized maths will be crazy in any system. You can only hope automation will get better at hiding this crazyness. And it seems DTT is better that set theory in order to build automation</p>

#### [ Mario Carneiro (May 28 2018 at 12:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198697):
<p>You can use <code>id</code> like you did, but you need a lemma about it</p>

#### [ Kevin Buzzard (May 28 2018 at 12:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198699):
<p>I cannot envisage a single problem doing this in ZFC</p>

#### [ Kevin Buzzard (May 28 2018 at 12:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198743):
<p>The issue is making a computer assert this statement?</p>

#### [ Mario Carneiro (May 28 2018 at 12:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198744):
<p>this would be WAY harder in metamath because of all the dependencies</p>

#### [ Kenny Lau (May 28 2018 at 12:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198746):
<blockquote>
<p>I cannot envisage a single problem doing this in ZFC</p>
</blockquote>
<p>no, you would need as many lemmas</p>

#### [ Kevin Buzzard (May 28 2018 at 12:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198747):
<p>is metamath ZFC?</p>

#### [ Kenny Lau (May 28 2018 at 12:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198748):
<p>ZFC / DTT is not the issue at all</p>

#### [ Mario Carneiro (May 28 2018 at 12:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198749):
<p>lean is good at hiding complexity, which is not always a good thing</p>

#### [ Kevin Buzzard (May 28 2018 at 12:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198757):
<p>I should do a proper survey.</p>

#### [ Mario Carneiro (May 28 2018 at 12:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198758):
<p>on the one hand it means you can formalize much bigger statements, on the other it means you don't work as much on parsimony and as a result have to struggle with large goals</p>

#### [ Kevin Buzzard (May 28 2018 at 12:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198759):
<p>Do I have a complete list of "computer programs which help you do ZFC"?</p>

#### [ Mario Carneiro (May 28 2018 at 12:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198798):
<p>Of course lean is on that list</p>

#### [ Kevin Buzzard (May 28 2018 at 12:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198806):
<p><span class="user-mention" data-user-id="110064">@Kenny Lau</span> No! Simp didn't prove it! You had to write some .set.image gobble-de-gook theorem as well which probably also says "two identical things are equal"</p>

#### [ Kenny Lau (May 28 2018 at 12:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198810):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> no, I had to write <code>-set.image_id</code> to show that it isn't automated</p>

#### [ Kenny Lau (May 28 2018 at 12:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198811):
<p>because <code>set.image_id</code> is the theorem</p>

#### [ Mario Carneiro (May 28 2018 at 12:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198812):
<p>the set_image thing is just to avoid an even more trivial proof</p>

#### [ Kevin Buzzard (May 28 2018 at 12:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198814):
<p>If simp worked properly, it would solve that goal</p>

#### [ Kevin Buzzard (May 28 2018 at 12:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198815):
<p>just by simp</p>

#### [ Kevin Buzzard (May 28 2018 at 12:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198817):
<p>because it's simple</p>

#### [ Kenny Lau (May 28 2018 at 12:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198818):
<p>Kevin.</p>

#### [ Kenny Lau (May 28 2018 at 12:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198819):
<p>it's a minus.</p>

#### [ Kenny Lau (May 28 2018 at 12:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198820):
<p>I'm telling <code>simp</code> not to use that theorem.</p>

#### [ Kevin Buzzard (May 28 2018 at 12:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198821):
<p>I know</p>

#### [ Kenny Lau (May 28 2018 at 12:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198861):
<p>because otherwise the proof would be trivial</p>

#### [ Mario Carneiro (May 28 2018 at 12:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198863):
<p>just <code>by simp</code> does prove that theorem</p>

#### [ Mario Carneiro (May 28 2018 at 12:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198866):
<p>because it's a simp lemma</p>

#### [ Mario Carneiro (May 28 2018 at 12:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198868):
<p>and without the theorem, the proof is <code>ext $ by simp</code></p>

#### [ Kevin Buzzard (May 28 2018 at 12:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198869):
<div class="codehilite"><pre><span></span><span class="n">Tactic</span> <span class="n">State</span>

<span class="n">X</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">,</span>
<span class="n">U</span> <span class="o">:</span> <span class="n">set</span> <span class="n">X</span>
<span class="err">⊢</span> <span class="n">image</span> <span class="n">id</span> <span class="n">U</span> <span class="bp">=</span> <span class="n">U</span>
<span class="n">id_U_equals_U</span><span class="bp">.</span><span class="n">lean</span><span class="o">:</span><span class="mi">11</span><span class="o">:</span><span class="mi">51</span><span class="o">:</span> <span class="n">error</span>

<span class="n">simplify</span> <span class="n">tactic</span> <span class="n">failed</span> <span class="n">to</span> <span class="n">simplify</span>
<span class="n">state</span><span class="o">:</span>
<span class="n">X</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">,</span>
<span class="n">U</span> <span class="o">:</span> <span class="n">set</span> <span class="n">X</span>
<span class="err">⊢</span> <span class="n">image</span> <span class="n">id</span> <span class="n">U</span> <span class="bp">=</span> <span class="n">U</span>
</pre></div>

#### [ Kevin Buzzard (May 28 2018 at 12:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198872):
<p>"by simp" doesn't solve it so "by simp" is broken</p>

#### [ Kevin Buzzard (May 28 2018 at 12:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198873):
<p>because it's simple</p>

#### [ Kevin Buzzard (May 28 2018 at 12:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198874):
<p>that's all I'm saying</p>

#### [ Mario Carneiro (May 28 2018 at 12:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198875):
<p>you defined your own image</p>

#### [ Mario Carneiro (May 28 2018 at 12:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198878):
<p>it has no simp lemmas like the real one</p>

#### [ Kevin Buzzard (May 28 2018 at 12:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198883):
<p>you guys are just weirdos</p>

#### [ Kenny Lau (May 28 2018 at 12:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198885):
<p>Kevin</p>

#### [ Mario Carneiro (May 28 2018 at 12:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198887):
<p>It's like you shot me in the leg and asked why I can't run as fast</p>

#### [ Kenny Lau (May 28 2018 at 12:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198889):
<p>have we established that in ZFC you still need to prove it</p>

#### [ Kevin Buzzard (May 28 2018 at 12:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198890):
<p>Maybe it's time I tried Mizar.</p>

#### [ Kevin Buzzard (May 28 2018 at 12:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198892):
<p>I'll come back with egg on my face later</p>

#### [ Kenny Lau (May 28 2018 at 12:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198929):
<p>I don't really see the issue</p>

#### [ Kenny Lau (May 28 2018 at 12:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198932):
<p>I think you're misunderstanding</p>

#### [ Kenny Lau (May 28 2018 at 12:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198933):
<p>you said it's stupid because they aren't defeq</p>

#### [ Kevin Buzzard (May 28 2018 at 12:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198935):
<p>if it's not by simp for some reason</p>

#### [ Mario Carneiro (May 28 2018 at 12:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198936):
<p>simp requires a whole library of carefully crafted lemmas to work well</p>

#### [ Kevin Buzzard (May 28 2018 at 12:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198937):
<p>then it should be by schoolkid</p>

#### [ Mario Carneiro (May 28 2018 at 12:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198938):
<p>because it's not magic</p>

#### [ Kevin Buzzard (May 28 2018 at 12:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198940):
<p>How can you claim it works well</p>

#### [ Kevin Buzzard (May 28 2018 at 12:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198942):
<p>if it cannot even prove id(U)=U</p>

#### [ Kevin Buzzard (May 28 2018 at 12:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198945):
<p>when they're the same object</p>

#### [ Kevin Buzzard (May 28 2018 at 12:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198950):
<p>That's what I'm hearing :-)</p>

#### [ Mario Carneiro (May 28 2018 at 12:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198951):
<p>you are being unusually stubborn today</p>

#### [ Kenny Lau (May 28 2018 at 12:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198952):
<p>1. you said Lean is stupid because <code>id '' U = U</code> isn't <code>rfl</code>. But they also aren't rfl in ZFC, you also need to prove it (remember how you mixed comprehension notation and subset notation)</p>

#### [ Kevin Buzzard (May 28 2018 at 12:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198956):
<p>and I know it's not what you're saying</p>

#### [ Kevin Buzzard (May 28 2018 at 12:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198957):
<p>but I'm a bit deaf</p>

#### [ Kenny Lau (May 28 2018 at 12:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198958):
<p>2. you said Lean is stupid because <code>id '' U = u</code> isn't <code>by simp</code>. But it is.</p>

#### [ Kevin Buzzard (May 28 2018 at 12:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198959):
<p>I was just doing my ZFC-baiting thing</p>

#### [ Kenny Lau (May 28 2018 at 12:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198960):
<p>3. you said Lean is stupid because <code>id '' U = U</code> isn't <code>ext $ by simp</code>. But it is.</p>

#### [ Kenny Lau (May 28 2018 at 12:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127198961):
<p>so I don't know what your issue is</p>

#### [ Kevin Buzzard (May 28 2018 at 12:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199000):
<p>by simp doesn't work for me</p>

#### [ Kevin Buzzard (May 28 2018 at 12:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199002):
<p>does it work for you?</p>

#### [ Kenny Lau (May 28 2018 at 12:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199004):
<p>because you're using the wrong image</p>

#### [ Kevin Buzzard (May 28 2018 at 12:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199006):
<p>I'm using the image I wrote</p>

#### [ Kenny Lau (May 28 2018 at 12:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199007):
<p>use the official image and everything will be fine</p>

#### [ Kenny Lau (May 28 2018 at 12:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199011):
<p>of course your new image doesn't have simp lemmas</p>

#### [ Kevin Buzzard (May 28 2018 at 12:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199012):
<p>Wait so didn't lots of people tell me that this was impossible or something?</p>

#### [ Kenny Lau (May 28 2018 at 12:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199016):
<p>4. you said Lean is stupid because <code>simp</code> doesn't simplify it with your <strong>new</strong> image definition. But we already established that it is not a rfl theorem, so you have to use the official image if you want to use a simp lemma</p>

#### [ Kevin Buzzard (May 28 2018 at 12:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199027):
<p>that's stupid. What if I can't find the official image so I just make my own image which would then be identical so all the old theorems would work anyway</p>

#### [ Kevin Buzzard (May 28 2018 at 12:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199028):
<p>hmm</p>

#### [ Mario Carneiro (May 28 2018 at 12:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199030):
<p>no</p>

#### [ Kevin Buzzard (May 28 2018 at 12:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199032):
<p>OK so</p>

#### [ Kevin Buzzard (May 28 2018 at 12:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199063):
<p>I can see there might be issues here</p>

#### [ Kenny Lau (May 28 2018 at 12:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199071):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> read my point 4 again</p>

#### [ Kevin Buzzard (May 28 2018 at 12:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199072):
<p>at least</p>

#### [ Kevin Buzzard (May 28 2018 at 12:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199075):
<p>from an engineering point of view</p>

#### [ Mario Carneiro (May 28 2018 at 12:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199079):
<p>the theorems only "work" if you apply them</p>

#### [ Kenny Lau (May 28 2018 at 12:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199081):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> it doesn't work</p>

#### [ Kevin Buzzard (May 28 2018 at 12:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199082):
<p>No</p>

#### [ Kevin Buzzard (May 28 2018 at 12:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199083):
<p>I'm listening</p>

#### [ Mario Carneiro (May 28 2018 at 12:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199084):
<p>yeah, I messed up the copy there</p>

#### [ Kevin Buzzard (May 28 2018 at 12:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199090):
<p>I understand that I have to apply my theorems</p>

#### [ Kenny Lau (May 28 2018 at 12:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199091):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> so I don't really see where the issue is.</p>

#### [ Kevin Buzzard (May 28 2018 at 12:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199093):
<p>but in return</p>

#### [ Kevin Buzzard (May 28 2018 at 12:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199095):
<p>here's the thing</p>

#### [ Kenny Lau (May 28 2018 at 12:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199098):
<p>you're complaining that <code>simp</code> doesn't know about your new <code>image</code></p>

#### [ Johan Commelin (May 28 2018 at 12:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199099):
<p>Kevin, don't think of <code>simp</code> as "simple", but as "simplify"</p>

#### [ Kevin Buzzard (May 28 2018 at 12:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199100):
<p>when I prove a theorem that says that A and B are equal</p>

#### [ Kevin Buzzard (May 28 2018 at 12:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199101):
<p>in DTT speak</p>

#### [ Kevin Buzzard (May 28 2018 at 12:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199143):
<p><code>theorem they_are_equal : X = Y := by schoolkid</code></p>

#### [ Johan Commelin (May 28 2018 at 12:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199144):
<p>So, it's not <code>simp</code>'s purpose to prove it. But <code>schoolkid</code> or <code>math_trivial</code> should be able to prove it</p>

#### [ Kevin Buzzard (May 28 2018 at 12:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199146):
<p>Whenever that happens in dependent type theory</p>

#### [ Kenny Lau (May 28 2018 at 12:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199147):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> Kevin.</p>

#### [ Kevin Buzzard (May 28 2018 at 12:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199148):
<p>I want dependent type theory to now collapse a little</p>

#### [ Kenny Lau (May 28 2018 at 12:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199149):
<p>I think this will convince you.</p>

#### [ Kenny Lau (May 28 2018 at 12:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199150):
<div class="codehilite"><pre><span></span><span class="kn">definition</span> <span class="n">image</span> <span class="o">:=</span> <span class="o">{</span><span class="n">y</span> <span class="o">:</span> <span class="n">Y</span> <span class="bp">|</span> <span class="bp">∃</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">U</span><span class="o">,</span> <span class="n">f</span> <span class="n">x</span> <span class="bp">=</span> <span class="n">y</span><span class="o">}</span>
<span class="kn">example</span> <span class="o">:</span> <span class="n">image</span> <span class="o">(</span><span class="bp">@</span><span class="n">id</span> <span class="n">X</span><span class="o">)</span> <span class="n">U</span> <span class="bp">=</span> <span class="n">U</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">simp</span> <span class="o">[</span><span class="n">image</span><span class="o">]</span>
</pre></div>

#### [ Mario Carneiro (May 28 2018 at 12:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199214):
<p>I think you are focusing on the wrong issue Kevin</p>

#### [ Kenny Lau (May 28 2018 at 12:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199217):
<p>you broke the silence &gt;_&gt;</p>

#### [ Johan Commelin (May 28 2018 at 12:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199218):
<p>So we want <code>schoolkid_1</code> which just does <code>simp [..every definition preceding it in the file..]</code></p>

#### [ Mario Carneiro (May 28 2018 at 12:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199231):
<p>There is nothing at all wrong with the proof of id '' U = U, but it caused problems later when you used it as a functor in your presheaf</p>

#### [ Mario Carneiro (May 28 2018 at 12:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199275):
<p>For that you need theorems about the action of <code>eq.rec</code> or <code>cast</code></p>

#### [ Kevin Buzzard (May 28 2018 at 12:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199279):
<p>Is this supposed to be rfl?</p>

#### [ Mario Carneiro (May 28 2018 at 12:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199280):
<p>and they aren't free, you have to state them</p>

#### [ Kevin Buzzard (May 28 2018 at 12:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199282):
<p><code>theorem X : id '' U = U := sorry </code></p>

#### [ Kenny Lau (May 28 2018 at 12:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199285):
<blockquote>
<p>Is this supposed to be rfl?</p>
</blockquote>
<p>I thought we already established that it is not rfl</p>

#### [ Kenny Lau (May 28 2018 at 12:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199286):
<p>not in ZFC either</p>

#### [ Kevin Buzzard (May 28 2018 at 12:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199287):
<p>So that is not rfl</p>

#### [ Kevin Buzzard (May 28 2018 at 12:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199288):
<p>but what was rfl?</p>

#### [ Kenny Lau (May 28 2018 at 12:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199290):
<p>rfl is using "forall x, x = x"</p>

#### [ Mario Carneiro (May 28 2018 at 12:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199292):
<p><code>schoolkid_1</code> is <code>simp!</code></p>

#### [ Kenny Lau (May 28 2018 at 12:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199299):
<p>so in ZFC, you need to do reductions to simplify them to the same expression, and then use that axiom</p>

#### [ Kenny Lau (May 28 2018 at 12:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199301):
<p>but they can't be reduced to the same thing</p>

#### [ Mario Carneiro (May 28 2018 at 12:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199302):
<p>ZFC has no reductions at all</p>

#### [ Kenny Lau (May 28 2018 at 12:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199304):
<blockquote>
<p><code>schoolkid_1</code> is <code>simp!</code></p>
</blockquote>
<p>nope, doesn't work</p>

#### [ Mario Carneiro (May 28 2018 at 12:23)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199310):
<p>In fact rfl is much weaker in ZFC</p>

#### [ Kenny Lau (May 28 2018 at 12:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199346):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> you aren't working in ZFC. you are working in ZFC + definition expansion + delta reduction</p>

#### [ Kevin Buzzard (May 28 2018 at 12:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199349):
<p>Mario quote</p>
<div class="codehilite"><pre><span></span>import data.set

-- ZFC-safe! The below code uses only Prop and Type

variables {X Y : Type} (f : X → Y) (U : set X)

theorem they_are_not_defeq : image (@id X) U = U := rfl -- works
</pre></div>


<p>Doesn't work for me</p>

#### [ Mario Carneiro (May 28 2018 at 12:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199355):
<p><code>+</code> equality reflection</p>

#### [ Kevin Buzzard (May 28 2018 at 12:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199361):
<p><code>unknown identifier 'image'</code></p>

#### [ Kenny Lau (May 28 2018 at 12:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199362):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> I really do not see any problem at all. <code>id '' U</code> does not expand to <code>U</code>. you have to destruct the definitions and <strong>use extensionality</strong></p>

#### [ Mario Carneiro (May 28 2018 at 12:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199365):
<p>I didn't say that</p>

#### [ Kenny Lau (May 28 2018 at 12:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199367):
<p>that's what I mean</p>

#### [ Kevin Buzzard (May 28 2018 at 12:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199373):
<p>I am just trying to get to the bottom of things</p>

#### [ Kevin Buzzard (May 28 2018 at 12:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199374):
<p>but I have never seen refl work for anything</p>

#### [ Kenny Lau (May 28 2018 at 12:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199377):
<p>if you need to <strong>use the axiom of extensionality</strong> to prove that they are equal, then they aren't definitionally equal</p>

#### [ Kevin Buzzard (May 28 2018 at 12:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199378):
<p>and I've never seen by simp work either</p>

#### [ Kenny Lau (May 28 2018 at 12:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199380):
<p>and i'm working in ZFC to say that</p>

#### [ Kevin Buzzard (May 28 2018 at 12:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199381):
<p>but I'm just trying to put everything together</p>

#### [ Kevin Buzzard (May 28 2018 at 12:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199384):
<p>it's hard trying to distinguish between equal things</p>

#### [ Mario Carneiro (May 28 2018 at 12:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199440):
<p>It's not so hard: <code>id '' U</code> has more words than <code>U</code>, so they aren't the same</p>

#### [ Mario Carneiro (May 28 2018 at 12:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199502):
<p>Here's an example of <code>rfl</code> working:</p>
<div class="codehilite"><pre><span></span>definition image := {y : Y | ∃ x ∈ U, y = f x}

example : image (@id X) U = {y | ∃ x ∈ U, y = x} := rfl
</pre></div>

#### [ Mario Carneiro (May 28 2018 at 12:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199506):
<p>that's how definitional expansion is supposed to work</p>

#### [ Mario Carneiro (May 28 2018 at 12:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199512):
<p>this is what ZFC gives you (except you would have to work on id(x) = x in the middle there, that's not definitional in ZFC)</p>

#### [ Kenny Lau (May 28 2018 at 12:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199516):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> here's how I can formalize what I say: if you didn't have <code>propext</code> as an axiom, then you won't be able to prove that the two sets are equal, in Lean</p>

#### [ Kenny Lau (May 28 2018 at 12:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199557):
<p>the ZFC version replaces <code>propext</code> with the axiom of extensionality</p>

#### [ Kevin Buzzard (May 28 2018 at 12:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199573):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">set</span>

<span class="c1">-- ZFC-safe! The below code uses only Prop and Type</span>

<span class="kn">variables</span> <span class="o">{</span><span class="n">X</span> <span class="n">Y</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">}</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">X</span> <span class="bp">→</span> <span class="n">Y</span><span class="o">)</span> <span class="o">(</span><span class="n">U</span> <span class="o">:</span> <span class="n">set</span> <span class="n">X</span><span class="o">)</span>

<span class="kn">definition</span> <span class="n">image&#39;</span> <span class="o">:=</span> <span class="o">{</span><span class="n">y</span> <span class="o">:</span> <span class="n">Y</span> <span class="bp">|</span> <span class="bp">∃</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">U</span><span class="o">,</span> <span class="n">f</span> <span class="n">x</span> <span class="bp">=</span> <span class="n">y</span><span class="o">}</span>

<span class="kn">theorem</span> <span class="n">they_are_the_same</span> <span class="o">:</span> <span class="n">image&#39;</span> <span class="o">(</span><span class="bp">@</span><span class="n">id</span> <span class="n">X</span><span class="o">)</span> <span class="n">U</span> <span class="bp">=</span> <span class="n">U</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">refl</span> <span class="c1">-- fails</span>
<span class="kn">theorem</span> <span class="n">they_are_the_same&#39;</span> <span class="o">:</span> <span class="n">id</span> <span class="err">&#39;&#39;</span> <span class="n">U</span> <span class="bp">=</span> <span class="n">U</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">refl</span> <span class="c1">-- fails</span>
<span class="kn">theorem</span> <span class="n">they_are_all_the_same_thing_</span> <span class="o">:</span> <span class="n">id</span> <span class="err">&#39;&#39;</span> <span class="n">U</span> <span class="bp">=</span> <span class="n">image&#39;</span> <span class="o">(</span><span class="bp">@</span><span class="n">id</span> <span class="n">X</span><span class="o">)</span> <span class="n">U</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">refl</span> <span class="c1">-- fails</span>
<span class="kn">theorem</span> <span class="n">but_they_are_all_the_same</span> <span class="o">:</span> <span class="n">set</span><span class="bp">.</span><span class="n">image</span> <span class="o">(</span><span class="bp">@</span><span class="n">id</span> <span class="n">X</span><span class="o">)</span> <span class="n">U</span> <span class="bp">=</span> <span class="n">U</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">refl</span> <span class="c1">-- fails</span>
<span class="kn">theorem</span> <span class="n">why_are_they_all_different</span> <span class="o">:</span> <span class="n">id</span> <span class="err">&#39;&#39;</span> <span class="n">U</span> <span class="bp">=</span> <span class="n">set</span><span class="bp">.</span><span class="n">image</span> <span class="o">(</span><span class="bp">@</span><span class="n">id</span> <span class="n">X</span><span class="o">)</span> <span class="n">U</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">refl</span> <span class="c1">-- thank god</span>
</pre></div>

#### [ Kevin Buzzard (May 28 2018 at 12:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199574):
<p>:-(</p>

#### [ Kevin Buzzard (May 28 2018 at 12:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199585):
<p>They are the same -- you just have the wrong equivalence relation</p>

#### [ Kenny Lau (May 28 2018 at 12:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199588):
<p>I've been repeating the same thing 100 times.</p>

#### [ Mario Carneiro (May 28 2018 at 12:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199627):
<p><code>set.image</code> is defined as <code>{y : Y | ∃ x, x ∈ U ∧ f x = y}</code></p>

#### [ Kevin Buzzard (May 28 2018 at 12:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199633):
<blockquote>
<p>I've been repeating the same thing 100 times.</p>
</blockquote>
<p>I know but you didn't fix it yet</p>

#### [ Kevin Buzzard (May 28 2018 at 12:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199634):
<p>all the proofs are "by schoolkid"</p>

#### [ Kevin Buzzard (May 28 2018 at 12:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199636):
<p>Kenny do you want to do that for your 1st year project?</p>

#### [ Kenny Lau (May 28 2018 at 12:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199637):
<blockquote>
<div class="codehilite"><pre><span></span><span class="kn">definition</span> <span class="n">image</span> <span class="o">:=</span> <span class="o">{</span><span class="n">y</span> <span class="o">:</span> <span class="n">Y</span> <span class="bp">|</span> <span class="bp">∃</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">U</span><span class="o">,</span> <span class="n">f</span> <span class="n">x</span> <span class="bp">=</span> <span class="n">y</span><span class="o">}</span>
<span class="kn">example</span> <span class="o">:</span> <span class="n">image</span> <span class="o">(</span><span class="bp">@</span><span class="n">id</span> <span class="n">X</span><span class="o">)</span> <span class="n">U</span> <span class="bp">=</span> <span class="n">U</span> <span class="o">:=</span>
<span class="k">by</span> <span class="n">simp</span> <span class="o">[</span><span class="n">image</span><span class="o">]</span>
</pre></div>


</blockquote>

#### [ Kenny Lau (May 28 2018 at 12:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199638):
<p>you must be blind</p>

#### [ Kevin Buzzard (May 28 2018 at 12:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199643):
<p>but it never just says "by simp"</p>

#### [ Kevin Buzzard (May 28 2018 at 12:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199648):
<p>which ones get done by simp</p>

#### [ Mario Carneiro (May 28 2018 at 12:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199649):
<p>no because that would be horrible in most proofs</p>

#### [ Kenny Lau (May 28 2018 at 12:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199651):
<p>Kevin, you don't want <code>by simp</code> to automatically unfold every definition for you.</p>

#### [ Kevin Buzzard (May 28 2018 at 12:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199692):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">set</span>

<span class="c1">-- ZFC-safe! The below code uses only Prop and Type</span>

<span class="kn">variables</span> <span class="o">{</span><span class="n">X</span> <span class="n">Y</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">}</span> <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">X</span> <span class="bp">→</span> <span class="n">Y</span><span class="o">)</span> <span class="o">(</span><span class="n">U</span> <span class="o">:</span> <span class="n">set</span> <span class="n">X</span><span class="o">)</span>

<span class="kn">definition</span> <span class="n">image&#39;</span> <span class="o">:=</span> <span class="o">{</span><span class="n">y</span> <span class="o">:</span> <span class="n">Y</span> <span class="bp">|</span> <span class="bp">∃</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">U</span><span class="o">,</span> <span class="n">f</span> <span class="n">x</span> <span class="bp">=</span> <span class="n">y</span><span class="o">}</span>

<span class="kn">theorem</span> <span class="n">they_are_the_same</span> <span class="o">:</span> <span class="n">image&#39;</span> <span class="o">(</span><span class="bp">@</span><span class="n">id</span> <span class="n">X</span><span class="o">)</span> <span class="n">U</span> <span class="bp">=</span> <span class="n">U</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">simp</span> <span class="c1">-- fails</span>
<span class="kn">theorem</span> <span class="n">they_are_the_same&#39;</span> <span class="o">:</span> <span class="n">id</span> <span class="err">&#39;&#39;</span> <span class="n">U</span> <span class="bp">=</span> <span class="n">U</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">simp</span> <span class="c1">-- fails</span>
<span class="kn">theorem</span> <span class="n">they_are_all_the_same_thing_</span> <span class="o">:</span> <span class="n">id</span> <span class="err">&#39;&#39;</span> <span class="n">U</span> <span class="bp">=</span> <span class="n">image&#39;</span> <span class="o">(</span><span class="bp">@</span><span class="n">id</span> <span class="n">X</span><span class="o">)</span> <span class="n">U</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">simp</span> <span class="c1">-- fails</span>
<span class="kn">theorem</span> <span class="n">but_they_are_all_the_same</span> <span class="o">:</span> <span class="n">set</span><span class="bp">.</span><span class="n">image</span> <span class="o">(</span><span class="bp">@</span><span class="n">id</span> <span class="n">X</span><span class="o">)</span> <span class="n">U</span> <span class="bp">=</span> <span class="n">U</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">simp</span> <span class="c1">-- fails</span>
<span class="kn">theorem</span> <span class="n">why_are_they_all_different</span> <span class="o">:</span> <span class="n">id</span> <span class="err">&#39;&#39;</span> <span class="n">U</span> <span class="bp">=</span> <span class="n">set</span><span class="bp">.</span><span class="n">image</span> <span class="o">(</span><span class="bp">@</span><span class="n">id</span> <span class="n">X</span><span class="o">)</span> <span class="n">U</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">simp</span> <span class="c1">-- I wasn&#39;t 100% confident but we got through</span>
</pre></div>

#### [ Kevin Buzzard (May 28 2018 at 12:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199695):
<p>Why do I have to work, or even <em>think</em>, about proving that two objects are the same, when they are the same object?</p>

#### [ Kenny Lau (May 28 2018 at 12:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199696):
<p>here we go again</p>

#### [ Kevin Buzzard (May 28 2018 at 12:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199697):
<p>Why doesn't it do it for me?</p>

#### [ Kevin Buzzard (May 28 2018 at 12:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199699):
<p>That's what I want</p>

#### [ Kevin Buzzard (May 28 2018 at 12:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199700):
<p>Make it do it for me</p>

#### [ Kevin Buzzard (May 28 2018 at 12:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199701):
<p>simp is rubbish</p>

#### [ Kevin Buzzard (May 28 2018 at 12:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199703):
<p>make a proper one</p>

#### [ Kenny Lau (May 28 2018 at 12:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199704):
<p>do we have to go through the ZFC proof that they are the same again?</p>

#### [ Kevin Buzzard (May 28 2018 at 12:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199705):
<p>make schoolkid</p>

#### [ Mario Carneiro (May 28 2018 at 12:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199710):
<p>Stop trolling Kevin</p>

#### [ Kevin Buzzard (May 28 2018 at 12:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199713):
<p>I don't understand why this can't be done</p>

#### [ Kenny Lau (May 28 2018 at 12:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199715):
<p>I already explained 100 times</p>

#### [ Kevin Buzzard (May 28 2018 at 12:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199716):
<p>Why can my brain do it?</p>

#### [ Kevin Buzzard (May 28 2018 at 12:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199717):
<p>Aren't I just a computer?</p>

#### [ Kenny Lau (May 28 2018 at 12:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199718):
<p>because your brain knows when to expand a definition and when not to</p>

#### [ Kevin Buzzard (May 28 2018 at 12:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199763):
<p>I think Lean can also decide when to expand a definition and when not to</p>

#### [ Kenny Lau (May 28 2018 at 12:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199765):
<p>how?</p>

#### [ Kevin Buzzard (May 28 2018 at 12:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199768):
<p>I don't get what I'm so good at that Lean can't do</p>

#### [ Kenny Lau (May 28 2018 at 12:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199769):
<p>with 10 definitions that is 1024 choices</p>

#### [ Kenny Lau (May 28 2018 at 12:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199771):
<p>humans are good at small things</p>

#### [ Kenny Lau (May 28 2018 at 12:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199773):
<p>humans don't have the guarantee that their algorithm works in every case</p>

#### [ Kevin Buzzard (May 28 2018 at 12:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199775):
<p>I guess here's a good analogue.</p>

#### [ Kevin Buzzard (May 28 2018 at 12:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199784):
<p>"OK so I'm quite good at go. Why don't you CS guys quickly knock up something that's as good as me at go and then I can retire"</p>

#### [ Kenny Lau (May 28 2018 at 12:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199787):
<p>a human may be able to square a small number faster than a computer (not really)</p>

#### [ Kenny Lau (May 28 2018 at 12:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199789):
<p>but as the number gets large, the computer wins by a lot</p>

#### [ Kevin Buzzard (May 28 2018 at 12:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199793):
<p>I square small numbers by lookup</p>

#### [ Kevin Buzzard (May 28 2018 at 12:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199794):
<p>they're hard wired</p>

#### [ Kenny Lau (May 28 2018 at 12:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199796):
<p>right</p>

#### [ Kevin Buzzard (May 28 2018 at 12:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199799):
<p>unlike whatever I said 5 minutes ago</p>

#### [ Kenny Lau (May 28 2018 at 12:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199800):
<p>humans are good at small things</p>

#### [ Kenny Lau (May 28 2018 at 12:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199803):
<p><code>id '' U = U</code> is short</p>

#### [ Kevin Buzzard (May 28 2018 at 12:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199806):
<p>and true!</p>

#### [ Kenny Lau (May 28 2018 at 12:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199822):
<p>here we go again</p>

#### [ Kevin Buzzard (May 28 2018 at 12:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199846):
<p>The world just became a smaller place!</p>

#### [ Kevin Buzzard (May 28 2018 at 12:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199849):
<p>Two things became equal!</p>

#### [ Kevin Buzzard (May 28 2018 at 12:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199851):
<p>They are now the same thing, everyone please update your records</p>

#### [ Kevin Buzzard (May 28 2018 at 12:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199852):
<p>Why doesn't it work like that?</p>

#### [ Kevin Buzzard (May 28 2018 at 12:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199856):
<p>Where's the tactic that takes care of this for me?</p>

#### [ Kenny Lau (May 28 2018 at 12:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199858):
<p>you want a tactic to try to expand definitions</p>

#### [ Kevin Buzzard (May 28 2018 at 12:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199862):
<p>I have no clear idea what tactics do</p>

#### [ Kenny Lau (May 28 2018 at 12:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199864):
<p>that will work for small cases</p>

#### [ Kenny Lau (May 28 2018 at 12:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199866):
<p>that will not work for big cases</p>

#### [ Mario Carneiro (May 28 2018 at 12:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199867):
<p>In general that's undecidable</p>

#### [ Kenny Lau (May 28 2018 at 12:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199868):
<p>humans are <strong>only</strong> good at small things</p>

#### [ Kevin Buzzard (May 28 2018 at 12:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199869):
<p>Maybe learning tactics would help me understand my frustrations better.</p>

#### [ Andrew Ashworth (May 28 2018 at 12:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199870):
<blockquote>
<p>Maybe learning tactics would help me understand my frustrations better.</p>
</blockquote>
<p>yes</p>

#### [ Kevin Buzzard (May 28 2018 at 12:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199871):
<p>It's a huge hole in my Lean knowledge</p>

#### [ Kenny Lau (May 28 2018 at 12:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199873):
<div class="codehilite"><pre><span></span><span class="kn">definition</span> <span class="n">image&#39;</span> <span class="o">:=</span> <span class="o">{</span><span class="n">y</span> <span class="o">:</span> <span class="n">Y</span> <span class="bp">|</span> <span class="bp">∃</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">U</span><span class="o">,</span> <span class="n">f</span> <span class="n">x</span> <span class="bp">=</span> <span class="n">y</span><span class="o">}</span>

<span class="n">attribute</span> <span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="n">set</span><span class="bp">.</span><span class="n">image_id</span>

<span class="kn">theorem</span> <span class="n">they_are_the_same</span> <span class="o">:</span> <span class="n">image&#39;</span> <span class="o">(</span><span class="bp">@</span><span class="n">id</span> <span class="n">X</span><span class="o">)</span> <span class="n">U</span> <span class="bp">=</span> <span class="n">U</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">simp</span> <span class="o">[</span><span class="n">image&#39;</span><span class="o">]</span> <span class="c1">-- works</span>
<span class="kn">theorem</span> <span class="n">they_are_the_same&#39;</span> <span class="o">:</span> <span class="n">id</span> <span class="err">&#39;&#39;</span> <span class="n">U</span> <span class="bp">=</span> <span class="n">U</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">simp</span> <span class="c1">-- works</span>
<span class="kn">theorem</span> <span class="n">they_are_all_the_same_thing_</span> <span class="o">:</span> <span class="n">id</span> <span class="err">&#39;&#39;</span> <span class="n">U</span> <span class="bp">=</span> <span class="n">image&#39;</span> <span class="o">(</span><span class="bp">@</span><span class="n">id</span> <span class="n">X</span><span class="o">)</span> <span class="n">U</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">simp</span> <span class="o">[</span><span class="n">image&#39;</span><span class="o">]</span> <span class="c1">-- works</span>
<span class="kn">theorem</span> <span class="n">but_they_are_all_the_same</span> <span class="o">:</span> <span class="n">set</span><span class="bp">.</span><span class="n">image</span> <span class="o">(</span><span class="bp">@</span><span class="n">id</span> <span class="n">X</span><span class="o">)</span> <span class="n">U</span> <span class="bp">=</span> <span class="n">U</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">simp</span> <span class="c1">-- works</span>
<span class="kn">theorem</span> <span class="n">why_are_they_all_different</span> <span class="o">:</span> <span class="n">id</span> <span class="err">&#39;&#39;</span> <span class="n">U</span> <span class="bp">=</span> <span class="n">set</span><span class="bp">.</span><span class="n">image</span> <span class="o">(</span><span class="bp">@</span><span class="n">id</span> <span class="n">X</span><span class="o">)</span> <span class="n">U</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">simp</span>
</pre></div>

#### [ Kevin Buzzard (May 28 2018 at 12:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199874):
<p>All I know is that tactic is a monoid or monad or something</p>

#### [ Kevin Buzzard (May 28 2018 at 12:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199920):
<p><code>theorem they_are_the_same' : id '' U = U := by simp -- fails</code></p>

#### [ Kevin Buzzard (May 28 2018 at 12:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199921):
<p>?</p>

#### [ Kevin Buzzard (May 28 2018 at 12:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199923):
<p>it works for you?</p>

#### [ Kenny Lau (May 28 2018 at 12:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199924):
<p><span class="user-mention" data-user-id="110049">@Mario Carneiro</span> can I get <code>simp</code> to automatically unfold certain definitions? <code>reducible</code> doesn't work</p>

#### [ Kevin Buzzard (May 28 2018 at 12:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199928):
<p>oh you CHEATED</p>

#### [ Mario Carneiro (May 28 2018 at 12:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199929):
<p><code>@[simp]</code> can go on definitions</p>

#### [ Kevin Buzzard (May 28 2018 at 12:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199931):
<p>You gave simp a hint</p>

#### [ Mario Carneiro (May 28 2018 at 12:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199934):
<p>YES</p>

#### [ Kevin Buzzard (May 28 2018 at 12:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199938):
<p>So that hint should have been there alreadyt</p>

#### [ Kevin Buzzard (May 28 2018 at 12:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199939):
<p>already</p>

#### [ Kenny Lau (May 28 2018 at 12:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199941):
<p>thanks <span class="user-mention" data-user-id="110049">@Mario Carneiro</span></p>

#### [ Kevin Buzzard (May 28 2018 at 12:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199942):
<p>why isn't it a simp lemma?</p>

#### [ Kenny Lau (May 28 2018 at 12:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199943):
<p>now I can convince him:</p>

#### [ Kenny Lau (May 28 2018 at 12:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199944):
<div class="codehilite"><pre><span></span><span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="n">def</span> <span class="n">image&#39;</span> <span class="o">:=</span> <span class="o">{</span><span class="n">y</span> <span class="o">:</span> <span class="n">Y</span> <span class="bp">|</span> <span class="bp">∃</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">U</span><span class="o">,</span> <span class="n">f</span> <span class="n">x</span> <span class="bp">=</span> <span class="n">y</span><span class="o">}</span>

<span class="n">attribute</span> <span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="n">set</span><span class="bp">.</span><span class="n">image</span>

<span class="kn">theorem</span> <span class="n">they_are_the_same</span> <span class="o">:</span> <span class="n">image&#39;</span> <span class="o">(</span><span class="bp">@</span><span class="n">id</span> <span class="n">X</span><span class="o">)</span> <span class="n">U</span> <span class="bp">=</span> <span class="n">U</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">simp</span> <span class="c1">-- works</span>
<span class="kn">theorem</span> <span class="n">they_are_the_same&#39;</span> <span class="o">:</span> <span class="n">id</span> <span class="err">&#39;&#39;</span> <span class="n">U</span> <span class="bp">=</span> <span class="n">U</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">simp</span> <span class="c1">-- works</span>
<span class="kn">theorem</span> <span class="n">they_are_all_the_same_thing_</span> <span class="o">:</span> <span class="n">id</span> <span class="err">&#39;&#39;</span> <span class="n">U</span> <span class="bp">=</span> <span class="n">image&#39;</span> <span class="o">(</span><span class="bp">@</span><span class="n">id</span> <span class="n">X</span><span class="o">)</span> <span class="n">U</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">simp</span> <span class="c1">-- works</span>
<span class="kn">theorem</span> <span class="n">but_they_are_all_the_same</span> <span class="o">:</span> <span class="n">set</span><span class="bp">.</span><span class="n">image</span> <span class="o">(</span><span class="bp">@</span><span class="n">id</span> <span class="n">X</span><span class="o">)</span> <span class="n">U</span> <span class="bp">=</span> <span class="n">U</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">simp</span> <span class="c1">-- works</span>
<span class="kn">theorem</span> <span class="n">why_are_they_all_different</span> <span class="o">:</span> <span class="n">id</span> <span class="err">&#39;&#39;</span> <span class="n">U</span> <span class="bp">=</span> <span class="n">set</span><span class="bp">.</span><span class="n">image</span> <span class="o">(</span><span class="bp">@</span><span class="n">id</span> <span class="n">X</span><span class="o">)</span> <span class="n">U</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">simp</span>
</pre></div>

#### [ Mario Carneiro (May 28 2018 at 12:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199945):
<p>like I said, you shoot me in the leg and ask me to run a marathon</p>

#### [ Mario Carneiro (May 28 2018 at 12:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199947):
<p>it should be a simp lemma, I fixed</p>

#### [ Johan Commelin (May 28 2018 at 12:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199948):
<blockquote>
<p>why isn't it a simp lemma?</p>
</blockquote>
<p>you mean a simp definition?</p>

#### [ Kenny Lau (May 28 2018 at 12:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199949):
<p><span class="user-mention" data-user-id="112680">@Johan Commelin</span> no, <code>set.image_id</code></p>

#### [ Kenny Lau (May 28 2018 at 12:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199951):
<p>not a definition</p>

#### [ Johan Commelin (May 28 2018 at 12:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199990):
<p>Aaah, ok, true</p>

#### [ Kenny Lau (May 28 2018 at 12:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199991):
<p>now is <span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> happy?</p>

#### [ Kenny Lau (May 28 2018 at 12:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199995):
<p>after the fix I will be able to remove that line</p>

#### [ Kevin Buzzard (May 28 2018 at 12:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199996):
<p>Oh!</p>

#### [ Kenny Lau (May 28 2018 at 12:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199997):
<div class="codehilite"><pre><span></span><span class="bp">@</span><span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="n">def</span> <span class="n">image&#39;</span> <span class="o">:=</span> <span class="o">{</span><span class="n">y</span> <span class="o">:</span> <span class="n">Y</span> <span class="bp">|</span> <span class="bp">∃</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">U</span><span class="o">,</span> <span class="n">f</span> <span class="n">x</span> <span class="bp">=</span> <span class="n">y</span><span class="o">}</span>

<span class="n">attribute</span> <span class="o">[</span><span class="n">simp</span><span class="o">]</span> <span class="n">set</span><span class="bp">.</span><span class="n">image_id</span>

<span class="kn">theorem</span> <span class="n">they_are_the_same</span> <span class="o">:</span> <span class="n">image&#39;</span> <span class="o">(</span><span class="bp">@</span><span class="n">id</span> <span class="n">X</span><span class="o">)</span> <span class="n">U</span> <span class="bp">=</span> <span class="n">U</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">simp</span> <span class="c1">-- works</span>
<span class="kn">theorem</span> <span class="n">they_are_the_same&#39;</span> <span class="o">:</span> <span class="n">id</span> <span class="err">&#39;&#39;</span> <span class="n">U</span> <span class="bp">=</span> <span class="n">U</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">simp</span> <span class="c1">-- works</span>
<span class="kn">theorem</span> <span class="n">they_are_all_the_same_thing_</span> <span class="o">:</span> <span class="n">id</span> <span class="err">&#39;&#39;</span> <span class="n">U</span> <span class="bp">=</span> <span class="n">image&#39;</span> <span class="o">(</span><span class="bp">@</span><span class="n">id</span> <span class="n">X</span><span class="o">)</span> <span class="n">U</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">simp</span> <span class="c1">-- works</span>
<span class="kn">theorem</span> <span class="n">but_they_are_all_the_same</span> <span class="o">:</span> <span class="n">set</span><span class="bp">.</span><span class="n">image</span> <span class="o">(</span><span class="bp">@</span><span class="n">id</span> <span class="n">X</span><span class="o">)</span> <span class="n">U</span> <span class="bp">=</span> <span class="n">U</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">simp</span> <span class="c1">-- works</span>
<span class="kn">theorem</span> <span class="n">why_are_they_all_different</span> <span class="o">:</span> <span class="n">id</span> <span class="err">&#39;&#39;</span> <span class="n">U</span> <span class="bp">=</span> <span class="n">set</span><span class="bp">.</span><span class="n">image</span> <span class="o">(</span><span class="bp">@</span><span class="n">id</span> <span class="n">X</span><span class="o">)</span> <span class="n">U</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">simp</span>
</pre></div>

#### [ Kevin Buzzard (May 28 2018 at 12:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127199998):
<p>You see I have <em>absolutely no idea</em> about whether this is suitable as a simp lemma.</p>

#### [ Kevin Buzzard (May 28 2018 at 12:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127200003):
<p>All i know is that it passes two basic tests</p>

#### [ Kevin Buzzard (May 28 2018 at 12:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127200004):
<p>(1) it's an equality</p>

#### [ Kevin Buzzard (May 28 2018 at 12:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127200005):
<p>(2) the left hand side has more characters than the right hand side</p>

#### [ Mario Carneiro (May 28 2018 at 12:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127200007):
<p>image_id is a good simp lemma</p>

#### [ Kevin Buzzard (May 28 2018 at 12:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127200009):
<p>My entry requirements for simp are pretty low</p>

#### [ Kenny Lau (May 28 2018 at 12:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127200010):
<p>so is <span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> satisfied now?</p>

#### [ Mario Carneiro (May 28 2018 at 12:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127200011):
<p>most theorems of the form "my_func special_arg = value" are good simp lemmas</p>

#### [ Kevin Buzzard (May 28 2018 at 12:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127200013):
<blockquote>
<p>image_id is a good simp lemma</p>
</blockquote>
<p>I feel I could not say that with confidence</p>

#### [ Kevin Buzzard (May 28 2018 at 12:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127200051):
<p>and that's what I mean when I say that I still don't understand simp properly</p>

#### [ Mario Carneiro (May 28 2018 at 12:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127200058):
<p>It takes more knowledge to set up good simp lemmas than to use simp of course</p>

#### [ Kevin Buzzard (May 28 2018 at 12:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127200060):
<p>Exactly.</p>

#### [ Kevin Buzzard (May 28 2018 at 12:44)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127200061):
<p>I want to become a power user</p>

#### [ Mario Carneiro (May 28 2018 at 12:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127200062):
<p>because it's a global problem with some locality</p>

#### [ Kevin Buzzard (May 28 2018 at 12:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127200072):
<p>but I don't know anywhere where random nuggets such as</p>

#### [ Kevin Buzzard (May 28 2018 at 12:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127200074):
<blockquote>
<p>most theorems of the form "my_func special_arg = value" are good simp lemmas</p>
</blockquote>

#### [ Kevin Buzzard (May 28 2018 at 12:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127200075):
<p>appear, other than here</p>

#### [ Mario Carneiro (May 28 2018 at 12:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127200080):
<p>You could just look at the many many examples in mathlib</p>

#### [ Kevin Buzzard (May 28 2018 at 12:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127200120):
<p>reading code is so <em>boring</em></p>

#### [ Andrew Ashworth (May 28 2018 at 12:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127200121):
<p>only masochistic CS graduate students get interested in software verification</p>

#### [ Kevin Buzzard (May 28 2018 at 12:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127200122):
<p>that's what CS people do</p>

#### [ Andrew Ashworth (May 28 2018 at 12:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127200123):
<p>your tips are folklore in CS departments</p>

#### [ Kevin Buzzard (May 28 2018 at 12:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127200126):
<p>I want to talk to more CS people</p>

#### [ Andrew Ashworth (May 28 2018 at 12:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127200127):
<p>and that textbook I mentioned yesterday</p>

#### [ Kevin Buzzard (May 28 2018 at 12:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127200128):
<p>I need simp tips so I can be a power user</p>

#### [ Mario Carneiro (May 28 2018 at 12:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127200130):
<p>term rewriting and all that?</p>

#### [ Andrew Ashworth (May 28 2018 at 12:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127200131):
<p>yeah</p>

#### [ Kevin Buzzard (May 28 2018 at 12:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127200132):
<p>I remember a couple of months ago it all dawning on Chris</p>

#### [ Mario Carneiro (May 28 2018 at 12:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127200134):
<p>I'm willing to bet it's full of tips on setting up simp</p>

#### [ Kevin Buzzard (May 28 2018 at 12:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127200135):
<p>all of a sudden every other day he was saying to me "wooah simp does much more than you'd expect"</p>

#### [ Kevin Buzzard (May 28 2018 at 12:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127200141):
<p>and then I knew he'd cracked it</p>

#### [ Mario Carneiro (May 28 2018 at 12:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127200146):
<p>and now you are stuck on the other end, where you think simp is magic that solves all problems</p>

#### [ Kevin Buzzard (May 28 2018 at 12:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127200191):
<p>I'm still at the novice stage, behind Patrick who can remember the {something = true} stuff that you sometimes have to write at the end of simp for some reason and which you don't have to write in schoolkid</p>

#### [ Kevin Buzzard (May 28 2018 at 12:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127200194):
<p>Actually, how about this for a tactic</p>

#### [ Kevin Buzzard (May 28 2018 at 12:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127200200):
<p>I look through all the permutations and incantations that people have been using with simp recently</p>

#### [ Kevin Buzzard (May 28 2018 at 12:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127200203):
<p>and I just write a tactic that tries all of them on my goal</p>

#### [ Kevin Buzzard (May 28 2018 at 12:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127200204):
<p>and calls it schoolkid</p>

#### [ Mario Carneiro (May 28 2018 at 12:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127200215):
<p>I think you could use some CS education, if only so that your suggestions come with algorithms</p>

#### [ Kevin Buzzard (May 28 2018 at 12:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127200216):
<p>that way I will never have to remember what comes after the [] in simp</p>

#### [ Kevin Buzzard (May 28 2018 at 12:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127200280):
<p>So I was under the misapprehension that the "your brain is just a big computer" people think that writing tactics to do what we do should be fine</p>

#### [ Kenny Lau (May 28 2018 at 12:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127200283):
<p>your brain is a big computer that doesn't have to do everything correctly, just the small things</p>

#### [ Mario Carneiro (May 28 2018 at 12:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127200284):
<p>That same argument says that general AI is just around the corner</p>

#### [ Kevin Buzzard (May 28 2018 at 12:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127200289):
<p>I see</p>

#### [ Kevin Buzzard (May 28 2018 at 12:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127200294):
<p>So is it possible to isolate "the techniques that I use to solve goals in ZFC"?</p>

#### [ Kevin Buzzard (May 28 2018 at 12:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127200295):
<p>Is that the question?</p>

#### [ Kevin Buzzard (May 28 2018 at 12:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127200296):
<p>Can I code this in a Lean tactic?</p>

#### [ Kenny Lau (May 28 2018 at 12:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127200297):
<p>those techniques only work for small cases</p>

#### [ Kevin Buzzard (May 28 2018 at 12:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127200303):
<p>Are you saying that this is hard</p>

#### [ Kenny Lau (May 28 2018 at 12:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127200336):
<p>they can't be verified</p>

#### [ Andrew Ashworth (May 28 2018 at 12:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127200340):
<p>can you write those techniques down as a sequence of steps in the language of Lean?</p>

#### [ Kevin Buzzard (May 28 2018 at 12:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127200342):
<p>I find it so difficult to see how it can be hard when it's just checking that things are all the same</p>

#### [ Kevin Buzzard (May 28 2018 at 12:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127200344):
<p><span class="user-mention" data-user-id="110025">@Andrew Ashworth</span> This is exactly the point.</p>

#### [ Kenny Lau (May 28 2018 at 12:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127200345):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> the techniques include "run upon seeing a theorem with 10000 characters", which can't be one of the things a verified algorithm can do</p>

#### [ Mario Carneiro (May 28 2018 at 12:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127200346):
<p><a href="https://en.wikipedia.org/wiki/Word_problem_for_groups" target="_blank" title="https://en.wikipedia.org/wiki/Word_problem_for_groups">https://en.wikipedia.org/wiki/Word_problem_for_groups</a></p>

#### [ Kevin Buzzard (May 28 2018 at 12:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127200347):
<p>When I discovered Lean I realised that it was the computer language I had been waiting for all my life</p>

#### [ Kevin Buzzard (May 28 2018 at 12:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127200350):
<p>and so just thought I'd code my brain up in it</p>

#### [ Kevin Buzzard (May 28 2018 at 12:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127200353):
<p>and I was just assuming it was going to be easy</p>

#### [ Kenny Lau (May 28 2018 at 12:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127200354):
<p>the world is imperfect</p>

#### [ Kenny Lau (May 28 2018 at 12:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127200357):
<p>computability matters</p>

#### [ Mario Carneiro (May 28 2018 at 12:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127200358):
<p>just checking that things are all the same is undecidable in some simple situations</p>

#### [ Kevin Buzzard (May 28 2018 at 12:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127200360):
<p>that's an engineering problem</p>

#### [ Kevin Buzzard (May 28 2018 at 12:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127200361):
<p>you CS guys write great algos</p>

#### [ Kevin Buzzard (May 28 2018 at 12:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127200363):
<p>I'm sure you can decide all the stuff I want decided</p>

#### [ Mario Carneiro (May 28 2018 at 12:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127200364):
<p>no that's a fundamental limit on progress</p>

#### [ Kenny Lau (May 28 2018 at 12:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127200367):
<p>no, you can't</p>

#### [ Kevin Buzzard (May 28 2018 at 12:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127200368):
<p>because I have a <em>really good feeling</em> for the provability boundaries of ZFC</p>

#### [ Kevin Buzzard (May 28 2018 at 12:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127200409):
<p>I know which questions look "weird to me" like CH</p>

#### [ Kenny Lau (May 28 2018 at 12:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127200410):
<p>you don't</p>

#### [ Kevin Buzzard (May 28 2018 at 12:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127200411):
<p>and which questions look sensible to me like the Langlands Programme</p>

#### [ Kenny Lau (May 28 2018 at 12:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127200414):
<p>there are infinitely many independent theorem in any computable extension of ZFC</p>

#### [ Kenny Lau (May 28 2018 at 12:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127200416):
<p>and there's no way any algorithm can decide whether a theorem is independent</p>

#### [ Kenny Lau (May 28 2018 at 12:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127200418):
<p>including your brain</p>

#### [ Kenny Lau (May 28 2018 at 12:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127200423):
<p>your brain only knows special cases like CH and AD and AC</p>

#### [ Mario Carneiro (May 28 2018 at 12:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127200439):
<p>and it only knows those because it has lots of simp lemmas</p>

#### [ Andrew Ashworth (May 28 2018 at 12:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127200440):
<p>hmm, I don't know if you will have long-term success with formal proofs if you don't engage with CS theory and tactic writing. because the tedious bits need to be attacked via automation, and lots of custom automation at that. Remember Bertrand Russell tried to do everything by hand and spent 5 years proving 2+2=4</p>

#### [ Andrew Ashworth (May 28 2018 at 12:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127200442):
<p>and this is my own failing too, it's hard, I haven't learned Lean tactics yet</p>

#### [ Mario Carneiro (May 28 2018 at 12:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127200482):
<p>I could argue that automation is not necessary for getting things done formally</p>

#### [ Mario Carneiro (May 28 2018 at 12:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127200484):
<p>I have plenty of theorems in metamath as evidence</p>

#### [ Mario Carneiro (May 28 2018 at 12:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127200487):
<p>but proof engineering is a really important skill</p>

#### [ Andrew Ashworth (May 28 2018 at 12:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127200534):
<p>but there's also evidence from adam chlipala and john harrison that automation is kind of a big deal</p>

#### [ Andrew Ashworth (May 28 2018 at 12:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127200547):
<p>well, and I don't know about math, but software definitely needs automation to discharge repetitive, yet tediously involved goals</p>

#### [ Mario Carneiro (May 28 2018 at 12:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127200548):
<p>there are multiple styles of proof, and they are all effective in the right hands</p>

#### [ Andrew Ashworth (May 28 2018 at 12:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127200550):
<p>and i get the feeling from Kevin's worry about schemes that advanced mathematical constructs could also use a large helping of custom automation</p>

#### [ Mario Carneiro (May 28 2018 at 12:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127200551):
<p>I find that good lemmas take most of the brunt of that</p>

#### [ Mario Carneiro (May 28 2018 at 13:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127200599):
<p>but I grant that working with lean encourages good automation practices</p>

#### [ Andrew Ashworth (May 28 2018 at 13:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127200608):
<p>there was that whole week long discussion about transporting across equivs and I was thinking "so use <code>transfer</code> or write a tactic" bingo problem solved</p>

#### [ Kenny Lau (May 28 2018 at 13:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127200610):
<p>what was the solution?</p>

#### [ Andrew Ashworth (May 28 2018 at 13:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127200664):
<p>to what?</p>

#### [ Kevin Buzzard (May 28 2018 at 13:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127200954):
<blockquote>
<p>in ZFC <code>id '' U</code> isn't even defined</p>
</blockquote>
<p>Oh what a bore, you're right</p>

#### [ Mario Carneiro (May 28 2018 at 13:12)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127201003):
<p>metamath uses ZFC + classes to get around this</p>

#### [ Mario Carneiro (May 28 2018 at 13:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127201012):
<p>it's a conservative extension, it just lets you express class equalities like this</p>

#### [ Mario Carneiro (May 28 2018 at 13:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127201028):
<p><a href="http://us.metamath.org/mpeuni/imai.html" target="_blank" title="http://us.metamath.org/mpeuni/imai.html">http://us.metamath.org/mpeuni/imai.html</a></p>

#### [ Kevin Buzzard (May 28 2018 at 13:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127201134):
<blockquote>
<p>that's stupid. What if I can't find the official image so I just make my own image which would then be identical so all the old theorems would work anyway</p>
</blockquote>
<p>This is bad, isn't it? Doesn't it mean that every time I have a terrific new idea for a function, I have to stop what I'm doing and plough through the library to see if someone already wrote it?</p>

#### [ Kenny Lau (May 28 2018 at 13:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127201143):
<p>it's called using interface to make your life better</p>

#### [ Kevin Buzzard (May 28 2018 at 13:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127201412):
<blockquote>
<p><code>schoolkid_1</code> is <code>simp!</code></p>
</blockquote>
<p>Then why do I even bother using simp? Should I just be using simp! all the time? Is there any case where simp works and simp! doesn't?</p>

#### [ Kevin Buzzard (May 28 2018 at 13:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127201465):
<blockquote>
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> I really do not see any problem at all. <code>id '' U</code> does not expand to <code>U</code>. you have to destruct the definitions and <strong>use extensionality</strong></p>
</blockquote>
<p>Yes -- you mean the definition of equal, right?</p>

#### [ Kenny Lau (May 28 2018 at 13:26)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127201474):
<p>no, I mean the axiom of extensionality.</p>

#### [ Kevin Buzzard (May 28 2018 at 13:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127201493):
<blockquote>
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> here's how I can formalize what I say: if you didn't have <code>propext</code> as an axiom, then you won't be able to prove that the two sets are equal, in Lean</p>
</blockquote>
<p>But propext is in Lean! Is it a good simp lemma?</p>

#### [ Mario Carneiro (May 28 2018 at 13:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127201500):
<p>no</p>

#### [ Kevin Buzzard (May 28 2018 at 13:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127201502):
<p>it looks good to me</p>

#### [ Kevin Buzzard (May 28 2018 at 13:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127201504):
<p>simple predicate</p>

#### [ Kevin Buzzard (May 28 2018 at 13:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127201505):
<p>implies an equality</p>

#### [ Mario Carneiro (May 28 2018 at 13:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127201545):
<p>it says p = q in the conclusion</p>

#### [ Kevin Buzzard (May 28 2018 at 13:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127201548):
<p>it got over my simp bar</p>

#### [ Mario Carneiro (May 28 2018 at 13:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127201551):
<p>that means anything equals anything</p>

#### [ Mario Carneiro (May 28 2018 at 13:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127201553):
<p>it's too general</p>

#### [ Kevin Buzzard (May 28 2018 at 13:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127201555):
<p>Just apply it sensibly</p>

#### [ Kevin Buzzard (May 28 2018 at 13:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127201556):
<p>and stop moaning</p>

#### [ Kevin Buzzard (May 28 2018 at 13:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127201557):
<p>don't just apply it randomly</p>

#### [ Kevin Buzzard (May 28 2018 at 13:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127201558):
<p>:-/</p>

#### [ Kevin Buzzard (May 28 2018 at 13:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127201559):
<p>This is really interesting</p>

#### [ Kevin Buzzard (May 28 2018 at 13:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127201576):
<p>this is the hard bit</p>

#### [ Mario Carneiro (May 28 2018 at 13:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127201577):
<p>Here's another constraint: all the variables on the RHS should appear on the LHS</p>

#### [ Kevin Buzzard (May 28 2018 at 13:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127201583):
<p>You can't make all the things I know are obvious yield to one tactic because you haven't worked hard enough</p>

#### [ Mario Carneiro (May 28 2018 at 13:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127201584):
<p>otherwise simp has to be creative when rewriting</p>

#### [ Kevin Buzzard (May 28 2018 at 13:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127201586):
<p>So again this is somehow about can we build a tactic that beats a human at maths</p>

#### [ Kevin Buzzard (May 28 2018 at 13:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127201629):
<p>Will this happen before I die? Say I live another 30 years</p>

#### [ Mario Carneiro (May 28 2018 at 13:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127201630):
<p>I think you should try writing that tactic and get back to me</p>

#### [ Kevin Buzzard (May 28 2018 at 13:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127201635):
<p>That's your job</p>

#### [ Kevin Buzzard (May 28 2018 at 13:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127201637):
<p>you went to math classe</p>

#### [ Kevin Buzzard (May 28 2018 at 13:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127201638):
<p>s</p>

#### [ Kevin Buzzard (May 28 2018 at 13:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127201640):
<p>you know how we think</p>

#### [ Mario Carneiro (May 28 2018 at 13:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127201643):
<p>I want you to fail at it first so you understand what you are asking</p>

#### [ Kevin Buzzard (May 28 2018 at 13:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127201644):
<p>can you write a better interface?</p>

#### [ Johan Commelin (May 28 2018 at 13:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127201659):
<p>Kevin, I completely agree that we need a smarter tactic. But I think that doesn't have to be <code>simp</code>. Simp is a very straightforward tool, that shouldn't try to be smart.</p>

#### [ Kevin Buzzard (May 28 2018 at 13:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127201667):
<p>Yes, I need to go and play with Mizar and then some things which are conflated in my mind will become more separate</p>

#### [ Kevin Buzzard (May 28 2018 at 13:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127201677):
<p>no, we should use schoolkid or whatever you wanted to call it</p>

#### [ Kevin Buzzard (May 28 2018 at 13:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127201678):
<p>I think you had a more grown-up name</p>

#### [ Kenny Lau (May 28 2018 at 13:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127201682):
<blockquote>
<p>Yes, I need to go and play with Mizar and then some things which are conflated in my mind will become more separate</p>
</blockquote>
<p>I don't see the point going to a weaker foundational system</p>

#### [ Johan Commelin (May 28 2018 at 13:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127201689):
<blockquote>
<p>I think you had a more grown-up name</p>
</blockquote>
<p><code>math_trivial</code>?</p>

#### [ Mario Carneiro (May 28 2018 at 13:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127201726):
<p>Mizar is actually stronger axiomatically than lean</p>

#### [ Kenny Lau (May 28 2018 at 13:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127201733):
<p>why?</p>

#### [ Mario Carneiro (May 28 2018 at 13:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127201734):
<p>it has a proper class of inaccessibles</p>

#### [ Johan Commelin (May 28 2018 at 13:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127201735):
<p>But I wouldn't mind have <code>kindergarten</code> or <code>schoolkid</code></p>

#### [ Kenny Lau (May 28 2018 at 13:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127201750):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> again, your issue is not in the foundational system</p>

#### [ Kenny Lau (May 28 2018 at 13:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127201752):
<p>but it seems that you are deaf</p>

#### [ Andrew Ashworth (May 28 2018 at 13:33)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127201760):
<p>it can't hurt to play around with Mizar and Isabelle</p>

#### [ Kevin Buzzard (May 28 2018 at 13:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127201761):
<blockquote>
<p>why are you proving trivial set theorems?</p>
</blockquote>
<p>in this case it was because I was trying to understand something. But on other occasions the answer is "because I don't really know a good way of finding it in the library and it's almost certainly in a file which I haven't imported yet"</p>

#### [ Andrew Ashworth (May 28 2018 at 13:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127201798):
<p>most of us here are refugees from Coq / Agda / Isabelle anyway</p>

#### [ Mario Carneiro (May 28 2018 at 13:34)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127201807):
<p>they are organized fairly logically</p>

#### [ Mario Carneiro (May 28 2018 at 13:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127201810):
<p><code>set.image_id</code> is in the <code>image</code> section of <code>data.set.basic</code></p>

#### [ Kevin Buzzard (May 28 2018 at 13:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127201820):
<blockquote>
<p>I don't see the point going to a weaker foundational system</p>
</blockquote>
<p>I need to see it, in order to refine my definition of "equality in ZFC".</p>

#### [ Kevin Buzzard (May 28 2018 at 13:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127201903):
<blockquote>
<p><code>set.image_id</code> is in the <code>image</code> section of <code>data.set.basic</code></p>
</blockquote>
<p>I just can't remember all this data.set.basic stuff. I just want to write set.image and hit tab a few times. This is a genuine frustration I have in my lean life</p>

#### [ Kevin Buzzard (May 28 2018 at 13:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127201904):
<p>I am not capable of learning all the names of all the library files</p>

#### [ Kevin Buzzard (May 28 2018 at 13:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127201907):
<p>it's init this and data that</p>

#### [ Kevin Buzzard (May 28 2018 at 13:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127201908):
<p>when I want set.image_id</p>

#### [ Kevin Buzzard (May 28 2018 at 13:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127201947):
<p>I type <code>#check set.image_id</code></p>

#### [ Kevin Buzzard (May 28 2018 at 13:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127201948):
<p>and it's not there</p>

#### [ Kevin Buzzard (May 28 2018 at 13:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127201951):
<p>and then I have to stop what I'm doing and start faffing around with the search tool</p>

#### [ Kevin Buzzard (May 28 2018 at 13:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127201953):
<p>I have no clue where anything is</p>

#### [ Kevin Buzzard (May 28 2018 at 13:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127201954):
<p>they're just all theorems</p>

#### [ Kevin Buzzard (May 28 2018 at 13:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127201965):
<p>Can we have a better search?</p>

#### [ Mario Carneiro (May 28 2018 at 13:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127201974):
<p>I just type <code>import set</code> and the autocomplete is pretty smart about it</p>

#### [ Kevin Buzzard (May 28 2018 at 13:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127201988):
<p>oh!</p>

#### [ Kevin Buzzard (May 28 2018 at 13:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127201994):
<p>Because I know it's set.something I can just import set?</p>

#### [ Kevin Buzzard (May 28 2018 at 13:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127201996):
<p>Does that work with everything?</p>

#### [ Mario Carneiro (May 28 2018 at 13:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127202000):
<p>it's not even set.something</p>

#### [ Kevin Buzzard (May 28 2018 at 13:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127202001):
<p>can I import scheme?</p>

#### [ Mario Carneiro (May 28 2018 at 13:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127202002):
<p>it's data.set.basic</p>

#### [ Mario Carneiro (May 28 2018 at 13:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127202004):
<p>but vscode will still give it to you</p>

#### [ Kevin Buzzard (May 28 2018 at 13:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127202007):
<p>I see</p>

#### [ Kevin Buzzard (May 28 2018 at 13:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127202054):
<p>I should "key on set"</p>

#### [ Kevin Buzzard (May 28 2018 at 13:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127202211):
<blockquote>
<p>there are infinitely many independent theorem in any computable extension of ZFC</p>
</blockquote>
<p>I know but Kenny my point is that those independent theorems are just junk theorems like stupid theorems about how pi can't be a complex manifold.</p>

#### [ Kenny Lau (May 28 2018 at 13:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127202214):
<p>are they</p>

#### [ Kevin Buzzard (May 28 2018 at 13:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127202215):
<p>All the undecidable statements about stupid things like sets. [added later] -- that's not what ZFC is even _for_!</p>

#### [ Kevin Buzzard (May 28 2018 at 13:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127202255):
<p>I am only interested in the Langlands Programme</p>

#### [ Kevin Buzzard (May 28 2018 at 13:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127202302):
<blockquote>
<p>there was that whole week long discussion about transporting across equivs and I was thinking "so use <code>transfer</code> or write a tactic" bingo problem solved</p>
</blockquote>
<p>That's on my todo list. I'm going to write a short paper about my whole scheme experience for the ZFC people and I am going to have to get up to date as to exactly what we think is possible there</p>

#### [ Kevin Buzzard (May 28 2018 at 13:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127202312):
<blockquote>
<p>it's called using interface to make your life better</p>
</blockquote>
<p>I need better interface search.</p>

#### [ Kevin Buzzard (May 28 2018 at 13:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127202315):
<p>I thought we have google nowadays. Why isn't search easy?</p>

#### [ Kevin Buzzard (May 28 2018 at 13:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127202321):
<p>Why can't I write set.image_id and something pops up saying "do you want to import data.set.basic"?</p>

#### [ Kevin Buzzard (May 28 2018 at 13:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127202323):
<p>Can that be a thing one day?</p>

#### [ Sean Leather (May 28 2018 at 13:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127202339):
<p>Because nobody's written the code to do it. That's usually your answer.</p>

#### [ Andrew Ashworth (May 28 2018 at 13:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127202392):
<p>It could be. Maybe Lean gets tremendously popular, gets a research grant, and somebody gets hired to work on it to make it easier to use for mathematicians</p>

#### [ Kevin Buzzard (May 28 2018 at 13:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127202401):
<blockquote>
<p>Here's another constraint: all the variables on the RHS should appear on the LHS</p>
</blockquote>
<p>Is it possible to make a flowchart -- "am I a good simp lemma?"</p>

#### [ Kevin Buzzard (May 28 2018 at 13:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127202484):
<blockquote>
<p>It could be. Maybe Lean gets tremendously popular, gets a research grant, and somebody gets hired to work on it to make it easier to use for mathematicians</p>
</blockquote>
<p>How much does that cost in your CS world?</p>

#### [ Kevin Buzzard (May 28 2018 at 13:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127202487):
<p>I could do all the costings for that other than salary</p>

#### [ Kevin Buzzard (May 28 2018 at 13:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127202488):
<p>I have no idea how much you guys get paid</p>

#### [ Kevin Buzzard (May 28 2018 at 13:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127202490):
<p>the administration would be able to fill in the other boxes</p>

#### [ Kevin Buzzard (May 28 2018 at 13:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127202537):
<p>I'm meeting with EPSRC in two weeks</p>

#### [ Kevin Buzzard (May 28 2018 at 13:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127202540):
<p>I have several hours of meetings with them and I have already pre-warned them that I will be after money to spend on computer scientists</p>

#### [ Kevin Buzzard (May 28 2018 at 13:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127202557):
<p>But it would be good to get an idea of how much to pay someone to do that job</p>

#### [ Andrew Ashworth (May 28 2018 at 14:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127202970):
<p>I'm not too familiar with London CS pay, my general instinct is that it ranges from 30 ~ 70 thousand pounds / year</p>

#### [ Andrew Ashworth (May 28 2018 at 14:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127203100):
<p>you could wait until Lean 4. We've been promised by <strong>Moses Schönfinkel</strong> that he wants to take a look at theorem search in Lean after the parser and tactics framework settles down</p>

#### [ Kevin Buzzard (May 28 2018 at 14:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127203426):
<p>I just wrote a theorem that was in the library</p>

#### [ Kevin Buzzard (May 28 2018 at 14:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127203427):
<p>yay me</p>

#### [ Kevin Buzzard (May 28 2018 at 14:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127203430):
<p><code>#check topological_space.open_immersion_id </code></p>

#### [ Kevin Buzzard (May 28 2018 at 14:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127203433):
<p><code>#check topological_space.id_open_immersion</code></p>

#### [ Kevin Buzzard (May 28 2018 at 14:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127203436):
<p>what should it be called?</p>

#### [ Kevin Buzzard (May 28 2018 at 14:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127203444):
<p>The statement that the identity map is an open immersion</p>

#### [ Kevin Buzzard (May 28 2018 at 14:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127203447):
<p>I did the other one</p>

#### [ Kevin Buzzard (May 28 2018 at 14:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127203495):
<p>is there a hard and fast convention for naming that extends beyond my <code>mul_one</code> levels?</p>

#### [ Kevin Buzzard (May 28 2018 at 14:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127203497):
<p>I get the feeling that there's more of an art to it</p>

#### [ Kevin Buzzard (May 28 2018 at 14:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127203498):
<p>What do the artists say about this one?</p>

#### [ Patrick Massot (May 28 2018 at 14:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127203562):
<p>Yeah, Kevin is back to work! I'm amazed how fast he travels those math formalization <a href="https://en.wikipedia.org/wiki/K%C3%BCbler-Ross_model#Stages_of_grief" target="_blank" title="https://en.wikipedia.org/wiki/K%C3%BCbler-Ross_model#Stages_of_grief">DTT stages</a> every month or so.</p>

#### [ Patrick Massot (May 28 2018 at 14:25)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127203575):
<p>I'm much slower</p>

#### [ Kevin Buzzard (May 28 2018 at 14:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127203932):
<p>I am trying to write a hard level for these CS guys</p>

#### [ Kevin Buzzard (May 28 2018 at 14:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127203934):
<p>But I am stuck on something</p>

#### [ Kevin Buzzard (May 28 2018 at 14:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127203938):
<p>If I have <code>x :
  (presheaf_of_types_pullback_under_open_immersion ((zariski.structure_presheaf_of_rings R).to_presheaf_of_types) id
     _).F
    HU
</code></p>

#### [ Kevin Buzzard (May 28 2018 at 14:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127203939):
<p>in my context</p>

#### [ Kevin Buzzard (May 28 2018 at 14:36)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127203941):
<p>oh I can answer my own question</p>

#### [ Kevin Buzzard (May 28 2018 at 14:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127204007):
<p>oh no I can't</p>

#### [ Kevin Buzzard (May 28 2018 at 14:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127204009):
<p>Ok so there's my x</p>

#### [ Kevin Buzzard (May 28 2018 at 14:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127204015):
<p>and <code>presheaf_of_types_pullback_under_open_immersion</code> just has some definition</p>

#### [ Kevin Buzzard (May 28 2018 at 14:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127204017):
<p>which explictly says what its F bit is</p>

#### [ Kevin Buzzard (May 28 2018 at 14:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127204021):
<p>and so probably this expands out to something with no .F in, by rfl</p>

#### [ Kevin Buzzard (May 28 2018 at 14:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127204022):
<p>but how do I find out what it expands to without having to work it out myself?</p>

#### [ Kevin Buzzard (May 28 2018 at 14:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127204062):
<p>I can't unfold <code>presheaf_of_types_pullback_under_open_immersion</code></p>

#### [ Kevin Buzzard (May 28 2018 at 14:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127204066):
<p>Do people need more context?</p>

#### [ Kevin Buzzard (May 28 2018 at 14:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127204070):
<p>I can provide a MWE but I just wondered if I'd already said enough for someone to tell me a trick</p>

#### [ Patrick Massot (May 28 2018 at 14:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127204078):
<p>Did you try <code>dsimp at x</code>?</p>

#### [ Kevin Buzzard (May 28 2018 at 14:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127204083):
<p>I did</p>

#### [ Kevin Buzzard (May 28 2018 at 14:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127204089):
<p>it wasn't very effective</p>

#### [ Kevin Buzzard (May 28 2018 at 14:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127204090):
<p>it turned <code>presheaf_of_rings_pullback_under_open_immersion</code></p>

#### [ Kevin Buzzard (May 28 2018 at 14:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127204091):
<p>into <code>presheaf_of_types_pullback_under_open_immersion</code></p>

#### [ Kevin Buzzard (May 28 2018 at 14:42)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127204093):
<p>and then stopped</p>

#### [ Kevin Buzzard (May 28 2018 at 14:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127204146):
<p>Actually I should do it manually and see if it is refl</p>

#### [ Patrick Massot (May 28 2018 at 14:43)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127204154):
<p>Is it something I can git clone?</p>

#### [ Kevin Buzzard (May 28 2018 at 14:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127204298):
<p>I have just done a bunch of editing to scheme.lean but not committed or pushed or anything</p>

#### [ Kevin Buzzard (May 28 2018 at 14:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127204299):
<p>I'd rather just move all those edits to a different file</p>

#### [ Kevin Buzzard (May 28 2018 at 14:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127204303):
<p>can git help me here?</p>

#### [ Kevin Buzzard (May 28 2018 at 14:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127204309):
<p>i.e. I want to push the file I have open</p>

#### [ Kevin Buzzard (May 28 2018 at 14:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127204312):
<p>but unfortunately it's an important file which I just broke</p>

#### [ Kevin Buzzard (May 28 2018 at 14:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127204326):
<p>goofing around</p>

#### [ Patrick Massot (May 28 2018 at 14:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127204355):
<p>you could create a broken branch</p>

#### [ Kevin Buzzard (May 28 2018 at 14:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127204372):
<p>Can I do that in VS Code?</p>

#### [ Kevin Buzzard (May 28 2018 at 14:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127204380):
<p>I only have master</p>

#### [ Patrick Massot (May 28 2018 at 14:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127204398):
<p><code>git stash</code>, <code>git checkout -b experimental</code>, <code>git stash pop</code>, <code>git commit -a</code>, <code>git push --set-upstream experimental</code></p>

#### [ Kevin Buzzard (May 28 2018 at 14:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127204401):
<p>I've got it</p>

#### [ Patrick Massot (May 28 2018 at 14:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127204403):
<p>you can problably do it in VScode but it would be longer</p>

#### [ Kevin Buzzard (May 28 2018 at 14:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127204445):
<p>Oh crap I didn't stash</p>

#### [ Kevin Buzzard (May 28 2018 at 14:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127204449):
<p>is that an issue?</p>

#### [ Patrick Massot (May 28 2018 at 14:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127204453):
<p>maybe not</p>

#### [ Patrick Massot (May 28 2018 at 14:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127204459):
<p>it wrote that to be on the safe side</p>

#### [ Kevin Buzzard (May 28 2018 at 14:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127204471):
<div class="codehilite"><pre><span></span>      let y := (presheaf_of_types_pullback_under_open_immersion ((zariski.structure_presheaf_of_rings R).to_presheaf_of_types) id
</pre></div>

#### [ Kevin Buzzard (May 28 2018 at 14:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127204473):
<p>oops</p>

#### [ Kevin Buzzard (May 28 2018 at 14:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127204479):
<p><a href="https://github.com/kbuzzard/lean-stacks-project/blob/broken/src/scheme.lean#L495" target="_blank" title="https://github.com/kbuzzard/lean-stacks-project/blob/broken/src/scheme.lean#L495">https://github.com/kbuzzard/lean-stacks-project/blob/broken/src/scheme.lean#L495</a></p>

#### [ Kevin Buzzard (May 28 2018 at 14:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127204480):
<p>was what I meant to say</p>

#### [ Kevin Buzzard (May 28 2018 at 14:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127204485):
<p>line 495, I want to unfold that presheaf_of_types_pullback_under_open_immersion</p>

#### [ Kevin Buzzard (May 28 2018 at 14:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127204523):
<p>no</p>

#### [ Kevin Buzzard (May 28 2018 at 14:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127204528):
<p>I want Lean to unfold it</p>

#### [ Kevin Buzzard (May 28 2018 at 14:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127204532):
<p>I'm going to try it myself to see what I'm missing</p>

#### [ Patrick Massot (May 28 2018 at 15:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127205165):
<p>This is really irritating</p>

#### [ Kevin Buzzard (May 28 2018 at 15:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127206165):
<p>OK I minimised</p>

#### [ Kevin Buzzard (May 28 2018 at 15:38)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127206167):
<p><a href="https://gist.github.com/kbuzzard/e051858b8e3348e884610ace8cd87c20" target="_blank" title="https://gist.github.com/kbuzzard/e051858b8e3348e884610ace8cd87c20">https://gist.github.com/kbuzzard/e051858b8e3348e884610ace8cd87c20</a></p>

#### [ Kevin Buzzard (May 28 2018 at 15:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127206173):
<p>That is me setting up the theory of pre-semi-sheaves</p>

#### [ Kevin Buzzard (May 28 2018 at 15:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127206176):
<p>which are a bit like distribs</p>

#### [ Kevin Buzzard (May 28 2018 at 15:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127206178):
<p>and although the objects are a bit silly</p>

#### [ Kevin Buzzard (May 28 2018 at 15:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127206184):
<p>I have tried to set up the theory in a sensible way</p>

#### [ Kevin Buzzard (May 28 2018 at 15:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127206235):
<p>and to create Line 53 of that script I had to do some work</p>

#### [ Kevin Buzzard (May 28 2018 at 15:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127206236):
<p>which I am convinced a computer could have done for me</p>

#### [ Kevin Buzzard (May 28 2018 at 15:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127206243):
<p>I cut and pasted the definition of <code>pre_semi_sheaf_of_rings_pullback</code></p>

#### [ Kevin Buzzard (May 28 2018 at 15:40)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127206245):
<p>because I wanted to know what would happen if I unfolded it</p>

#### [ Kevin Buzzard (May 28 2018 at 15:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127206254):
<p>but the problem is that the unfolding is refl</p>

#### [ Kevin Buzzard (May 28 2018 at 15:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127206257):
<p>so the lemma has no name and I can't rewrite it to see what the answer is</p>

#### [ Kevin Buzzard (May 28 2018 at 15:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127206258):
<p>I have to work it out myself</p>

#### [ Kevin Buzzard (May 28 2018 at 15:41)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127206265):
<p>This is an independent question</p>

#### [ Johan Commelin (May 28 2018 at 15:45)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127206396):
<p>(Aside: Kevin, you can tell Github that your gist is a lean file. Then you/we have syntax highlighting.)</p>

#### [ Kevin Buzzard (May 28 2018 at 15:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127206440):
<p>Oh cool</p>

#### [ Kevin Buzzard (May 28 2018 at 15:46)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127206445):
<p>but OK I have finally minimised my question</p>

#### [ Kevin Buzzard (May 28 2018 at 15:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127206468):
<p>my question is this gist which I'll attempt to highlight properly</p>

#### [ Kevin Buzzard (May 28 2018 at 15:47)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127206469):
<p><a href="https://gist.github.com/kbuzzard/123384f9132d6db8650c3484e42bda81" target="_blank" title="https://gist.github.com/kbuzzard/123384f9132d6db8650c3484e42bda81">https://gist.github.com/kbuzzard/123384f9132d6db8650c3484e42bda81</a></p>

#### [ Kevin Buzzard (May 28 2018 at 15:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127206511):
<p>That's my challenge to the CS people, I think</p>

#### [ Kevin Buzzard (May 28 2018 at 15:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127206515):
<p>I'm not sure I can prove that goal</p>

#### [ Kevin Buzzard (May 28 2018 at 15:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127206517):
<p>I'm not even sure that goal is true</p>

#### [ Kevin Buzzard (May 28 2018 at 15:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127206519):
<p>but I think it is</p>

#### [ Kevin Buzzard (May 28 2018 at 15:48)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127206521):
<p>for some reason it's a pain to prove though</p>

#### [ Kevin Buzzard (May 28 2018 at 15:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127206545):
<p>I'm hoping the file is fairly self-explanatory</p>

#### [ Johan Commelin (May 28 2018 at 15:49)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127206550):
<p>It is "math-true", right?</p>

#### [ Kevin Buzzard (May 28 2018 at 15:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127206592):
<p>exactly Johan</p>

#### [ Kevin Buzzard (May 28 2018 at 15:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127206597):
<p>Before I had something which was math-true</p>

#### [ Kevin Buzzard (May 28 2018 at 15:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127206600):
<p>and Kenny and Mario kept telling me it could be done by simp</p>

#### [ Kevin Buzzard (May 28 2018 at 15:50)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127206603):
<p>I would like them to tell me how to do this one</p>

#### [ Johan Commelin (May 28 2018 at 15:52)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127206673):
<p>Are the rings essential to the problem?</p>

#### [ Johan Commelin (May 28 2018 at 15:53)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127206679):
<p>Or could you just use semi-quasi-demi-pre-sheaves of types?</p>

#### [ Kevin Buzzard (May 28 2018 at 15:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127206859):
<p>No it's crucial they're rings</p>

#### [ Kevin Buzzard (May 28 2018 at 15:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127206863):
<p>because it's a trivial way to make it even harder</p>

#### [ Kevin Buzzard (May 28 2018 at 15:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127206876):
<p>this is a content-free statement from where I'm standing</p>

#### [ Kevin Buzzard (May 28 2018 at 15:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127206880):
<p>and if there aren't algorithms which currently prove content-free statements like this</p>

#### [ Kevin Buzzard (May 28 2018 at 15:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127206883):
<p>then I think that mathematicians will find it hard to learn Lean</p>

#### [ Kevin Buzzard (May 28 2018 at 15:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127206885):
<p><span class="user-mention" data-user-id="110064">@Kenny Lau</span> <span class="user-mention" data-user-id="110049">@Mario Carneiro</span> Can you fill in my sorry?</p>

#### [ Kevin Buzzard (May 28 2018 at 15:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127206888):
<p>Am I missing something easy?</p>

#### [ Patrick Massot (May 28 2018 at 16:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127206939):
<p>Oh, he went back a couple of stages</p>

#### [ Kevin Buzzard (May 28 2018 at 16:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127206941):
<p>I removed topology</p>

#### [ Kevin Buzzard (May 28 2018 at 16:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127206944):
<p>and open immersions</p>

#### [ Kenny Lau (May 28 2018 at 16:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127206945):
<blockquote>
<p>Am I missing something easy?</p>
</blockquote>
<p>no</p>

#### [ Kevin Buzzard (May 28 2018 at 16:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127206948):
<p>crap</p>

#### [ Kevin Buzzard (May 28 2018 at 16:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127206950):
<p>is that a provable but hard goal?</p>

#### [ Kenny Lau (May 28 2018 at 16:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127206953):
<p>well not really hard</p>

#### [ Kenny Lau (May 28 2018 at 16:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127206954):
<p>i could do it</p>

#### [ Kenny Lau (May 28 2018 at 16:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127206957):
<p>but not exactly easy</p>

#### [ Kevin Buzzard (May 28 2018 at 16:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127206958):
<p>Teach me how to do it</p>

#### [ Kevin Buzzard (May 28 2018 at 16:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127206962):
<p>I can't do it</p>

#### [ Kevin Buzzard (May 28 2018 at 16:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127206963):
<p>and it's obvious</p>

#### [ Kevin Buzzard (May 28 2018 at 16:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127206968):
<p>and these are my least favourite things in Lean</p>

#### [ Kevin Buzzard (May 28 2018 at 16:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127206970):
<p>teach me how to kill this pokemon</p>

#### [ Johan Commelin (May 28 2018 at 16:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127206971):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> you don't only want <code>schoolkid</code> tactic, you also want <code>kenny_lau</code> and <code>mario_carneiro</code></p>

#### [ Kevin Buzzard (May 28 2018 at 16:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127206972):
<p>exactly</p>

#### [ Kevin Buzzard (May 28 2018 at 16:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127206974):
<p>Kenny</p>

#### [ Kevin Buzzard (May 28 2018 at 16:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127206975):
<p>I'm up to here</p>

#### [ Kevin Buzzard (May 28 2018 at 16:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127206977):
<div class="codehilite"><pre><span></span><span class="kn">theorem</span> <span class="n">pre_semi_sheaves_iso</span> <span class="o">(</span><span class="n">X</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">(</span><span class="n">F</span> <span class="o">:</span> <span class="n">pre_semi_sheaf_of_rings</span> <span class="n">X</span><span class="o">)</span> <span class="o">:</span>
<span class="n">are_isomorphic_pre_semi_sheaves_of_rings</span>
    <span class="o">(</span><span class="n">pre_semi_sheaf_of_rings_pullback</span> <span class="n">F</span> <span class="n">id</span><span class="o">)</span> <span class="n">F</span>
<span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">constructor</span><span class="o">,</span>
  <span class="o">{</span> <span class="n">constructor</span><span class="o">,</span><span class="n">tactic</span><span class="bp">.</span><span class="n">swap</span><span class="o">,</span>
    <span class="o">{</span> <span class="n">constructor</span><span class="o">,</span><span class="n">tactic</span><span class="bp">.</span><span class="n">swap</span><span class="o">,</span>
      <span class="o">{</span> <span class="n">intros</span> <span class="n">U</span> <span class="n">s</span><span class="o">,</span>
        <span class="n">unfold</span> <span class="n">pre_semi_sheaf_of_rings_pullback</span><span class="o">,</span>
        <span class="n">suffices</span> <span class="o">:</span> <span class="n">F</span><span class="bp">.</span><span class="n">F</span> <span class="o">(</span><span class="n">id</span> <span class="err">&#39;&#39;</span> <span class="n">U</span><span class="o">),</span> <span class="k">by</span> <span class="n">simpa</span> <span class="kn">using</span> <span class="n">this</span><span class="o">,</span>
        <span class="k">have</span> <span class="n">reluctant_to_use</span> <span class="o">:</span> <span class="n">id</span> <span class="err">&#39;&#39;</span> <span class="n">U</span> <span class="bp">=</span> <span class="n">U</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">rw</span> <span class="n">set</span><span class="bp">.</span><span class="n">image_id</span><span class="o">,</span>
        <span class="n">rw</span> <span class="n">reluctant_to_use</span><span class="o">,</span>
        <span class="n">exact</span> <span class="n">s</span><span class="o">,</span>
      <span class="o">},</span>
      <span class="n">intro</span> <span class="n">U</span><span class="o">,</span>
      <span class="n">simp</span><span class="o">,</span>
      <span class="n">sorry</span>
    <span class="o">},</span>
    <span class="n">sorry</span><span class="o">,</span>
  <span class="o">},</span>
  <span class="n">sorry</span><span class="o">,</span>
<span class="kn">end</span>
</pre></div>

#### [ Kenny Lau (May 28 2018 at 16:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127207029):
<p>I'm trying</p>

#### [ Kevin Buzzard (May 28 2018 at 16:02)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127207030):
<p>Thanks</p>

#### [ Kevin Buzzard (May 28 2018 at 16:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127207039):
<p>Are you writing a tactic?</p>

#### [ Kevin Buzzard (May 28 2018 at 16:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127207041):
<p>Don't try to solve the goal</p>

#### [ Kenny Lau (May 28 2018 at 16:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127207042):
<p>no</p>

#### [ Kevin Buzzard (May 28 2018 at 16:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127207043):
<p>try to write a tactic which solves the goal</p>

#### [ Kenny Lau (May 28 2018 at 16:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127207045):
<p>I don't know how to write tactics</p>

#### [ Kevin Buzzard (May 28 2018 at 16:03)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127207046):
<p>because this goal is solved by math_trivial</p>

#### [ Kevin Buzzard (May 28 2018 at 16:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127207095):
<p>This goal is the nightmare which I could avoid in my case of presheaves</p>

#### [ Kevin Buzzard (May 28 2018 at 16:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127207098):
<p>but a pre_semi_sheaf does not have res</p>

#### [ Kevin Buzzard (May 28 2018 at 16:04)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127207100):
<p>so you have to bite the bullet</p>

#### [ Kevin Buzzard (May 28 2018 at 16:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127207109):
<p><span class="user-mention" data-user-id="110026">@Simon Hudon</span> Can you solve my goal with a tactic?</p>

#### [ Kevin Buzzard (May 28 2018 at 16:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127207122):
<p><a href="https://gist.github.com/kbuzzard/123384f9132d6db8650c3484e42bda81" target="_blank" title="https://gist.github.com/kbuzzard/123384f9132d6db8650c3484e42bda81">https://gist.github.com/kbuzzard/123384f9132d6db8650c3484e42bda81</a></p>

#### [ Kevin Buzzard (May 28 2018 at 16:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127207124):
<p>Last line</p>

#### [ Kevin Buzzard (May 28 2018 at 16:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127207128):
<p>the pre_semi_sheaves are isomorphic via the identity map</p>

#### [ Kevin Buzzard (May 28 2018 at 16:05)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127207134):
<p>but checking the details is apparently a little tricky</p>

#### [ Kevin Buzzard (May 28 2018 at 16:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127207138):
<p>Would I have exactly the same problems in Mizar?</p>

#### [ Kevin Buzzard (May 28 2018 at 16:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127207186):
<p><span class="user-mention" data-user-id="110172">@Assia Mahboubi</span> Would my goal be any easier to solve in Coq?</p>

#### [ Kevin Buzzard (May 28 2018 at 16:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127207194):
<p>I have isolated a frustration I have with dependent type theory</p>

#### [ Kevin Buzzard (May 28 2018 at 16:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127207202):
<p>I need to define a map from <code>F U</code> to <code>F (id '' U)</code></p>

#### [ Kevin Buzzard (May 28 2018 at 16:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127207205):
<p>where <code>id '' U</code> is the image of the set U under the identity map</p>

#### [ Kevin Buzzard (May 28 2018 at 16:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127207244):
<p>I define the map by rewriting <code>id '' U = U</code> and then using the identity</p>

#### [ Kevin Buzzard (May 28 2018 at 16:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127207245):
<p>and I never recover</p>

#### [ Kevin Buzzard (May 28 2018 at 16:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127207253):
<p>But I don't know any other way of doing it</p>

#### [ Kevin Buzzard (May 28 2018 at 16:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127207319):
<p>Is there some sort of reason why I should not be proving this goal at all?</p>

#### [ Simon Hudon (May 28 2018 at 16:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127207481):
<p>How would you prove it without tactics?</p>

#### [ Kenny Lau (May 28 2018 at 16:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127207490):
<p>he can't function without tactics</p>

#### [ Kenny Lau (May 28 2018 at 16:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127207496):
<p>you would do <code>eq.drec</code> without tactics</p>

#### [ Simon Hudon (May 28 2018 at 16:24)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127207893):
<p>I mean, I don't know any of the context so I'm not sure how the definitions relate to each other</p>

#### [ Assia Mahboubi (May 28 2018 at 17:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127209693):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> It will take me some time to catch up, the thread is long. Why did you use this equality at all? Aren't <code>F U</code> and <code>F (id '' U)</code> the exact same thing (aka convertible?). How can I play your formalization?</p>

#### [ Kenny Lau (May 28 2018 at 17:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127209705):
<p><a href="https://gist.github.com/kbuzzard/123384f9132d6db8650c3484e42bda81" target="_blank" title="https://gist.github.com/kbuzzard/123384f9132d6db8650c3484e42bda81">https://gist.github.com/kbuzzard/123384f9132d6db8650c3484e42bda81</a></p>

#### [ Kenny Lau (May 28 2018 at 17:07)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127209710):
<p><span class="user-mention" data-user-id="110172">@Assia Mahboubi</span> just prove the above</p>

#### [ Kenny Lau (May 28 2018 at 17:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127209792):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> you know what, I take back my word, it's harder than I thought</p>

#### [ Assia Mahboubi (May 28 2018 at 17:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127209810):
<p>Hi <span class="user-mention" data-user-id="110064">@Kenny Lau</span> ! Thanks! But I am more ignorant than you think : I meant, what install instructions should I follow. I am not a regular Lean user.</p>

#### [ Kenny Lau (May 28 2018 at 17:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127209855):
<p>oh, sorry</p>

#### [ Kenny Lau (May 28 2018 at 17:10)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127209865):
<p>I think you can try it online</p>

#### [ Kenny Lau (May 28 2018 at 17:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127209872):
<p><a href="https://leanprover.github.io/live/latest/" target="_blank" title="https://leanprover.github.io/live/latest/">https://leanprover.github.io/live/latest/</a></p>

#### [ Assia Mahboubi (May 28 2018 at 17:11)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127209873):
<p>Ok thanks, I am doing that now.</p>

#### [ Kevin Buzzard (May 28 2018 at 17:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127209968):
<p>Does one run into the same issues in Coq?</p>

#### [ Kevin Buzzard (May 28 2018 at 17:13)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127209974):
<p>Does one run into the same issues in Mizar?</p>

#### [ Kevin Buzzard (May 28 2018 at 17:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127210018):
<p>Which systems is this easy in?</p>

#### [ Kevin Buzzard (May 28 2018 at 17:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127210029):
<p><span class="user-mention" data-user-id="110172">@Assia Mahboubi</span> I suspect you can see what I'm trying to do</p>

#### [ Kevin Buzzard (May 28 2018 at 17:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127210064):
<p>I'm happy to let a lean expert like Mario or Kenny solve the lean one</p>

#### [ Kevin Buzzard (May 28 2018 at 17:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127210072):
<p>I am trying to understand to what extent my worldview of mathematics is naive</p>

#### [ Kenny Lau (May 28 2018 at 17:15)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127210074):
<p>lol it's been an hour already</p>

#### [ Kevin Buzzard (May 28 2018 at 17:16)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127210131):
<p>The challenge was embedded well in a very long thread and I would imagine many have stopped reading</p>

#### [ Kevin Buzzard (May 28 2018 at 17:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127210149):
<p>One could ask in a new thread, I think this question is sufficiently interesting</p>

#### [ Kevin Buzzard (May 28 2018 at 17:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127210215):
<p>I am hoping that someone will come up with a curve ball solution of the form "don't prove that, prove something that implies that</p>

#### [ Kenny Lau (May 28 2018 at 17:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127210220):
<p>I tried to build up an interface</p>

#### [ Kenny Lau (May 28 2018 at 17:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127210221):
<p>didn't work</p>

#### [ Assia Mahboubi (May 28 2018 at 17:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127210326):
<p>Thanks <span class="user-mention" data-user-id="110064">@Kenny Lau</span>, it works like a charm. But unfortunately I will have to leave now (and I have not finished to read the problem <span class="emoji emoji-1f61e" title="disappointed">:disappointed:</span> ).  I will definitely look again later.</p>

#### [ Kenny Lau (May 28 2018 at 17:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127210332):
<p>see you</p>

#### [ Kevin Buzzard (May 28 2018 at 17:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127210576):
<p><span class="user-mention" data-user-id="110064">@Kenny Lau</span></p>

#### [ Kevin Buzzard (May 28 2018 at 17:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127210577):
<p>I had an idea</p>

#### [ Kevin Buzzard (May 28 2018 at 17:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127210579):
<p>but you would be quicker to implement it than me</p>

#### [ Kenny Lau (May 28 2018 at 17:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127210581):
<p>what is it</p>

#### [ Kevin Buzzard (May 28 2018 at 17:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127210583):
<p>and I have to tidy the kitchen anyway</p>

#### [ Kevin Buzzard (May 28 2018 at 17:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127210585):
<p>I claim that my definition is incomplete</p>

#### [ Kevin Buzzard (May 28 2018 at 17:28)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127210586):
<p>as far as Lean is concerned</p>

#### [ Kevin Buzzard (May 28 2018 at 17:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127210587):
<p>I am missing some extra structure</p>

#### [ Kevin Buzzard (May 28 2018 at 17:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127210591):
<p>which can be filled in easily</p>

#### [ Kevin Buzzard (May 28 2018 at 17:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127210600):
<p>Is the "correct" object a pre_semi_sheaf whatever, but also equipped with maps res : F U -&gt; F V whenever U = V</p>

#### [ Kevin Buzzard (May 28 2018 at 17:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127210603):
<p>plus axiom that res U U = id</p>

#### [ Kevin Buzzard (May 28 2018 at 17:29)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127210604):
<p>plus axiom of composition</p>

#### [ Kevin Buzzard (May 28 2018 at 17:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127210649):
<p>res U V then res V W is res U W</p>

#### [ Kevin Buzzard (May 28 2018 at 17:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127210654):
<p>Given my stupid annoying structure</p>

#### [ Kevin Buzzard (May 28 2018 at 17:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127210655):
<p>can it be beefed up to such a structure</p>

#### [ Kevin Buzzard (May 28 2018 at 17:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127210657):
<p>and for this beefed-up structure</p>

#### [ Kevin Buzzard (May 28 2018 at 17:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127210659):
<p>can the map be defined to be res</p>

#### [ Kevin Buzzard (May 28 2018 at 17:30)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127210673):
<p>and then we deduce the result for the stupid structure</p>

#### [ Kevin Buzzard (May 28 2018 at 17:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127210679):
<p>My experience with schemes tells me</p>

#### [ Kevin Buzzard (May 28 2018 at 17:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127210680):
<p>that when the map is res</p>

#### [ Kevin Buzzard (May 28 2018 at 17:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127210684):
<p>all the hard proofs become rfl</p>

#### [ Kevin Buzzard (May 28 2018 at 17:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127210688):
<p>maybe not the ring one</p>

#### [ Kevin Buzzard (May 28 2018 at 17:31)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127210690):
<p>the ring one we have to use some equiv tactic thing</p>

#### [ Reid Barton (May 28 2018 at 20:17)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127216106):
<p><span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> </p>
<div class="codehilite"><pre><span></span><span class="kn">definition</span> <span class="n">pre_semi_sheaf_of_rings_pullback_setmap</span>
  <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">}</span>
  <span class="o">{</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">}</span>
  <span class="o">(</span><span class="n">PR</span> <span class="o">:</span> <span class="n">pre_semi_sheaf_of_rings</span> <span class="n">β</span><span class="o">)</span>
  <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">set</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">set</span> <span class="n">β</span><span class="o">)</span>
  <span class="o">:</span> <span class="n">pre_semi_sheaf_of_rings</span> <span class="n">α</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">F</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">V</span><span class="o">,</span><span class="n">PR</span><span class="bp">.</span><span class="n">F</span> <span class="o">(</span><span class="n">f</span> <span class="n">V</span><span class="o">)</span>
<span class="o">}</span>

<span class="kn">theorem</span> <span class="n">pre_semi_sheaves_iso_setmap</span> <span class="o">(</span><span class="n">X</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">(</span><span class="n">F</span> <span class="o">:</span> <span class="n">pre_semi_sheaf_of_rings</span> <span class="n">X</span><span class="o">)</span> <span class="o">:</span>
<span class="n">are_isomorphic_pre_semi_sheaves_of_rings</span>
    <span class="o">(</span><span class="n">pre_semi_sheaf_of_rings_pullback_setmap</span> <span class="n">F</span> <span class="n">id</span><span class="o">)</span> <span class="n">F</span> <span class="o">:=</span>
<span class="bp">⟨⟨λ</span> <span class="o">(</span><span class="n">U</span> <span class="o">:</span> <span class="n">set</span> <span class="n">X</span><span class="o">),</span> <span class="n">id</span><span class="o">,</span> <span class="k">by</span> <span class="n">apply_instance</span><span class="bp">⟩</span><span class="o">,</span>
 <span class="bp">⟨λ</span> <span class="o">(</span><span class="n">U</span> <span class="o">:</span> <span class="n">set</span> <span class="n">X</span><span class="o">),</span> <span class="n">id</span><span class="o">,</span> <span class="k">by</span> <span class="n">apply_instance</span><span class="bp">⟩</span><span class="o">,</span>
 <span class="bp">λ</span> <span class="bp">_</span><span class="o">,</span> <span class="n">rfl</span><span class="o">,</span> <span class="bp">λ</span> <span class="bp">_</span><span class="o">,</span> <span class="n">rfl</span><span class="bp">⟩</span>

<span class="kn">definition</span> <span class="n">pre_semi_sheaf_of_rings_pullback</span>
  <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">}</span>
  <span class="o">{</span><span class="n">β</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">}</span>
  <span class="o">(</span><span class="n">PR</span> <span class="o">:</span> <span class="n">pre_semi_sheaf_of_rings</span> <span class="n">β</span><span class="o">)</span>
  <span class="o">(</span><span class="n">f</span> <span class="o">:</span> <span class="n">α</span> <span class="bp">→</span> <span class="n">β</span><span class="o">)</span>
  <span class="o">:</span> <span class="n">pre_semi_sheaf_of_rings</span> <span class="n">α</span> <span class="o">:=</span>
<span class="o">{</span> <span class="n">F</span> <span class="o">:=</span> <span class="bp">λ</span> <span class="n">V</span><span class="o">,</span><span class="n">PR</span><span class="bp">.</span><span class="n">F</span> <span class="o">(</span><span class="n">f</span> <span class="err">&#39;&#39;</span> <span class="n">V</span><span class="o">)</span>
<span class="o">}</span>

<span class="kn">theorem</span> <span class="n">pre_semi_sheaves_iso</span> <span class="o">(</span><span class="n">X</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">(</span><span class="n">F</span> <span class="o">:</span> <span class="n">pre_semi_sheaf_of_rings</span> <span class="n">X</span><span class="o">)</span> <span class="o">:</span>
<span class="n">are_isomorphic_pre_semi_sheaves_of_rings</span>
    <span class="o">(</span><span class="n">pre_semi_sheaf_of_rings_pullback</span> <span class="n">F</span> <span class="n">id</span><span class="o">)</span> <span class="n">F</span>
<span class="o">:=</span> <span class="k">begin</span>
  <span class="n">convert</span> <span class="n">pre_semi_sheaves_iso_setmap</span> <span class="n">X</span> <span class="n">F</span><span class="o">,</span>
  <span class="n">change</span> <span class="n">pre_semi_sheaf_of_rings_pullback_setmap</span> <span class="n">F</span> <span class="o">(</span><span class="bp">λ</span> <span class="n">U</span><span class="o">,</span> <span class="n">id</span> <span class="err">&#39;&#39;</span> <span class="n">U</span><span class="o">)</span> <span class="bp">=</span> <span class="bp">_</span><span class="o">,</span>
  <span class="n">congr</span><span class="o">,</span> <span class="n">funext</span> <span class="n">U</span><span class="o">,</span> <span class="n">simp</span> <span class="o">[</span><span class="n">set</span><span class="bp">.</span><span class="n">image_id</span><span class="o">]</span>
<span class="kn">end</span>
</pre></div>

#### [ Kevin Buzzard (May 28 2018 at 20:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127216158):
<p>I was hoping you'd show up</p>

#### [ Kevin Buzzard (May 28 2018 at 20:18)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127216160):
<p>I thought you'd like this one</p>

#### [ Kevin Buzzard (May 28 2018 at 20:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127216179):
<p>I am cooking, will look later. Did you do it?</p>

#### [ Reid Barton (May 28 2018 at 20:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127216188):
<p>Yes</p>

#### [ Kevin Buzzard (May 28 2018 at 20:19)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127216190):
<p>Convert? What does that do?</p>

#### [ Reid Barton (May 28 2018 at 20:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127216241):
<p>I split your construction into two pieces: pullback of a presheaf by a functor between sites and the functor between sites induced by a map of spaces</p>

#### [ Reid Barton (May 28 2018 at 20:20)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127216251):
<p><code>convert</code> basically says "this is the term I want to be the proof, aside from some fiddling about the type not being definitionally equal to the desired one"</p>

#### [ Reid Barton (May 28 2018 at 20:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127216267):
<p>so it generates a new goal which is that the type of the term you provided is the same as the goal type</p>

#### [ Mario Carneiro (May 28 2018 at 21:56)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127219336):
<blockquote>
<p><a href="#narrow/stream/116395-maths/subject/ZFC.20equality/near/127204479" title="#narrow/stream/116395-maths/subject/ZFC.20equality/near/127204479">https://leanprover.zulipchat.com/#narrow/stream/116395-maths/subject/ZFC.20equality/near/127204479</a></p>
</blockquote>
<p>Here's how you can use <code>cast</code> as a morphism without any <code>res</code> trickery:</p>
<div class="codehilite"><pre><span></span>def pre_semi_sheaf_of_rings.cast {α} (FPT : pre_semi_sheaf_of_rings α)
  {U V : set α} (e : U = V) : FPT.F U → FPT.F V :=
cast (congr_arg _ e)

instance pre_semi_sheaf_of_rings.cast.is_ring_hom
  {α} (FPT : pre_semi_sheaf_of_rings α) {U V : set α} (e : U = V) :
  is_ring_hom (FPT.cast e) :=
by subst e; exact is_ring_hom.id

theorem pre_semi_sheaf_of_rings.cast_comp
  {α} (FPT : pre_semi_sheaf_of_rings α) {U V W : set α}
  (e₁ : U = V) (e₂ : V = W) (a) :
  FPT.cast e₂ (FPT.cast e₁ a) = FPT.cast (e₁.trans e₂) a :=
by substs e₂ e₁; exact rfl

theorem presheaves_iso (X : Type) (F : pre_semi_sheaf_of_rings X) :
are_isomorphic_pre_semi_sheaves_of_rings
    (pre_semi_sheaf_of_rings_pullback F id) F :=
begin
  refine ⟨⟨λ U, F.cast (by simp), by apply_instance⟩,
     ⟨λ U, F.cast (by simp), by apply_instance⟩, _, _⟩;
  { intros U, funext a,
    dsimp [is_identity_morphism_of_pre_semi_sheaves_of_rings,
      composition_of_morphisms_of_pre_semi_sheaves_of_rings],
    rw F.cast_comp, refl }
end
</pre></div>

#### [ Patrick Massot (May 29 2018 at 10:51)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127241361):
<blockquote>
<p>I think you can try it online</p>
</blockquote>
<p>I think it's a bad idea to tell people to use the online version. Maybe it's my computer fault, but I find it too slow to be usable. I think it's very bad advertisement. So let me try something new: <a href="https://www.math.u-psud.fr/~pmassot/en/misc/index.html" target="_blank" title="https://www.math.u-psud.fr/~pmassot/en/misc/index.html">https://www.math.u-psud.fr/~pmassot/en/misc/index.html</a> <span class="user-mention" data-user-id="110172">@Assia Mahboubi</span> I guess you have a Debian/Ubuntu computer at hand. Could you try using my installation script? It's meant to be a single step, one minute fully setup Lean install  (this obviously includes a compiled mathlib).</p>

#### [ Johan Commelin (May 29 2018 at 10:54)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127241525):
<p>Does <code>https://www.math.u-psud.fr/~pmassot/files/lean/install_lean.sh</code> contain precompiled mathlib nightlies?</p>

#### [ Patrick Massot (May 29 2018 at 10:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127241534):
<p>yes</p>

#### [ Johan Commelin (May 29 2018 at 10:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127241549):
<p>Nice! I guess in this file, right? <code>https://www.math.u-psud.fr/~pmassot/files/lean/.lean.tar.gz</code></p>

#### [ Patrick Massot (May 29 2018 at 10:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127241555):
<p>yes</p>

#### [ Johan Commelin (May 29 2018 at 10:55)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127241560):
<p>Ok, you should change the topic of your anouncement. This deserves more PR.</p>

#### [ Patrick Massot (May 29 2018 at 10:57)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127241637):
<p>I think this deserves to be taken up by Mario and Johannes. Right now, I set up an emergency solution. I don't want Assia to go away because Javascript was never meant to run proof assistants</p>

#### [ Patrick Massot (May 29 2018 at 10:58)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127241710):
<p>But now I need to stop. This was meant to be a no Lean day. I'll go to my IHES office where I can't install anything on the computer (and nothing Lean related is pre-installed) and get some real work done</p>

#### [ Patrick Massot (May 29 2018 at 10:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127241720):
<p>Have fun!</p>

#### [ Assia Mahboubi (May 29 2018 at 10:59)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127241724):
<p>Hi <span class="user-mention" data-user-id="110031">@Patrick Massot</span> . Yes, it was very slow and I eventually gave up. I was planning to (re)install Lean on my machine today. What is your script doing? Will it be easy for me to update my Lean later? My plan is to look at <span class="user-mention" data-user-id="110038">@Kevin Buzzard</span> 's stack project and he says <a href="https://github.com/kbuzzard/lean-stacks-project" target="_blank" title="https://github.com/kbuzzard/lean-stacks-project">here</a> that I need a version from nightly of 2018-04-06. Does it matter? And yes, I have Debian/Ubuntu OS.</p>

#### [ Patrick Massot (May 29 2018 at 11:00)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127241791):
<p>It does what it says in <a href="https://www.math.u-psud.fr/~pmassot/files/lean/install_lean.sh" target="_blank" title="https://www.math.u-psud.fr/~pmassot/files/lean/install_lean.sh">https://www.math.u-psud.fr/~pmassot/files/lean/install_lean.sh</a></p>

#### [ Patrick Massot (May 29 2018 at 11:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127241810):
<p>install VScode using MS debian package, manually install the Lean extension, download Lean 3.4.1 and set the bash path variable, download precompiled mathlib</p>

#### [ Patrick Massot (May 29 2018 at 11:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127241834):
<p>Let me check you can run Kevin's code using this version of mathlib</p>

#### [ Johan Commelin (May 29 2018 at 11:01)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127241835):
<p>[sorry, wrong topic]</p>

#### [ Assia Mahboubi (May 29 2018 at 11:06)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127242075):
<p><span class="user-mention" data-user-id="110031">@Patrick Massot</span> Thanks for the answer to my silly question: I should have open the file first. It looks great. I'll wait from a confirmation (from you or from anyone else) and try (I guess that otherwise it's just a matter of changing a couple of lines in your script). Happy no-Lean day.</p>

#### [ Johan Commelin (May 29 2018 at 11:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127242147):
<p><span class="user-mention" data-user-id="110172">@Assia Mahboubi</span> It will be super easy to update Lean later.</p>

#### [ Johan Commelin (May 29 2018 at 11:08)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127242154):
<p>Patrick's script just puts together the steps that you would otherwise perform manually.</p>

#### [ Johan Commelin (May 29 2018 at 11:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127242162):
<p>And he has compiled mathlib for you. Which saves you an hour of coffee breaks <span class="emoji emoji-1f609" title="wink">:wink:</span></p>

#### [ Assia Mahboubi (May 29 2018 at 11:09)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127242169):
<p>Hi <span class="user-mention" data-user-id="112680">@Johan Commelin</span> , thanks for the help. I am trying it now.</p>

#### [ Patrick Massot (May 29 2018 at 11:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127242352):
<p>It seems you still need to manually copy mathlib to the stacks directory. Maybe I shouldn't have skipped using Sbeastian's elan. So, after running my script, the next steps are: <code>git clone https://github.com/kbuzzard/lean-stacks-project.git</code> then <code>cp -r ~/.lean/_target/ lean-stacks-project</code> then <code>cd lean-stacks-project</code>, <code>lean --make</code></p>

#### [ Patrick Massot (May 29 2018 at 11:14)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127242357):
<p>There will probably be some errors because this repo is still a messy playground</p>

#### [ Patrick Massot (May 29 2018 at 11:21)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127242554):
<p>Ok, I confirm I'm able to do that and then open the lean-stacvks-project folder in VScode and open scheme.lean without error. Assia: the first command to learn after opening a Lean file in VScode (and putting the cursor anywhere in that file) is Ctrl-shift-return which opens the Lean message window where all the interesting communication with lean takes place</p>

#### [ Patrick Massot (May 29 2018 at 11:22)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127242565):
<p>Now I'll really go to IHES where I'll probably open Zulip anyway, but not VScode</p>

#### [ Assia Mahboubi (May 29 2018 at 11:27)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127242718):
<p>Thanks again! Meanwhile I tried the instruction provided in the README.md (using <code>leanpkg</code>) and it is now indeed building stuff. If it goes wrong I''fall back to your suggestion.</p>

#### [ Assia Mahboubi (May 29 2018 at 11:32)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127242887):
<p>It's very long (and warms my office) : it seems that a mathlib has been copied and is being re-compiled in a <code>_target/dep</code> sub-directory...</p>

#### [ Johan Commelin (May 29 2018 at 11:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127242954):
<p>Yes, we know that feeling... (-;</p>

#### [ Johan Commelin (May 29 2018 at 11:35)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127242957):
<p>I wasn't joking when I told you about the "hour of coffee breaks"</p>

#### [ Patrick Massot (May 29 2018 at 11:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127243006):
<p>This is exactly what I tried to avoid</p>

#### [ Patrick Massot (May 29 2018 at 11:37)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127243011):
<p>My instructions should bypass mathlib compilation</p>

#### [ Patrick Massot (May 29 2018 at 11:39)](https://leanprover.zulipchat.com/#narrow/stream/116395-maths/topic/ZFC%20equality/near/127243059):
<p>(I'm waiting for my train)</p>


{% endraw %}
