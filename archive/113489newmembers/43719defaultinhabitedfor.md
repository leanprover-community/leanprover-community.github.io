---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113489newmembers/43719defaultinhabitedfor.html
---

## Stream: [new members](index.html)
### Topic: [default / inhabited for ℚ, ℝ, ℂ](43719defaultinhabitedfor.html)

---


{% raw %}
#### [ Bryan Gin-ge Chen (Aug 13 2018 at 22:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/default%20/%20inhabited%20for%20%E2%84%9A%2C%20%E2%84%9D%2C%20%E2%84%82/near/132070075):
<p>I'm going through <a href="https://leanprover.github.io/theorem_proving_in_lean/type_classes.html#type-classes-and-instances" target="_blank" title="https://leanprover.github.io/theorem_proving_in_lean/type_classes.html#type-classes-and-instances">TPIL's chapter on typeclasses</a> and while messing around tried the following:</p>
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">complex</span><span class="bp">.</span><span class="n">basic</span>
<span class="bp">#</span><span class="n">reduce</span> <span class="n">default</span> <span class="n">ℚ</span> <span class="c1">-- no type class instance of inhabited ℚ</span>
<span class="bp">#</span><span class="n">reduce</span> <span class="n">default</span> <span class="n">ℝ</span> <span class="c1">-- timeout</span>
<span class="bp">#</span><span class="n">reduce</span> <span class="n">default</span> <span class="n">ℂ</span> <span class="c1">-- timeout</span>
</pre></div>


<p><code>#check</code> succeeds on the last two.</p>
<p>Questions: Is the lack of something like </p>
<div class="codehilite"><pre><span></span><span class="kn">instance</span> <span class="o">:</span> <span class="n">inhabited</span> <span class="n">ℚ</span> <span class="o">:=</span> <span class="bp">⟨</span><span class="mi">0</span><span class="bp">⟩</span>
</pre></div>


<p>in data.rat just an oversight or was this intentional? Why do the other two lines time out?</p>
<p>Meta-question: am I right that this doesn't really matter; i.e. <code>default</code> is unlikely to be used in an "actual" proof?</p>

#### [ Kevin Buzzard (Aug 13 2018 at 22:35)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/default%20/%20inhabited%20for%20%E2%84%9A%2C%20%E2%84%9D%2C%20%E2%84%82/near/132070230):
<p>I suspect that <code>#reduce</code> fails on the last two because the reals and complexes are in general a pain to compute with -- they don't have decidable equality and they might well not even have an algorithm for printing out a real number. What would you expect  sqrt(2) to look like in Lean? Is it supposed to print out all the digits? :-)</p>
<p>I would imagine that Q not being inhabited, if true, is an oversight.</p>

#### [ Chris Hughes (Aug 13 2018 at 22:37)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/default%20/%20inhabited%20for%20%E2%84%9A%2C%20%E2%84%9D%2C%20%E2%84%82/near/132070343):
<p>They time out because a real number is built from a Cauchy sequence, and making a Cauchy sequence requires a proof that the sequence is Cauchy. When you #reduce a real, it will try to unfold this proof to axioms, and this will be huge.</p>

#### [ Bryan Gin-ge Chen (Aug 13 2018 at 22:38)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/default%20/%20inhabited%20for%20%E2%84%9A%2C%20%E2%84%9D%2C%20%E2%84%82/near/132070420):
<p>Thanks, that makes sense! Out of curiosity, what would be the right way to get Lean to spit out the default elements for ℝ and ℂ then?</p>

#### [ Chris Hughes (Aug 13 2018 at 22:40)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/default%20/%20inhabited%20for%20%E2%84%9A%2C%20%E2%84%9D%2C%20%E2%84%82/near/132070513):
<p>The best way to check what they are is to look at the definition of the inhabited instance. Reals don't have decidable equality, so given a real, lean cannot tell if it equals zero or not.</p>

#### [ Kevin Buzzard (Aug 13 2018 at 22:47)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/default%20/%20inhabited%20for%20%E2%84%9A%2C%20%E2%84%9D%2C%20%E2%84%82/near/132070886):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">real</span><span class="bp">.</span><span class="n">basic</span>

<span class="kn">definition</span> <span class="n">d</span> <span class="o">:</span> <span class="n">inhabited</span> <span class="n">ℝ</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">apply_instance</span>

<span class="bp">#</span><span class="kn">print</span> <span class="n">d</span>

<span class="c">/-</span><span class="cm"></span>

<span class="cm">def d : inhabited ℝ :=</span>
<span class="cm">real.inhabited</span>

<span class="cm">-/</span>

<span class="bp">#</span><span class="kn">check</span> <span class="n">real</span><span class="bp">.</span><span class="n">inhabited</span> <span class="c1">-- inhabited ℝ</span>

