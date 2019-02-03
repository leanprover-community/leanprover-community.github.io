---
layout: page
title: Lean Prover Zulip Chat Archive 
permalink: archive/113488general/64403typeclassinstancesofsuperclasses.html
---

## Stream: [general](index.html)
### Topic: [type class instances of superclasses](64403typeclassinstancesofsuperclasses.html)

---


{% raw %}
#### [ Sean Leather (Jun 21 2018 at 14:08)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20instances%20of%20superclasses/near/128414454):
<p>Given roughly the following combination of classes and instances:</p>
<div class="codehilite"><pre><span></span><span class="n">class</span> <span class="n">A</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="o">:=</span> <span class="bp">...</span>
<span class="n">class</span> <span class="n">B</span> <span class="o">(</span><span class="n">a</span> <span class="o">:</span> <span class="kt">Type</span><span class="o">)</span> <span class="kn">extends</span> <span class="n">B</span> <span class="o">:=</span> <span class="bp">...</span>
<span class="n">def</span> <span class="n">T</span> <span class="o">:</span> <span class="kt">Type</span> <span class="o">:=</span> <span class="bp">...</span>
<span class="kn">instance</span> <span class="o">:</span> <span class="n">B</span> <span class="n">T</span> <span class="o">:=</span> <span class="bp">...</span>
</pre></div>


<p>do you also automatically get:</p>
<div class="codehilite"><pre><span></span><span class="kn">instance</span> <span class="o">:</span> <span class="n">A</span> <span class="n">T</span> <span class="o">:=</span> <span class="bp">...</span>
</pre></div>


<p>such that the latter instance is the appropriate component of the former instance?</p>

#### [ Mario Carneiro (Jun 21 2018 at 14:09)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20instances%20of%20superclasses/near/128414483):
<p>Depends on what you mean by "automatically get"</p>

#### [ Mario Carneiro (Jun 21 2018 at 14:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20instances%20of%20superclasses/near/128414546):
<p>typeclass inference should find it, but no additional def is made</p>

#### [ Sean Leather (Jun 21 2018 at 14:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20instances%20of%20superclasses/near/128414547):
<p>Let's assume I don't have a specific meaning and would welcome a precise definition of the phrase. <span class="emoji emoji-1f609" title="wink">:wink:</span></p>

#### [ Sean Leather (Jun 21 2018 at 14:13)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20instances%20of%20superclasses/near/128414628):
<blockquote>
<p>typeclass inference should find it, but no additional def is made</p>
</blockquote>
<p>So, if <code>class A</code> included a def <code>aaa : a -&gt; bool</code> and you used <code>aaa</code> on <code>t : T</code>, this would use the implementation in <code>instance : B T</code>?</p>

#### [ Mario Carneiro (Jun 21 2018 at 14:14)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20instances%20of%20superclasses/near/128414686):
<p>yes</p>

#### [ Sean Leather (Jun 21 2018 at 14:15)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20instances%20of%20superclasses/near/128414708):
<p>Interesting. But I would not be able to explicitly reference any definition of type <code>A T</code>: this is what you mean by “no additional def is made”?</p>

#### [ Mario Carneiro (Jun 21 2018 at 14:16)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20instances%20of%20superclasses/near/128414759):
<p>typeclass inference would insert a term of the type <code>BtoA BT</code> rather than making an <code>AT</code> def and using that</p>

#### [ Sean Leather (Jun 21 2018 at 14:19)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20instances%20of%20superclasses/near/128414845):
<p>Okay. Does that <code>BtoA</code> have a name that you can <code>#print</code>?</p>

#### [ Mario Carneiro (Jun 21 2018 at 14:22)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20instances%20of%20superclasses/near/128414928):
<p><code>B.to_A</code> I believe</p>

#### [ Sean Leather (Jun 21 2018 at 14:28)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20instances%20of%20superclasses/near/128415195):
<p>I just noticed that <code>lattice</code> is defined in the <code>namespace lattice</code>, resulting in <code>lattice.lattice</code> as the qualified name.</p>

#### [ Sean Leather (Jun 21 2018 at 14:29)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20instances%20of%20superclasses/near/128415218):
<div class="codehilite"><pre><span></span><span class="bp">#</span><span class="kn">print</span> <span class="n">instances</span> <span class="n">lattice</span><span class="bp">.</span><span class="n">lattice</span>
</pre></div>


