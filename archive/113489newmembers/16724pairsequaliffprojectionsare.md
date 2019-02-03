---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/16724pairsequaliffprojectionsare.html
---

## Stream: [new members](https://leanprover-community.github.io/archive/113489newmembers/index.html)
### Topic: [pairs equal iff projections are?](https://leanprover-community.github.io/archive/113489newmembers/16724pairsequaliffprojectionsare.html)

---

<base href="https://leanprover.zulipchat.com">
{% raw %}
#### [ Marcus Klaas (Dec 02 2018 at 13:50)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/pairs%20equal%20iff%20projections%20are%3F/near/150722245):
<p>Can anyone give me a pointer on how prove this?</p>
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">{</span><span class="n">α</span> <span class="n">β</span><span class="o">}</span> <span class="o">{</span><span class="n">a</span> <span class="n">c</span> <span class="o">:</span> <span class="n">α</span><span class="o">}</span> <span class="o">{</span><span class="n">b</span> <span class="n">d</span> <span class="o">:</span> <span class="n">β</span><span class="o">}</span> <span class="o">(</span><span class="n">h</span><span class="o">:</span> <span class="o">(</span><span class="n">a</span><span class="o">,</span> <span class="n">b</span><span class="o">)</span> <span class="bp">=</span> <span class="o">(</span><span class="n">c</span><span class="o">,</span> <span class="n">d</span><span class="o">))</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">=</span> <span class="n">c</span> <span class="o">:=</span> <span class="n">sorry</span>
</pre></div>

#### [ Kevin Buzzard (Dec 02 2018 at 13:51)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/pairs%20equal%20iff%20projections%20are%3F/near/150722253):
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">{</span><span class="n">α</span> <span class="n">β</span><span class="o">}</span> <span class="o">{</span><span class="n">a</span> <span class="n">c</span> <span class="o">:</span> <span class="n">α</span><span class="o">}</span> <span class="o">{</span><span class="n">b</span> <span class="n">d</span> <span class="o">:</span> <span class="n">β</span><span class="o">}</span> <span class="o">(</span><span class="n">h</span><span class="o">:</span> <span class="o">(</span><span class="n">a</span><span class="o">,</span> <span class="n">b</span><span class="o">)</span> <span class="bp">=</span> <span class="o">(</span><span class="n">c</span><span class="o">,</span> <span class="n">d</span><span class="o">))</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">=</span> <span class="n">c</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">cases</span> <span class="n">h</span><span class="o">,</span>
  <span class="n">refl</span><span class="o">,</span>
<span class="kn">end</span>
</pre></div>

#### [ Patrick Massot (Dec 02 2018 at 13:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/pairs%20equal%20iff%20projections%20are%3F/near/150722349):
<p>The state after <code>cases</code> is a bit weird. You can also directly provide the proof term <code>(prod.mk.inj h).left</code></p>

#### [ Kevin Buzzard (Dec 02 2018 at 13:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/pairs%20equal%20iff%20projections%20are%3F/near/150722350):
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">{</span><span class="n">α</span> <span class="n">β</span><span class="o">}</span> <span class="o">{</span><span class="n">a</span> <span class="n">c</span> <span class="o">:</span> <span class="n">α</span><span class="o">}</span> <span class="o">{</span><span class="n">b</span> <span class="n">d</span> <span class="o">:</span> <span class="n">β</span><span class="o">}</span> <span class="o">(</span><span class="n">h</span><span class="o">:</span> <span class="o">(</span><span class="n">a</span><span class="o">,</span> <span class="n">b</span><span class="o">)</span> <span class="bp">=</span> <span class="o">(</span><span class="n">c</span><span class="o">,</span> <span class="n">d</span><span class="o">))</span> <span class="o">:</span> <span class="n">a</span> <span class="bp">=</span> <span class="n">c</span> <span class="o">:=</span>
<span class="o">(</span><span class="n">prod</span><span class="bp">.</span><span class="n">mk</span><span class="bp">.</span><span class="n">inj</span> <span class="n">h</span><span class="o">)</span><span class="bp">.</span><span class="mi">1</span>
</pre></div>

