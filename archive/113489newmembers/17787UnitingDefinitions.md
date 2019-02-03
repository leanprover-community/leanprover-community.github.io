---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/17787UnitingDefinitions.html
---

## Stream: [new members](index.html)
### Topic: [Uniting Definitions](17787UnitingDefinitions.html)

---


{% raw %}
#### [ Ali Sever (Jul 28 2018 at 10:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Uniting%20Definitions/near/130457466):
<p>Is there a way I can join perp, perp1 and perp2 into 1 definition? Same thing for perpx.  <code>l : point → point → set point</code></p>
<div class="codehilite"><pre><span></span><span class="n">def</span> <span class="n">perpx</span> <span class="o">(</span><span class="n">x</span> <span class="o">:</span> <span class="n">point</span><span class="o">)</span> <span class="o">(</span><span class="n">A</span> <span class="n">A&#39;</span> <span class="o">:</span> <span class="n">set</span> <span class="n">point</span><span class="o">)</span> <span class="o">:</span> <span class="kt">Prop</span> <span class="o">:=</span> <span class="n">line</span> <span class="n">A</span> <span class="bp">∧</span> <span class="n">line</span> <span class="n">A&#39;</span> <span class="bp">∧</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">A</span> <span class="bp">∧</span> <span class="n">x</span> <span class="err">∈</span> <span class="n">A&#39;</span> <span class="bp">∧</span>
<span class="bp">∀</span> <span class="n">u</span> <span class="n">v</span><span class="o">,</span> <span class="n">u</span> <span class="err">∈</span> <span class="n">A</span> <span class="bp">→</span> <span class="n">v</span> <span class="err">∈</span> <span class="n">A&#39;</span> <span class="bp">→</span> <span class="n">R</span> <span class="n">u</span> <span class="n">x</span> <span class="n">v</span>

<span class="n">def</span> <span class="n">perpx1</span> <span class="o">(</span><span class="n">x</span> <span class="n">a</span> <span class="n">b</span> <span class="o">:</span> <span class="n">point</span><span class="o">)</span> <span class="o">(</span><span class="n">A</span> <span class="o">:</span> <span class="n">set</span> <span class="n">point</span><span class="o">)</span> <span class="o">:</span> <span class="kt">Prop</span> <span class="o">:=</span> <span class="n">a</span> <span class="bp">≠</span> <span class="n">b</span> <span class="bp">∧</span> <span class="n">perpx</span> <span class="n">x</span> <span class="n">A</span> <span class="o">(</span><span class="n">l</span> <span class="n">a</span> <span class="n">b</span><span class="o">)</span>

<span class="n">def</span> <span class="n">perpx2</span> <span class="o">(</span><span class="n">x</span> <span class="n">a</span> <span class="n">b</span> <span class="n">c</span> <span class="n">d</span> <span class="o">:</span> <span class="n">point</span><span class="o">)</span> <span class="o">:</span> <span class="kt">Prop</span> <span class="o">:=</span> <span class="n">a</span> <span class="bp">≠</span> <span class="n">b</span> <span class="bp">∧</span> <span class="n">c</span> <span class="bp">≠</span> <span class="n">d</span> <span class="bp">∧</span> <span class="n">perpx</span> <span class="n">x</span> <span class="o">(</span><span class="n">l</span> <span class="n">a</span> <span class="n">b</span><span class="o">)</span> <span class="o">(</span><span class="n">l</span> <span class="n">c</span> <span class="n">d</span><span class="o">)</span>

<span class="n">def</span> <span class="n">perp</span> <span class="o">(</span><span class="n">A</span> <span class="n">A&#39;</span> <span class="o">:</span> <span class="n">set</span> <span class="n">point</span><span class="o">)</span> <span class="o">:</span> <span class="kt">Prop</span> <span class="o">:=</span> <span class="bp">∃</span> <span class="n">x</span><span class="o">,</span> <span class="n">perpx</span> <span class="n">x</span> <span class="n">A</span> <span class="n">A&#39;</span>

<span class="n">def</span> <span class="n">perp1</span> <span class="o">(</span><span class="n">a</span> <span class="n">b</span> <span class="o">:</span> <span class="n">point</span><span class="o">)</span> <span class="o">(</span><span class="n">A</span> <span class="o">:</span> <span class="n">set</span> <span class="n">point</span><span class="o">)</span> <span class="o">:</span> <span class="kt">Prop</span> <span class="o">:=</span> <span class="n">a</span> <span class="bp">≠</span> <span class="n">b</span> <span class="bp">∧</span> <span class="n">perp</span> <span class="n">A</span> <span class="o">(</span><span class="n">l</span> <span class="n">a</span> <span class="n">b</span><span class="o">)</span>

<span class="n">def</span> <span class="n">perp2</span> <span class="o">(</span><span class="n">a</span> <span class="n">b</span> <span class="n">c</span> <span class="n">d</span> <span class="o">:</span> <span class="n">point</span><span class="o">)</span> <span class="o">:</span> <span class="kt">Prop</span> <span class="o">:=</span> <span class="n">a</span> <span class="bp">≠</span> <span class="n">b</span> <span class="bp">∧</span> <span class="n">c</span> <span class="bp">≠</span> <span class="n">d</span> <span class="bp">∧</span> <span class="n">perp</span> <span class="o">(</span><span class="n">l</span> <span class="n">a</span> <span class="n">b</span><span class="o">)</span> <span class="o">(</span><span class="n">l</span> <span class="n">c</span> <span class="n">d</span><span class="o">)</span>

<span class="kn">notation</span> <span class="n">A</span> <span class="err">⊥</span> <span class="n">B</span>  <span class="o">:=</span> <span class="n">perp</span> <span class="n">A</span> <span class="n">B</span>

<span class="kn">notation</span> <span class="n">A</span> <span class="err">⊥</span> <span class="n">B</span> <span class="err">%</span> <span class="n">x</span>  <span class="o">:=</span> <span class="n">perpx</span> <span class="n">x</span> <span class="n">A</span> <span class="n">B</span>
</pre></div>

#### [ Kevin Buzzard (Jul 28 2018 at 11:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Uniting%20Definitions/near/130457657):
<p>I don't understand the question. What are you unhappy about with what you have?</p>

#### [ Ali Sever (Jul 28 2018 at 11:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Uniting%20Definitions/near/130457768):
<p>If I leave it like this, I'm going to have to prove everything three times.</p>

#### [ Kevin Buzzard (Jul 28 2018 at 11:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Uniting%20Definitions/near/130458494):
<p>Are you likely to ever apply <code>perp</code> in a situation where <code>A</code> and <code>A'</code> are not lines?</p>

#### [ Kevin Buzzard (Jul 28 2018 at 11:27)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Uniting%20Definitions/near/130458495):
<p>I mean, where you don't already know that they're lines?</p>

#### [ Kevin Buzzard (Jul 28 2018 at 11:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Uniting%20Definitions/near/130458535):
<p>What I'm saying is that it sounds to me like the fact that <code>A</code> is a line should be a hypothesis rather than a conclusion of <code>perp</code></p>

#### [ Kevin Buzzard (Jul 28 2018 at 11:31)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Uniting%20Definitions/near/130458612):
<p>Presumably<code> R</code> is "these three points make a right angle"? Don't you want something like<br>
<code>def perpx (x : point) {A A' : set point} (HLA : line A) (HLA' : line A') (HxA : x ∈ A) (HxA' : x ∈ A') :=
∀ u v, u ∈ A → v ∈ A' → R u x v</code>?</p>

#### [ Kevin Buzzard (Jul 28 2018 at 11:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Uniting%20Definitions/near/130458720):
<p><code>def perp {A A' : set point} (HLA : line A) (HLA' : line A') : Prop := ∃ x, perpx x A A'</code></p>

#### [ Kevin Buzzard (Jul 28 2018 at 11:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Uniting%20Definitions/near/130458723):
<p>I'm just guessing -- but it sounds like you want <code>perp</code> to be a predicate which applies only to lines, so you should demand only lines as input. Do you want to apply the idea in other situations?</p>

#### [ Ali Sever (Jul 28 2018 at 11:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Uniting%20Definitions/near/130459039):
<p>What if I want to prove <code>perp A A' → something</code>? From the assumption I can obtain a proof of <code>line A</code> and <code>line A'</code>, but in your definition,  I have to add those to the hypotheses of every theorem.</p>

#### [ Kevin Buzzard (Jul 28 2018 at 11:46)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Uniting%20Definitions/near/130459044):
<p>So you're telling me that you can envisage a situation where you have no idea that <code>A</code> and <code>A'</code> are lines, but you've managed to prove <code>perp A A'</code> anyway?</p>

#### [ Johan Commelin (Jul 28 2018 at 11:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Uniting%20Definitions/near/130459059):
<p>Ali, that is where <code>variables</code> come in handy. Then you don't have to explicitly write them down in the statement of every theorem. You just write them once at the beginning of your section/file.</p>

#### [ Johan Commelin (Jul 28 2018 at 11:48)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Uniting%20Definitions/near/130459100):
<p>Also, I can imagine that <code>line</code> can be a class, and then type class inference will (hopefully) keep track of which things are proven to be lines.</p>

#### [ Kevin Buzzard (Jul 28 2018 at 11:49)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Uniting%20Definitions/near/130459109):
<p>I feel like you're saying the analogue of something like: "I want to define <code>a&lt;b</code> for <code>a</code> and <code>b</code> arbitrary things, and I want it to mean "<code>a</code> and <code>b</code> are numbers, and <code>a&lt;b</code>". And I'm saying "but we already have <code>a&lt;b</code> for numbers -- why would you want to talk about arbitrary things which you don't even know are numbers and then start talking about whether one is less than the other? In all cases where it even makes sense to talk about this, you know <code>a</code> and <code>b</code> are numbers, so that assumption should be an input not an output."</p>

#### [ Ali Sever (Jul 28 2018 at 11:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Uniting%20Definitions/near/130459201):
<p>So if I change it, does that mean <code>perp A A'</code> also implies that they are lines?</p>

#### [ Kevin Buzzard (Jul 28 2018 at 11:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Uniting%20Definitions/near/130459206):
<p>I'm suggesting that <code>perp A A'</code> <em>doesn't even make sense</em> unless <code>A</code> and <code>A'</code> are lines.</p>

#### [ Kevin Buzzard (Jul 28 2018 at 11:52)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Uniting%20Definitions/near/130459209):
<p>And there are two ways to do this.</p>

#### [ Kevin Buzzard (Jul 28 2018 at 11:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Uniting%20Definitions/near/130459223):
<p>One is to ask that <code>perp</code> takes as an input not the <em>sets</em> <code>A</code> and <code>A'</code> but <em>proofs</em> <code>HA : line A</code> and <code>HA' : line A</code></p>

#### [ Kevin Buzzard (Jul 28 2018 at 11:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Uniting%20Definitions/near/130459263):
<p>(it would also need <code>A</code> and <code>A'</code> as inputs but they can be guessed from <code>HA</code> and <code>HA'</code>, so you can put them in squiggly brackets <code>{}</code> like I did above)</p>

#### [ Kevin Buzzard (Jul 28 2018 at 11:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Uniting%20Definitions/near/130459266):
<p>and the other way is that you use type class inference.</p>

#### [ Johan Commelin (Jul 28 2018 at 11:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Uniting%20Definitions/near/130459274):
<p>I would say that type class inference feels more natural, but sometimes comes with unexpected challenges of its own. (I'm sure Kevin can tell you more about that (-; ....)</p>

#### [ Kevin Buzzard (Jul 28 2018 at 11:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Uniting%20Definitions/near/130459275):
<p>Then your function looks like <code>def perpx (x : point) (A A' : set point) [HLA : line A] [HLA' : line A'] (HxA : x ∈ A) (HxA' : x ∈ A') := ...</code> or even <code>def perpx (x : point) (A A' : set point) [line A] [line A'] (HxA : x ∈ A) (HxA' : x ∈ A') := ...</code>, and the proofs that <code>A</code> and <code>A'</code> are lines are supplied not by you but by the type class inference machine.</p>

#### [ Johan Commelin (Jul 28 2018 at 11:57)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Uniting%20Definitions/near/130459333):
<p>And you would have to tell Lean that <code>l a b</code> is a line by adding an instance for it to the type class system.</p>

#### [ Johan Commelin (Jul 28 2018 at 11:57)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Uniting%20Definitions/near/130459334):
<p>(If I inferred correctly that <code>l a b</code> is the line through points <code>a</code> and <code>b</code>.)</p>

#### [ Kevin Buzzard (Jul 28 2018 at 11:57)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Uniting%20Definitions/near/130459335):
<p>Right: if you do it with type class inference then you change some of your <code>theorem</code>s and <code>definitions</code> to <code>instance</code>s, which adds them into the system.</p>

#### [ Kevin Buzzard (Jul 28 2018 at 11:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Uniting%20Definitions/near/130459376):
<p>and you change your definition of <code>line</code> into a <code>class</code></p>

#### [ Kevin Buzzard (Jul 28 2018 at 12:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Uniting%20Definitions/near/130459441):
<p>Then you just feed the sets into your function and Lean checks in every case that it can construct a proof behind the scene that they're lines, typically by looking at the definition of <code>A</code> and noticing that it was defined using a function which it knows produces things which it can prove are lines.</p>

#### [ Ali Sever (Jul 28 2018 at 12:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Uniting%20Definitions/near/130459453):
<p>I think this means I have a lot of tidying to do, and even more reading before that.</p>

#### [ Johan Commelin (Jul 28 2018 at 12:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Uniting%20Definitions/near/130459466):
<p>But otoh, this creates a bit of a snowball effect. Because now you also want <code>point</code>s to be a type class, so that Lean can figure out itself that the intersection of two lines is a point.... (if the lines are not parallel)</p>

#### [ Kevin Buzzard (Jul 28 2018 at 12:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Uniting%20Definitions/near/130459504):
<p>If Lean can't find a proof, then it gives up with a "failed to synthesize type class instance" error:</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">complex</span><span class="bp">.</span><span class="n">basic</span>

<span class="kn">example</span> <span class="o">:</span> <span class="o">(</span><span class="mi">1</span> <span class="o">:</span> <span class="n">ℂ</span><span class="o">)</span> <span class="bp">&lt;</span> <span class="o">(</span><span class="mi">2</span> <span class="o">:</span> <span class="n">ℂ</span><span class="o">)</span> <span class="o">:=</span> <span class="n">sorry</span>
</pre></div>


<p>-&gt;</p>
<div class="codehilite"><pre><span></span>failed to synthesize type class instance for
⊢ has_lt ℂ
</pre></div>

#### [ Kevin Buzzard (Jul 28 2018 at 12:05)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Uniting%20Definitions/near/130459572):
<p>Of course <code>&lt;</code> is just notation. If you type <code>#print notation &lt;</code> you see it just means the function <code>has_lt.lt</code> and if you <code>#check @has_lt.lt</code> you find</p>
<div class="codehilite"><pre><span></span>has_lt.lt : Π {α : Type u_1} [c : has_lt α], α → α → Prop
</pre></div>


<p>which says "if the user asks me to make sense of <code>x&lt;y</code> with <code>x y: α</code> then I'm going to ask the type class inference system to check for me that it makes sense to talk about terms of type alpha being less than each other " -- that's what the square brackets means.</p>

#### [ Kevin Buzzard (Jul 28 2018 at 12:08)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Uniting%20Definitions/near/130459676):
<p>And lo and behold, in <code>data/real/basic.lean</code> we have <code>instance : has_lt ℝ := (some definition)</code> which is where Lean is told not just the definition of what it means for a real to be less than another real, but that this should be an "instance", which means "a definition but one which the type class inference system knows about".</p>

#### [ Kevin Buzzard (Jul 28 2018 at 12:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Uniting%20Definitions/near/130459694):
<p>So <code>#check (1 : ℝ) &lt; (2 : ℝ)</code> works fine, but <code>#check (1 : ℂ) &lt; (2 : ℂ)</code> doesn't -- you get the "failed to synthesize type class instance" error.</p>

#### [ Kevin Buzzard (Jul 28 2018 at 12:10)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Uniting%20Definitions/near/130459738):
<p>I guess <code>line A</code> will be a <code>Prop</code> so it sounds like an ideal candidate for type class inference.</p>

#### [ Ali Sever (Jul 28 2018 at 12:11)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Uniting%20Definitions/near/130459748):
<p>So I can get rid of the defintion <code>perp a b c d</code> and use <code>perp (l a b) (l c d)</code>, which automatically knows that  <code>a ≠ b ∧ line (l a b)</code>.</p>

#### [ Kevin Buzzard (Jul 28 2018 at 12:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Uniting%20Definitions/near/130459889):
<p>If you define something like <code>instance line_through_two_points_is_a_line (a b : point) (Hne : a \ne b) : is_line (line_through_two_points a b) := (proof it's a line)</code> then...hmm...this somehow doesn't look too good, because how will Lean guess that a isn't equal to b?</p>

#### [ Johan Commelin (Jul 28 2018 at 12:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Uniting%20Definitions/near/130459890):
<p>Hmm, the <code>a \ne b</code> bit seems non-trivial.</p>

#### [ Johan Commelin (Jul 28 2018 at 12:16)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Uniting%20Definitions/near/130459892):
<p>That might have to be supplied...</p>

#### [ Kevin Buzzard (Jul 28 2018 at 12:18)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Uniting%20Definitions/near/130459945):
<p>I guess you'll be carrying round a proof of that anyway. But feeding it into the system might be hard. Why don't you adopt the other approach for now? Then at least you'll get the logic straight. Just feed in the proofs that everything is a line. That's what I did with schemes. I couldn't figure out how type class inference worked so several of my functions were taking proofs as inputs.</p>

#### [ Ali Sever (Jul 28 2018 at 12:18)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Uniting%20Definitions/near/130459947):
<p>I mean <code>l a b</code> is only defined for <code>a \ne b</code></p>

#### [ Kevin Buzzard (Jul 28 2018 at 12:19)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Uniting%20Definitions/near/130460105):
<p>Lean doesn't like that kind of idea. You know <code>1/0=0</code> right?</p>

#### [ Kevin Buzzard (Jul 28 2018 at 12:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Uniting%20Definitions/near/130460118):
<p>Only defining it for <code>a \ne b</code> is pretty much the same as carrying round a proof of this, in some sense.</p>

#### [ Kevin Buzzard (Jul 28 2018 at 12:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Uniting%20Definitions/near/130460192):
<p>Why not go with <code>def perpx (x : point) {A A' : set point} (HLA : line A) (HLA' : line A') (HxA : x ∈ A) (HxA' : x ∈ A') :=
∀ u v, u ∈ A → v ∈ A' → R u x v</code>?</p>

#### [ Kevin Buzzard (Jul 28 2018 at 12:20)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Uniting%20Definitions/near/130460193):
<p>We can worry about type class inference later.</p>

#### [ Ali Sever (Jul 28 2018 at 12:21)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Uniting%20Definitions/near/130460198):
<p>If I adopt the other approach, won't it be harder in the future to switch to the more sophisticated method?</p>

#### [ Kevin Buzzard (Jul 28 2018 at 12:21)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Uniting%20Definitions/near/130460199):
<p>I'm not sure that this is what an expert would do. But this is what I did for schemes, when I wasn't ready to launch into type class inference, and when I decided I wanted to change it was surprisingly easy.</p>

#### [ Kevin Buzzard (Jul 28 2018 at 12:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Uniting%20Definitions/near/130460241):
<p>I just had to change a bunch of function inputs from <code>HU</code> to <code>U</code></p>

#### [ Mario Carneiro (Jul 28 2018 at 14:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Uniting%20Definitions/near/130465493):
<blockquote>
<p>If you define something like instance line_through_two_points_is_a_line (a b : point) (Hne : a \ne b) : is_line (line_through_two_points a b) := (proof it's a line) then...hmm...this somehow doesn't look too good, because how will Lean guess that a isn't equal to b?</p>
</blockquote>
<p>I often use partial functions for this. My general recommendation against partial functions notwithstanding, when you have typeclasses that depend on it this is usually a good reason to push the assumption into the arguments somehow, either by having an additional proof argument or using a more structured argument space (i.e. a subtype or sigma)</p>

#### [ Kevin Buzzard (Jul 28 2018 at 14:33)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Uniting%20Definitions/near/130465623):
<p><span class="user-mention" data-user-id="120256">@Ali Sever</span> so Mario is suggesting that you could use typeclasses. It might be easier to show you how to do all this on e.g. Monday if you're coming in, where I can explain face to face.</p>

#### [ Ali Sever (Jul 28 2018 at 17:42)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Uniting%20Definitions/near/130472981):
<p>Now that I have VS Code back up, I'll use your suggestion until Monday, and then we can do some CS.</p>

#### [ Patrick Massot (Jul 29 2018 at 00:53)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Uniting%20Definitions/near/130493666):
<p>Seriously, as far as choosing how to represent things, you could really use fifteen years of work gathered at <a href="http://geocoq.github.io/GeoCoq/" target="_blank" title="http://geocoq.github.io/GeoCoq/">http://geocoq.github.io/GeoCoq/</a> Definitions in Coq should be easy to read if you have the maths translation explained in the paper, eg <a href="https://hal.inria.fr/hal-00727117/file/adg2012_braun_narboux_postproc.pdf" target="_blank" title="https://hal.inria.fr/hal-00727117/file/adg2012_braun_narboux_postproc.pdf">https://hal.inria.fr/hal-00727117/file/adg2012_braun_narboux_postproc.pdf</a> You would still have fun I think</p>


{% endraw %}