<div class="codehilite"><pre><span></span><span class="n">finset</span><span class="bp">.</span><span class="n">lattice</span><span class="bp">.</span><span class="n">lattice</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u_1</span><span class="o">}</span> <span class="o">[</span><span class="bp">_</span><span class="n">inst_1</span> <span class="o">:</span> <span class="n">decidable_eq</span> <span class="n">α</span><span class="o">],</span> <span class="n">lattice</span><span class="bp">.</span><span class="n">lattice</span> <span class="o">(</span><span class="n">finset</span> <span class="n">α</span><span class="o">)</span>
<span class="n">multiset</span><span class="bp">.</span><span class="n">lattice</span><span class="bp">.</span><span class="n">lattice</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u_1</span><span class="o">}</span> <span class="o">[</span><span class="bp">_</span><span class="n">inst_1</span> <span class="o">:</span> <span class="n">decidable_eq</span> <span class="n">α</span><span class="o">],</span> <span class="n">lattice</span><span class="bp">.</span><span class="n">lattice</span> <span class="o">(</span><span class="n">multiset</span> <span class="n">α</span><span class="o">)</span>
<span class="n">with_zero</span><span class="bp">.</span><span class="n">lattice</span><span class="bp">.</span><span class="n">lattice</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">[</span><span class="bp">_</span><span class="n">inst_1</span> <span class="o">:</span> <span class="n">lattice</span><span class="bp">.</span><span class="n">lattice</span> <span class="n">α</span><span class="o">],</span> <span class="n">lattice</span><span class="bp">.</span><span class="n">lattice</span> <span class="o">(</span><span class="n">with_zero</span> <span class="n">α</span><span class="o">)</span>
<span class="n">with_top</span><span class="bp">.</span><span class="n">lattice</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">[</span><span class="bp">_</span><span class="n">inst_1</span> <span class="o">:</span> <span class="n">lattice</span><span class="bp">.</span><span class="n">lattice</span> <span class="n">α</span><span class="o">],</span> <span class="n">lattice</span><span class="bp">.</span><span class="n">lattice</span> <span class="o">(</span><span class="n">with_top</span> <span class="n">α</span><span class="o">)</span>
<span class="n">with_bot</span><span class="bp">.</span><span class="n">lattice</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">{</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">}</span> <span class="o">[</span><span class="bp">_</span><span class="n">inst_1</span> <span class="o">:</span> <span class="n">lattice</span><span class="bp">.</span><span class="n">lattice</span> <span class="n">α</span><span class="o">],</span> <span class="n">lattice</span><span class="bp">.</span><span class="n">lattice</span> <span class="o">(</span><span class="n">with_bot</span> <span class="n">α</span><span class="o">)</span>
</pre></div>

#### [ Sean Leather (Jun 21 2018 at 14:30)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20instances%20of%20superclasses/near/128415225):
<p>Lots of <code>lattice.lattice</code>.</p>

#### [ Sean Leather (Jun 21 2018 at 14:31)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20instances%20of%20superclasses/near/128415328):
<p>Ah, here are the conversions for <code>lattice</code> to <code>semilattice_inf</code> and <code>semilattice_sup</code>:</p>
<div class="codehilite"><pre><span></span><span class="bp">#</span><span class="kn">print</span> <span class="kn">prefix</span> <span class="n">lattice</span><span class="bp">.</span><span class="n">lattice</span>
</pre></div>


<div class="codehilite"><pre><span></span><span class="bp">...</span>
<span class="n">lattice</span><span class="bp">.</span><span class="n">lattice</span><span class="bp">.</span><span class="n">to_semilattice_inf</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">[</span><span class="n">s</span> <span class="o">:</span> <span class="n">lattice</span><span class="bp">.</span><span class="n">lattice</span> <span class="n">α</span><span class="o">],</span> <span class="n">lattice</span><span class="bp">.</span><span class="n">semilattice_inf</span> <span class="n">α</span>
<span class="n">lattice</span><span class="bp">.</span><span class="n">lattice</span><span class="bp">.</span><span class="n">to_semilattice_sup</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">[</span><span class="n">s</span> <span class="o">:</span> <span class="n">lattice</span><span class="bp">.</span><span class="n">lattice</span> <span class="n">α</span><span class="o">],</span> <span class="n">lattice</span><span class="bp">.</span><span class="n">semilattice_sup</span> <span class="n">α</span>
</pre></div>

