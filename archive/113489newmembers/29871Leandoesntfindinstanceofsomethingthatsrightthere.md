---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/29871Leandoesntfindinstanceofsomethingthatsrightthere.html
---

## Stream: [new members](index.html)
### Topic: [Lean doesn't find instance of something that's right there](29871Leandoesntfindinstanceofsomethingthatsrightthere.html)

---


{% raw %}
#### [ Abhimanyu Pallavi Sudhir (Oct 16 2018 at 00:38)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Lean%20doesn%27t%20find%20instance%20of%20something%20that%27s%20right%20there/near/135863594):
<p>Weird problem -- I have my goal, which is <code>(x ⋆ y) → (y ⋆ z) → (x ⋆ z)</code> (for some operation <code>⋆</code>) and I have a hypothesis <code>Hxy : x = y</code>. But when I try <code>rw Hxy,</code> Lean tells me:</p>
<div class="codehilite"><pre><span></span><span class="n">rewrite</span> <span class="n">tactic</span> <span class="n">failed</span><span class="o">,</span> <span class="n">did</span> <span class="n">not</span> <span class="n">find</span> <span class="kn">instance</span> <span class="n">of</span> <span class="n">the</span> <span class="n">pattern</span> <span class="k">in</span> <span class="n">the</span> <span class="n">target</span> <span class="n">expression</span>
  <span class="n">x</span>
</pre></div>

#### [ Abhimanyu Pallavi Sudhir (Oct 16 2018 at 00:39)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Lean%20doesn%27t%20find%20instance%20of%20something%20that%27s%20right%20there/near/135863628):
<p>But... it's right there.</p>

#### [ Kevin Buzzard (Oct 16 2018 at 00:43)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Lean%20doesn%27t%20find%20instance%20of%20something%20that%27s%20right%20there/near/135863810):
<p>Post a MWE</p>

#### [ Kevin Buzzard (Oct 16 2018 at 00:44)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Lean%20doesn%27t%20find%20instance%20of%20something%20that%27s%20right%20there/near/135863871):
<p>Sometimes it's because you have two variables called <code>x</code>, sometimes it's because something needs to be done by type class inference and type class inference fails but the error mesage is that the rewrite failed, there are all sorts of reasons.</p>

#### [ Kevin Buzzard (Oct 16 2018 at 00:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Lean%20doesn%27t%20find%20instance%20of%20something%20that%27s%20right%20there/near/135864347):
<p>Another reason it fails is that you can't rewrite under a binder. Does <code>simp only [Hxy]</code> work? As you can see, it's difficult to diagnose without a MWE.</p>

#### [ Abhimanyu Pallavi Sudhir (Oct 16 2018 at 00:55)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Lean%20doesn%27t%20find%20instance%20of%20something%20that%27s%20right%20there/near/135864405):
<p>Ok, I got the problem (it was the "two variables called <code>x</code>" thing) -- I had defined a symbol <code>S</code> for <code>fin 2</code> and mid-way through the proof had done <code>rw S at z y x</code>, which caused two sets of variables <code>x y z</code> to be defined.</p>

#### [ Kevin Buzzard (Oct 16 2018 at 00:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Lean%20doesn%27t%20find%20instance%20of%20something%20that%27s%20right%20there/near/135864450):
<p><code>rw</code> is a fickle beast.</p>

#### [ Abhimanyu Pallavi Sudhir (Oct 16 2018 at 00:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Lean%20doesn%27t%20find%20instance%20of%20something%20that%27s%20right%20there/near/135864454):
<p>(although I'm not sure why that happened -- usually when you do <code>rw something at something</code>, it just changes the statement, not create new ones.)</p>

#### [ Kevin Buzzard (Oct 16 2018 at 00:56)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Lean%20doesn%27t%20find%20instance%20of%20something%20that%27s%20right%20there/near/135864455):
<p>It takes a while to get to know its foibles</p>

#### [ Kevin Buzzard (Oct 16 2018 at 00:58)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Lean%20doesn%27t%20find%20instance%20of%20something%20that%27s%20right%20there/near/135864545):
<div class="codehilite"><pre><span></span><span class="kn">example</span> <span class="o">(</span><span class="n">n</span> <span class="n">x</span> <span class="n">y</span> <span class="o">:</span> <span class="bp">ℕ</span><span class="o">)</span> <span class="o">(</span><span class="n">h</span> <span class="o">:</span> <span class="n">n</span> <span class="bp">&gt;</span> <span class="mi">0</span> <span class="bp">→</span> <span class="n">x</span> <span class="bp">=</span> <span class="n">y</span><span class="o">)</span> <span class="o">:</span> <span class="n">x</span> <span class="bp">+</span> <span class="mi">1</span> <span class="bp">=</span> <span class="n">y</span> <span class="bp">+</span> <span class="mi">2</span> <span class="o">:=</span>
<span class="k">begin</span>
  <span class="n">rw</span> <span class="n">h</span><span class="o">,</span>
  <span class="c1">-- one goal became 2 -- we now need a proof of n &gt; 0</span>
  <span class="n">sorry</span><span class="o">,</span><span class="n">sorry</span>
<span class="kn">end</span>
</pre></div>

#### [ Abhimanyu Pallavi Sudhir (Oct 16 2018 at 01:02)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/Lean%20doesn%27t%20find%20instance%20of%20something%20that%27s%20right%20there/near/135864852):
<p>Yeah, I've encountered that before, but that actually makes sense (and is useful!). Treating rewrites differently based on whether they're done on a natural number or a proof is just weird.</p>


{% endraw %}