<span class="c1">-- Now right-click on real.inhabited and select &quot;peek definition&quot;</span>
</pre></div>

#### [ Kevin Buzzard (Aug 13 2018 at 23:07)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/default%20/%20inhabited%20for%20%E2%84%9A%2C%20%E2%84%9D%2C%20%E2%84%82/near/132071991):
<p>I only mention this because I know of no other way of figuring out the real number which was used other than by looking at the source. I don't know how to look at the definition of d directly, as it were.</p>

#### [ Bryan Gin-ge Chen (Aug 13 2018 at 23:22)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/default%20/%20inhabited%20for%20%E2%84%9A%2C%20%E2%84%9D%2C%20%E2%84%82/near/132072791):
<p>Ah, OK, so in general, <code>instance : typeclass something</code> can be accessed with <code>something.typeclass</code>. I must have read this somewhere...</p>
<p>Knowing that I can just <code>#print real.inhabited</code> and read off <code>{default := 0}.</code></p>
<p>As an aside, it seems that <code>rat</code> is missing a bunch of other stuff too, like <code>rat.ring</code>, <code>rat.add_group</code>, <code>rat.field</code>, etc. although they're all an easy <code>by apply_instance</code> away.</p>

#### [ Kevin Buzzard (Aug 13 2018 at 23:23)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/default%20/%20inhabited%20for%20%E2%84%9A%2C%20%E2%84%9D%2C%20%E2%84%82/near/132072805):
<p>waitwaitwait. If <code>by apply_instance</code> works, it's there.</p>

#### [ Kevin Buzzard (Aug 13 2018 at 23:24)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/default%20/%20inhabited%20for%20%E2%84%9A%2C%20%E2%84%9D%2C%20%E2%84%82/near/132072874):
<p>A lot of these instances might be being inferred automatically. For example, Lean knows that any <code>field</code> is automatically a <code>comm_ring</code>, a <code>ring</code>, an <code>add_monoid</code> etc etc.</p>

#### [ Bryan Gin-ge Chen (Aug 13 2018 at 23:25)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/default%20/%20inhabited%20for%20%E2%84%9A%2C%20%E2%84%9D%2C%20%E2%84%82/near/132072906):
<blockquote>
<p>waitwaitwait. If <code>by apply_instance</code> works, it's there.</p>
</blockquote>
<p>Maybe I used the wrong words, but I was referring to the following behavior:</p>
<div class="codehilite"><pre><span></span><span class="bp">#</span><span class="kn">check</span> <span class="n">rat</span><span class="bp">.</span><span class="n">comm_ring</span> <span class="c1">-- unknown identifier</span>
<span class="kn">instance</span> <span class="o">:</span> <span class="n">comm_ring</span> <span class="n">rat</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">apply_instance</span>
<span class="bp">#</span><span class="kn">check</span> <span class="n">rat</span><span class="bp">.</span><span class="n">comm_ring</span> <span class="c1">-- Lean is happy</span>
</pre></div>