#### [ Marcus Klaas (Dec 02 2018 at 13:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/pairs%20equal%20iff%20projections%20are%3F/near/150722351):
<p>Thanks so much!!</p>

#### [ Kevin Buzzard (Dec 02 2018 at 13:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/pairs%20equal%20iff%20projections%20are%3F/near/150722360):
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">{</span><span class="n">α</span> <span class="n">β</span><span class="o">}</span> <span class="o">:</span> <span class="bp">∀</span> <span class="o">{</span><span class="n">a</span> <span class="n">c</span> <span class="o">:</span> <span class="n">α</span><span class="o">}</span> <span class="o">{</span><span class="n">b</span> <span class="n">d</span> <span class="o">:</span> <span class="n">β</span><span class="o">}</span> <span class="o">(</span><span class="n">h</span><span class="o">:</span> <span class="o">(</span><span class="n">a</span><span class="o">,</span> <span class="n">b</span><span class="o">)</span> <span class="bp">=</span> <span class="o">(</span><span class="n">c</span><span class="o">,</span> <span class="n">d</span><span class="o">)),</span> <span class="n">a</span> <span class="bp">=</span> <span class="n">c</span>
<span class="bp">|</span> <span class="n">a</span> <span class="n">c</span> <span class="n">b</span> <span class="n">d</span> <span class="n">rfl</span> <span class="o">:=</span> <span class="n">rfl</span>
</pre></div>

#### [ Kevin Buzzard (Dec 02 2018 at 13:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/pairs%20equal%20iff%20projections%20are%3F/near/150722399):
<p>So that's a tactic mode proof, a term mode proof, and a proof using the equation compiler.</p>

#### [ Marcus Klaas (Dec 02 2018 at 13:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/pairs%20equal%20iff%20projections%20are%3F/near/150722448):
<p>Haha, that's great :D - I'm not quite sure how the equation compiler does it tho ;p</p>

#### [ Kevin Buzzard (Dec 02 2018 at 14:00)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/pairs%20equal%20iff%20projections%20are%3F/near/150722505):
<p><code>(a, b)</code> has type <code>prod \alpha \beta</code>, an inductive type, so you need tools to deal with terms of this type. When the inductive type <code>prod</code> is defined, Lean creates with it its recursor <code>prod.rec</code>, which is the universal way to define a map from <code>prod \alpha \beta</code> to anywhere. Lean then creates a bunch of other useful functions automatically, you can see what they are by typing <code>#print prefix prod</code>. There's usually something called <code>X.mk.inj</code> in there for an inductive type <code>X</code>, so that's what I was looking for. That's how I found the term proof. For the tactic mode proof, <code>cases</code> is a great tactic for any inductive type, it takes the type to pieces. </p>
<p>For the equation compiler proof, we make Lean do the work. I had to move things to the other side of the colon. The point is that I can tell Lean that without loss of generality <code>h</code> <em>must</em> be <code>rfl</code>. I still don't really understand how the equation compiler actually works, but I have sort-of got the hang of how to use it in practice. Your question is a great basic example of how to use its power.</p>

#### [ Mario Carneiro (Dec 02 2018 at 14:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/pairs%20equal%20iff%20projections%20are%3F/near/150722564):
<p>it uses <code>prod.no_confusion</code> under the hood, which is basically the same as <code>prod.inj</code></p>

#### [ Marcus Klaas (Dec 02 2018 at 14:03)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/pairs%20equal%20iff%20projections%20are%3F/near/150722580):
<p>You folks are amazing. Thank you.</p>

#### [ Kevin Buzzard (Dec 02 2018 at 14:04)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/pairs%20equal%20iff%20projections%20are%3F/near/150722619):
<p>Just to be clear -- moving stuff to before or after the colon doesn't change the proposition, it's just a trick for controlling whether or not you have to give the inputs yourself in the "first line" of your proof.</p>


{% endraw %}