#### [ Sean Leather (Jun 21 2018 at 14:33)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20instances%20of%20superclasses/near/128415413):
<p>Thanks, Mario!</p>

#### [ Sean Leather (Jun 21 2018 at 14:36)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20instances%20of%20superclasses/near/128415592):
<p>I suppose the goal of this feature is to reduce the number of instances one writes. However, it does make it more difficult to determine if <code>T</code> is an instance of <code>A</code>.</p>
<div class="codehilite"><pre><span></span><span class="bp">#</span><span class="kn">print</span> <span class="n">instances</span> <span class="n">lattice</span><span class="bp">.</span><span class="n">semilattice_inf</span>
</pre></div>


<div class="codehilite"><pre><span></span><span class="n">lattice</span><span class="bp">.</span><span class="n">semilattice_inf_bot</span><span class="bp">.</span><span class="n">to_semilattice_inf</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">[</span><span class="n">s</span> <span class="o">:</span> <span class="n">lattice</span><span class="bp">.</span><span class="n">semilattice_inf_bot</span> <span class="n">α</span><span class="o">],</span> <span class="n">lattice</span><span class="bp">.</span><span class="n">semilattice_inf</span> <span class="n">α</span>
<span class="n">lattice</span><span class="bp">.</span><span class="n">semilattice_inf_top</span><span class="bp">.</span><span class="n">to_semilattice_inf</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">[</span><span class="n">s</span> <span class="o">:</span> <span class="n">lattice</span><span class="bp">.</span><span class="n">semilattice_inf_top</span> <span class="n">α</span><span class="o">],</span> <span class="n">lattice</span><span class="bp">.</span><span class="n">semilattice_inf</span> <span class="n">α</span>
<span class="n">lattice</span><span class="bp">.</span><span class="n">lattice</span><span class="bp">.</span><span class="n">to_semilattice_inf</span> <span class="o">:</span> <span class="bp">Π</span> <span class="o">(</span><span class="n">α</span> <span class="o">:</span> <span class="kt">Type</span> <span class="n">u</span><span class="o">)</span> <span class="o">[</span><span class="n">s</span> <span class="o">:</span> <span class="n">lattice</span><span class="bp">.</span><span class="n">lattice</span> <span class="n">α</span><span class="o">],</span> <span class="n">lattice</span><span class="bp">.</span><span class="n">semilattice_inf</span> <span class="n">α</span>
</pre></div>

#### [ Mario Carneiro (Jun 21 2018 at 14:55)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20instances%20of%20superclasses/near/128416353):
<p>one trick for testing instance problems and getting the result is <code>#check (by apply_instance : T A)</code></p>

#### [ Sean Leather (Jun 21 2018 at 15:06)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20instances%20of%20superclasses/near/128416816):
<p>That works only if <code>A</code> is exactly the type of the instance. For example: <code>#check (by apply_instance : lattice.semilattice_inf (finset ℕ))</code> but not <code>#check (by apply_instance : lattice.semilattice_inf (finset α))</code>.</p>

#### [ Sean Leather (Jun 21 2018 at 15:10)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20instances%20of%20superclasses/near/128416961):
<p>Also, that's a tool for diagnosing an issue. It doesn't help discovering all the instances, which I have found to be useful in Haskell (and would find useful in Lean).</p>

#### [ Simon Hudon (Jun 21 2018 at 20:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20instances%20of%20superclasses/near/128430586):
<p>Do you know about <code>#print instances</code>?</p>

#### [ Sean Leather (Jun 22 2018 at 08:43)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20instances%20of%20superclasses/near/128458664):
<p><span class="user-mention" data-user-id="110026">@Simon Hudon</span> Did you see my uses of it above? <span class="emoji emoji-1f609" title="wink">:wink:</span></p>

#### [ Simon Hudon (Jun 22 2018 at 17:00)](https://leanprover.zulipchat.com/#narrow/stream/113488-general/topic/type%20class%20instances%20of%20superclasses/near/128476919):
<p>oops! Sorry!</p>


{% endraw %}