#### [ Chris Hughes (Aug 13 2018 at 23:26)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/default%20/%20inhabited%20for%20%E2%84%9A%2C%20%E2%84%9D%2C%20%E2%84%82/near/132072965):
<p>Another way of discovering the name is<br>
 ```lean<br>
def foo : inhabited real := by apply_instance<br>
#print foo</p>
<div class="codehilite"><pre><span></span>
</pre></div>

#### [ Patrick Massot (Aug 13 2018 at 23:26)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/default%20/%20inhabited%20for%20%E2%84%9A%2C%20%E2%84%9D%2C%20%E2%84%82/near/132072972):
<p>Bryan, this is not a bug, this is what the type class system is about</p>

#### [ Patrick Massot (Aug 13 2018 at 23:26)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/default%20/%20inhabited%20for%20%E2%84%9A%2C%20%E2%84%9D%2C%20%E2%84%82/near/132072982):
<p>You get cascading for free</p>

#### [ Bryan Gin-ge Chen (Aug 13 2018 at 23:28)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/default%20/%20inhabited%20for%20%E2%84%9A%2C%20%E2%84%9D%2C%20%E2%84%82/near/132073073):
<blockquote>
<p>Bryan, this is not a bug, this is what the type class system is about</p>
</blockquote>
<p>Right, I didn't intend to imply that there were any bugs other than in my understanding.</p>

#### [ Kevin Buzzard (Aug 13 2018 at 23:32)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/default%20/%20inhabited%20for%20%E2%84%9A%2C%20%E2%84%9D%2C%20%E2%84%82/near/132073292):
<p><a href="https://github.com/leanprover/mathlib/pull/254" target="_blank" title="https://github.com/leanprover/mathlib/pull/254">https://github.com/leanprover/mathlib/pull/254</a></p>

#### [ Kevin Buzzard (Aug 13 2018 at 23:38)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/default%20/%20inhabited%20for%20%E2%84%9A%2C%20%E2%84%9D%2C%20%E2%84%82/near/132073578):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">rat</span>

<span class="kn">definition</span> <span class="n">x</span> <span class="o">:</span> <span class="n">comm_ring</span> <span class="n">ℚ</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">apply_instance</span>

<span class="bp">#</span><span class="kn">print</span> <span class="n">x</span>

<span class="c">/-</span><span class="cm"></span>

<span class="cm">def x : comm_ring ℚ :=</span>
<span class="cm">field.to_comm_ring ℚ</span>

<span class="cm">-/</span>
</pre></div>


<p>Lean knows that the rationals are a commutative ring, but the instance is not called <code>rat.comm_ring</code>, it's called something else. </p>
<p>If <code>X</code> is an inductive type and there's something called <code>X.foo</code>, and if <code>a</code> has type <code>X</code>, then you can sometimes talk about <code>a.foo</code> on a good day. But that's not what's happening here. It's not <code>rat</code> that has type <code>comm_ring</code>, it's some other thing which has type <code>comm_ring rat</code>.</p>

#### [ Chris Hughes (Aug 13 2018 at 23:41)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/default%20/%20inhabited%20for%20%E2%84%9A%2C%20%E2%84%9D%2C%20%E2%84%82/near/132073675):
<blockquote>
<p>Lean knows that the rationals are a commutative ring, but the instance is not called <code>rat.comm_ring</code>, it's called something else. </p>
</blockquote>
<p>I don't think it has a name, it's just inferred from <code>rat.discrete_linear_ordered_field</code> or something.</p>

#### [ Kevin Buzzard (Aug 13 2018 at 23:43)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/default%20/%20inhabited%20for%20%E2%84%9A%2C%20%E2%84%9D%2C%20%E2%84%82/near/132073758):
<p>I guess the term is <code>field.to_comm_ring ℚ</code> and there's no name for this term. On the other hand when <code>instance : foo bar  := blah </code> is run, Lean has a go at naming the instance itself using some vaguely sane algorithm.</p>

#### [ Bryan Gin-ge Chen (Aug 13 2018 at 23:54)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/default%20/%20inhabited%20for%20%E2%84%9A%2C%20%E2%84%9D%2C%20%E2%84%82/near/132074255):
<p>It looks like <code>field.to_comm_ring</code> itself is created automatically from <code>extends comm_ring</code> in the <code>class field</code> declaration.</p>

#### [ Kevin Buzzard (Aug 14 2018 at 00:01)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/default%20/%20inhabited%20for%20%E2%84%9A%2C%20%E2%84%9D%2C%20%E2%84%82/near/132074504):
<p>Yeah, that's a cool part of type class inference. The projectors get constructed automatically.</p>

#### [ Kevin Buzzard (Aug 14 2018 at 00:09)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/default%20/%20inhabited%20for%20%E2%84%9A%2C%20%E2%84%9D%2C%20%E2%84%82/near/132074849):
<div class="codehilite"><pre><span></span><span class="kn">import</span> <span class="n">data</span><span class="bp">.</span><span class="n">rat</span>

<span class="kn">definition</span> <span class="n">d</span> <span class="o">:</span> <span class="n">comm_monoid</span> <span class="n">ℚ</span> <span class="o">:=</span> <span class="k">by</span> <span class="n">apply_instance</span>

<span class="kn">set_option</span> <span class="n">pp</span><span class="bp">.</span><span class="n">all</span> <span class="n">true</span>
<span class="bp">#</span><span class="kn">print</span> <span class="n">d</span>

<span class="c">/-</span><span class="cm"></span>

<span class="cm">def d : comm_monoid.{0} rat :=</span>
<span class="cm">@linear_ordered_comm_ring.to_comm_monoid.{0} rat</span>
<span class="cm">  (@decidable_linear_ordered_comm_ring.to_linear_ordered_comm_ring.{0} rat</span>
<span class="cm">     (@discrete_linear_ordered_field.to_decidable_linear_ordered_comm_ring.{0} rat rat.discrete_linear_ordered_field))</span>

<span class="cm">-/</span>
</pre></div>


<p>Type class inference is quite clever.</p>

#### [ Bryan Gin-ge Chen (Aug 14 2018 at 00:15)](https://leanprover.zulipchat.com/#narrow/stream/113489-new%20members/topic/default%20/%20inhabited%20for%20%E2%84%9A%2C%20%E2%84%9D%2C%20%E2%84%82/near/132075092):
<p>It looks much more persistent than clever when I put on <code>set_option trace.class_instances true</code> <span class="emoji emoji-1f609" title="wink">:wink:</span></p>


{% endraw %}
